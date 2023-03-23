import socket

tablero = [
    [''] * 3,
    [''] * 3,
    [''] * 3,
]

tablero5_5= [
    [''] * 5,
    [''] * 5,
    [''] * 5,
    [''] * 5,
    [''] * 5,
]


# Función para imprimir el tablero
def imprimir_tablero():
    global tablero
    for fila in tablero:
        print(" ")
        print(fila)

def imprimir_tablero5_5():
    global tablero5_5
    for fila in tablero5_5:
        print(" ")
        print(fila)

def ocupada(fila, columna):
    if tablero[fila][columna] == '':
        return False
    else:
        return True

def ocupada5_5(fila, columna):
    if tablero5_5[fila][columna] == '':
        return False
    else:
        return True

def enviar_datos(fila, columna):
    TCPCLientSocket.send(fila.encode())
    TCPCLientSocket.send(columna.encode())

def jugador(fila, columna):
    global tablero
    while True:
        if not ocupada(fila, columna):
            tablero[fila][columna] = 'X'
            break
        else:
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna"))
            a = str(fila)
            b = str(columna)
            enviar_datos(a, b)

def jugador5_5(fila, columna):
    global tablero5_5
    while True:
        if not ocupada5_5(fila, columna):
            tablero5_5[fila][columna] = 'X'
            break
        else:
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna"))
            a = str(fila)
            b = str(columna)
            enviar_datos(a, b)


def computadora():
    global tablero
    
    while True:
        fila = int(TCPCLientSocket.recv(buffer_size).decode())
        columna = int(TCPCLientSocket.recv(buffer_size).decode())
        if not ocupada(fila, columna):
            tablero[fila][columna] = 'O'
            break
        #else:
            #fila = int(TCPCLientSocket.recv(buffer_size).decode())
            #columna = int(TCPCLientSocket.recv(buffer_size).decode())

def computadora5_5():
    global tablero5_5
    
    while True:
        fila = int(TCPCLientSocket.recv(buffer_size).decode())
        columna = int(TCPCLientSocket.recv(buffer_size).decode())
        if not ocupada5_5(fila, columna):
            tablero5_5[fila][columna] = 'O'
            break
        #else:
            #fila = int(TCPCLientSocket.recv(buffer_size).decode())
            #columna = int(TCPCLientSocket.recv(buffer_size).decode())

def ganador(tiro):
    global tablero
    if ((tablero[0][0] == tablero[0][1] == tablero[0][2] == tiro) or (tablero[1][0] == tablero[1][1] == tablero[1][2] == tiro) or (tablero[2][0] == tablero[2][1] == tablero[2][2] == tiro) or
       (tablero[0][0] == tablero[1][0] == tablero[2][0] == tiro) or (tablero[0][1] == tablero[1][1] == tablero[2][1] == tiro) or (tablero[0][2] == tablero[1][2] == tablero[2][2] == tiro) or
       (tablero[0][0] == tablero[1][1] == tablero[2][2] == tiro) or (tablero[0][2] == tablero[1][1] == tablero[2][0] == tiro)):
       return True
    else:
        return False

def ganador5_5(tiro):
    global tablero5_5
    if ((tablero5_5[0][0] == tablero5_5[0][1] == tablero5_5[0][2] == tablero5_5[0][3] == tablero5_5[0][4] == tiro) or (tablero5_5[1][0] == tablero5_5[1][1] == tablero5_5[1][2] == tablero5_5[1][3] == tablero5_5[1][4] == tiro) or (tablero5_5[2][0] == tablero5_5[2][1] == tablero5_5[2][2] == tablero5_5[2][3] == tablero5_5[2][4] == tiro) or (tablero5_5[3][0] == tablero5_5[3][1] == tablero5_5[3][2] == tablero5_5[3][3] == tablero5_5[3][4] == tiro) or (tablero5_5[4][0] == tablero5_5[4][1] == tablero5_5[4][2] == tablero5_5[4][3] == tablero5_5[4][4] == tiro) or
       (tablero5_5[0][0] == tablero5_5[1][0] == tablero5_5[2][0] == tablero5_5[3][0] == tablero5_5[4][0] == tiro) or (tablero5_5[0][1] == tablero5_5[1][1] == tablero5_5[2][1] == tablero5_5[3][1] == tablero5_5[4][1] == tiro) or (tablero5_5[0][2] == tablero5_5[1][2] == tablero5_5[2][2] ==  tablero5_5[3][2] == tablero5_5[4][2] == tiro) or (tablero5_5[0][3] == tablero5_5[1][3] == tablero5_5[2][3] ==  tablero5_5[3][3] == tablero5_5[4][3] == tiro) or (tablero5_5[0][4] == tablero5_5[1][4] == tablero5_5[2][4] ==  tablero5_5[3][4] == tablero5_5[4][4] == tiro) or
       (tablero5_5[0][0] == tablero5_5[1][1] == tablero5_5[2][2] == tablero5_5[3][3] == tablero5_5[4][4] == tiro ) or (tablero5_5[0][4] == tablero5_5[1][3] == tablero5_5[2][2] == tablero5_5[3][1] == tablero5_5[4][0] == tiro)):
       return True
    else:
        return False

HOST = input("Ingrese la dirección IP del servidor") # IP del servidor
PORT = int(input("Ingrese el puerto")) # Puertos menores 1024, estan definidos por el SO
buffer_size = 1024 # Limitar el tamaño de los mensajes 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPCLientSocket:
    TCPCLientSocket.connect((HOST,PORT))
    recdif = TCPCLientSocket.recv(buffer_size).decode()
    print(recdif)
    dificultad = input()
    TCPCLientSocket.send(dificultad.encode())
    if dificultad == "principiante":
        while True:
            fila = input("Ingrese la fila: ")
            columna = input("Ingrese la columna: ")
            c = int(fila)
            d = int(columna)
            enviar_datos(fila, columna)
            jugador(c,d)
            imprimir_tablero()
            if ganador('X'):
                recibido = TCPCLientSocket.recv(buffer_size).decode()
                print(recibido)
                break

            computadora()
            imprimir_tablero()
            if ganador('O'):
                recibido = TCPCLientSocket.recv(buffer_size).decode()
                print(recibido)
                break

    elif dificultad == "experto":
        while True:
            fila = input("Ingrese la fila: ")
            columna = input("Ingrese la columna")
            c = int(fila)
            d = int(columna)
            enviar_datos(fila, columna)
            jugador5_5(c,d)
            imprimir_tablero5_5()
            if ganador5_5('X'):
                recibido = TCPCLientSocket.recv(buffer_size).decode()
                print(recibido)
                break

            computadora5_5()
            imprimir_tablero5_5()
            if ganador5_5('O'):
                recibido = TCPCLientSocket.recv(buffer_size).decode()
                print(recibido)
                break
    tiempo = TCPCLientSocket.recv(buffer_size).decode()
    print("\n")
    print(f'EL tiempo que duró la partida es: {tiempo}')
    