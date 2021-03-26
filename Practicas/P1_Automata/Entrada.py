"""
    Compiladores
    Escuela Superior de Computo
    Autor: Carlos Nevárez

    El archivo a leer tiene la siguiente estructura:
    (Q)     0,1,2,3 -> Conjunto de enteros
    (Sigma) a,b     -> Conjunto de caracteres
    (S)     0       -> Entero
    (F)     2       -> Conjunto de enteros
    (Delta) 0,a,0   -> Lista (Entero, caracter, entero)
            0,b,0
            0,a,1
            1,b,2
            1,a,3
            2,a,3
            2,b,3
            3,a,3
            3,b,3
    Descripcion de la funcionalidad:
        - Leer el archivo linea por linea
        - Manejar la cadena leida y separar elementos por comas
        - Las primeras 4 lineas son de tuplas distintas, de la 5 en adelante es para transiciones
"""
from Transicion import Transicion

class Entrada:
    # Constructor
    def __init__(self, nomA):
        # Abro archivo en modo lectura
        self.entrada = open(nomA, 'r')
        
        # Guardo lineas en una lista
        self.lineas = self.entrada.readlines()

        # Quito el salto de línea que estorba
        for i in range(0, len(self.lineas)):
            self.lineas[i] = self.lineas[i].rstrip()

        # Atributos para pasar al automata
        self.estados = []
        self.alfabeto = []
        self.estado_inicial = 0
        self.estados_finales = []
        self.transiciones = []
    
    # Funcion para imprimir la Entrada
    def __str__(self):
        cadena = " Q:\t" + str(self.estados) + "\n"
        cadena += " Sigma:\t" + str(self.alfabeto) + "\n"
        cadena += " S:\t" + str(self.estado_inicial) +"\n"
        cadena += " F:\t" + str(self.estados_finales) + "\n"
        cadena += " Delta:"
        for tran in self.transiciones:
            cadena += "\t" + str(tran) + "\n"
        return cadena

    # ---- Manejo del texto de entrada ----- #
    # Se extrae linea a linea las características del automata
    def extraerAutomata(self):
        # Leer estados
        estados = self.lineas[0].split(',')
        self.estados = self.__pasar_IntList(estados)
        #print(self.estados)

        # Leer alfabeto
        self.alfabeto = self.lineas[1].split(',')
        #print(self.alfabeto)

        # Leer simbolo inicial
        self.estado_inicial = int(self.lineas[2])
        #print(self.estado_inicial)

        # Leer simbolos iniciales
        if len(self.lineas[3]) == 1:
            self.estados_finales = [int(self.lineas[3])]
            #print(self.estados_finales)
        else:
            edosFin = self.lineas[3].split(',')
            # Pasar los estados a digitos 
            self.estados_finales = self.__pasar_IntList(edosFin)
            #print(self.estados_finales)

        # Leer transiciones
        for linea in self.lineas[4:]:
            transicion = linea.split(',')
            self.transiciones.append(Transicion(int(transicion[0]), transicion[1], int(transicion[2])))
            #print(Transicion(int(transicion[0]), transicion[1], int(transicion[2])))
        #print(self.transiciones)

        self.entrada.close()

    # Pasar los estados a digitos para agregarlos a los estados del automata
    def __pasar_IntList(self, lista):
        for i in range(len(lista)):
            lista[i] = int(lista[i])
        return lista

    # ---- Funciones para completar el automata ---- #

    # Ve si es un AFN
    def esAFN(self):
        registros = []
        for t in self.transiciones:
            registros.append(t.darRegistro())
        
        if self.__hayRepetidos(registros):
            return True # Es un AFN
        else:
            return False # No es un AFN

    # Funcion para ver si hay elementos repetidos en una lista
    def __hayRepetidos(self, lista):
        revisado = []
        # Revisa elemento a elemento
        for elem in lista:
            if elem not in revisado:
                revisado.append(elem)
            else:
                return True
        
        return False

    # Se comprueba que cada estado tenga transiciones con todos los símbolos del alfabeto, los que no se tengan se agregan 
    def completarAF(self):
        fueCompletado = False
        # Por cada estado
        for edo in self.estados:
            #print(edo)
            # revisa cada simbolo
            for simb in self.alfabeto:
                esta = False
                #print("\t" + simb)
                for transi in self.transiciones:
                    #print("\t\t" + str(transi))
                    if (transi.edo_act == edo) and (transi.simb == simb):
                        esta = True
                        break
                if not esta:
                    # Agrega un transicion al estado de error
                    self.transiciones.append(Transicion(edo, simb, -1))
                    fueCompletado = True
        
        if fueCompletado:
            self.estados.append(-1)
                

# ---- Pruebas ----- #
#nombre = input(" Ingresa el nombre del archivo: ") 
#inic = Entrada('4.txt')
#inic.extraerAutomata()
#
#print(inic)
#
#if inic.esAFN():
#    print(" Es un AFN ")
#else:
#    print(" No es un AFN")
#
#inic.completarAF()
#print(inic)