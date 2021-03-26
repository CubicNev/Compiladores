"""
    Compiladores
    Escuela Superior de Computo
    Autor: Carlos Nevárez
    
    Este codigo es la abstraccion de la parte de Transicion de un Automata Finito
    Partes de una Transicion de la forma: T(q,a)=p
        - q es el estado actual
        - a es un simbolo alfa de un Alfabeto
        - p es el estado siguiente
"""

class Transicion:
    # Constructor
    def __init__(self, edo_act, simb, edo_sig):
        self.edo_act = edo_act
        self.simb = simb
        self.edo_sig = edo_sig

    # --- Funciones para imprimir instacias --- #
    def __repr__(self):
        cadena = "[" + str(self.edo_act) + ",'" + self.simb + "'," + str(self.edo_sig) + "]"
        return cadena

    def __str__(self):
        cadena = "[" + str(self.edo_act) + ",'" + self.simb + "'," + str(self.edo_sig) + "]"
        return cadena

    # Funcion que devuelve unicamente los campos: estado actual y simbolo; en forma de una cadena
    def darRegistro(self):
        return str(self.edo_act) + self.simb