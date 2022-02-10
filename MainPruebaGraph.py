import random
import Graph as gp

def main():
    graficas=gp.Graph()
    times=random.randint(35,45)
    for i in range(times):
        #Simula la detección de carros

        if(i==times//2):
            #Simula que se presiona el botón de mostrar grafica
            graficas.graficarYMostrar()
            graficas=gp.Graph(graficas)

        #Faltaría la captura pero pues luego...
        temp= [i,random.randint(30,80),random.choice([True,False])]
        graficas.guardarCarros(temp)
    graficas.graficarYMostrar()