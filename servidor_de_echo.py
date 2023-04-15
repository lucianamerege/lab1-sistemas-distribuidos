# passivo

import socket

HOST = ''
PORTA = 5000

sock = socket.socket()

sock.bind((HOST, PORTA))

sock.listen(1)

print("Esperando conexões")

novoSock, endereco = sock.accept()

print("Conectado com ", endereco)

while True:
    # aqui eu precisei usar o decode senão dava erro
    # quando o cliente fechava a conexao
    msg = novoSock.recv(1024).decode()
    if not msg:
        break
    else:
        novoSock.send(msg.encode())

novoSock.close()

print("Conexao com ", endereco, " fechada.")

sock.close()

print("Desligando")
