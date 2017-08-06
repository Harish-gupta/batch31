import socket
try:
	s=socket.socket()
	host = "tcloudost-VirtualBox"
	port=8890
	s.connect((host,port))
	ack = s.recv(1024)
	print "ack from the service:",ack
	s.send(raw_input("Enter a value:"))
	resp = s.recv(10)
	print "response from the service:",resp
except Exception as err:
	print err
finally:
	s.close()