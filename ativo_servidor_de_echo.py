# ativo

import socket

HOST = 'localhost'
PORTA = 5000

sock = socket.socket()

sock.connect((HOST, PORTA))

print("Pronto para enviar mensagens. Digite e aperte enter.")

while True:
    msg = input("> ")
    if msg != 'fim':
        # eu precisei botar o ecode nos send pq sem eles eu
        # recebia o erro "a bytes-like object is required, not 'str'"
        sock.send(msg.encode('utf-8'))
        echo = sock.recv(1024)
        print(str(echo,  encoding='utf-8'))
    else:
        sock.send(msg.encode('utf-8'))
        break

sock.close()

print("Conexao encerrada")
