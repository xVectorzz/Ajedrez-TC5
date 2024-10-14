import random
import pygame
import sys
import networkx as nx
import matplotlib.pyplot as plt
COLOR = {
    'black': 'BLACK',
    'white': 'WHITE'
}

class Cuadrado:
    def __init__(self, id, color):
        self._blancos = []
        self._negros = []
        self._id = id
        self._color = color

    @property
    def blancosAdj(self):
        return self._blancos

    @property
    def negrosAdj(self):
        return self._negros

    @property
    def identificador(self):
        return self._id

    @property
    def color(self):
        return self._color

    @property
    def blancos(self):
        return self._blancos

    @blancos.setter
    def blancos(self, blanco):
        self._blancos = blanco

    @property
    def negros(self):
        return self._negros

    @negros.setter
    def negros(self, negro):
        self._negros = negro


class Arbol:
    def __init__(self, estadofinal, archivoganador, archivomovimientos):
        self.movimientoSeleccionado = ''
        self.todosLosMov = open(archivomovimientos, 'w')
        self.movimientosGanadores = open(archivoganador, 'w')
        self.estadofinal = estadofinal

    def crearArbol(self, cadMovimientos, cuadradoActual, posPatronActMov, actual):
        if posPatronActMov > (len(cadMovimientos) - 1):
            if actual == '':
                actual = actual + str(cuadradoActual.identificador)
            else:
                actual = actual + ' ' + str(cuadradoActual.identificador)
            movimiento = actual.strip() + '\n'
            self.todosLosMov.write(movimiento)

            if actual.endswith(self.estadofinal):
                self.movimientosGanadores.write(movimiento)
                self.movimientoSeleccionado = actual.strip()
        else:
            patronAElegir = cadMovimientos[posPatronActMov]
            if patronAElegir == 'w':
                for cuadradoBlanco in cuadradoActual.blancosAdj:
                    self.crearArbol(
                        cadMovimientos,
                        cuadradoBlanco,
                        posPatronActMov + 1,
                        actual + ' ' + str(cuadradoActual.identificador)
                    )

            if patronAElegir == 'b':
                for cuadradoNegro in cuadradoActual.negrosAdj:
                    self.crearArbol(
                        cadMovimientos,
                        cuadradoNegro,
                        posPatronActMov + 1,
                        actual + ' ' + str(cuadradoActual.identificador)
                    )


class Tablero:
    def __init__(self):
        self.movJugUno = ''
        self.movJugDos = ''
        self.cuadrado1 = Cuadrado(1, COLOR['black'])
        self.cuadrado2 = Cuadrado(2, COLOR['white'])
        self.cuadrado3 = Cuadrado(3, COLOR['black'])
        self.cuadrado4 = Cuadrado(4, COLOR['white'])
        self.cuadrado5 = Cuadrado(5, COLOR['black'])
        self.cuadrado6 = Cuadrado(6, COLOR['white'])
        self.cuadrado7 = Cuadrado(7, COLOR['black'])
        self.cuadrado8 = Cuadrado(8, COLOR['white'])
        self.cuadrado9 = Cuadrado(9, COLOR['black'])
        self.cuadrado10 = Cuadrado(10, COLOR['white'])
        self.cuadrado11 = Cuadrado(11, COLOR['black'])
        self.cuadrado12 = Cuadrado(12, COLOR['white'])
        self.cuadrado13 = Cuadrado(13, COLOR['black'])
        self.cuadrado14 = Cuadrado(14, COLOR['white'])
        self.cuadrado15 = Cuadrado(15, COLOR['black'])
        self.cuadrado16 = Cuadrado(16, COLOR['white'])
        self.build_board()

    def set_player_one_move(self, move):
        self.movJugUno = move

    def set_player_two_move(self, move):
        self.movJugDos = move

    def generate_moves(self):
        if self.movJugUno and not self.movJugDos:
            tree = Arbol('16', 'ganadores.txt', 'movimientos.txt')
            tree.crearArbol(self.movJugUno, self.cuadrado1, 0, '')
            return {'moveForPlayerOne': tree.movimientoSeleccionado}
        else:
            arboljug1 = Arbol('16', 'ganadores.txt', 'movimientos.txt')
            arboljug2 = Arbol('13', 'ganadores2.txt', 'movimientos2.txt')
            arboljug1.crearArbol(self.movJugUno, self.cuadrado1, 0, '')
            arboljug2.crearArbol(self.movJugDos, self.cuadrado4, 0, '')
            return {
                'moveForPlayerOne': arboljug1.movimientoSeleccionado,
                'moveForPlayerTwo': arboljug2.movimientoSeleccionado
            }

    def build_board(self):
        self.cuadrado1._blancos = [self.cuadrado2, self.cuadrado5]
        self.cuadrado1._negros = [self.cuadrado6]

        self.cuadrado2._blancos = [self.cuadrado5, self.cuadrado7]
        self.cuadrado2._negros = [self.cuadrado1, self.cuadrado3, self.cuadrado6]

        self.cuadrado3._blancos = [self.cuadrado2, self.cuadrado4, self.cuadrado7]
        self.cuadrado3._negros = [self.cuadrado6, self.cuadrado8]

        self.cuadrado4._blancos = [self.cuadrado7]
        self.cuadrado4._negros = [self.cuadrado3, self.cuadrado8]

        self.cuadrado5._blancos = [self.cuadrado2, self.cuadrado10]
        self.cuadrado5._negros = [self.cuadrado1, self.cuadrado6, self.cuadrado9]

        self.cuadrado6._blancos = [self.cuadrado2, self.cuadrado5, self.cuadrado7, self.cuadrado10]
        self.cuadrado6._negros = [self.cuadrado1, self.cuadrado3, self.cuadrado9, self.cuadrado11]

        self.cuadrado7._blancos = [self.cuadrado2, self.cuadrado4, self.cuadrado10, self.cuadrado12]
        self.cuadrado7._negros = [self.cuadrado3, self.cuadrado6, self.cuadrado11, self.cuadrado8]

        self.cuadrado8._blancos = [self.cuadrado4, self.cuadrado7, self.cuadrado12]
        self.cuadrado8._negros = [self.cuadrado3, self.cuadrado11]

        self.cuadrado9._blancos = [self.cuadrado5, self.cuadrado10, self.cuadrado13]
        self.cuadrado9._negros = [self.cuadrado6, self.cuadrado14]

        self.cuadrado10._blancos = [self.cuadrado5, self.cuadrado7, self.cuadrado13, self.cuadrado15]
        self.cuadrado10._negros = [self.cuadrado6, self.cuadrado9, self.cuadrado11, self.cuadrado14]

        self.cuadrado11._blancos = [self.cuadrado7, self.cuadrado12, self.cuadrado15, self.cuadrado10]
        self.cuadrado11._negros = [self.cuadrado6, self.cuadrado8, self.cuadrado14, self.cuadrado16]

        self.cuadrado12._blancos = [self.cuadrado7, self.cuadrado15]
        self.cuadrado12._negros = [self.cuadrado8, self.cuadrado11, self.cuadrado16]

        self.cuadrado13._blancos = [self.cuadrado10]
        self.cuadrado13._negros = [self.cuadrado9, self.cuadrado14]

        self.cuadrado14._blancos = [self.cuadrado13, self.cuadrado10, self.cuadrado15]
        self.cuadrado14._negros = [self.cuadrado9, self.cuadrado11]

        self.cuadrado15._blancos = [self.cuadrado10, self.cuadrado12]
        self.cuadrado15._negros = [self.cuadrado14, self.cuadrado11, self.cuadrado16]

        self.cuadrado16._blancos = [self.cuadrado15, self.cuadrado12]
        self.cuadrado16._negros = [self.cuadrado11]


def get_last_move_for_one(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            movimientos = archivo.readlines()
            if movimientos:
                ultimo_movimiento = movimientos[-1].strip().split()
                ultimo_movimiento = list(map(int, ultimo_movimiento))
                return ultimo_movimiento
            else:
                return None
    except FileNotFoundError:
        return None
def generar_cadena_aleatoria():
    longitud = random.randint(3, 49)  # Longitud aleatoria entre 4 y 50
    cadena_aleatoria = ''.join(random.choice('wb') for _ in range(longitud))
    return cadena_aleatoria

def get_last_moves(player1_file, player2_file):
    with open(player1_file, 'r') as file:
        player1_moves = [list(map(int, line.strip().split())) for line in file.readlines()]

    with open(player2_file, 'r') as file:
        player2_moves = [list(map(int, line.strip().split())) for line in file.readlines()]

    last_player1_move = player1_moves[-1]
    last_player2_move = player2_moves[-1]

    collision_index = -1
    for i in range(min(len(last_player1_move), len(last_player2_move))):
        if last_player1_move[i] == last_player2_move[i]:
            collision_index = i
            break

    if collision_index != -1:
        print(f'Colisión en la casilla {last_player1_move[collision_index]}')
        print(f'En el movimiento {collision_index}')

        alternative_move_found = False

        with open(player2_file, 'r') as file:
            for line in file:
                moves = list(map(int, line.strip().split()))
                if moves[collision_index] != last_player2_move[collision_index]:
                    last_player2_move = moves
                    alternative_move_found = True
                    break

        if not alternative_move_found:
            print('No se pudo encontrar un camino alternativo para el jugador 2.')

    return last_player1_move, last_player2_move


# Ejemplo de uso

def main():

    board = Tablero()

    j = input("Desea 1 o 2 jugadores: \n")
    if j == '1':

        p= input("Desea ingresar una cadena o que sea generada aleatoriamente? 1.-Ingresar 2.-Aleatoria\n")
        if p== '1':
            cadena=input("Ingrese la cadena:\n")
            cadenaj1= cadena+'b'
            print("Las cadenas son: ")
            print("Jugador 1: ")
            print(cadenaj1)
            board.set_player_one_move(cadenaj1)
            board.generate_moves()
        else:
            cadena = generar_cadena_aleatoria()
            cadenaj1 = cadena + 'b'
            print("Las cadenas son: ")
            print("Jugador 1: ")
            print(cadenaj1)
            board.set_player_one_move(cadenaj1)
            board.generate_moves()
    elif j == '2':

        p = input("Desea ingresar una cadena o que sea generada aleatoriamente? 1.-Ingresar 2.-Aleatoria\n")
        if p == '1':
            cadena = input("Ingrese la cadena:\n")
            jugadorescogido= int(input("Quien desea que inicie presione 1.-Jug1 2.-Jug2"))
            cadenaj1 = cadena + 'b'
            cadenaj2 = cadena + 'w'
            print("Las cadenas son: ")
            print("Jugador 1: ")
            print(cadenaj1)
            print("Jugador 2: ")
            print(cadenaj2)
            board.set_player_one_move(cadenaj1)
            board.set_player_two_move(cadenaj2)
            board.generate_moves()
        else:
            cadena = generar_cadena_aleatoria()
            jugadorescogido= random.randint(1, 2)
            print(f"Inicia el jugador ",jugadorescogido)
            cadenaj1 = cadena + 'b'
            cadenaj2 = cadena + 'w'
            print("Las cadenas son: ")
            print("Jugador 1: ")
            print(cadenaj1)
            print("Jugador 2: ")
            print(cadenaj2)
            board.set_player_one_move(cadenaj1)
            board.set_player_two_move(cadenaj2)
            board.generate_moves()
    elif j != '1' or '2':
        print("Numero equivocado, cerrando el programa")
        exit(0)


    def crear_grafo_desde_archivo(nombre_archivo):
        grafo = nx.Graph()
        try:
            with open(nombre_archivo, 'r') as archivo:
                movimientos = archivo.readlines()
                for movimiento in movimientos:
                    nodos = list(map(int, movimiento.strip().split()))
                    for i in range(len(nodos) - 1):
                        grafo.add_edge(nodos[i], nodos[i + 1])
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
        return grafo

    opcionGrafos= input("Desea presentar los grafos disponibles? 1.-Si 2.-No")
    if opcionGrafos=='1':
        if j=='1':
            nombre_archivo = 'movimientos.txt'  # Reemplaza esto con el nombre de tu
            grafo = crear_grafo_desde_archivo(nombre_archivo)
            # Dibujar el grafo
            nx.draw(grafo, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')

            plt.title("Grafo de Movimientos")
            plt.show()
        else:
            nombre_archivo = 'movimientos.txt'  # Reemplaza esto con el nombre de tu
            grafo = crear_grafo_desde_archivo(nombre_archivo)
            # Dibujar el grafo
            nx.draw(grafo, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
            plt.title("Grafo de Movimientos Numero 1")
            plt.show()
            nombre_archivo2 = 'movimientos2.txt'
            grafo2 = crear_grafo_desde_archivo(nombre_archivo2)
            # Dibujar el grafo
            nx.draw(grafo2, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
            plt.title("Grafo de Movimientos Numero 2")
            plt.show()

    WIDTH, HEIGHT = 400, 400
    CELL_SIZE = 100
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tablero 4x4")

    def draw_board():
        for row in range(4):
            for col in range(4):
                color = WHITE if (row + col) % 2 == 0 else BLACK  # Alterna entre blanco y negro
                pygame.draw.rect(window, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)

    # Función para dibujar los jugadores en el tablero
    def draw_player1(player1_pos):
        pygame.draw.circle(window, RED,
                           (player1_pos[1] * CELL_SIZE + CELL_SIZE // 2, player1_pos[0] * CELL_SIZE + CELL_SIZE // 2),
                           CELL_SIZE // 3)

    def draw_player2(player2_pos):
        pygame.draw.circle(window, BLUE,
                           (player2_pos[1] * CELL_SIZE + CELL_SIZE // 2, player2_pos[0] * CELL_SIZE + CELL_SIZE // 2),
                           CELL_SIZE // 3)

    # Función para obtener las coordenadas a partir del número de casilla
    def get_coordinates(num):
        row = (num - 1) // 4
        col = (num - 1) % 4
        return row, col

    # Función para simular el movimiento del jugador en el tablero
    def simulate_movement(moves):
        positions = []
        for move in moves:
            row, col = get_coordinates(move)
            positions.append((row, col))
        return positions

    if j == '1':
        player1_file = 'ganadores.txt'
        last_player1_move = get_last_move_for_one(player1_file)
        print('Último movimiento del jugador 1:', last_player1_move)
        player1_positions = simulate_movement(last_player1_move)  # Simular movimientos para ambos jugadores
        print("Posiciones del jugador 1:")
        print(player1_positions)
    if j == '2' and jugadorescogido==1:
        player1_file = 'ganadores.txt'
        player2_file = 'ganadores2.txt'
        last_player1_move, last_player2_move = get_last_moves(player1_file, player2_file)
        print('Último movimiento del jugador 1:', last_player1_move)
        print('Último movimiento del jugador 2:', last_player2_move)
        player1_positions = simulate_movement(last_player1_move)
        player2_positions = simulate_movement(last_player2_move)  # Simular movimientos para ambos jugadores
        print("Posiciones del jugador 1:")
        print(player1_positions)
        print("Posiciones del jugador 2:")
        print(player2_positions)

    if j == '2' and jugadorescogido==2:
        player1_file = 'ganadores.txt'
        player2_file = 'ganadores2.txt'
        last_player2_move, last_player1_move = get_last_moves(player2_file, player1_file)
        print('Último movimiento del jugador 1:', last_player1_move)
        print('Último movimiento del jugador 2:', last_player2_move)
        player1_positions = simulate_movement(last_player1_move)
        player2_positions = simulate_movement(last_player2_move)  # Simular movimientos para ambos jugadores
        print("Posiciones del jugador 1:")
        print(player1_positions)
        print("Posiciones del jugador 2:")
        print(player2_positions)

    # Mostrar resultados

    totalTurnos = (len(player1_positions) * 2) - 2
    turnP1 = 0
    turnP2 = 0
    turn = 0
    colisionesturn1 = 0
    colisionesturn2 = 0
    if j=='2'and jugadorescogido==1:
        while True:
            window.fill((255, 255, 255))  # Limpiar la pantalla
            draw_board()  # Dibujar el tablero

            if turn - 1 == totalTurnos:
                print("Juego terminado ambos llegaron a su destino.")
                turn = 0
                turnP1 = 0
                turnP2 = 0
                colisionesturn1 = 0
                colisionesturn2 = 0
                cerrar = input("Si desea cerrar el juego escriba :1 en caso de que no, solo de enter...")
                if cerrar == '1':
                    pygame.quit()
                    sys.exit()
                print("Movimientos terminados el juego se repetira en 5 segundos...")
                pygame.time.wait(5000)
                print("Juego iniciando nuevamente...")

            if turn == 0:
                draw_player1(player1_positions[turn])
                draw_player2(player2_positions[turn])
                turn += 1
            elif (turn - (colisionesturn1 + colisionesturn2)) % 2 == 0:
                if turnP2 == len(player2_positions) - 1:
                    turnP1 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    turn += 1

                elif player1_positions[turnP1] == player2_positions[turnP2 + 1]:
                    print("Se detecto una colisión en la casilla: ")
                    print(player1_positions[turnP1])
                    print("Jugador 2 cede turno...")

                    turnP1 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    colisionesturn2 += 1

                    turn += 1
                else:
                    turnP2 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    turn += 1
            else:
                if turnP1 == len(player1_positions) - 1:
                    turnP2 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    turn += 1
                elif player1_positions[turnP1 + 1] == player2_positions[turnP2]:
                    print("Se detecto una colisión en la casilla: ")
                    print(player2_positions[turnP2])
                    print("Jugador 1 cede turno...")

                    turnP2 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    colisionesturn1 += 1

                    turn += 1
                else:
                    turnP1 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])

                    turn += 1

            if turnP1 == len(player1_positions) - 1:
                print("Player 1 ganó")
            elif turnP2 == len(player2_positions) - 1:
                print("Player 2 ganó")

            # Eventos del teclado y del ratón
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

            # Esperar un segundo antes de avanzar al siguiente turno (para visualizar mejor)
            pygame.time.wait(1500)
    elif j=='2' and jugadorescogido== 2:
        while True:
            window.fill((255, 255, 255))  # Limpiar la pantalla
            draw_board()  # Dibujar el tablero

            if turn - 1 == totalTurnos:
                print("Juego terminado ambos llegaron a su destino.")
                turn = 0
                turnP1 = 0
                turnP2 = 0
                colisionesturn1 = 0
                colisionesturn2 = 0
                cerrar = input("Si desea cerrar el juego escriba :1 en caso de que no, solo de enter...")
                if cerrar == '1':
                    pygame.quit()
                    sys.exit()
                print("Movimientos terminados el juego se repetira en 5 segundos...")
                pygame.time.wait(5000)
                print("Juego iniciando nuevamente...")

            if turn == 0:
                draw_player1(player1_positions[turn])
                draw_player2(player2_positions[turn])
                turn += 1
            elif (turn - (colisionesturn1 + colisionesturn2)) % 2 == 0:
                if turnP1 == len(player1_positions) - 1:
                    turnP2 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    turn += 1
                elif player1_positions[turnP1 + 1] == player2_positions[turnP2]:
                    print("Se detecto una colisión en la casilla: ")
                    print(player2_positions[turnP2])
                    print("Jugador 1 cede turno...")

                    turnP2 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    colisionesturn1 += 1

                    turn += 1
                else:
                    turnP1 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])

                    turn += 1
            else:
                if turnP2 == len(player2_positions) - 1:
                    turnP1 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    turn += 1

                elif player1_positions[turnP1] == player2_positions[turnP2 + 1]:
                    print("Se detecto una colisión en la casilla: ")
                    print(player1_positions[turnP1])
                    print("Jugador 2 cede turno...")

                    turnP1 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    colisionesturn2 += 1

                    turn += 1
                else:
                    turnP2 += 1
                    draw_player1(player1_positions[turnP1])
                    draw_player2(player2_positions[turnP2])
                    turn += 1

            if turnP2 == len(player2_positions) - 1:
                print("Player 2 ganó")
            elif turnP1 == len(player1_positions) - 1:
                print("Player 1 ganó")

            # Eventos del teclado y del ratón
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

            # Esperar un segundo antes de avanzar al siguiente turno (para visualizar mejor)
            pygame.time.wait(1500)


    elif j=='1':

        while True:
            window.fill((255, 255, 255))  # Limpiar la pantalla
            draw_board()  # Dibujar el tablero

            if turn==len(player1_positions):

                cerrar = input("Programa terminado si desea cerrar la animación escriba 1, si no, solo presione enter...")
                if cerrar == '1':
                    pygame.quit()
                    sys.exit()
                print("Movimientos terminados el juego se repetira en 5 segundos...")
                pygame.time.wait(5000)
                turn = 0
                print("Juego iniciando nuevamente...")

            draw_player1(player1_positions[turn])


            pygame.display.flip()

            # Esperar un segundo antes de avanzar al siguiente turno (para visualizar mejor)
            pygame.time.wait(1500)
            turn += 1

if __name__ == "__main__":
    main()