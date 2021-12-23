from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)

host = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]

clientSocket = socket(AF_INET,SOCK_STREAM)
try:
	clientSocket.connect((host,int(port)))
	
	clientSocket.send("GET /" + filename + " HTTP/1.1\r\n\r\n")
	clientSocket.send("\r\n".encode())
	output = clientSocket.recv(1024)
	print output
	
	clientSocket.close()

except IOError:
	clientSocket.send("HTTP/ 1.1 404 not Found \r\n\r\n")
	sys.exit()#Terminate the program after sending the corresponding data
