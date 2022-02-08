import random
import Graph
def main():
    idvideo,idusuario,idvias,multa=1,2,3,900000
    graficas=Graph.Graph(idvideo,idusuario,idvias,multa)
    times=random.randint(35,45)
    for i in range(times):
        #Simula la detección de carros
        if(i==times//2):
            #Simula que se presiona el botón de mostrar grafica
            graficas.graficarYMostrar()
            graficas=Graph.Graph(graficas)
        #Faltaría la captura pero pues luego...
        temp= [i,random.randint(30,80),random.choice([True,False])]
        graficas.guardarCarros(temp)
    graficas.graficarYMostrar()
    
main()#----------------------------------------------------------