import socket
import sys

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print "Usage: %s <host> <port> <username_file>"%(sys.argv[0])
		sys.exit(0)
	
	users = []
	infile = open(sys.argv[3],'r')
	lines = infile.readlines()
	infile.close()
	i=0
	for line in lines:
		line = line.strip()
		if line not in users:
			users += [line]
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect = s.connect((sys.argv[1],int(sys.argv[2])))
	
	#Receive banner and HELO first
	banner = s.recv(1024)
	s.send('HELO OSCP-OFFSEC\r\n')
	result = s.recv(1024)
	
	i=0
	while i<len(users):
		try:
			#VRFY a user
			s.send('VRFY '+users[i]+'\r\n')
			result = s.recv(1024)
			print result,
			i+=1
		except socket.error: #if connection closes due to too many errors, re-establish connection
			s.close()
			print "Connection closed by server, re-establishing connection"
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			connect = s.connect((sys.argv[1],int(sys.argv[2])))
			banner = s.recv(1024)
			s.send('HELO OSCP-OFFSEC\r\n')
	
	s.close()

