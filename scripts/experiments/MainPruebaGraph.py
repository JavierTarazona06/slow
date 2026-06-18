import random
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from slow import Graph as gp

def main():
    graficas=gp.Graph(0)
    times=random.randint(35,45)
    for i in range(times):
        #Simula la detección de carros

        if(i==times//2):
            #Simula que se presiona el botón de mostrar grafica
            graficas.graficarYMostrar()
            graficas=gp.Graph(graficas, 0)

        #Faltaría la captura pero pues luego...
        temp= [i,random.randint(30,80),random.choice([True,False])]
        graficas.guardarCarros(temp)
    graficas.graficarYMostrar()


if __name__ == "__main__":
    main()
