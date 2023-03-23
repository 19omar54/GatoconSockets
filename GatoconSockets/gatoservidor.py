import socket
from timeit import default_timer
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

def imprimir_tablero5_5():
    global tablero5_5
    for fila in tablero5_5:
        print(" ")
        print(fila)

# Función para imprimir el tablero
def imprimir_tablero():
    global tablero
    for fila in tablero:
        print(" ")
        print(fila)

def ocupada5_5(fila, columna):
    if tablero5_5[fila][columna] == '':
        return False
    else:
        return True

def ocupada(fila, columna):
    if tablero[fila][columna] == '':
        return False
    else:
        return True
    

def jugador():
    global tablero
    while True:
        fila = int(conn.recv(buffer_size).decode())
        columna = int(conn.recv(buffer_size).decode())
        if not ocupada(fila, columna):
            tablero[fila][columna] = 'X'
            break
        #else:
            #fila = int(conn.recv(buffer_size).decode())
            #columna = int(conn.recv(buffer_size).decode())

def jugador5_5():
    global tablero5_5
    while True:
        fila = int(conn.recv(buffer_size).decode())
        columna = int(conn.recv(buffer_size).decode())
        if not ocupada5_5(fila, columna):
            tablero5_5[fila][columna] = 'X'
            break
        #else:
            #fila = int(conn.recv(buffer_size).decode())
            #columna = int(conn.recv(buffer_size).decode())
            

def enviar_datos(fila1, columna1):
    conn.send(str(fila1).encode())
    conn.send(str(columna1).encode())
    
def computadora(fila, columna):
    global tablero
    while True:
        if not ocupada(fila, columna):
            tablero[fila][columna] = 'O'
            break
        else:
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna"))
            enviar_datos(fila, columna)

def computadora5_5(fila, columna):
    global tablero5_5
    while True:
        if not ocupada5_5(fila, columna):
            tablero5_5[fila][columna] = 'O'
            break
        else:
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna"))
            enviar_datos(fila, columna)

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

 # IP del servidor
HOST = '127.0.0.1'                                             
PORT = 65432 # Puertos menores 1024, estan definidos por el SO -> 1023 son puertos de escucha
buffer_size = 1024 # Limitar el tamño de los mensajes 

# Colocamos el servidor en modo escucha
                    # estamos usando el protocolo ip    Stream, usamos el protocolo TCP
                    # de red version 4

# Justificación Este tipo de sockets establece conexión antes de la comunicación y garantiza la consistencia 
# en los bytes de los datos que se reciben y en la secuencia de envío.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    conectar = "Ingrese la dirección IP a la que se desea conectar"
    TCPServerSocket.bind((HOST,PORT)) # crea el canal de comunicación entre el puerto y el objeto socket
    TCPServerSocket.listen() # Pone el estado del protocolo en listo, empieza a aceptar las conecciones y recibir las solicitudes
    conn, addr = TCPServerSocket.accept() # Genera la conexión 
    with conn:
        print(f"Conectado a: {addr}: ")
        inicio = default_timer()
        nivel = "Digite la dificultad del juego"
        conn.send(nivel.encode())
        dificultad = conn.recv(buffer_size).decode()
        print(f'Se recibió la dificultad: {dificultad}')
        if dificultad == 'principiante':
            while True:                                       
                jugador()
                imprimir_tablero()
                if ganador('X'):
                    mensaje = "Ganaste!!!"
                    conn.send(mensaje.encode())
                    break
                fila = int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna"))
                enviar_datos(fila, columna)
                computadora(fila, columna)
                imprimir_tablero()
                if ganador('O'):
                    mensaje = "¡Ganó el jugador que se encuentra en el servidor!"
                    conn.send(mensaje.encode())               
                    break
        elif dificultad == 'experto':
            while True:                                       
                jugador5_5()
                imprimir_tablero5_5()
                if ganador5_5('X'):
                    mensaje = "Ganaste!!"
                    conn.send(mensaje.encode())
                    break
                fila = int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna"))
                enviar_datos(fila, columna)
                computadora5_5(fila, columna)
                imprimir_tablero5_5()
                if ganador5_5('O'):
                    mensaje = "Ganó el jugador que se encuentra en el servidor"
                    conn.send(mensaje.encode())               
                    break
        fin = default_timer()
        tiempo = fin - inicio
        tiempoPartida = str(tiempo)
        conn.send(tiempoPartida.encode())  



    

        
        





