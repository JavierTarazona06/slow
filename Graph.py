import random
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class Graph:
    #Elementos de la carpeta de archivos, por si se tiene que implementar uncommentar el import
#     self.ventana = Tk()
# 
#         self.ancho = self.ventana.winfo_screenwidth()
#         self.alto = self.ventana.winfo_screenheight()
    
    
    def __init__(self,ventana):
        #Toca pasar como parametro la ventana a la cual va a pertenecer 
        self.ventana=ventana
        self.ancho = self.ventana.winfo_screenwidth()
        self.alto = self.ventana.winfo_screenheight()
        self.DURACION= 100
        self.carros=[] # Aquí se guarda el carro mientras se da la instrucción de graficar
        
        self.construirFrames()
   
    def construirFrames(self):
        #Base Para Grafica, Botones y Tabla------------
        self.frame1 = tk.Frame(self.ventana, background="white")
        self.frame1.config(width=str(int(self.ancho*0.65)), height=self.alto)
        
        self.crearGrafico()
        
        self.frame2 = tk.Frame(self.ventana, background="#F0F0F0")
        self.frame2.config(width=str(int(self.ancho*0.35)), height=self.alto)
        
        self.estilarFrame2()
    
    def crearGrafico(self):
        #Crea el grafico con un unico subplot----------------
        self.grafica = Figure(figsize=((self.ancho*0.65/100),(self.alto/140)),dpi=100)
        self.area_dibujo = self.grafica.add_subplot(1,1,1)
    
        self.grafica.suptitle('Velocidades de Vehiculos')
        self.grafica.supxlabel("% Tiempo")
        self.grafica.supylabel("Velocidad(Km/h)")
    
    def estilarFrame2(self):
        #Añade estilo a la tabla de el frame2----------
        tipo_tabla= ttk.Style()
        tipo_tabla.map("Treeview", background=[("selected", "#76909c")])
        
        #Añade Tabla y boton al frame2-------------        
        self.tabla = ttk.Treeview(self.frame2, columns=("#1","#2","#3"), height=int(self.alto/22.995))
        self.tabla.pack(side = tk.TOP)
        self.tabla.heading("#1", text= "IdCarro")
        self.tabla.column("#1", width=int(self.ancho*0.185/3), anchor="center")
        self.tabla.heading("#2", text= "Velocidad")
        self.tabla.column("#2", width=int(self.ancho*0.185/3), anchor="center")
        self.tabla.heading("#3", text= "Infractor")
        self.tabla.column("#3", width=int(self.ancho*0.185/3), anchor="center")
        
        self.boton2= tk.Button(self.frame2, text="Retroceder", command= self.ocultarGraficos).pack(side = tk.TOP)
        
    def guardarCarros(self,datos):
        #Recibe una lista de datos [ID,Velocidad,Infractor]
        #Guarda los datos del carro para luego graficarlos y los añade a la tabla----------
        self.carros.append([datos[0],datos[1]])
        self.tabla.insert('',tk.END,values=(datos[0],datos[1],datos[2]))
            
        #Añadir Funcion para Guardar a la base de datos el carro infractor///
        #////

    def graficarYMostrar(self):
        self.graficar()
        
       #Añade y empaqueta los frames------------
        self.frame1.grid(row=0,column=0)
        self.tabla['show'] = 'headings'
        self.frame2.grid(row=0,column=1)
        
        #Añade y empaqueta el grafico al frame1 ----------
        canvas = FigureCanvasTkAgg(self.grafica,master=self.frame1)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP)
        
        #Añade y empaqueta el widget enlazandolo con el grafico (varias opciones implementadas)---------
        barratareas = NavigationToolbar2Tk(canvas,self.frame1)
        barratareas.update()
        canvas._tkcanvas.pack(side=tk.TOP)
    
    def graficar(self):
        #Grafica todos los carros guardados hasta ahora con una distancia entre datos fija-------
        distancia=(self.DURACION/len(self.carros))
        for i in range(len(self.carros)-1):
            #Escoge un color aleatorio para cada carro
            col = "#%06x" % random.randint(0, 0xFFFFFF)
            self.area_dibujo.plot([0,self.DURACION],[self.carros[i][1],self.carros[i][1]], color=col)
            self.area_dibujo.text((i+1)*distancia,(self.carros[i][1]-0.5),self.carros[i][0], fontsize="small")
    
    def ocultarGraficos(self):
        self.frame1.grid_forget()
        self.frame2.grid_forget()
