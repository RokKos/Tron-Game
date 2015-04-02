#Socket client

import socket 
import sys
from thread import *

#Poskusi ce lahko naredi socket
try:
	#naredi socket(TCP)	AF_INET -> IPv4   SOCK_STREAM -> Za Tcp orientirane povezave
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	sys.exit();

print 'Socket Created'

host = "www.google.com"
port = 80

try:
	#poisce njegov ip
	remote_ip = socket.gethostbyname(host)

except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

print 'IP addres of ' + host + ' is ' + remote_ip

#Poveze se s serverjem
s.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

message = "GET / HTTP/1.1\r\n\r\n"

try:
	#posli sporocilo
	s.sendall(message)
except stocket.error:
	
	print 'Send failed'
	sys.exit()

print 'Message send successfully'

#sprejme podatke
reply = s.recv(4096)
print reply

#zapre socket
s.close()


#######################
#Bind socket

#Poskusi ce lahko naredi socket
try:
	#naredi socket(TCP)	AF_INET -> IPv4   SOCK_STREAM -> Za Tcp orientirane povezave
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	sys.exit();

print 'Socket Created'

host = "" #local host
port = 5000

try:
	s.bind((host, port))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
 	sys.exit()

print 'Socket bind complete'

#poslusamo na portu
s.listen(10) #stevilka 10 pomeni da lahko najvec 10 povezav od enkrat caka in da bo 11 zavrnjena
print 'Socket now listening'

#Funkcija za handlanje povezav. Delala bo razlicne threade da bo lahko vse povezave pohanlala
def clientthread(conn):
	conn.send('Welcome to the server. Type something and hit enter\n')

	#neskoncna zanka zato da se funkcija ne terminira in da se threadi ne koncajo
	while True:
    	#pogovor z serverjem/clientom
		data = conn.recv(1024)
		reply = 'Sprejel sm: ' + data
		if(not data):
			break
		conn.sendall(reply)

	conn.close()

while True:
	#pocaka in sprejme povezavo
	conn, addr = s.accept()

	#pokaze kaj je dobil
	print 'Connected with ' + addr[0] + ':' + str(addr[1])

	#zacne nov thread ki vzame za prvi argument ime funkcije, ki se bo pognala in zraven se parametre ki ji poda
	start_new_thread(clientthread ,(conn,))
	
	

s.close()