"""
    Compiladores
    Escuela Superior de Computo
    Autor: Carlos Nevárez
    
    Este codigo simula a un Automata Finito No determinista, cuya representacion se da por la quintupla:
        - Q: Conjunto de N estados (indicados por digitos)
        - Sigma: Un alfabeto que indica los simbolos validos (Todo caracter que no se un digito)
        - Delta: Transiciones
        - S: Un estado inicial
        - F: Un conjunto de estados Finales
    tales que AFN = {Q, Sigma, Delta, S, F}

    En un AFN un mismo símbolo puede conducir a distintos estados desde un mismo esatdo
"""
from Transicion import Transicion

class AFN:
    # Constructor
    def __init__(self):
        # Quintupla
        self.estados = []
        self.alfabeto = []
        self.estado_inicial = 0
        self.estados_finales = []
        self.transiciones = []
        # Datos auxiliares
        self.estados_actuales = []

    # Para imprimir instancias
    def __str__(self):
        cadena = " Q:\t" + str(self.estados) + "\n"
        cadena += " Sigma:\t" + str(self.alfabeto) + "\n"
        cadena += " S:\t" + str(self.estado_inicial) +"\n"
        cadena += " F:\t" + str(self.estados_finales) + "\n"
        cadena += " Delta:"
        for tran in self.transiciones:
            cadena += "\t" + str(tran) + "\n"
        return cadena

    # ---- Funciones para agregar atributos al automata ---- # 
    # Para un estado
    def addEstado(self, estado):
        if estado not in self.estados:
            self.estados.add(estado)
        else:
            print(" El estado ya se encuentra en el conjunto de estados ")

    # Para un conjunto de estados
    def addEstados(self, estados):
        self.estados = estados
    
    # Para el conjunto de simbolos
    def addAlfabeto(self, alfabeto):
        self.alfabeto = alfabeto
    
    # Para el estado inicial
    def addEdoInic(self, estadoI):
        if estadoI in self.estados:
            self.estado_inicial = estadoI
        else:
            print(" El estado inicial debe estar en el conjunto de estados")

    # Para el conjunto de estados finales
    def addEdosFin(self, eFinales):
        self.estados_finales = eFinales

    # Para agregar una transicion
    def addTransicion(self, actual, caracter, siguiente):    
        self.transiciones.append(Transicion(actual, caracter, siguiente))

    # Voy a las tranciones que corresponden al estado actual, con base en el símbolo veo los estados siguientes
    def saltos(self, simbolo):
        saltosA = []
        for edo in self.estados_actuales:
            for t in self.transiciones:
                if edo == t.edo_act and t.simb == simbolo:
                    # Agrega estado siguiente correspondiente 
                    saltosA.append(t.edo_sig)

        return saltosA

    # ---- Funcion de validacion ---- #
    def validarCadena(self, cadena):
        print(" Validando " + cadena)
        # Se coloca el estado actual en el estado inicial
        self.estados_actuales = []
        self.estados_actuales.append(self.estado_inicial)
        
        # Recorre la cadena simbolo por simbolo
        for s in cadena:
            # Si el simbolo no pertenece al alfabeto regresa Falso
            if s not in self.alfabeto:
                print(" El simbolo " + s + " no pertenece al alfabeto")
                return False
            
            # Veo que estados siguen
            edos_sigs = self.saltos(s)
            # Actualizo los estados actuales
            self.estados_actuales = []
            self.estados_actuales.extend(edos_sigs)

        # Verifica en que estados termino para ver si es una cadena valida
        for edo in self.estados_actuales:
            if edo in self.estados_finales:
                return True
        
        # Verifica porque no es una cadena valida
        for edo in self.estados_actuales:
            if edo == -1:
                print(' INVALIDO: Se llego a un estado de error')
            else:
                print(" INVALIDO: No se llego a un estado final, se llego a " + str(edo))

        return False

# ---- Pruebas ----- #
#Af = AFN()
#print(Af)
#
#Af.addEstados([0, 1, 2])
#Af.addAlfabeto(['a', 'b'])
#Af.addEdoInic(0)
#Af.addEdosFin([2])
#Af.addTransicion(0,'a',0)
#Af.addTransicion(0,'a',1)
#Af.addTransicion(0,'b',0)
#Af.addTransicion(1,'b',2)
#
#print(Af)
#
#print(Af.validarCadena('xaa'))
#print(Af.validarCadena('aa'))
#print(Af.validarCadena('ab'))