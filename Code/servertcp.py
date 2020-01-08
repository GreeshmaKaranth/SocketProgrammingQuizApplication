from socket import *
serverPort = 6000
b = 1024

x1 = "What is Marcel\'s favourite song? \n a. The Lion Sleeps Tonight \n b. The Macarena \n c. My Heart Will Go On"

x2 = 'What is Chandler\'s job? \n a. W.e.i.n.e.s.s processing \n b. Accountant \n c. Statistical Analysis and Data Compilation '

x3 =  'Who from Rachel\'s work called her Rocky?\n a. Her assistant\n b. The mailroom guys\n c. The copy guy'

x4 = 'What is Rachel\'s father\'s favourite drink? \n a. Scotch neat \n b. Scotch on the Rocks \n c. Scotch on the Rocks with a twist '

x5 = 'What was Emma\'s first word?\n a. Gleeba\n b. Dadda\n c. Bleega'

x6 = 'Who tried to take Rachel\'s job after her maternity leave?\n a. Ralph\n b. Gavin\n c. Stuart'

x7 = 'What is Ross allergic to?\n a. Ice Cream\n b. Kiwi\n c. Anchovies'

x8 = 'Who turns of the lamp at the end of the opening credits?\n a. Ross\n b. Chandler\n c. Monica'

x9 = 'What is the name of Joey\'s chair?\n a. Rosita\n b. Denise\n c. Hugsy'

x10 = 'What is the name of Chandler\'s crazy roommate?\n a. Kip\n b. Eddie\n c. Janine'

count = 0

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

while 1:
	connectionSocket, addr = serverSocket.accept()

	connectionSocket.send(x1.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'a'):
		count = count + 1

	connectionSocket.send(x2.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'c'):
		count = count + 1
	
	connectionSocket.send(x3.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'c'):
		count = count + 1
	
	connectionSocket.send(x4.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'c'):
		count = count + 1

	connectionSocket.send(x5.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'a'):
		count = count + 1
	
	connectionSocket.send(x6.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'a'):
		count = count + 1

	connectionSocket.send(x7.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'a'):
		count = count + 1
	
	connectionSocket.send(x8.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'c'):
		count = count + 1

	connectionSocket.send(x9.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'a'):
		count = count + 1

	connectionSocket.send(x10.encode())
	answer = connectionSocket.recv(b)
	if(answer.decode() == 'b'):
		count = count + 1
	
	connectionSocket.send(str(count).encode())
	connectionSocket.close()


# from socket import *
# serverPort = 12000
# serverSocket = socket(AF_INET,SOCK_STREAM)
# serverSocket.bind(('127.0.0.1',serverPort))
# serverSocket.listen(1)
# print ('The server is ready to receive')
# while 1:
# 	connectionSocket, addr = serverSocket.accept()
# 	sentence = connectionSocket.recv(1024)
# 	capitalizedSentence = (sentence.decode()).upper()
# 	connectionSocket.send(capitalizedSentence.encode())
# 	connectionSocket.close()
