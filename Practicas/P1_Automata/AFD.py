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

    En un AFD un mismo símbolo solo puede conducir a un estado desde un mismo estado, es decir, un AFN
    mas pequeño
"""

from AFN import AFN

# ---- Funcion de validacion ---- #
class AFD(AFN):
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
            
            # Revisa las transiciones hasta encontrar las que corresponden al esatdo actual
            for t in self.transiciones:
                if t.edo_act == self.estados_actuales[0]:
                    if t.simb == s:
                        self.estados_actuales[0] = t.edo_sig
                        break # Ya encontro la transicion, procede

        # Ve si termino en un estado final
        if self.estados_actuales[0] in self.estados_finales:
            return True
        elif  self.estados_actuales[0] == -1:
            print(' INVALIDO: Se llego a un estado de error')
            return False
        else:
             print(" INVALIDO: No se llego a un estado final, se llego a " + str(self.estados_actuales[0]))
             return False

                
# ---- Pruebas ----- #
#Af = AFD()
#print(Af)
#
#Af.addEstados([0, 1, 2])
#Af.addAlfabeto(['a', 'b'])
#Af.addEdoInic(0)
#Af.addEdosFin([2])
#Af.addTransicion(0,'a',0)
#Af.addTransicion(0,'b',1)
#Af.addTransicion(1,'b',2)
#
#print(Af)
#print(Af.validarCadena('xaa'))
#print(Af.validarCadena('aa'))
#print(Af.validarCadena('aabb'))