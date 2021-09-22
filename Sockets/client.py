import socket
import threading

cliente = input('Por favor, ingrese su usuario: ')

host = '127.0.0.1'
port = 55555

clientes = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientes.connect((host, port))

def recibe_mensaje():
    while True:
        try:
            alerta = clientes.recv(1024).decode('utf-8')
            if alerta == "@cliente":
                clientes.send(cliente.encode('utf-8'))
            else:
                print(mensaje)
        except:
            print("ERROR, el programa se cerrará.")
            clientes.close
            break


def escribe_mensaje():
    while True:
        alerta = f"{cliente}: {input('')}"
        clientes.send(message.encode('utf-8'))

receive_thread = threading.Thread(target = recibe_mensajes)
receive_thread.start()

write_thread = threading.Thread(target = escribe_mensajes)
write_thread.start()