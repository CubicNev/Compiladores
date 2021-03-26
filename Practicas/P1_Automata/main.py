from Entrada import Entrada
from AFN import AFN 
from AFD import AFD
"""
    Compiladores
    Escuela Superior de Computo
    Autor: Carlos Nevárez

    Practica 1: Se valida cualquier automata (ya sea AFD o AFN), el cual entra por medio de un archivo .txt
                se completa este automata de entrada (si es que lo necesita) y se ingresan cadenas al automata ingresado 
                para saber si es valida o no dentro del lenguaje descrito por el mismo. Si la cadena llega a ser invalida 
                se especifica el porque.
"""
class main():
    def __init__(self):
        self.Af = None

        archivo = input(" Ingresa el nombre del archivo: ")
        entrada = Entrada(archivo)
        entrada.extraerAutomata()
        
        if entrada.esAFN():
            Af = AFN()
        else:
            Af = AFD()
        
        entrada.completarAF()
        print(" El automata esta dado por: ")
        #print(entrada)

        # Se pasa lo obtenido de la entrada a un Automata Finito
        Af.addEstados(entrada.estados)
        Af.addAlfabeto(entrada.alfabeto)
        Af.addEdoInic(entrada.estado_inicial)
        Af.addEdosFin(entrada.estados_finales)
        for transicion in entrada.transiciones:
            Af.addTransicion(transicion.edo_act, transicion.simb, transicion.edo_sig)
        
        while True:
            print(Af)
            cadena = input(" Ingresa una cadena a validar: ")
            if Af.validarCadena(cadena):
                print(" VALIDA: La cadena " + cadena + " pertenece al lenguaje descrito por el automata.")
            
            opc = input(" Ingresar otra cadena? (S/N): ")
            if opc == 'N':
                break

m = main()