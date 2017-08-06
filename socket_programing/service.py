import socket
try:
	s=socket.socket()
	host = "tcloudost-VirtualBox"
	port=8890
	s.bind((host,port))
	s.listen(6)
	print "waiting for the client request."
	co, cinfo = s.accept()
	co.send("connected successfully")
	inp = co.recv(10)
	print "input from the client",inp
	inp = int(inp)
	rep="EVEN" if inp%2==0 else "ODD"
	co.send(rep)
except Exception as err:
	print err
finally:
	s.close()
