import math
class Localizador_ob:
    def __init__(self):# metodo constructor
        self.coordenada_centro={}# esto es un hashmap que guardara el centro de los objetos detectados
        self.conteo_obj=1

    def localizar(self,objetos):
        objetos_identificados=[] #aqui se guardan los objetos
        for figura in objetos:
            x,y,anchoo,alturaa=figura  #x y y son coordenadas que se imparten desde la parte superior izquiera
            punto_centralx= (x+x+anchoo)//2 #nos bota el punto central en x
            punto_centraly=(y+y+alturaa)//2 #nos botael punto central en y 
            #esto en caso
            objeto_detectado=False

            for id, pt in self.coordenada_centro.items():#pt es el iterador de nuestro array incial
                distancia_obj= math.hypot(punto_centralx-pt[0],punto_centraly-pt[1])#

                if distancia_obj<30:
                    self.coordenada_centro[id]=(punto_centralx,punto_centraly)
                    #print(self.coordenada_centro)
                    objetos_identificados.append([x,y,anchoo,alturaa,id])
                    objeto_detectado=True
                    break
            if objeto_detectado is False:
                self.coordenada_centro[self.conteo_obj]=(punto_centralx,punto_centraly)
                objetos_identificados.append([x,y,anchoo,alturaa,self.conteo_obj])
                self.conteo_obj+=1 #se aumenta el numero de los objetos detectados
        return objetos_identificados


