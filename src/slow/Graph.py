from tkinter import * 
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from .paths import graph_path, path_string
from .window_icon import set_window_icon

class Graph:
    
    def __init__(self, *args):
        #Toma argumentos que puede ser la base de datos con el idvideo, idvia y la multa
        #o un objeto de tipo grafica anterior para seguir graficando con datos anteriores
        if(len(args)==2):
            self.ongoingConstructor(args)
        else: self.mainConstructor(args[0])
        
    def mainConstructor(self,idVideo):
        self.pathToSaveGraphs = path_string(graph_path(f"GraficaVideo-{idVideo}.png"))
        #Si no hay argumentos crea todo desde cero
        self.ventana=Tk()
        self.ventana.resizable(False,False)
        self.ventana.title("SLOW - Graphs and Data")
        set_window_icon(self.ventana)
        self.ventana.withdraw()

        self.ancho = 1120
        self.alto = 630
        
        self.ventana.geometry("{0}x{1}".format(self.ancho,self.alto))
        self.DURACION= 100
        self.limiteVelocidad = None
        self.carros=[] # Aquí se guarda el carro mientras se da la instrucción de graficar
        
        self.construirFrames()
        
    def ongoingConstructor(self, args):
        self.pathToSaveGraphs = args[0].pathToSaveGraphs
        #Si hay argumentos agrega los vehículos ya creados y establece el tamaño de ventana facilmente
        self.ventana=Tk()
        self.ventana.resizable(False,False)
        self.ventana.title("SLOW - Graphs and Data")
        set_window_icon(self.ventana)
        self.ventana.withdraw()
        
        self.ancho = args[0].ancho
        self.alto = args[0].alto
        
        self.ventana.geometry("{0}x{1}".format(self.ancho,self.alto))
        self.DURACION= args[0].DURACION
        self.limiteVelocidad = args[0].limiteVelocidad
        self.carros= args[0].carros
        
        self.construirFrames()
        
        #Finalmente añade los datos de la tabla anterior a la nueva tabla luego de creada
        for datos in self.carros:
            self.tabla.insert('',END,values=(datos[0],datos[1],datos[2]))
        
    def construirFrames(self):
        #Base Para Grafica, Botones y Tabla------------
        self.frame1 = Frame(self.ventana, background="white")
        self.frame1.config(width=str(int(self.ancho*0.65)), height=self.alto)
        
        self.crearGrafico()
        
        self.frame2 = Frame(self.ventana, background="#F0F0F0")
        self.frame2.config(width=str(int(self.ancho*0.35)), height=self.alto)
        
        self.estilarFrame2()
    
    def crearGrafico(self):
        #Crea el grafico con un unico subplot----------------
        self.grafica = Figure(figsize=((self.ancho*0.65/100),(self.alto/133.8)),dpi=118)
        self.area_dibujo = self.grafica.add_subplot(1,1,1)

        self.grafica.suptitle("Detected Vehicle Speeds")
        self.grafica.supxlabel("Detected vehicle")
        self.grafica.supylabel("Speed (km/h)")
    
    def estilarFrame2(self):
        #Añade estilo a la tabla de el frame2----------
        tipo_tabla= ttk.Style()
        tipo_tabla.map("Treeview", background=[("selected", "#76909c")])
        
        #Añade Tabla y boton al frame2-------------        
        self.tabla = ttk.Treeview(self.frame2, columns=("#1","#2","#3"), height=int(self.alto/22))
        self.tabla.pack(side = TOP)
        self.tabla.heading("#1", text= "Vehicle ID")
        self.tabla.column("#1", width=int(self.ancho*0.19/3), anchor="center")
        self.tabla.heading("#2", text= "Speed")
        self.tabla.column("#2", width=int(self.ancho*0.19/3), anchor="center")
        self.tabla.heading("#3", text= "Over limit")
        self.tabla.column("#3", width=int(self.ancho*0.19/3), anchor="center")
        
        self.boton2= Button(self.frame2, text="Back", command= self.ventana.destroy).pack(side = TOP)
        
    def guardarCarros(self,datos):
        #Recibe una lista de datos [ID,Velocidad,Infractor, Captura]
        #Guarda los datos del carro para luego graficarlos y los añade a la tabla----------
        carro = [datos[0],round(float(datos[1]), 2), bool(datos[2])]
        if carro[0] in [item[0] for item in self.carros]:
            return
        self.carros.append(carro)
        self.tabla.insert('',END,values=(carro[0],f"{carro[1]:.2f} km/h","Yes" if carro[2] else "No"))
        
    def graficarYMostrar(self):
        self.graficar()
        self.grafica.savefig(self.pathToSaveGraphs)
       #Añade y empaqueta los frames------------
        self.frame1.grid(row=0,column=0)
        self.tabla['show'] = 'headings'
        self.frame2.grid(row=0,column=1)
        
        #Añade y empaqueta el grafico al frame1 ----------
        canvas = FigureCanvasTkAgg(self.grafica,master=self.frame1)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP)
        
        #Añade y empaqueta el widget enlazandolo con el grafico (varias opciones implementadas)---------
        barratareas = NavigationToolbar2Tk(canvas,self.frame1)
        barratareas.update()
        canvas._tkcanvas.pack(side=TOP)
        
        self.ventana.update()
    
    def graficar(self):
        self.area_dibujo.clear()
        self.area_dibujo.set_title("Speed by Detected Vehicle")
        self.area_dibujo.set_xlabel("Vehicle ID")
        self.area_dibujo.set_ylabel("Speed (km/h)")
        self.area_dibujo.grid(axis="y", linestyle="--", alpha=0.35)

        if len(self.carros) == 0:
            self.area_dibujo.text(
                0.5,
                0.5,
                "No vehicles were detected.",
                transform=self.area_dibujo.transAxes,
                ha="center",
                va="center",
                fontsize=13,
            )
            return

        carros = sorted(self.carros, key=lambda carro: carro[0])
        ids = [str(carro[0]) for carro in carros]
        velocidades = [carro[1] for carro in carros]
        colores = ["#d62728" if carro[2] else "#2ca02c" for carro in carros]

        barras = self.area_dibujo.bar(ids, velocidades, color=colores, edgecolor="#222222", linewidth=0.7)
        for barra, velocidad in zip(barras, velocidades):
            self.area_dibujo.text(
                barra.get_x() + barra.get_width() / 2,
                barra.get_height(),
                f"{velocidad:.1f}",
                ha="center",
                va="bottom",
                fontsize=8,
            )

        if self.limiteVelocidad is not None:
            self.area_dibujo.axhline(
                self.limiteVelocidad,
                color="#111111",
                linestyle="--",
                linewidth=1.2,
                label=f"Speed limit: {self.limiteVelocidad:g} km/h",
            )
            self.area_dibujo.legend(loc="upper right")

        margen_superior = max(velocidades + ([self.limiteVelocidad] if self.limiteVelocidad is not None else []))
        self.area_dibujo.set_ylim(0, max(margen_superior * 1.18, 10))
