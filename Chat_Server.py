####################
#TCP Chat Server

import socket, select

#funkcija, ki prenasa sporocila do vseh povezanih uporabnikov
def broadcast_data(sock, msg):
	for socket in CONNECTION_LIST:
		#preveri da ne poslje sporocilo master socketu in tistemu, ki nam ga je poslal
		if (socket != server_socket and socket !=sock):
			try:
				socket.send(msg)
			except:
				#ce pride do napake pri posiljanju socketov ali ce je uporabnik pritisnil ctr-c
				socket.close()
				CONNECTION_LIST.remove(socket)

if __name__ == "__main__":
	#seznam vse socketov
	CONNECTION_LIST = []
	RECV_BUFFER = 4096
	HOST = ""
	PORT = 5000

	#initializiramo server in ga pozenemo ter pripravimo da poslusa
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((HOST, PORT))
	server_socket.listen(10)

	#doda server socket v seznam berljivih povezav
	CONNECTION_LIST.append(server_socket)

	print "Chat server started on ip" + str(HOST) +"and port " + str(PORT)

	#glavni loop
	while True:
		#dobi seznam socketov, ki so pripravljeni za branje
		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 		
 		for sock in read_sockets:
 			#nova povezava
 			if(sock == server_socket):
 				#ustvari novo povezavo
 				sockfd, addr = server_socket.accept()
 				CONNECTION_LIST.append(sockfd)
 				print "Client (%s, %s) connected" % addr

 				broadcast_data(sockfd, "[%s: %s] entered room\n" %addr)

 			#sporocilo od uporabnika
	 		else:
	 			#sprejme in pohandla informacije od uporabnika
	 			try:
	 				data = sock.recv(RECV_BUFFER)
	 				if (data):
	 					broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)

	 			except:
	 				broadcast_data(sock, "Client (%s, %s) is offline" %addr)
	 				print "Client (%s, %s) is offline" % addr
	 				sock.close()
	 				CONNECTION_LIST.remove(sock)
	 				continue

 	server_socket.close()