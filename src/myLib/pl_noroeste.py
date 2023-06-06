# Created by: Jesus Capriel 5-06-2023

class PLNoroeste:
    def __init__(self, matt):
        self.mat = matt
        self.result = 0

        self.matriz_costos = [] # Matriz que almacena los costos de transporte

        # Recorro las cols y rows -1 de la matriz original y asigna los costos a la matriz mat
        # Despues de asginar el varlor lo vuelve 0
        for i in range(len(self.mat)-1):
            self.matriz_costos.append([])
            for j in range(len(self.mat[0])-1):
                self.matriz_costos[i].append(int(self.mat[i][j]))
                self.mat[i][j] = 0

        # De string a int matriz mat
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.mat[i][j] = int(self.mat[i][j])
        
        print("Matriz")
        print(self.mat)
        print("Matriz de costos")
        print(self.matriz_costos)

        # Parametros iniciales
        self.x = 0
        self.y = 0
        self.l_y = 0
        self.l_x = 0
        self.flag = True

    def OfferGreaterDemand(self, x, y):
        self.mat[y][x] = self.mat[self.l_y][x] # Cubro toda la demanda
        self.mat[y][self.l_x] = self.mat[y][self.l_x] - self.mat[self.l_y][x] # Resto la oferta
        self.mat[self.l_y][x] = 0 # Demanda a 0

        for i in range(y + 1, self.l_y, 1): # Tachar columna
            self.mat[i][x] = -1
        
        self.x = x + 1 # Moverse una posicion en x
        
    
    def OfferLessThanDemand(self, x, y):
        self.mat[y][x] = self.mat[y][self.l_x] # Cubro la demanda que pueda
        self.mat[self.l_y][x] = self.mat[self.l_y][x] - self.mat[y][self.l_x] # Resto la demanda
        self.mat[y][self.l_x] = 0 # La oferta queda en 0

        for i in range(x + 1, self.l_x, 1): # Tachar fila
            self.mat[y][i] = -1
        
        self.y = y + 1 # Moverse una posicion en y

    def OfferEqualsDemand(self, x, y):
        self.mat[y][x] = self.mat[y][self.l_x] # Cubro la demanda que pueda
        self.mat[self.l_y][x] = 0 # La demanda quda en 0
        self.mat[y][self.l_x] = 0 # La oferta queda en 0

        for i in range(x + 1, self.l_x, 1): # Tachar fila
            self.mat[y][i] = -1

        for i in range(y + 1, self.l_y, 1): # Tachar columna
            self.mat[i][x] = -1
        
        self.x = x + 1 # Moverse una posicion en x
        self.y = y + 1 # Moverse una posicion en y

    def solve(self):
        # Valores constantes que al combinarlos con x, y podemos obtener el balro de la oferta o demanda
        self.l_y = len(self.mat) - 1
        self.l_x = len(self.mat[0]) - 1

        print("Operaciones")
        # Ciclo que se ejectua hasta que se resuelva la matriz
        while (self.flag):
            # El valor de la matriz[x][y] debe ser igual a 0 y menor a las constantes de demanda y ofertea
            if (self.mat[self.y][self.x] == 0 and self.x < self.l_x and self.y < self.l_y):
                if (self.mat[self.y][self.l_x] > self.mat[self.l_y][self.x]):
                    self.OfferGreaterDemand(self.x, self.y)
                    print(" oferta mayor demanda")
                elif (self.mat[self.y][self.l_x] < self.mat[self.l_y][self.x]):
                    self.OfferLessThanDemand(self.x, self.y)
                    print(" oferta menor demanda")
                elif (self.mat[self.y][self.l_x] == self.mat[self.l_y][self.x]):
                    self.OfferEqualsDemand(self.x, self.y)
                    print(" oferta igual demanda")
            else:
                self.flag = False

        print("Matriz resuelta")

        r_matriz = []
        for i in range(len(self.mat)-1):
            r_matriz.append([])
            for j in range(len(self.mat[0])-1):
                if (self.mat[i][j] == -1):
                    r_matriz[i].append(0)
                else:
                    r_matriz[i].append(self.mat[i][j])

        print(r_matriz)

        # Suma de los productos de matriz de costos * asignacion
        for i in range(len(r_matriz)):
            for j in range(len(r_matriz[0])):
                self.result = int(r_matriz[i][j] * self.matriz_costos[i][j]) + self.result

        print('El resultado es: ' + str(self.result))

