import socket
port=223#443#80
host="www.google.com"
s=None
try:
	s=socket.socket()
	s.connect((host,port))
	print "connection successfully"
	'''
	ack=None
	try:
		ack=s.recv(1024)
		print "ack: ",ack
	except Exception as err:
		print err
		print "connection successfully"
	'''
except Exception as err:
	print err
finally:
	if s:
		s.close()