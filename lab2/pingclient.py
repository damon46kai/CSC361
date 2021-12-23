import random
import time
import sys
from socket import *

# Create a new datagram socket

	s = socket(AF_INET,SOCK_DGRAM)


host = str(sys.argv[1])
port = int(sys.argv[2])

# Loop to send 10 pings
for i in range(1,11):
	
	# Find the start time
	starttime = time.time()

	# Send the server the message (Ping sequence_number time)
	message = 'Ping ' + str(i) + ' ' + str(time.strftime('%H:%M:%S'))
	s.sendto(message, (host,port))

	# Set the timeout for 1 second
	s.settimeout(1)

	# If we receive the data, calculate RTT and print message
	try:
		data, addr = s.recvfrom(1024)
		receivetime = time.time()
		rttime = receivetime - starttime
		print(data + ' ' + str(rttime))

	# Exception if we time out
	except:
		print('Request timed out')
		continue

# Close socket, mission accomplished
s.close()
