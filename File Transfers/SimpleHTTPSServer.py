#generate certificate: openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

import BaseHTTPServer, SimpleHTTPServer
import ssl
import sys

if __name__ == '__main__':
	port = 4443
	
	if len(sys.argv)>1:
		try:
			port = int(sys.argv[1])
			if (port<1) or (port>65535):
				raise ValueError()
		except(ValueError):
			print "Usage: python %s [PORT]\n\tOption PORT argument must be an integer from 1 to 65535"%(sys.argv[0])
			exit(1)
	
	httpd = BaseHTTPServer.HTTPServer(('0.0.0.0',port), SimpleHTTPServer.SimpleHTTPRequestHandler)
	httpd.socket = ssl.wrap_socket(httpd.socket,certfile='server.pem',server_side=True)
	print "Serving HTTPS on 0.0.0.0 port %i ..."%(port)
	httpd.serve_forever()

