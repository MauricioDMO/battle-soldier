class Juego:
    tablero = [[0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]]

    def llenar_tablero(tablero):
        soldados = 5

        while soldados > 0:
            print(f"Soldados restantes: {soldados}")
            posicion_x = input("Coordenadas del nuevo soldado (x): ")
            posicion_y = input("Coordenadas del nuevo soldado (y): ")

            try:
                tablero[int(posicion_y)][int(posicion_x)] = 1
            except ValueError:
                print("Debes escribir números enteros")
                continue

            soldados -= 1
    
    def atacar(tablero):
        
        while True:
            ataque_x = input("Ataque (x): ")
            ataque_y = input("Ataque (y): ")

            try:
                if tablero[int(ataque_y)][int(ataque_x)] == 1:
                    print("¡Le diste a uno!")

                    tablero[int(ataque_y)][int(ataque_x)] = 0
                else:
                    print("Fallaste")
                
                break
            except ValueError:
                print("Debes escribir números enteros")
    
    def juego_estado(tablero):
        terminado = True

        for i in range(4):
            for j in range(4):
                if tablero[i][j] == 1:
                    terminado = False
                    return terminado
                
        return terminado