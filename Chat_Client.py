####################################
#TCP Chat Client

import socket, select, string, sys

def prompt():
	sys.stdout.write('<You> ')
	sys.stdout.flush()

#glavna funkcija
if __name__ == "__main__":
	#pogleda ce so argumenti pravilno podani
	if(len(sys.argv) < 3):
		print 'Usage : python telnet.py hostname port'
		sys.exit()

	HOST = sys.argv[1]
	PORT = int(sys.argv[2])

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	#povezava na server
	try:
		s.connect((HOST, PORT))

	except:
		print 'Unable to connect'
		sys.exit()

	print 'Connected to remote host. Start sending messages'
	prompt()

	while True:
		#POMEMBNO: bere iz serverja in iz standardnega vhoda(termilala)
		socket_list = [sys.stdin, s]

		#dobi vse sockete, ki so dostopni in berljivi
		read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

		for sock in read_sockets:
			#dobi sporocilo iz serverja
			if (sock == s): #primerja dobljeno s socketom
				data = sock.recv(4096)
				if (data):
					#izpise podatke
					sys.stdout.write(data)
					prompt()

				else:
					#drugace disconeta uporabnika
					print '\nDisconnected from chat server'
					sys.exit()
			else:
				msg = sys.stdin.readline()
				s.send(msg)
				prompt()
		 
###################################################
#OPOMBA:
###Ta chat client dela samo na windowsu ker funkcija select v vrstici 39 bere iz serverja in 
###iz input strema. To pise v python dokumentaciji:File objects on Windows are not acceptable, but sockets are. On Windows, the underlying select() 
###function is provided by the WinSock library, and does not handle file descriptors that don’t originate from WinSock.
###In se en bug je ce uporanik pise in medtem dobi sporocilo od serverja mu bo pobrisalo vse kar je napisal
###zaradi prompt() funkicje ki flusha(pobrise) ves stream
