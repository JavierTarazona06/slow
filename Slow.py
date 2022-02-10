from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import cv2, windnd, imutils
from functools import partial
import ConexionBaseDeDatosSlow as bD
import Imagenes, ArchivosYCarpetas, os
from tkinter import messagebox
import MAIN_DETECCION as Deteccion

# interfaz principal
class App:
  def __init__(self, root=None):
    
    
    self.root = root
    self.frame =Frame(self.root,bg='white',width=ancho,height=alto)
    self.PosBottonY=0.71
    self.widgets()
    self.frame.pack()
  # botones e imagenes de la interfaz
  def widgets(self):
    self.imSlow= ImInter(self.frame,"Logo_ SLOW.png", 0.5,0.1) 
    self.imSlow.create()

    self.imPolice= ImInter(self.frame,"Policia Nacional Logo.png", 0.1,0.1)
    self.imPolice.create()

    self.imColombia= ImInter(self.frame,"Colombia Slogan.png", 0.9,0.1)
    self.imColombia.create()

    self.imWelcome= ImInter(self.frame,"Bienvenido.png", 0.5,0.25)
    self.imWelcome.create()
    self.create_botton_info(0.2)
    self.create_botton_datos(0.35)
    self.create_botton_video(0.5) 
    self.create_botton_vias(0.65) 
    self.create_botton_history(0.8)

    self.imPerfil= ImInter(self.frame,imagenPerfilPath, 0.4,0.45)
    self.imPerfil.sizeImage(223,223)
    self.imPerfil.create()

    self.nombreUsuarioTit = Label(self.frame, text=f"{nombreUsuario}\n{apellidoUsuario}", bg="white", font=("",30,"bold"),justify=LEFT)
    self.nombreUsuarioTit.place(relx=0.519,rely=0.35)

    if jefe==0:
      self.usuarioTit = Label(self.frame, text=f"Usuario: {usuario} - ID SLOW: {idUsuario} - Jefe", bg="white", font=("",12,"italic"), justify=LEFT)
      self.usuarioTit.place(relx=0.519,rely=0.47)
    else:
      self.usuarioTit = Label(self.frame, text=f"Usuario: {usuario} - ID SLOW: {idUsuario} - Policía", bg="white", font=("",12,"italic"), justify=LEFT)
      self.usuarioTit.place(relx=0.519,rely=0.47)

    self.cuadranteTit = Label(self.frame, text=f"Cuadrante: {cuadrante} No. {numeroCuadrante}", bg="white", font=("",12,"italic"), justify=LEFT)
    self.cuadranteTit.place(relx=0.519,rely=0.5)

    self.ciudadTit = Label(self.frame, text=f"{ciudad}, {departamento}", bg="white", font=("",12,"italic"), justify=LEFT)
    self.ciudadTit.place(relx=0.519,rely=0.53)

    self.BottExit = BottInter(self.frame,"Cerrar Sesión.png",0.5,0.9,None,App.cerrarSesionBotonAccion)
    self.BottExit.modzise(130,50)
    self.BottExit.create()

    self.BottExit.panel.bind("<Enter>",self.enCerrarSesionBoton)
    self.BottExit.panel.bind("<Leave>",self.fueraCerrarSesionBoton)

  def cerrarSesionBotonAccion():
    root.destroy()
    from InicioSesion import VentanaInicioSesion
    ventanaInicioSesion = VentanaInicioSesion()
    ventanaInicioSesion.ventana.mainloop()

  def enCerrarSesionBoton(self, event):
    self.BottExit.panel.config(bd=2)
  
  def fueraCerrarSesionBoton(self, event):
    self.BottExit.panel.config(bd=0)

  def create_botton_info(self,positiony):
    self.positiony=positiony
    self.BottInfo = BottInter(self.frame,"Info icon.png",self.positiony,
      self.PosBottonY,'Información',self.make_page_info)
    self.BottInfo.create()
    
    self.open_create_text(self.BottInfo)

  def create_botton_datos(self,positiony):  

    self.positiony=positiony
    self.BottDatos = BottInter(self.frame,"Data Update Icon.png",self.positiony,self.PosBottonY,
    'Actualizar Datos',self.make_page_date)
    self.BottDatos.create()
    
    self.open_create_text(self.BottDatos)

  def create_botton_video(self,positiony):

    self.positiony=positiony
    self.BottVideo = BottInter(self.frame,"Video Speed Icon.png",self.positiony,self.PosBottonY,
     'Registrar Video',self.make_page_video)
    self.BottVideo.modzise(170,115)
    self.BottVideo.create()
    
    self.open_create_text(self.BottVideo)

  def create_botton_vias(self,positiony):
    
    self.positiony=positiony
    self.BottVias = BottInter(self.frame,"Vias Icon.png",self.positiony,self.PosBottonY,
    'Vehículos / Vías',self.make_page_vias)
    self.BottVias.modzise(170)
    self.BottVias.create()

    self.open_create_text(self.BottVias)

  def create_botton_history(self,positiony):

    self.positiony=positiony
    self.BottHistory = BottInter(self.frame,"History Icon.png",self.positiony,self.PosBottonY,
    'Histórico',self.make_page_history)
    self.BottHistory.create()
    
    self.open_create_text(self.BottHistory)
  
  def open_create_text(self,botton):
    
    self.botton=botton
    self.botton.createText()

  # volver a interfaz principal
  def main_page(self):
    self.frame.pack()
  # ir a interfaz de informacion
  def make_page_info(self):
    global ac
    ac=False
    self.page_info = info(master=self.root, app=self)
    self.frame.pack_forget()
    self.page_info.start_page()
  # ir a interfaz de datos
  def make_page_date(self):
    global ac
    ac=False
    self.page_date = Date(master=self.root, app=self)
    self.frame.pack_forget()
    self.page_date.start_page()
  
  def make_page_video(self):
    global ac
    ac=False
    self.page_video = video(master=self.root, app=self)
    self.frame.pack_forget()
    self.page_video.start_page()
  
  def make_page_vias(self):
    global ac
    ac=False
    self.page_vias = Vias(master=self.root, app=self)
    self.frame.pack_forget()
    self.page_vias.start_page()
  
  def make_page_history(self):
    global ac
    ac=False
    self.page_history = history(master=self.root, app=self)
    self.frame.pack_forget()
    self.page_history.start_page()

class menu(App):
  def __init__(self,name,root,app=None,additional=None):
    self.name=name
    self.root=root
    self.App=app
    self.additional=additional
    self.frame= Frame(self.root,bg='white',highlightbackground="black",
     highlightthickness=3,width=800,height=200)
    
    
    self.PosBottonY=0.4

    self.posBotton1=0.12
    self.posBotton2=0.36
    self.posBotton3=0.62
    self.posBotton4=0.88

    if self.name=="info":
      self.create_botton_datos(self.posBotton1)
      self.create_botton_video(self.posBotton2) 
      self.create_botton_vias(self.posBotton3) 
      self.create_botton_history(self.posBotton4)
    elif self.name=="datos":
      self.create_botton_info(self.posBotton1)
      self.create_botton_video(self.posBotton2) 
      self.create_botton_vias(self.posBotton3) 
      self.create_botton_history(self.posBotton4)

    elif self.name=="video":
      self.create_botton_info(self.posBotton1)
      self.create_botton_datos(self.posBotton2) 
      self.create_botton_vias(self.posBotton3) 
      self.create_botton_history(self.posBotton4)
    
    elif self.name=="vias":
      self.create_botton_info(self.posBotton1)
      self.create_botton_datos(self.posBotton2) 
      self.create_botton_video(self.posBotton3) 
      self.create_botton_history(self.posBotton4)
    else:
      self.create_botton_info(self.posBotton1)
      self.create_botton_datos(self.posBotton2) 
      self.create_botton_video(self.posBotton3) 
      self.create_botton_vias(self.posBotton4)

  def open_create_text(self,botton):
    
    self.botton=botton
    self.botton.createText(0.8)

  def start_page(self):
    self.frame.place(in_=self.root, anchor = CENTER, relx=.5, rely=.78)
    self.root.bind("<1>", self.on_click)
    if (self.additional != None):

      self.additional.bind("<1>", self.on_click)
    

  def on_click(self, event):
    global ac
    ac=False
    self.frame.destroy()
    

  
# grevy
class info:
  def __init__(self, master=None, app=None):
    self.master = master
    self.app = app
    self.frame = Frame(self.master,bg='white',width=ancho,height=alto)
    self.common_widgets()
    self.own_widgets()
    self.frame.pack()
    global ac
    ac=False

  def common_widgets(self):
  
    self.imSlow= ImInter(self.frame,"Logo_ SLOW.png", 0.5,0.1) 
    self.imSlow.create()

    self.imPolice= ImInter(self.frame,"Policia Nacional Logo.png", 0.1,0.1)
    self.imPolice.create()

    self.imColombia= ImInter(self.frame,"Colombia Slogan.png", 0.9,0.1)
    self.imColombia.create()

    self.police = ImInter(self.frame,f"{imagenPerfilPath}", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

    self.BottReturn = BottInter(self.frame,"Return Arrow Icon.png",0.4,0.9, None,self.go_back)
    self.BottReturn.modzise(70,70)
    self.BottReturn.create()
    
    self.BottMenu = BottInter(self.frame,"Menu icon.png",0.5,0.9,None,None,self)
    
    self.BottMenu.modzise(70,70)
    self.BottMenu.create()

  def own_widgets(self):
    self.iminfo= ImInter(self.frame,"Info icon.png", 0.8,0.06) 
    self.iminfo.sizeImage(80,80)
    self.iminfo.create()
    
    self.imRoad= ImInter(self.frame,"Imagen Carretera Velocidad.png", 0.5,0.33)
    self.imRoad.sizeImage(92,170)
    self.imRoad.create()
    
    self.Text="Información"
    self.Title1 = textInter(self.frame,self.Text,30,0.5,0.23)
    self.Title1.create_Tittle()

    self.Text="¿Qué es Slow?"
    self.Title2 = textInter(self.frame,self.Text,18,0.5,0.41)
    self.Title2.create_Tittle()

    self.Text="¿Qué roles hay en Slow?"
    self.Title3 = textInter(self.frame,self.Text,18,0.5,0.52)
    self.Title3.create_Tittle()

    self.Text="¿Qué funciones tengo en Slow?"
    self.Title4 = textInter(self.frame,self.Text,18,0.5,0.64)
    self.Title4.create_Tittle()

    self.Text="¿Como funciona la Detección en Slow?"
    self.Title5 = textInter(self.frame,self.Text,18,0.5,0.76)
    self.Title5.create_Tittle()

    self.Text="Slow es una aplicación de escitorio que permite detectar la velocidad de vehículos en carretera o en ciudad. Está enfocada a los organismos de índole\n policial y/o de tránsito de cualquier tipo de gobierno. Así mismo, Slow se puede usar para realizar estudios de tránsito urbano o rural."
    self.paragraph1 = textInter(self.frame,self.Text,12,0.5,0.45)
    self.paragraph1.create_paragraph()

    self.Text="Los roles disponibles dentro de Slow son el de polícia o jefe de polícia. La diferencia está en que el jefe de polícia podrá editar vías y vehículos mientras que\n el subordinado solo las podrá ver. Asi mismo, el jefe podrá ver los vídeos subidos por sus polícias asigandos."
    self.paragraph2 = textInter(self.frame,self.Text,12,0.5,0.59)
    self.paragraph2.create_paragraph()
    
    self.Text="El usuario puede actualizar sus datos en la aplicación, registrar (subir) videos para utilizar la función de detección de la velocidad de los vehículos, ver tipos\n de vehículos y vías junto con las restricciones (el jefe las puede editar) y por último el histórico de los videos subidos (el jefe puede ver los del equipo)."
    self.paragraph3 = textInter(self.frame,self.Text,12,0.5,0.7)
    self.paragraph3.create_paragraph()

    self.Text="Para detectar la velocidad de vehículos en movimiento se requiere subir a la aplicación un video grabado en ángulo picado en cámara alta que enfoque\n la carretera o calle donde se desea detectar de velocidad."
    self.paragraph4 = textInter(self.frame,self.Text,12,0.5,0.82)
    self.paragraph4.create_paragraph()
  
  def Open_menu(self,event=None):
    global ac
    self.name="info"
    if (ac== False):

      self.Menu = menu(self.name,root=self.frame, app=self)
      
    
      self.Menu.start_page()
      ac=True
  def start_page(self):
    self.frame.pack()

  def go_back(self):
    global ac
    ac=False
    self.frame.pack_forget()
    self.Principal = App(self.master)


# daniel
class Date(info):
  

  def own_widgets(self):
    self.inDate= ImInter(self.frame,"Data Update Icon.png", 0.8,0.06) 
    self.inDate.sizeImage(80,80)
    self.inDate.create()

    self.police = ImInter(self.frame,f"{imagenPerfilPath}", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

    self.tituloCrearCuenta = Label(self.frame, text="Actualizar Datos", bg="white", font=("",20,"bold"))
    self.tituloCrearCuenta.place(relx=0.43, rely=0.1944)

    self.xCol1, self.yCol1 = 0.0375, 0.28
    self.xCol1b, self.yCol1b = 0.146, 0.285
    self.xCol2, self.yCol2 = 0.383, 0.28
    self.xCol2b, self.yCol2b = 0.4925, 0.285
    self.xCol3, self.yCol3 = 0.6975, 0.28
    self.xCol3b, self.yCol3b = 0.806, 0.285
    self.altura = 0.088

    self.usuarioText = Label(self.frame, text="Usuario:", bg="white", font=("",17,"bold"))
    self.usuarioText.place(relx=self.xCol1, rely=self.yCol1)
    self.usuarioTexto = StringVar()
    self.usuarioEntrada = Entry(self.frame,bg="white",textvariable=self.usuarioTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.usuarioEntrada.place(relx=self.xCol1b, rely=self.yCol1b)
    self.usuarioTexto.set(f"{usuario}")

    self.contrasenaText = Label(self.frame, text="Contraseña:", bg="white", font=("",17,"bold"))
    self.contrasenaText.place(relx=self.xCol1, rely=self.yCol1+self.altura)
    self.contrasenaTexto = StringVar()
    self.contrasenaEntrada = Entry(self.frame,bg="white",textvariable=self.contrasenaTexto,fg="black", justify="left", font=(16), width=25, border=3, show="*")
    self.contrasenaEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura)
    self.contrasenaNota = Label(self.frame, text="*De 10 carácteres mínimo e incluya números.", bg="white", fg="red", font=("",8,""), justify="left")
    self.contrasenaNota.place(relx=self.xCol1b, rely=self.yCol1b+self.altura+0.03)
    self.contrasenaTexto.set("")

    self.ojoClaveAbiertoImg = PhotoImage(file="RecursosGraficos\\\OJOCLAVEABIERTO.png")
    self.ojoClaveAbiertoImg = self.ojoClaveAbiertoImg.subsample(15)
    self.ojoClaveBoton = Button(self.frame, image=self.ojoClaveAbiertoImg, command=self.abrirOjo,bg="white", border=1, relief="raised", cursor="hand2", bd=0)
    self.ojoClaveBoton.place(relx=self.xCol1b+0.153, rely=self.yCol1b+0.083)
    self.ojoClaveBoton.bind("<Enter>",self.enOjoClaveBoton)
    self.ojoClaveBoton.bind("<Leave>",self.fueraOjoClaveBoton)

    self.nombreText = Label(self.frame, text="Nombre:", bg="white", font=("",17,"bold"))
    self.nombreText.place(relx=self.xCol1, rely=self.yCol1+self.altura*2)
    self.nombreTexto = StringVar()
    self.nombreEntrada = Entry(self.frame,bg="white",textvariable=self.nombreTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.nombreEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*2)
    self.nombreTexto.set(f"{nombreUsuario}")

    self.apellidoText = Label(self.frame, text="Apellido:", bg="white", font=("",17,"bold"))
    self.apellidoText.place(relx=self.xCol1, rely=self.yCol1+self.altura*3)
    self.apellidoTexto = StringVar()
    self.apellidoEntrada = Entry(self.frame,bg="white",textvariable=self.apellidoTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.apellidoEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*3)
    self.apellidoTexto.set(f"{apellidoUsuario}")

    self.tipoDocumentoText = Label(self.frame, text="Tipo de\nDocumento:", bg="white", font=("",17,"bold"), justify="left")
    self.tipoDocumentoText.place(relx=self.xCol1, rely=self.yCol1+self.altura*4-0.011)
    self.tipoDocumentoEntrada = ttk.Combobox(self.frame, state="readonly")
    self.tipoDocumentoEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*4)
    self.tipoDocumentoList = ["C.C", "C.E", "T.P"]
    self.tipoDocumentoEntrada["values"] = self.tipoDocumentoList
    self.tipoDocumentoEntrada.current(self.tipoDocumentoList.index(tipoDocumento))

    self.numeroDocumentoText = Label(self.frame, text="Número de\nDocumento:", bg="white", font=("",17,"bold"), justify="left")
    self.numeroDocumentoText.place(relx=self.xCol1, rely=self.yCol1+self.altura*5-0.011)
    self.numeroDocumentoTexto = StringVar()
    self.numeroDocumentoEntrada = Entry(self.frame,bg="white",textvariable=self.numeroDocumentoTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.numeroDocumentoEntrada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*5)
    self.numeroDocumentoTexto.set(f"{numeroDocumento}")

    self.imagenPerfilText = Label(self.frame, text="Imagen de\nPerfil:", bg="white", font=("",17,"bold"), justify="left")
    self.imagenPerfilText.place(relx=self.xCol1, rely=self.yCol1+self.altura*6-0.011)
    self.imgPrlBoton = Button(self.frame,text="Subir Imagen",bg="black",fg="white", cursor="hand2", font=(40), bd=4, command=self.abrirArchivo)
    self.imgPrlBoton.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*6)
    self.imgPrlBoton.bind("<Enter>",self.enBotonImagenPerfil)
    self.imgPrlBoton.bind("<Leave>",self.fueraBotonImagenPerfil)
    self.confirmacionImagenCargada = Label(self.frame, text="No se ha cargado\nla imagen opcional", bg="white", font=(5), fg="red")
    self.confirmacionImagenCargada.place(relx=self.xCol1b, rely=self.yCol1b+self.altura*6+0.044)
    self.imagenPerfilEntrada = ""
    self.imPerfil= ImInter(self.frame,imagenPerfilPath, self.xCol1b+0.135,self.yCol1b+self.altura*6+0.03)
    self.imPerfil.sizeImage(100,100)
    self.imPerfil.create()

    self.tipoSangreText = Label(self.frame, text="Tipo de\nSangre:", bg="white", font=("",17,"bold"), justify="left")
    self.tipoSangreText.place(relx=self.xCol2, rely=self.yCol2-0.011)
    self.tipoSangreEntrada = ttk.Combobox(self.frame, state="readonly")
    self.tipoSangreEntrada.place(relx=self.xCol2b, rely=self.yCol2b)
    self.sangreList = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
    self.tipoSangreEntrada["values"] = self.sangreList
    self.tipoSangreEntrada.current(self.sangreList.index(tipoSangre))

    self.jefeText = Label(self.frame, text="ID Jefe:", bg="white", font=("",17,"bold"), justify="left")
    self.jefeText.place(relx=self.xCol2, rely=self.yCol2+self.altura)
    self.jefeDisplay = StringVar()
    self.jefeEntrada = Entry(self.frame,bg="white",fg="black", justify="left", font=(16), width=25, border=3, textvariable=self.jefeDisplay)
    self.jefeEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura)
    self.jefeTextNota = Label(self.frame, text="*Sí es policía, indique el ID de su jefe\nde la app Slow.", bg="white", fg="red", font=("",8,""), justify="left")
    self.jefeTextNota.place(relx=self.xCol2b, rely=self.yCol2b+self.altura+0.029)
    self.jefeDisplay.set(f"{jefe}")

    self.policiasAsignadosText = Label(self.frame, text="Policías\nAsignados:", bg="white", font=("",17,"bold"), justify="left")
    self.policiasAsignadosText.place(relx=self.xCol2, rely=self.yCol2+self.altura*2-0.011)
    self.policiasAsignadosDisplay = StringVar()
    self.policiasAsignadosEntrada = Entry(self.frame,bg="white",fg="black", justify="left", font=(16), width=25, border=3, textvariable=self.policiasAsignadosDisplay)
    self.policiasAsignadosEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*2)
    self.policiasAsignadosTextNota = Label(self.frame, text="*Sí es jefe de policía, indique el ID de sus\npolicías asignados separados por comas.", bg="white", fg="red", font=("",8,""), justify="left")
    self.policiasAsignadosTextNota.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*2+0.029)
    self.policiasAsignadosDisplay.set(f"{policiasAsignados}")

    self.asignacionText = Label(self.frame, text="Asignación:", bg="white", font=("",17,"bold"), justify="left")
    self.asignacionText.place(relx=self.xCol2, rely=self.yCol2+self.altura*3)
    self.asignacionEntrada = ttk.Combobox(self.frame, state="readonly")
    self.asignacionEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*3)
    self.asignacionEntrada["values"] = ["TRÁNSITO"]
    self.asignacionEntrada.current(0)

    self.rolText = Label(self.frame, text="Rol:", bg="white", font=("",17,"bold"), justify="left")
    self.rolText.place(relx=self.xCol2, rely=self.yCol2+self.altura*4)
    self.rolEntrada = Label(self.frame, text=f"{rol}", bg="white", font=("",17,"bold"), justify="left")
    self.rolEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*4)

    self.numeroCuadranteText = Label(self.frame, text="Número de\nCuadrante:", bg="white", font=("",17,"bold"), justify="left")
    self.numeroCuadranteText.place(relx=self.xCol2, rely=self.yCol2+self.altura*5-0.011)
    self.numeroCuadranteTexto = StringVar()
    self.numeroCuadranteEntrada = Entry(self.frame,bg="white", textvariable=self.numeroCuadranteTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.numeroCuadranteEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*5)
    self.numeroCuadranteTexto.set(f"{numeroCuadrante}")

    self.cuadranteText = Label(self.frame, text="Cuadrante:", bg="white", font=("",17,"bold"), justify="left")
    self.cuadranteText.place(relx=self.xCol2, rely=self.yCol2+self.altura*6)
    self.cuadranteTexto = StringVar()
    self.cuadranteEntrada = Entry(self.frame,bg="white", textvariable=self.cuadranteTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.cuadranteEntrada.place(relx=self.xCol2b, rely=self.yCol2b+self.altura*6)
    self.cuadranteTexto.set(f"{cuadrante}")

    self.ciudadText = Label(self.frame, text="Ciudad:", bg="white", font=("",17,"bold"), justify="left")
    self.ciudadText.place(relx=self.xCol3, rely=self.yCol3)
    self.ciudadTexto = StringVar()
    self.ciudadEntrada = Entry(self.frame,bg="white", textvariable=self.ciudadTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.ciudadEntrada.place(relx=self.xCol3b, rely=self.yCol3b)
    self.ciudadTexto.set(f"{ciudad}")

    self.departamentoText = Label(self.frame, text="Departamento:", bg="white", font=("",17,"bold"), justify="left")
    self.departamentoText.place(relx=self.xCol3, rely=self.yCol3+self.altura)
    self.departamentoTexto = StringVar()
    self.departamentoEntrada = Entry(self.frame,bg="white", textvariable=self.departamentoTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.departamentoEntrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura)
    self.departamentoTexto.set(f"{departamento}")

    self.horaTexto = horario
    self.tiempo1, self.tiempo2 = self.horaTexto.split(" / ")[0],self.horaTexto.split(" / ")[1]
    self.horaCompleta1,self.horaCompleta2 = self.tiempo1.split("-")[0],self.tiempo1.split("-")[1]
    self.horaCompleta3,self.horaCompleta4 = self.tiempo2.split("-")[0],self.tiempo2.split("-")[1]
    self.hora1,self.minuto1,self.hora2,self.minuto2 = self.horaCompleta1.split(":")[0],self.horaCompleta1.split(":")[1],self.horaCompleta2.split(":")[0],self.horaCompleta2.split(":")[1]
    self.hora3,self.minuto3,self.hora4,self.minuto4 = self.horaCompleta3.split(":")[0],self.horaCompleta3.split(":")[1],self.horaCompleta4.split(":")[0],self.horaCompleta4.split(":")[1]
    self.horarioText = Label(self.frame, text="Horario:", bg="white", font=("",17,"bold"), justify="left")
    self.horarioText.place(relx=self.xCol3, rely=self.yCol3+self.altura*2)
    self.horarioTextNota = Label(self.frame, text="*En formato: 7:00-12:00 / 14:00-18:00", bg="white", fg="red", font=("",8,""), justify="left")
    self.horarioTextNota.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*2+0.055)
    self.listaHoras = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
    self.listaMinutos = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25",
      "26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
    self.hora1Entrada = ttk.Combobox(self.frame, state="readonly")
    self.hora1Entrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*2, width=35)
    self.hora1Entrada["values"] = self.listaHoras
    self.hora1Entrada.current(self.listaHoras.index(self.hora1))
    self.sep1 = Label(self.frame, text=":", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.021875, rely=self.yCol3b+self.altura*2)
    self.minuto1Entrada = ttk.Combobox(self.frame, state="readonly")
    self.minuto1Entrada.place(relx=self.xCol3b+0.028125, rely=self.yCol3b+self.altura*2, width=35)
    self.minuto1Entrada["values"] = self.listaMinutos
    self.minuto1Entrada.current(self.listaMinutos.index(self.minuto1))
    self.sep2 = Label(self.frame, text="-", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.05, rely=self.yCol3b+self.altura*2)
    self.hora2Entrada = ttk.Combobox(self.frame, state="readonly")
    self.hora2Entrada.place(relx=self.xCol3b+0.05625, rely=self.yCol3b+self.altura*2, width=35)
    self.hora2Entrada["values"] = self.listaHoras
    self.hora2Entrada.current(self.listaHoras.index(self.hora2))
    self.sep3 = Label(self.frame, text=":", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.078125, rely=self.yCol3b+self.altura*2)
    self.minuto2Entrada = ttk.Combobox(self.frame, state="readonly")
    self.minuto2Entrada.place(relx=self.xCol3b+0.084375, rely=self.yCol3b+self.altura*2, width=35)
    self.minuto2Entrada["values"] = self.listaMinutos
    self.minuto2Entrada.current(self.listaMinutos.index(self.minuto2))
    self.sep4 = Label(self.frame, text=" / ", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.109375, rely=self.yCol3b+self.altura*2)
    self.hora3Entrada = ttk.Combobox(self.frame, state="readonly")
    self.hora3Entrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*2+0.029, width=35)
    self.hora3Entrada["values"] = self.listaHoras
    self.hora3Entrada.current(self.listaHoras.index(self.hora3))
    self.sep5 = Label(self.frame, text=":", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.021875, rely=self.yCol3b+self.altura*2+0.029)
    self.minuto3Entrada = ttk.Combobox(self.frame, state="readonly")
    self.minuto3Entrada.place(relx=self.xCol3b+0.028125, rely=self.yCol3b+self.altura*2+0.029, width=35)
    self.minuto3Entrada["values"] = self.listaMinutos
    self.minuto3Entrada.current(self.listaMinutos.index(self.minuto3))
    self.sep6 = Label(self.frame, text="-", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.05, rely=self.yCol3b+self.altura*2+0.029)
    self.hora4Entrada = ttk.Combobox(self.frame, state="readonly")
    self.hora4Entrada.place(relx=self.xCol3b+0.05625, rely=self.yCol3b+self.altura*2+0.029, width=35)
    self.hora4Entrada["values"] = self.listaHoras
    self.hora4Entrada.current(self.listaHoras.index(self.hora4))
    self.sep7 = Label(self.frame, text=":", bg="white", font=("",10,"bold"), justify="left").place(relx=self.xCol3b+0.078125, rely=self.yCol3b+self.altura*2+0.029)
    self.minuto4Entrada = ttk.Combobox(self.frame, state="readonly")
    self.minuto4Entrada.place(relx=self.xCol3b+0.084375, rely=self.yCol3b+self.altura*2+0.029, width=35)
    self.minuto4Entrada["values"] = self.listaMinutos
    self.minuto4Entrada.current(self.listaMinutos.index(self.minuto4))

    self.direccionText = Label(self.frame, text="Dirección:", bg="white", font=("",17,"bold"), justify="left")
    self.direccionText.place(relx=self.xCol3, rely=self.yCol3+self.altura*3)
    self.direccionTexto = StringVar()
    self.direccionEntrada = Entry(self.frame,bg="white",textvariable=self.direccionTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.direccionEntrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*3)
    self.direccionTexto.set(f"{direccion}")
    self.direccionTextNota = Label(self.frame, text="*En formato: CRA 70 A No. 4242 BRR\nFELICIDAD CASA 2 BOGOTÁ", bg="white", fg="red", font=("",8,""), justify="left")
    self.direccionTextNota.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*3+0.029)

    self.celularText = Label(self.frame, text="Celular:", bg="white", font=("",17,"bold"), justify="left")
    self.celularText.place(relx=self.xCol3, rely=self.yCol3+self.altura*4)
    self.celularTexto = StringVar()
    self.celularEntrada = Entry(self.frame,bg="white",textvariable=self.celularTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.celularEntrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*4)
    self.celularTexto.set(f"{celular}")

    self.correoText = Label(self.frame, text="Correo:", bg="white", font=("",17,"bold"), justify="left")
    self.correoText.place(relx=self.xCol3, rely=self.yCol3+self.altura*5)
    self.correoTexto = StringVar()
    self.correoEntrada = Entry(self.frame,bg="white",textvariable=self.correoTexto,fg="black", justify="left", font=(16), width=25, border=3)
    self.correoEntrada.place(relx=self.xCol3b, rely=self.yCol3b+self.altura*5)
    self.correoTexto.set(f"{correo}")

    self.guardarBoton = Button(self.frame,text="Guardar Cambios Realizados",bg="black",fg="white", cursor="hand2", font=(40), command=self.guardarCambios, bd=4)
    self.guardarBoton.place(relx=self.xCol3b-0.040625, rely=self.yCol3b+self.altura*6)
    self.guardarBoton.bind("<Enter>",self.enBotonGuardar)
    self.guardarBoton.bind("<Leave>",self.fueraBotonGuardar)

  def enOjoClaveBoton(self, event):
    self.ojoClaveBoton.config(bd=2)

  def fueraOjoClaveBoton(self, event):
    self.ojoClaveBoton.config(bd=0)

  def abrirOjo(self):
    self.ojoClaveCerradoImg = PhotoImage(file="RecursosGraficos\\\OJOCLAVECERRADO.png")
    self.ojoClaveCerradoImg = self.ojoClaveCerradoImg.subsample(15)
    self.ojoClaveBoton.config(image=self.ojoClaveCerradoImg, command=self.cerrarOjo)
    self.contrasenaEntrada.config(show="")

  def cerrarOjo(self):
    self.ojoClaveAbiertoImg = PhotoImage(file="RecursosGraficos\\\OJOCLAVEABIERTO.png")
    self.ojoClaveAbiertoImg = self.ojoClaveAbiertoImg.subsample(15)
    self.ojoClaveBoton.config(image=self.ojoClaveAbiertoImg, command=self.abrirOjo)
    self.contrasenaEntrada.config(show="*")

  def enBotonImagenPerfil(self, event):
    self.imgPrlBoton.config(bd=6)

  def fueraBotonImagenPerfil(self, event):
      self.imgPrlBoton.config(bd=4)

  def abrirArchivo(self):
    self.imagenPerfilEntrada = str(filedialog.askopenfile(title="Abrir Archivo Foto de Perfil",initialdir="C:/",
      filetypes=(("PNG Image","*.png"),("JPG Image","*.jpg"))))
    startPath = self.imagenPerfilEntrada.find("'")
    endPath = self.imagenPerfilEntrada.find("'",startPath+1)
    self.imagenPerfilEntrada = self.imagenPerfilEntrada[startPath+1:endPath]
    if self.imagenPerfilEntrada != "Non":
        self.confirmacionImagenCargada.config(text="Imagen Cargada", fg="green")
        self.imPerfil.panel.destroy()
        self.imPerfil= ImInter(self.frame,self.imagenPerfilEntrada, self.xCol1b+0.135,self.yCol1b+self.altura*6+0.03)
        self.imPerfil.sizeImage(100,100)
        self.imPerfil.create()

  def enBotonGuardar(self, event):
    self.guardarBoton.config(bd=6)

  def fueraBotonGuardar(self, event):
    self.guardarBoton.config(bd=4)

  def guardarCambios(self):
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    messageBoxTit, messageBoxContent = "Error al Crear Cuenta", "Todos los campos son requeridos.\nFavor registre: "
    usuarioN = str(self.usuarioEntrada.get())
    if usuarioN == "":
        return messagebox.showerror(messageBoxTit, messageBoxContent+"Usuario")
    conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE USUARIO='{usuario}' AND NOT IDUSUARIO={idUsuario}")
    usuarioEncontrado = conexionSlow.cursorSlow.fetchall()
    if len(usuarioEncontrado)>0:
        return messagebox.showerror(messageBoxTit, "Usuario ya existe.")
    claveN = str(self.contrasenaEntrada.get())
    if not claveN == "":
      if (len(claveN)<10)or((claveN.find("0")==-1)and(claveN.find("1")==-1)and(claveN.find("2")==-1)and(claveN.find("3")==-1)and(claveN.find("4")==-1)and(claveN.find("5")==-1)and(claveN.find("6")==-1)and(claveN.find("7")==-1)and(claveN.find("8")==-1)and(claveN.find("9")==-1)):
        return messagebox.showerror(messageBoxTit, "Clave digitada de forma Incorrecta.")
    nombreN = str(self.nombreEntrada.get())
    if nombreN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Nombre")
    apellidoN = str(self.apellidoEntrada.get())
    if apellidoN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Apellido")
    tipoDocumentoN = str(self.tipoDocumentoEntrada.get())
    if tipoDocumentoN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Tipo de Documento")
    numeroDocumentoN = str(self.numeroDocumentoEntrada.get())
    if numeroDocumentoN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Número de Documento")
    else:
      try:
        numeroDocumentoN = int(numeroDocumentoN)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"El Número de Documento debe ser un Número.")
    if numeroDocumentoN <= 99999:
      return messagebox.showerror(messageBoxTit,"El Número de Documento debe ser un Número mayor a 99999")
    conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE NUMERODOCUMENTO='{numeroDocumento}' AND NOT IDUSUARIO={idUsuario}")
    numeroDocumentoEncontrado = conexionSlow.cursorSlow.fetchall()
    if len(numeroDocumentoEncontrado)>0:
      return messagebox.showerror(messageBoxTit, "Número de documento ya existe.")
    imagenPerfilPathN = str(self.imagenPerfilEntrada)
    try:
      imagenPerfilObjetoN = Imagenes.Imagen(imagenPerfilPathN)
      imagenPerfilN = imagenPerfilObjetoN.aHexaDecimalStr()
    except FileNotFoundError:
      imagenPerfilObjetoN = Imagenes.Imagen(imagenPerfilPath)
      imagenPerfilN = imagenPerfilObjetoN.aHexaDecimalStr()
    tipoSangreN = str(self.tipoSangreEntrada.get())
    if tipoSangreN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Tipo de Sangre")
    if rol=="JEFE":
      idJefeN = 0
      self.jefeDisplay.set("0")
      policiasAsignadosN = str(self.policiasAsignadosEntrada.get())
      if policiasAsignadosN == "":
        policiasAsignadosN = "0"
        self.policiasAsignadosDisplay.set("0")
      listaPoliciasAsignadosN = policiasAsignadosN.split(sep=",")
      if (not listaPoliciasAsignadosN[0]=="0") and len(listaPoliciasAsignadosN)==1:
        for i in listaPoliciasAsignadosN:
          try:
            idPoliciaN = int(i)
          except ValueError:
            return messagebox.showerror(messageBoxTit,"Recuerde ingresar solo los ID válidos de Slow para\nlos policías asignados separados por comas")
          conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE IDUSUARIO='{idPoliciaN}' AND ROL='POLICIA'")
          policiaEncontrado = conexionSlow.cursorSlow.fetchall()
          if len(policiaEncontrado)==0:
            return messagebox.showerror(messageBoxTit, f"No existe el ID del policía {idPoliciaN}. Ingresar uno existente o crear uno nuevo")
    else:
      idJefeN = str(self.jefeDisplay.get())
      if idJefeN == "":
        return messagebox.showerror(messageBoxTit,messageBoxContent+"ID de Jefe")
      else:
        try:
          idJefeN = int(idJefeN)
        except ValueError:
          return messagebox.showerror(messageBoxTit,"El ID de Jefe debe ser un Número.")
        if idJefeN <= 0:
          return messagebox.showerror(messageBoxTit,"ID de Jefe incorrecto.")
      conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE IDUSUARIO='{idJefeN}' AND ROL='JEFE'")
      jefeEncontrado = conexionSlow.cursorSlow.fetchall()
      if len(jefeEncontrado)==0:
        return messagebox.showerror(messageBoxTit, "No existe ese jefe. Ingresar uno existente o crear uno nuevo")
      policiasAsignadosN = "0"
      self.policiasAsignadosDisplay.set("0")
    numeroCuadranteN = self.numeroCuadranteEntrada.get()
    if numeroCuadranteN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Número de Cuadrante")
    else:
      try:
        numeroCuadranteN = int(numeroCuadranteN)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"El Número de Cuadrante debe ser un Número.")
      if numeroCuadranteN <= 0:
        return messagebox.showerror(messageBoxTit,"El Número de Cuadrante debe ser un Número mayor a 0.")
    cuadranteN = str(self.cuadranteEntrada.get())
    if cuadranteN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Cuadrante")
    ciudadN = str(self.ciudadEntrada.get())
    if ciudadN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Ciudad")
    departamentoN = str(self.departamentoEntrada.get())
    if departamentoN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Departamento")
    if (int(self.hora1Entrada.get())>int(self.hora2Entrada.get())) or (int(self.hora2Entrada.get())>int(self.hora3Entrada.get())) or (int(self.hora3Entrada.get())>int(self.hora4Entrada.get())) or (self.hora1Entrada.get()=="0" and self.hora2Entrada.get()=="0"):
      return messagebox.showerror(messageBoxTit,"El horario se digitó Incorrectamente.")
    self.horarioEntradaN = f"{self.hora1Entrada.get()}:{self.minuto1Entrada.get()}-{self.hora2Entrada.get()}:{self.minuto2Entrada.get()} / {self.hora3Entrada.get()}:{self.minuto3Entrada.get()}-{self.hora4Entrada.get()}:{self.minuto4Entrada.get()}"
    horarioN = str(self.horarioEntradaN)
    if horarioN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Horario")
    direccionN = str(self.direccionEntrada.get())
    if direccionN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Dirección")
    celularN = self.celularEntrada.get()
    if celularN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Celular")
    else:
      try:
        celularN = int(celularN)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"El Número de Celular debe ser un Número.")
      if celularN <= 0:
        return messagebox.showerror(messageBoxTit,"El Número de Celular debe ser un Número mayor a 0.")
    correoN = str(self.correoEntrada.get())
    if correoN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Correo")
    if (correoN.find("@policia.gov.co")==-1):
      return messagebox.showerror(messageBoxTit,"El correo electrónico debe terminar en @policia.gov.co")
    conexionSlow.cursorSlow.execute(f'''UPDATE USUARIOS SET
        USUARIO='{usuarioN}',NOMBRE='{nombreN}',APELLIDO='{apellidoN}',TIPODOCUMENTO='{tipoDocumentoN}',NUMERODOCUMENTO={numeroDocumentoN},
        IMAGENPERFIL='{imagenPerfilN}',TIPOSANGRE='{tipoSangreN}',JEFE={idJefeN},POLICIASASIGNADOS='{policiasAsignadosN}',
        NUMEROCUADRANTE={numeroCuadranteN},CUADRANTE='{cuadranteN}',CIUDAD='{ciudadN}',DEPARTAMENTO='{departamentoN}',HORARIO='{horarioN}',
        DIRECCION='{direccionN}',CELULAR={celularN},CORREO='{correoN}' WHERE IDUSUARIO='{idUsuario}'
        ''')
    if not claveN=="":
      conexionSlow.cursorSlow.execute(f"UPDATE USUARIOS SET CLAVE=AES_ENCRYPT('{claveN}','clave') WHERE IDUSUARIO={idUsuario}")
    conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE IDUSUARIO='{idUsuario}'")
    usuarioEncontrado = conexionSlow.cursorSlow.fetchall()
    if len(usuarioEncontrado)>0:
      messagebox.showinfo("Información Slow", f"Información Guardada Exitosamente en el Usuario ID: {idUsuario}.\nCierre sesión y vuelva a ingresar para ver los cambios")
    else:
      messagebox.showerror(messageBoxTit,"No se guardaron los datos. Inténtelo nuevamente o reporte el problema para una solución")
    conexionSlow.cerrarBaseDeDatosSlow()

  def Open_menu(self,event=None):
    
    global ac
    self.name="datos"
    if (ac== False):

      self.Menu = menu(self.name,root=self.frame, app=self)
      
    
      self.Menu.start_page()
      ac=True

  def start_page(self):
    self.frame.pack()

# grevy
class video(info):

  def own_widgets(self):
    self.widgetscreados = False
    self.widgetArrastre = False
    self.iminfo= ImInter(self.frame,"Video Speed Icon.png", 0.8,0.06) 
    self.iminfo.sizeImage(70,110)
    self.iminfo.create()

    self.police = ImInter(self.frame,f"{imagenPerfilPath}", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

    self.Text="Registrar Video"
    self.Title1 = textInter(self.frame,self.Text,30,0.5,0.2)
    self.Title1.create_Tittle()

    self.TitleViaParaDeteccion = textInter(self.frame,"Ingrese la vía del vídeo para\ndetectar la velocidad de los vehículos:",16,0.18,0.28,'w')
    self.TitleViaParaDeteccion.create_Tittle()
    self.ViaParaDeteccion = StringVar()
    self.entradaViaParaDeteccion = Entry(self.frame,textvariable=self.ViaParaDeteccion,width=15, font = ('comics Sans MS',18))
    self.entradaViaParaDeteccion.place(relx = 0.44,rely=0.28,anchor ='w')
    self.entradaViaParaDeteccion.bind("<Return>",self.viaSeleccionadaE)

    self.TitleCiudad = textInter(self.frame,"Ciudad:",16,0.28,0.34,'w')
    self.TitleCiudad.create_Tittle()
    self.Ciudad = StringVar()
    self.entradaCiudad = Entry(self.frame,textvariable=self.Ciudad,width=15, font = ('comics Sans MS',18))
    self.entradaCiudad.place(relx = 0.34,rely=0.34,anchor ='w')

    self.TitleDireccion = textInter(self.frame,"Dirección:",16,0.5,0.34,'w')
    self.TitleDireccion.create_Tittle()
    self.Direccion = StringVar()
    self.entradaDireccion = Entry(self.frame,textvariable=self.Direccion,width=15, font = ('comics Sans MS',18))
    self.entradaDireccion.place(relx = 0.58,rely=0.34,anchor ='w')

    self.ButtonPuedeSubirVideo = BottInter(self.frame,"SeleccionarVia.png",0.65,0.28,None, self.viaSeleccionada)
    self.ButtonPuedeSubirVideo.modzise(180,45)
    self.ButtonPuedeSubirVideo.create()

    self.imagenDrag = ImInter(self.frame,"Upload.png", 0.51,0.57) 
    self.imagenDrag.sizeImage(250,300)
    self.imagenDrag.create()

  def viaSeleccionadaE(self, event):
    viaActual = self.ViaParaDeteccion.get()
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.cursorSlow.execute(f"SELECT IDVIA FROM VIAS WHERE VIA='{viaActual}'")
    idVia = conexionSlow.cursorSlow.fetchall()
    if len(idVia)==0:
      if (self.widgetscreados):
        self.Button_file.panel.destroy()
        self.paragraph1.panel.destroy()
        self.idViaVideo = -1
        self.widgetscreados = False
      return messagebox.showerror("Error al ingresar información",f"La vía ingresada {viaActual} no existe")
    self.idViaVideo = idVia[0][0]
    self.crearWidgetsSubirVideo()

  def viaSeleccionada(self):
    viaActual = self.ViaParaDeteccion.get()
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.cursorSlow.execute(f"SELECT IDVIA FROM VIAS WHERE VIA='{viaActual}'")
    idVia = conexionSlow.cursorSlow.fetchall()
    if len(idVia)==0:
      if (self.widgetscreados):
        self.Button_file.panel.destroy()
        self.paragraph1.panel.destroy()
        self.idViaVideo = -1
        self.widgetscreados = False
      return messagebox.showerror("Error al ingresar información",f"La vía ingresada {viaActual} no existe")
    self.idViaVideo = idVia[0][0]
    self.crearWidgetsSubirVideo()
  
  def crearWidgetsSubirVideo(self):
    self.Button_file = BottInter(self.frame,"Boton.png",0.5,0.78,None,self.Open_File)
    self.Button_file.modzise(370,60)
    self.Button_file.create()

    self.Text="A continuación puede registrar el video arrastrándolo o seleccionándolo desde la carpeta"
    self.paragraph1 = textInter(self.frame,self.Text,16,0.5,0.4)
    self.paragraph1.create_paragraph()

    if not self.widgetArrastre:
      windnd.hook_dropfiles(self.frame, func=self.dragged_files)
      self.widgetArrastre = True
    self.widgetscreados = True

  def dragged_files(self,files):
    self.File = '\n'.join((item.decode('gbk') for item in files))
    if (self.File.endswith('.mp4')):
        if self.idViaVideo == -1:
          return messagebox.showerror("Error al ingresar la información","La vía ingresada no existe")
        if (self.Ciudad.get()=="") or (self.Direccion.get() ==""):
          return messagebox.showerror("Error al ingresar la información","Complete todos los campos")
        else:
          self.make_page_detection(self.idViaVideo,idUsuario,self.File,self.Ciudad.get(),self.Direccion.get())

  def Open_File(self):
    self.File= filedialog.askopenfile(title="Abrir Archivo",initialdir="C:/",filetypes=(("MP4 video","*.mp4"),))
    self.File = str(self.File)
    startPath = self.File.find("'")
    endPath = self.File.find("'",startPath+1)
    self.File = self.File[startPath+1:endPath]

    if bool(self.File)!=0:  
      if self.idViaVideo == -1:
        return messagebox.showerror("Error al ingresar la información","La vía ingresada no existe")
      if (self.Ciudad.get()=="") or (self.Direccion.get() ==""):
        return messagebox.showerror("Error al ingresar la información","Complete todos los campos")
      else:
        self.make_page_detection(self.idViaVideo,idUsuario,self.File,self.Ciudad.get(),self.Direccion.get())       
    
  
  def make_page_detection(self,idVia,idUsuario,videoPath,ciudad,direccion):
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.cursorSlow.execute(f"SELECT MULTA FROM VIAS WHERE IDVIA={idVia}")
    multa = conexionSlow.cursorSlow.fetchone()[0]
    conexionSlow.cerrarBaseDeDatosSlow()

    self.deteccion = Deteccion.Grafico_muestra(idUsuario,idVia,multa,ciudad,direccion,videoPath)
    self.page_detection = detection(self.File,self.deteccion,master=self.master, app=self)
    self.frame.pack_forget()
    self.page_detection.start_page()
    self.deteccion.abrirVideo()

  def Open_menu(self,event=None):
    global ac
    self.name="video"
    if (ac== False):

      self.Menu = menu(self.name,root=self.frame, app=self)
      
    
      self.Menu.start_page()
      ac=True
# daniel


class Vias(info):
  def own_widgets(self):

    self.inDate = ImInter(self.frame,"Vias Icon.png", 0.82,0.06)
    self.inDate.sizeImage(80,80)
    self.inDate.create()

    self.Tittle_Vias= ImInter(self.frame,"Vias.png", 0.35,0.25) 
    self.Tittle_Vias.sizeImage(80,120)
    self.Tittle_Vias.create()

    self.police = ImInter(self.frame,f"{imagenPerfilPath}", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

    self.canvas = Canvas(self.frame, bg='white')
    self.canvas.place(relx = 0.5,rely=0.58,anchor = CENTER, relheight=0.5,relwidth=0.7)

    self.scrollbar = Scrollbar(self.canvas,bg='white')
    self.scrollbar.place(relx = 0.99,rely=0.5,anchor = CENTER, relheight=1)

    self.xDCV_C1 = 94.48
    self.xDCV_C2 = 280
    self.xDCV_C3 = 510
    self.xDCV_C4 = 750
    self.xDCV_C5 = 982.67
    self.yDCV = 50
    self.crearTextoDentroCanvas(self.xDCV_C1,self.yDCV,"ID VIA",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C2,self.yDCV,"NOMBRE VIA",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C3,self.yDCV,"IMAGEN VIA",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C4,self.yDCV,"LIMITE VELOCIDAD",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C5,self.yDCV,"MULTA",'bold')

    self.llamarVias()

    self.BottVehiculos = BottInter(self.frame,"Vehiculos.png",0.7,0.25, None,self.go_vehiculos)
    self.BottVehiculos.modzise(130,70)
    self.BottVehiculos.create()

    if rol=="JEFE":
      self.Button_crear_editar_via = BottInter(self.frame,"Crear_Editar_Via.png",0.85,0.89,None, self.make_agregar_editar_via)
      self.Button_crear_editar_via.modzise(170,70)
      self.Button_crear_editar_via.create()

    self.canvas.config(yscrollcommand=self.scrollbar.set, scrollregion = self.canvas.bbox("all"))
    self.scrollbar.configure(command= self.canvas.yview )

  def make_agregar_editar_via(self):
    self.page_agregar_crear_via = guardarVia(master=self.master, app=self)
    self.frame.pack_forget()
    self.page_agregar_crear_via.start_page()

  def crearTextoDentroCanvas(self,x,y,text,bold="",font=11):
    self.canvas.create_text(x,y,font=('Helvetica', font, f'{bold}'), text=f"{text}")

  def llamarVias(self):
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.abrirBasedeDatosSlow()
    conexionSlow.cursorSlow.execute("SELECT * FROM VIAS")
    self.vias = conexionSlow.cursorSlow.fetchall()
    if len(self.vias)==0:
      self.canvas.create_text(100,100,font=('Helvetica', 11, 'bold'), text="Aún no hay vías para mostrar")
    else:
      self.intervAltCrecimiento = 50
      self.intervAltura = self.yDCV+self.intervAltCrecimiento
      for i in self.vias:
        self.crearTextoDentroCanvas(self.xDCV_C1,self.intervAltura+50,f"{i[0]}")
        self.crearTextoDentroCanvas(self.xDCV_C2,self.intervAltura+50,f"{i[1]}")

        self.carpetaImgVias = ArchivosYCarpetas.Carpeta("RecursosGraficos\\ImgVias")
        if not self.carpetaImgVias.existeCarpeta:
          self.carpetaImgVias.crearCarpeta()
        self.imagenVia = Imagenes.ImagenHexaDecimalStr(i[2])
        self.imagenViaPath = f"RecursosGraficos\\ImgVias\\imagenVia-{i[1]}.png"
        try:
          os.remove(self.imagenViaPath)
        except FileNotFoundError:
          pass
        self.imagenVia.aImagen(self.imagenViaPath)

        self.imgViaEnCanvas = Image.open(f"{self.imagenViaPath}")
        self.dimImgVia = 150
        self.imgViaEnCanvas = self.imgViaEnCanvas.resize((self.dimImgVia,self.dimImgVia), Image.ANTIALIAS)
        globals()["imgViaEnCanvas" + str(i)] = ImageTk.PhotoImage(self.imgViaEnCanvas)

        self.canvas.create_image(self.xDCV_C3,self.intervAltura+60,image=globals()["imgViaEnCanvas" + str(i)])

        self.crearTextoDentroCanvas(self.xDCV_C4,self.intervAltura+50,"{:,}".format(i[3])+" Km/h")
        self.crearTextoDentroCanvas(self.xDCV_C5,self.intervAltura+50,"$ "+"{:,}".format(i[4]))

        self.intervAltura += 150+self.intervAltCrecimiento
    conexionSlow.cerrarBaseDeDatosSlow()


  def go_vehiculos(self):
    self.page_vehiculos = Vehiculos(master=self.master, app=self)
    self.frame.pack_forget()
    self.page_vehiculos.start_page()
  
  def Open_menu(self,event=None):
    global ac
    self.name="vias"
    if (ac== False):

      self.Menu = menu(self.name,root=self.frame, app=self)
      
    
      self.Menu.start_page()
      ac=True


# Daniel
class Vehiculos(info):
  def own_widgets(self):

    self.inDate = ImInter(self.frame,"Vias Icon.png", 0.82,0.06)
    self.inDate.sizeImage(80,80)
    self.inDate.create()

    self.police = ImInter(self.frame,f"{imagenPerfilPath}", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

    self.inVe = ImInter(self.frame,"Ve_guardados.png", 0.6,0.25)
    self.inVe.sizeImage(80,120)
    self.inVe.create()

    self.BottVehiculos = BottInter(self.frame,"ViasImage.png",0.4,0.25, None,self.go_Vias)
    self.BottVehiculos.modzise(130,70)
    self.BottVehiculos.create()

    self.canvas = Canvas(self.frame, bg='white')
    self.canvas.place(relx = 0.5,rely=0.58,anchor = CENTER, relheight=0.5,relwidth=0.7)

    self.scrollbar = Scrollbar(self.canvas,bg='white')
    self.scrollbar.place(relx = 0.99,rely=0.5,anchor = CENTER, relheight=1)

    self.xDCV_C1 = 56.7
    self.xDCV_C2 = self.xDCV_C1+80
    self.xDCV_C3 = self.xDCV_C2+120
    self.xDCV_C4 = self.xDCV_C3+140
    self.xDCV_C5 = self.xDCV_C4+110
    self.xDCV_C6 = self.xDCV_C5+95
    self.xDCV_C7 = self.xDCV_C6+110
    self.xDCV_C8 = self.xDCV_C7+115
    self.xDCV_C9 = self.xDCV_C8+100
    self.xDCV_C10 = self.xDCV_C9+110
    self.yDCV = 50
    self.crearTextoDentroCanvas(self.xDCV_C1,self.yDCV,"ID\nVEHÍCULO",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C2,self.yDCV,"IDVIDEO",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C3,self.yDCV,"CAPTURA",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C4,self.yDCV,"TIPO VEHÍCULO",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C5,self.yDCV,"PLACA",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C6,self.yDCV,"VELOCIDAD",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C7,self.yDCV,"VÍA",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C8,self.yDCV,"VELOCIDAD\nEXCEDIDA",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C9,self.yDCV,"MULTA",'bold')
    self.crearTextoDentroCanvas(self.xDCV_C10,self.yDCV,"USUARIO",'bold')

    self.llamarVehiculos()
    
    if rol=="JEFE":
      self.BotonBorrarEditarVehiculo = BottInter(self.frame,"Boton Borrar o Editar Vehiculo.png",0.85,0.89,None, self.accionBorrarEditarVehiculo)
      self.BotonBorrarEditarVehiculo.modzise(170,70)
      self.BotonBorrarEditarVehiculo.create()

    self.canvas.config(yscrollcommand=self.scrollbar.set, scrollregion = self.canvas.bbox("all"))
    self.scrollbar.configure(command= self.canvas.yview )

  def accionBorrarEditarVehiculo(self):
    self.pageBorrarEditarVehiculo = GuardarVehiculo(master=self.master, app=self)
    self.frame.pack_forget()
    self.pageBorrarEditarVehiculo.start_page()

  def llamarVehiculos(self):
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.abrirBasedeDatosSlow()
    if rol=="JEFE":
      listaPoliciasAsignados = policiasAsignados.split(sep=",")
      listaPoliciasAsignados.append(idUsuario)
      self.vehiculosA = []
      for i in listaPoliciasAsignados:
        conexionSlow.cursorSlow.execute(f"SELECT * FROM VEHICULOS WHERE IDUSUARIO={i}")
        self.vehiculosPolicia = conexionSlow.cursorSlow.fetchall()
        for j in self.vehiculosPolicia:
          self.vehiculosA.append(j)
      self.vehiculos = self.ordenarVehiculos(self.vehiculosA)
    else:
      conexionSlow.cursorSlow.execute(f"SELECT * FROM VEHICULOS WHERE IDUSUARIO={idUsuario}")
      self.vehiculos = conexionSlow.cursorSlow.fetchall()
    if len(self.vehiculos)==0:
      self.canvas.create_text(100,100,font=('Helvetica', 11, 'bold'), text="Aún no hay vehículos para mostrar")
    else:
      self.intervAltCrecimiento = 50
      self.intervAltura = self.yDCV+self.intervAltCrecimiento
      for i in self.vehiculos:
        self.crearTextoDentroCanvas(self.xDCV_C1,self.intervAltura+50,f"{i[0]}")
        self.crearTextoDentroCanvas(self.xDCV_C2,self.intervAltura+50,f"{i[1]}")

        self.carpetaImgVehiculos = ArchivosYCarpetas.Carpeta("RecursosGraficos\\ImgVehiculos")
        if not self.carpetaImgVehiculos.existeCarpeta:
          self.carpetaImgVehiculos.crearCarpeta()
        self.imagenVehiculo = Imagenes.ImagenHexaDecimalStr(i[2])
        self.imagenVehiculoPath = f"RecursosGraficos\\ImgVehiculos\\imagenVehiculo-{i[1]}.png"
        try:
          os.remove(self.imagenVehiculoPath)
        except FileNotFoundError:
          pass
        self.imagenVehiculo.aImagen(self.imagenVehiculoPath)

        self.imgVehiculoEnCanvas = Image.open(f"{self.imagenVehiculoPath}")
        self.dimImgVehiculo = 150
        self.imgVehiculoEnCanvas = self.imgVehiculoEnCanvas.resize((self.dimImgVehiculo,self.dimImgVehiculo), Image.ANTIALIAS)
        globals()["imgVehiculoEnCanvas" + str(i)] = ImageTk.PhotoImage(self.imgVehiculoEnCanvas)

        self.canvas.create_image(self.xDCV_C3,self.intervAltura+60,image=globals()["imgVehiculoEnCanvas" + str(i)])

        self.crearTextoDentroCanvas(self.xDCV_C4,self.intervAltura+50,f"{i[3]}")
        self.crearTextoDentroCanvas(self.xDCV_C5,self.intervAltura+50,f"{i[4]}")
        self.crearTextoDentroCanvas(self.xDCV_C6,self.intervAltura+50,"{:,}".format(i[5])+" Km/h")

        conexionSlow.cursorSlow.execute(f"SELECT VIA FROM VIAS WHERE IDVIA={i[6]}")
        viaActTablaVehic =conexionSlow.cursorSlow.fetchone()
        self.crearTextoDentroCanvas(self.xDCV_C7,self.intervAltura+50,f"{viaActTablaVehic[0]}")

        if i[7]==1:
          self.crearTextoDentroCanvas(self.xDCV_C8,self.intervAltura+50,"Verdadero")
        else:
          self.crearTextoDentroCanvas(self.xDCV_C8,self.intervAltura+50,"Falso")

        self.crearTextoDentroCanvas(self.xDCV_C9,self.intervAltura+50,"$ "+"{:,}".format(i[8]))

        conexionSlow.cursorSlow.execute(f"SELECT NOMBRE,APELLIDO FROM USUARIOS WHERE IDUSUARIO={i[9]}")
        usuarioActTablaVehic =conexionSlow.cursorSlow.fetchone()
        self.crearTextoDentroCanvas(self.xDCV_C10,self.intervAltura+50,f"{usuarioActTablaVehic[0]}\n{usuarioActTablaVehic[1]}")

        self.intervAltura += 150+self.intervAltCrecimiento

    conexionSlow.cerrarBaseDeDatosSlow()

  def ordenarVehiculos(self,listaVehiculos):
    listaVehiculosOr = []
    tam = len(listaVehiculos)
    for i in range (0,tam):
      minAct = self.minListaVehiculos(listaVehiculos)
      listaVehiculosOr.append(minAct)
      listaVehiculos.remove(minAct)
    return listaVehiculosOr

  def minListaVehiculos(self,listaVehiculos):
    minLista = listaVehiculos[0]
    numListaMinId = minLista[0]
    for i in listaVehiculos:
      listaActual = i
      numListaActual = listaActual[0]
      if numListaActual<numListaMinId:
        numListaMinId = numListaActual
        minLista = listaActual
    return minLista

  def crearTextoDentroCanvas(self,x,y,text,bold="",font=11):
    self.canvas.create_text(x,y,font=('Helvetica', font, f'{bold}'), text=f"{text}")

  def go_Vias(self):
    self.page_vias = Vias(master=self.master, app=self)
    self.frame.pack_forget()
    self.page_vias.start_page()
  
  def Open_menu(self,event=None):
    global ac
    self.name="vias"
    if (ac== False):

      self.Menu = menu(self.name,root=self.frame, app=self)
      
    
      self.Menu.start_page()
      ac=True



# deteccion
class detection(info):
  def __init__(self,video, deteccion,master=None, app=None):
    self.video=video
    self.deteccion = deteccion
    super().__init__(master, app)

  def own_widgets(self):
    self.inDate = ImInter(self.frame,"deteccionimage.png", 0.82,0.06)
    self.inDate.sizeImage(80,120)
    self.inDate.create()

    self.TitleVideoSubido = textInter(self.frame,f"Video Subido\nID:{self.deteccion.idVideo}",20,0.44,0.3,'w')
    self.TitleVideoSubido.create_Tittle()

    self.imgVideoSubido = ImInter(self.frame,"videoSubido.png", 0.49,0.49)
    self.imgVideoSubido.sizeImage(240,253)
    self.imgVideoSubido.create()

    self.police = ImInter(self.frame,f"{imagenPerfilPath}", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()
    '''
    self.BottGuardar = BottInter(self.frame,"GuardarBoton.png",0.5,0.8, None,None)
    self.BottGuardar.modzise(190,60)
    self.BottGuardar.create()
    '''

    self.create_botton_velo(0.5)

  def create_botton_velo(self,positionx):

    self.positionx=positionx
    self.Bottvelo2 = BottInter(self.frame,"velocidadPromedio.png",self.positionx, 0.68,
    'Velocidad promedio',self.deteccion.evento_boton)
    self.Bottvelo2.modzise(50,50)
    self.Bottvelo2.create()
    
    self.open_create_text(self.Bottvelo2)

  def open_create_text(self,botton):
    
    self.botton=botton
    self.botton.createText()
  
  def Open_menu(self,event=None):
    global ac
    self.name="video"
    if (ac== False):

      self.Menu = menu(self.name,root=self.frame, app=self,)
      
    
      self.Menu.start_page()
      ac=True
  
  def go_back(self):
    global ac
    ac=False
    self.frame.pack_forget()
    self.go_back = self.app.start_page()



class Graficas():
  def __init__(self, master=None, app=None):
    self.master = master
    self.app = app
    self.frame = Frame(self.master,background="#d6d6d6",width=1366,height=768)
    self.common_widgets()
    self.own_widgets()
    self.frame.pack()

  def common_widgets(self):

    self.Button_regresar = BottInter(self.frame,"regresar.png",0.85,0.9,None, self.make_regresar)
    self.Button_regresar.modzise(250,60)
    self.Button_regresar.create()

  def own_widgets(self):

    self.Button_ver_tabla = BottInter(self.frame,"ver_tabla.png",0.85,0.7, None,self.make_tabla_graficas)
    self.Button_ver_tabla.modzise(250,60)
    self.Button_ver_tabla.create()

    self.Button_agregar_vehiculo = BottInter(self.frame,"agregar_vehiculo.png",0.85,0.8,None, self.make_agregar_vehiculo)
    self.Button_agregar_vehiculo.modzise(250,60)
    self.Button_agregar_vehiculo.create()
  
  def make_tabla_graficas(self):
    self.page_tabla_graficas = tablaGraficas(master=self.master, app=self)
    self.frame.pack_forget()
    self.page_tabla_graficas.start_page()


  def make_regresar(self):
    self.page_regresar = detection(master=self.master, app=self)
    self.frame.pack_forget()
    self.page_regresar.start_page()


  def start_page(self):
    self.frame.pack()

class Graficas2(Graficas):
  a=1

class tablaGraficas(info):
  pass

class CampoCanvas():
  def __init__(self):
      pass

#Crea imagenes 
class ImInter:

  def __init__(self, frame,objeto,relx,rely,bg=True,anchor=None):
    self.frame = frame
    self.anchor=anchor
    self.objeto = objeto
    self.relx = relx
    self.rely = rely
    self.bg=bg
    self.open = Image.open(self.objeto)
    
  #muestra la imagen creada
  def show(self):
    if (self.anchor==None):

      self.panel.place(relx = self.relx,rely=self.rely,anchor = CENTER)
    else:
      self.panel.place(relx = self.relx,rely=self.rely,anchor = self.anchor)
  #modifica el tamaño del
  def modzise(self,sizex=130,sizey=130):
    
    self.sizey = sizey
    self.sizex = sizex
    
  def sizeImage(self,x,y):
    self.x=x
    self.y=y
    self.open = self.open.resize((self.y,self.x),Image.ANTIALIAS)

  def create(self):
    
    if (self.bg):
      self.img = ImageTk.PhotoImage(self.open)
      self.panel= Label(self.frame, image = self.img, bg='white')
      self.show()
    else:
      self.img = ImageTk.PhotoImage(self.open)
      self.panel= Canvas(self.frame,bg="black",width=150, height=150)
      self.panel.pack()
      self.panel.create_image(75,75,image=self.img)
  
  def config(self):
    self.panel.configure(bg=None)
# crear botones, hereda de la clase que crea imagenes


class BottInter(ImInter):
  # variable de tamaño
  sizex=100
  sizey=100
  def __init__(self,frame,objeto,relx,rely,texto,action=None,App=None):
    self.texto = texto
    self.action = action
    self.App=App
    super().__init__(frame,objeto,relx,rely)
  # crea el boton
  def create(self):
    
    self.photo =  ImageTk.PhotoImage(self.open.resize((self.sizex,self.sizey), Image.ANTIALIAS))

    self.panel = Button(self.frame, image = self.photo, bg='white' ,highlightthickness = 0, bd = 0,height = self.sizey, width = self.sizex, command = self.action)
    if (self.objeto =="Menu icon.png"):
      self.panel.bind('<Enter>', self.App.Open_menu)
    self.show() # funcion heredada de ImInter
    
    
  # crea el texto del boton
  def createText(self,RELY=0):
    self.RELY=RELY
    if (RELY==0):
      self.rely += 0.08
    else:
      self.rely=RELY

    self.panel= Label(self.frame, text = self.texto,bg= 'white',font =('Helvetica 15 underline italic'))

    
    self.show()
  def return_panel(self):
    return self.panel

# grevy
class guardarVia(info):
  def __init__(self,idusuario=None, idvideo=None,velocidad=None,velocidad_excedida=None, captura=None, master=None, app=None):
    super().__init__(master,app)

  def own_widgets(self):
    self.iminfo= ImInter(self.frame,"Vias Icon.png", 0.8,0.06) 
    self.iminfo.sizeImage(70,110)
    self.iminfo.create()

    self.police = ImInter(self.frame,f"{imagenPerfilPath}", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

    self.Text="Crear o Editar Vía"
    self.Title1 = textInter(self.frame,self.Text,30,0.5,0.225)
    self.Title1.create_Tittle()
    
    self.Text="Si quiere editar vía\ningrese el nombre de la Vía"
    self.Title_viaEditar = textInter(self.frame,self.Text,14,0.21,0.33,'w')
    self.Title_viaEditar.create_Tittle()

    self.Text="Nombre Vía:"
    self.Title_nombreVia = textInter(self.frame,self.Text,16,0.15,0.41,'w')
    self.Title_nombreVia.create_Tittle()
    self.NombreVia= StringVar(self.frame)
    self.entradaNombreVia = Entry(self.frame,textvariable=self.NombreVia,width=10,font = ('comics Sans MS',18))
    self.entradaNombreVia.place(relx = 0.34,rely=0.41,anchor ='w')

    self.ButtonBuscar= BottInter(self.frame,"BotonBuscar.png",0.23,0.48,None, self.buscarVia)
    self.ButtonBuscar.modzise(120,45)
    self.ButtonBuscar.create()

    self.BotonEliminarVia= BottInter(self.frame,"EliminarViaBoton.png",0.34,0.48,None, self.eliminarVia)
    self.BotonEliminarVia.modzise(120,45)
    self.BotonEliminarVia.create()

    self.Text="Imagen Via:"
    self.Title_ImgVia = textInter(self.frame,self.Text,16,0.56,0.38,'w')
    self.Title_ImgVia.create_Tittle()

    self.imgViaBoton = Button(self.frame,text="Subir Imagen",bg="black",fg="white", cursor="hand2", font=(40), bd=4, command=self.abrirArchivo)
    self.imgViaBoton.place(relx=0.56, rely=0.61)
    self.imgViaBoton.bind("<Enter>",self.enBotonImagenVia)
    self.imgViaBoton.bind("<Leave>",self.fueraBotonImagenVia)
    self.confirmacionImagenCargada = Label(self.frame, text="No se ha cargado la imagen", bg="white", font=(5), fg="red")
    self.confirmacionImagenCargada.place(relx=0.65, rely=0.61)
    self.imagenViaEntrada = ""
    self.imVia= ImInter(self.frame,"Vias Icon.png", 0.61,0.51)
    self.imVia.sizeImage(150,200)
    self.imVia.create()

    self.Text="Limite Velocidad (km/h):"
    self.Title_LimVel = textInter(self.frame,self.Text,16,0.15,0.57,'w')
    self.Title_LimVel.create_Tittle()
    self.limiteVelocidad= StringVar()
    self.entradaLimiteVelocidad = Entry(self.frame,textvariable=self.limiteVelocidad,width=10, font = ('comics Sans MS',18))
    self.entradaLimiteVelocidad.place(relx = 0.34,rely=0.57,anchor ='w')

    self.Text="Multa:"
    self.Title_multa = textInter(self.frame,self.Text,16,0.15,0.64,'w')
    self.Title_multa.create_Tittle()
    self.multa= DoubleVar(self.frame,value=500000)
    self.entrada_multa = Entry(self.frame,textvariable=self.multa,width=10, font = ('comics Sans MS',18))
    self.entrada_multa.place(relx = 0.34,rely=0.64,anchor ='w')

    self.Button_guardar = BottInter(self.frame,"Boton_guardar.png",0.5,0.8,None, self.make_guardar_via)
    self.Button_guardar.modzise(250,60)
    self.Button_guardar.create()

    self.canvas = Canvas(self.frame,bg="white",width=3,height=370,relief=FLAT)
    self.canvas.create_line(1.5, 0, 1.5, 370)
    self.canvas.place(relx = 0.5,rely=0.5,anchor = CENTER)

  def abrirArchivo(self):
    self.imagenViaEntrada = str(filedialog.askopenfile(title="Abrir Archivo Imagen de Via",initialdir="C:/",
      filetypes=(("PNG Image","*.png"),("JPG Image","*.jpg"))))
    startPath = self.imagenViaEntrada.find("'")
    endPath = self.imagenViaEntrada.find("'",startPath+1)
    self.imagenViaEntrada = self.imagenViaEntrada[startPath+1:endPath]
    if self.imagenViaEntrada != "Non":
        self.confirmacionImagenCargada.config(text="Imagen Cargada", fg="green")
        self.imVia.panel.destroy()
        self.imVia= ImInter(self.frame,self.imagenViaEntrada, 0.65,0.51)
        self.imVia.sizeImage(150,200)
        self.imVia.create()

  def enBotonImagenVia(self, event):
    self.imgViaBoton.config(bd=6)

  def fueraBotonImagenVia(self, event):
    self.imgViaBoton.config(bd=4)
  
  def make_guardar_via(self):
    via = self.NombreVia.get()
    imagenViaPath = self.imagenViaEntrada
    limiteVelocidad = self.limiteVelocidad.get()
    multa = self.multa.get()
    messageBoxTit = "Error en información"
    if (via!="" and imagenViaPath!="Non" and limiteVelocidad !="" and multa!=""):
      try:
        imagenViaObjeto = Imagenes.Imagen(imagenViaPath)
        imagenVia = imagenViaObjeto.aHexaDecimalStr()
      except FileNotFoundError:
        imagenViaObjeto = Imagenes.Imagen("Vias Icon.png")
        imagenVia = imagenViaObjeto.aHexaDecimalStr()
      try:
        limiteVelocidad = float(limiteVelocidad)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"El limite de velocidad debe ser un Número.")
      try:
        multa = float(multa)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"La multa debe ser un Número.")
      conexionSlow = bD.ConexionBaseDeDatosSlow()
      conexionSlow.cursorSlow.execute(f"SELECT VIA FROM VIAS WHERE VIA='{via}'")
      posiblesVias = conexionSlow.cursorSlow.fetchall()
      conexionSlow.cerrarBaseDeDatosSlow()
      if len(posiblesVias)==0:
        return self.crearVia(via,imagenVia,limiteVelocidad,multa)
      else:
        return self.actualizarVia(via,imagenVia,limiteVelocidad,multa)
    else:
      return self.mensaje()

  def crearVia(self,via,imagenVia,limiteVelocidad,multa):
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.cursorSlow.execute(f"INSERT INTO VIAS (VIA,IMAGENVIA,LIMITEVELOCIDAD,MULTA) VALUES ('{via}','{imagenVia}',{limiteVelocidad},{multa})")
    conexionSlow.cursorSlow.execute(f"SELECT * FROM VIAS WHERE VIA='{via}'")
    viaEncontrada = conexionSlow.cursorSlow.fetchall()
    conexionSlow.cerrarBaseDeDatosSlow()
    if not len(viaEncontrada)==0:
      return messagebox.showinfo("Via Guardada",f"La vía ha sido creada y guardada.\nEl ID de la vía {viaEncontrada[0][1]} es {viaEncontrada[0][0]}")

  def actualizarVia(self,via,imagenVia,limiteVelocidad,multa):
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.cursorSlow.execute(f"UPDATE VIAS SET VIA='{via}', IMAGENVIA='{imagenVia}', LIMITEVELOCIDAD={limiteVelocidad}, MULTA={multa} WHERE VIA='{via}'")
    conexionSlow.cursorSlow.execute(f"SELECT * FROM VIAS WHERE VIA='{via}'")
    viaEncontrada = conexionSlow.cursorSlow.fetchone()
    conexionSlow.cerrarBaseDeDatosSlow()
    if not len(viaEncontrada)==0:
      return messagebox.showinfo("Via Guardada",f"La vía ha sido actualizada con éxito.\nEl ID de la vía {viaEncontrada[1]} es {viaEncontrada[0]}")
  
  def buscarVia(self):
    via = self.NombreVia.get()
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.cursorSlow.execute(f"SELECT * FROM VIAS WHERE VIA='{via}'")
    datosVia = conexionSlow.cursorSlow.fetchall()
    conexionSlow.cerrarBaseDeDatosSlow()
    if not len(datosVia)==0:
        self.NombreVia.set(datosVia[0][1])

        self.carpetaImgVias = ArchivosYCarpetas.Carpeta("RecursosGraficos\\ImgVias")
        if not self.carpetaImgVias.existeCarpeta:
          self.carpetaImgVias.crearCarpeta()
        self.imagenVia = Imagenes.ImagenHexaDecimalStr(datosVia[0][2])
        self.imagenViaPath = f"RecursosGraficos\\ImgVias\\imagenVia-{datosVia[0][1]}.png"
        try:
          os.remove(self.imagenViaPath)
        except FileNotFoundError:
          pass
        self.imagenVia.aImagen(self.imagenViaPath)
        self.imagenViaEntrada = self.imagenViaPath
        self.imVia= ImInter(self.frame,self.imagenViaEntrada, 0.65,0.51)
        self.imVia.sizeImage(150,200)
        self.imVia.create()

        self.limiteVelocidad.set(datosVia[0][3])
        self.multa.set(datosVia[0][4])
        return messagebox.showinfo("Datos Cargados",f"Datos de la vía {datosVia[0][1]} ID {datosVia[0][0]} cargados")
    else:
      return messagebox.showerror("Error al ingresar los datos",f"No existe la vía {via}")

  def eliminarVia(self):
    via = self.NombreVia.get()
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.cursorSlow.execute(f"SELECT * FROM VIAS WHERE VIA='{via}'")
    datosVia = conexionSlow.cursorSlow.fetchall()
    conexionSlow.cerrarBaseDeDatosSlow()
    if len(datosVia)==0:
      return messagebox.showerror("Error al ingresar los datos",f"No existe la vía {via}")
    else:
      eliminarViaConf = messagebox.askyesno("Eliminar Vía",f"¿Está seguro de eliminar la vía {datosVia[0][1]} ID {datosVia[0][0]}?")
      if eliminarViaConf:
        conexionSlow = bD.ConexionBaseDeDatosSlow()
        conexionSlow.cursorSlow.execute(f"DELETE FROM VIAS WHERE VIA='{via}'")
        conexionSlow.cerrarBaseDeDatosSlow()
        return messagebox.showinfo("Proceso Completado",f"La vía {datosVia[0][1]} ID {datosVia[0][0]} ha sido eliminada")
  
  def mensaje(self):
    messagebox.showinfo("Información","Por favor, rellene todas las casillas.")
    
  def go_back(self):
    global ac
    ac=False
    self.frame.pack_forget()
    self.go_back = self.app.start_page()

  def Open_menu(self,event=None):
    global ac
    self.name="video"

    if (ac== False):

      self.Menu = menu(self.name,root=self.frame, app=self)    
      self.Menu.start_page()
      ac=True

class GuardarVehiculo(info):
  def __init__(self,idusuario=None, idvideo=None,velocidad=None,velocidad_excedida=None, captura=None, master=None, app=None):
    super().__init__(master,app)

  def own_widgets(self):
    self.iminfo= ImInter(self.frame,"Vias Icon.png", 0.8,0.06) 
    self.iminfo.sizeImage(70,110)
    self.iminfo.create()

    self.police = ImInter(self.frame,f"{imagenPerfilPath}", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

    self.Text="Editar o Borrar Vehículo"
    self.Title1 = textInter(self.frame,self.Text,30,0.5,0.225)
    self.Title1.create_Tittle()
    
    self.Text="Para editar o borrar un vehículo\ningrese el ID o la Placa:"
    self.Title_vehiculoEditar = textInter(self.frame,self.Text,14,0.21,0.33,'w')
    self.Title_vehiculoEditar.create_Tittle()

    self.Text="ID Vehículo:"
    self.Title_idVehiculo = textInter(self.frame,self.Text,16,0.08,0.41,'w')
    self.Title_idVehiculo.create_Tittle()
    self.idVehiculo= StringVar(self.frame)
    self.entradaidVehiculo = Entry(self.frame,textvariable=self.idVehiculo,width=10,font = ('comics Sans MS',18))
    self.entradaidVehiculo.place(relx = 0.18,rely=0.41,anchor ='w')

    self.Text="Placa:"
    self.Title_placa= textInter(self.frame,self.Text,16,0.31,0.41,'w')
    self.Title_placa.create_Tittle()
    self.placa= StringVar(self.frame)
    self.entradaplaca = Entry(self.frame,textvariable=self.placa,width=10,font = ('comics Sans MS',18))
    self.entradaplaca.place(relx = 0.38,rely=0.41,anchor ='w')

    self.ButtonBuscar= BottInter(self.frame,"BotonBuscar.png",0.23,0.48,None, self.buscarVehiculo)
    self.ButtonBuscar.modzise(120,45)
    self.ButtonBuscar.create()

    self.BotonEliminarVehiculo= BottInter(self.frame,"BotonEliminarVehiculo.png",0.34,0.48,None, self.eliminarVehiculo)
    self.BotonEliminarVehiculo.modzise(120,45)
    self.BotonEliminarVehiculo.create()

    self.col1x = 0.15
    self.col1bx = self.col1x+0.19
    self.col2x= 0.56
    self.col2bx= self.col2x+0.19
    self.coly = 0.57
    self.col2y = 0.315
    self.interAlt = 0.07

    self.Text="ID Video:"
    self.Title_IdVideo = textInter(self.frame,self.Text,16,self.col1x,self.coly,'w')
    self.Title_IdVideo.create_Tittle()
    self.IdVideo= Label(self.frame,width=10, font = ('comics Sans MS',18),bg="white")
    self.IdVideo.place(relx = self.col1bx ,rely=self.coly,anchor ='w')
    self.IdVideoCamp = "-"
    self.IdVideo.config(text=self.IdVideoCamp)

    self.Text="Tipo Vehículo:"
    self.Title_TipoVehiculo = textInter(self.frame,self.Text,16,self.col1x,self.coly+self.interAlt,'w')
    self.Title_TipoVehiculo.create_Tittle()
    self.TipoVehiculo= StringVar()
    self.entrada_TipoVehiculo = Entry(self.frame,textvariable=self.TipoVehiculo,width=10, font = ('comics Sans MS',18))
    self.entrada_TipoVehiculo.place(relx = self.col1bx ,rely=self.coly+self.interAlt,anchor ='w')

    self.Text="Velocidad:"
    self.Title_Velocidad = textInter(self.frame,self.Text,16,self.col1x,self.coly+self.interAlt*2,'w')
    self.Title_Velocidad.create_Tittle()
    self.Velocidad= StringVar()
    self.entrada_Velocidad = Entry(self.frame,textvariable=self.Velocidad,width=10, font = ('comics Sans MS',18))
    self.entrada_Velocidad.place(relx = self.col1bx ,rely=self.coly+self.interAlt*2,anchor ='w')

    self.Text="Velocidad Excedida:"
    self.Title_VelocidadExcedida = textInter(self.frame,self.Text,16,self.col1x,self.coly+self.interAlt*3,'w')
    self.Title_VelocidadExcedida.create_Tittle()
    self.VelocidadExcedida = Label(self.frame,width=11, font = ('comics Sans MS',18),bg="white")
    self.VelocidadExcedida.place(relx = self.col1bx ,rely=self.coly+self.interAlt*3,anchor ='w')
    self.VelocidadExcedidaCamp = "-"
    self.VelocidadExcedida.config(text=self.VelocidadExcedidaCamp)

    self.Text="Imagen Vehiculo:"
    self.Title_ImgVehiculo = textInter(self.frame,self.Text,16,self.col2x,self.col2y,'w')
    self.Title_ImgVehiculo.create_Tittle()
    self.imVehiculo= ImInter(self.frame,"Video Speed Icon.png", self.col2x+0.05,self.col2y+self.interAlt*1.8)
    self.imVehiculo.sizeImage(150,200)
    self.imVehiculo.create()
    self.imgVehiculoBoton = Button(self.frame,text="Subir Imagen",bg="black",fg="white", cursor="hand2", font=(40), bd=4, command=self.abrirArchivo)
    self.imgVehiculoBoton.place(relx=self.col2x, rely=self.col2y+self.interAlt*3)
    self.imgVehiculoBoton.bind("<Enter>",self.enBotonImagenVehiculo)
    self.imgVehiculoBoton.bind("<Leave>",self.fueraBotonImagenVehiculo)
    self.confirmacionImagenCargada = Label(self.frame, text="No se ha cargado la imagen", bg="white", font=(5), fg="red")
    self.confirmacionImagenCargada.place(relx=self.col2x+0.09, rely=self.col2y+self.interAlt*3)
    self.imagenVehiculoEntrada = ""

    self.Text="Via:"
    self.Title_IdVia = textInter(self.frame,self.Text,16,self.col2x,self.col2y+self.interAlt*4,'w')
    self.Title_IdVia.create_Tittle()
    self.IdVia= Label(self.frame,width=10, font = ('comics Sans MS',18),bg="white")
    self.IdVia.place(relx = self.col2bx ,rely=self.col2y+self.interAlt*4,anchor ='w')
    self.IdViaCamp = "-"
    self.IdVia.config(text=self.IdViaCamp)

    self.Text="Multa:"
    self.Title_Multa = textInter(self.frame,self.Text,16,self.col2x,self.col2y+self.interAlt*5,'w')
    self.Title_Multa.create_Tittle()
    self.Multa= StringVar()
    self.entrada_Multa = Entry(self.frame,textvariable=self.Multa,width=10, font = ('comics Sans MS',18))
    self.entrada_Multa.place(relx = self.col2bx ,rely=self.col2y+self.interAlt*5,anchor ='w')

    self.Text="Usuario:"
    self.Title_IdUsuario = textInter(self.frame,self.Text,16,self.col2x,self.col2y+self.interAlt*6,'w')
    self.Title_IdUsuario.create_Tittle()
    self.IdUsuario = Label(self.frame,width=10, font = ('comics Sans MS',18),bg="white")
    self.IdUsuario.place(relx = self.col2bx ,rely=self.col2y+self.interAlt*6,anchor ='w')
    self.IdUsuarioCamp = "-"
    self.IdUsuario.config(text=self.IdUsuarioCamp)

    self.Button_guardar = BottInter(self.frame,"Boton_guardar.png",0.65,0.9,None, self.make_guardar_Vehiculo)
    self.Button_guardar.modzise(250,60)
    self.Button_guardar.create()

    self.canvas = Canvas(self.frame,bg="white",width=3,height=370,relief=FLAT)
    self.canvas.create_line(1.5, 0, 1.5, 370)
    self.canvas.place(relx = 0.5,rely=0.5,anchor = CENTER)

  def abrirArchivo(self):
    self.imagenVehiculoEntrada = str(filedialog.askopenfile(title="Abrir Archivo Imagen de Via",initialdir="C:/",
      filetypes=(("PNG Image","*.png"),("JPG Image","*.jpg"))))
    startPath = self.imagenVehiculoEntrada.find("'")
    endPath = self.imagenVehiculoEntrada.find("'",startPath+1)
    self.imagenVehiculoEntrada = self.imagenVehiculoEntrada[startPath+1:endPath]
    if self.imagenVehiculoEntrada != "Non":
        self.confirmacionImagenCargada.config(text="Imagen Cargada", fg="green")
        self.imVehiculo.panel.destroy()
        self.imVehiculo= ImInter(self.frame,self.imagenVehiculoEntrada,self.col2x+0.05,self.col2y+self.interAlt*1.8)
        self.imVehiculo.sizeImage(150,200)
        self.imVehiculo.create()

  def enBotonImagenVehiculo(self, event):
    self.imgVehiculoBoton.config(bd=6)

  def fueraBotonImagenVehiculo(self, event):
    self.imgVehiculoBoton.config(bd=4)
  
  def make_guardar_Vehiculo(self):
    idVehiculo= self.idVehiculo.get()
    idVideo = self.IdVideoCamp
    imagenVehiculoPath = self.imagenVehiculoEntrada
    tipoVehiculo = self.TipoVehiculo.get()
    placa = self.placa.get()
    velocidad = self.Velocidad.get()
    idVia = self.IdViaCamp
    velocidadExcedida = self.VelocidadExcedidaCamp
    multa = self.Multa.get()
    idUsuarioVehiculo = self.IdUsuarioCamp
    messageBoxTit = "Error en información"
    if (idVehiculo!="" and idVideo!="" and imagenVehiculoPath!="Non" and tipoVehiculo!="" and placa!=""
     and velocidad!="" and idVia!="" and velocidadExcedida!="" and multa!="" and idUsuarioVehiculo!=""):
      try:
        idVehiculo = int(idVehiculo)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"El ID de Vehículo debe ser un Número.")
      try:
        idVideo = int(idVideo)
      except ValueError:
        pass
      try:
        imagenVehiculoObjeto = Imagenes.Imagen(imagenVehiculoPath)
        imagenVehiculo = imagenVehiculoObjeto.aHexaDecimalStr()
      except FileNotFoundError:
        imagenVehiculoObjeto = Imagenes.Imagen("Video Speed Icon.png")
        imagenVehiculo = imagenVehiculoObjeto.aHexaDecimalStr()
      try:
        velocidad = float(velocidad)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"La velocidad debe ser un Número.")
      try:
        idVia = int(idVia)
      except ValueError:
        conexionSlow = bD.ConexionBaseDeDatosSlow()
        conexionSlow.cursorSlow.execute(f"SELECT IDVIA FROM VEHICULOS WHERE IDVEHICULO={idVehiculo}")
        idVia= int(conexionSlow.cursorSlow.fetchone()[0])
        conexionSlow.cerrarBaseDeDatosSlow()
      if (velocidadExcedida=="VERDADERO"):
        velocidadExcedida = True
      elif (velocidadExcedida=="FALSO"):
        velocidadExcedida = False
      else:
        return messagebox.showerror(messageBoxTit,"La velocidad excedida debe ser VERDADERO o FALSO.")
      conexionSlow = bD.ConexionBaseDeDatosSlow()
      conexionSlow.cursorSlow.execute(f"SELECT LIMITEVELOCIDAD FROM VIAS WHERE IDVIA='{idVia}'")
      velocidadEnVia = conexionSlow.cursorSlow.fetchone()
      velocidadEnVia = float(velocidadEnVia[0])
      conexionSlow.cerrarBaseDeDatosSlow()
      if velocidad>velocidadEnVia:
        velocidadExcedida = True
      else:
        velocidadExcedida = False
      self.VelocidadExcedidaCamp = "VERDADERO" if velocidadExcedida else "FALSO"
      self.VelocidadExcedida.config(text=self.VelocidadExcedidaCamp)
      try:
        multa = float(multa)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"La multa debe ser un Número.")
      try:
        idUsuarioVehiculo = int(idUsuarioVehiculo)
      except ValueError:
        conexionSlow = bD.ConexionBaseDeDatosSlow()
        conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM VEHICULOS WHERE IDVEHICULO={idVehiculo}")
        idUsuario = int(conexionSlow.cursorSlow.fetchone()[0])
        conexionSlow.cerrarBaseDeDatosSlow()
      conexionSlow = bD.ConexionBaseDeDatosSlow()
      conexionSlow.cursorSlow.execute(f"UPDATE VEHICULOS SET CAPTURA='{imagenVehiculo}', TIPOVEHICULO='{tipoVehiculo}', PLACA='{placa}', VELOCIDAD={velocidad}, VELOCIDADEXCEDIDA={velocidadExcedida}, MULTA={multa} WHERE IDVEHICULO='{idVehiculo}'")
      conexionSlow.cursorSlow.execute(f"SELECT * FROM VEHICULOS WHERE IDVEHICULO='{idVehiculo}'")
      vehiculoEncontrado = conexionSlow.cursorSlow.fetchall()
      conexionSlow.cerrarBaseDeDatosSlow()
      if not len(vehiculoEncontrado)==0:
        return messagebox.showinfo("Vehículo Guardado",f"El vehículo ha sido guardado con éxito.\nEl ID del vehículo es {vehiculoEncontrado[0][0]} de placa {vehiculoEncontrado[0][4]}")
      else:
        return messagebox.showinfo("Información",f"No se ha encontrado el vehículo\nID: {idVehiculo} de placa {placa}")
    else:
      return self.mensaje()
  
  def buscarVehiculo(self):
    idVehiculo = self.idVehiculo.get()
    placa = self.placa.get()
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.cursorSlow.execute(f"SELECT * FROM VEHICULOS WHERE IDVEHICULO='{idVehiculo}'")
    datosVehiculo = conexionSlow.cursorSlow.fetchall()
    if len(datosVehiculo)==0:
      conexionSlow.cursorSlow.execute(f"SELECT * FROM VEHICULOS WHERE PLACA='{placa}'")
      datosVehiculo = conexionSlow.cursorSlow.fetchall()
    conexionSlow.cerrarBaseDeDatosSlow()
    if not len(datosVehiculo)==0:
        self.idVehiculo.set(datosVehiculo[0][0])
        self.IdVideoCamp = datosVehiculo[0][1]
        self.IdVideo.config(text=self.IdVideoCamp)

        self.carpetaImgVehiculos = ArchivosYCarpetas.Carpeta("RecursosGraficos\\ImgVehiculos")
        if not self.carpetaImgVehiculos.existeCarpeta:
          self.carpetaImgVehiculos.crearCarpeta()
        self.imagenVehiculo = Imagenes.ImagenHexaDecimalStr(datosVehiculo[0][2])
        self.imagenVehiculoPath = f"RecursosGraficos\\ImgVehiculos\\imagenVehiculo-{datosVehiculo[0][0]}-{datosVehiculo[0][4]}.png"
        try:
          os.remove(self.imagenVehiculoPath)
        except FileNotFoundError:
          pass
        self.imagenVehiculo.aImagen(self.imagenVehiculoPath)
        self.imagenVehiculoEntrada = self.imagenVehiculoPath
        self.imVehiculo= ImInter(self.frame,self.imagenVehiculoEntrada,self.col2x+0.05,self.col2y+self.interAlt*1.8)
        self.imVehiculo.sizeImage(150,200)
        self.imVehiculo.create()

        self.TipoVehiculo.set(datosVehiculo[0][3])
        self.placa.set(datosVehiculo[0][4])
        self.Velocidad.set(datosVehiculo[0][5])

        conexionSlow = bD.ConexionBaseDeDatosSlow()
        conexionSlow.cursorSlow.execute(f"SELECT VIA FROM VIAS WHERE IDVIA={datosVehiculo[0][6]}")
        viaActVehic =conexionSlow.cursorSlow.fetchone()
        self.IdViaCamp = viaActVehic[0]
        self.IdVia.config(text=self.IdViaCamp)

        self.VelocidadExcedidaCamp = datosVehiculo[0][7]
        if self.VelocidadExcedidaCamp==1:
          self.VelocidadExcedidaCamp="VERDADERO"
        else:
          self.VelocidadExcedidaCamp="FALSO"
        self.VelocidadExcedida.config(text=self.VelocidadExcedidaCamp)
        self.Multa.set(datosVehiculo[0][8])

        conexionSlow.cursorSlow.execute(f"SELECT NOMBRE,APELLIDO FROM USUARIOS WHERE IDUSUARIO={datosVehiculo[0][9]}")
        usuarioActVehic =conexionSlow.cursorSlow.fetchone()
        self.IdUsuarioCamp = usuarioActVehic[0]+"\n"+usuarioActVehic[1]
        self.IdUsuario.config(text=self.IdUsuarioCamp)
        conexionSlow.cerrarBaseDeDatosSlow()
        return messagebox.showinfo("Datos Cargados",f"Datos del Vehículo ID: {datosVehiculo[0][0]} Placa: {datosVehiculo[0][4]} cargados")
    else:
      return messagebox.showerror("Error al ingresar los datos",f"No existe el vehiculo ID: {idVehiculo} o Placa: {placa}")

  def eliminarVehiculo(self):
    idVehiculo = self.idVehiculo.get()
    placa = self.placa.get()
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    conexionSlow.cursorSlow.execute(f"SELECT * FROM VEHICULOS WHERE IDVEHICULO='{idVehiculo}'")
    datosVehiculo = conexionSlow.cursorSlow.fetchall()
    conexionSlow.cerrarBaseDeDatosSlow()
    bandera = False
    if len(datosVehiculo)==0:
      conexionSlow = bD.ConexionBaseDeDatosSlow()
      conexionSlow.cursorSlow.execute(f"SELECT * FROM VEHICULOS WHERE PLACA='{placa}'")
      datosVehiculo = conexionSlow.cursorSlow.fetchall()
      conexionSlow.cerrarBaseDeDatosSlow()
      if len(datosVehiculo)==0:
        return messagebox.showerror("Error al ingresar los datos",f"No existe el vehículo ID: {idVehiculo} o Placa: {placa}")
      else:
        bandera = True
    else:
      bandera = True
    if bandera:
      eliminarVehiculoConf = messagebox.askyesno("Eliminar Vehículo",f"¿Está seguro de eliminar el Vehículo ID: {datosVehiculo[0][0]} Placa: {datosVehiculo[0][4]}?")
      if eliminarVehiculoConf:
        conexionSlow = bD.ConexionBaseDeDatosSlow()
        conexionSlow.cursorSlow.execute(f"DELETE FROM VEHICULOS WHERE IDVEHICULO='{datosVehiculo[0][0]}'")
        conexionSlow.cerrarBaseDeDatosSlow()
        return messagebox.showinfo("Proceso Completado",f"El Vehículo ID: {datosVehiculo[0][0]} Placa: {datosVehiculo[0][4]} ha sido eliminado")
  
  def mensaje(self):
    messagebox.showinfo("Información","Por favor, rellene todas las casillas.")
    
  def go_back(self):
    global ac
    ac=False
    self.frame.pack_forget()
    self.go_back = self.app.start_page()

  def Open_menu(self,event=None):
    global ac
    self.name="video"

    if (ac== False):

      self.Menu = menu(self.name,root=self.frame, app=self)    
      self.Menu.start_page()
      ac=True


class textInter(ImInter):

  def __init__(self, frame,texto,size,relx,rely,anchor=None):
    self.frame = frame
    self.texto = texto
    self.relx = relx
    self.rely = rely
    self.size=size
    self.anchor=anchor
  def create_Tittle(self):
    self.panel=Label(self.frame, text = self.texto,bg= 'white',font=('Helvetica', self.size, 'bold'))
    self.show()
  def create_paragraph(self):
    self.panel=Label(self.frame, text = self.texto,bg= 'white',font=('Helvetica', self.size))
    self.show()


class VidInter(ImInter):
  def __init__(self, frame,objeto,x,y,canvas,variable,app=None):

    self.frame = frame
    self.objeto = objeto
    self.app=app
    self.y = y
    self.x = x
    self.variable = variable
    self.canvas = canvas
    self.cap = cv2.VideoCapture(self.objeto)
    self.run = False
  
  def create_label(self):
    self.panel = Label(self.canvas)
    
  
  def show(self):
    self.canvas.create_window(self.x, self.y, window=self.panel, anchor=NW)
  
  def create(self):
    self.ret, self.frame2 = self.cap.read()
    if self.ret:
      self.frame2 = imutils.resize(self.frame2, height=215)
      self.frame2 = cv2.cvtColor(self.frame2, cv2.COLOR_BGR2RGB)

      self.im = Image.fromarray(self.frame2)
      self.img = ImageTk.PhotoImage(image=self.im)

      self.panel.configure( image = self.img)
      self.panel.image = self.img

    if self.run:
      self.panel.after(1, self.create)
      
  def action(self):
    self.panel.bind('<Button-1>', self.Pause_play)
    
  def Pause_play(self,Event):
    
    if self.run:
      self.run = False  
      
    else:
      self.run = True
      for x in range(len(History_Videos)):
        global id
        if (x!= self.variable):
          globals()["video" + str(x)].pausar_otros_videos()
          
      self.panel.after(1, self.create)
  
  def pausar_otros_videos(self):
    self.run = False
    

class history(info):
  global id
  
  def own_widgets(self):
    self.iminfo= ImInter(self.frame,"History Icon.png", 0.82,0.06) 
    self.iminfo.sizeImage(80,80)
    self.iminfo.create()

    self.Text="Histórico"
    self.Title1 = textInter(self.frame,self.Text,30,0.5,0.23)
    self.Title1.create_Tittle()

    self.canvas = Canvas(self.frame, bg='white')
    self.canvas.place(relx = 0.5,rely=0.58,anchor = CENTER, relheight=0.5,relwidth=0.61)

    self.scrollbar = Scrollbar(self.canvas,bg='white')
    self.scrollbar.place(relx = 0.99,rely=0.5,anchor = CENTER, relheight=1)

    self.y = 0
    self.x = 0
    self.contador=0

    if len(History_Videos)==0:
      self.canvas.create_text(self.x+10,self.y+10,font=('Helvetica', 11, 'bold'), text="Aún no hay vídeos para mostrar")
    else:
      for x in range(len(History_Videos)):
        global id

        conexionSlow = bD.ConexionBaseDeDatosSlow()
        self.IdVideo = History_Videos[x][0]

        self.IdUsuario = History_Videos[x][1]
        conexionSlow.cursorSlow.execute(f"SELECT NOMBRE,APELLIDO FROM USUARIOS WHERE IDUSUARIO={self.IdUsuario}")
        self.UsuarioVideo = conexionSlow.cursorSlow.fetchone()
        self.UsuarioVideo = self.UsuarioVideo[0]+" "+self.UsuarioVideo[1]

        self.videoPath = History_Videos[x][2]
        globals()["video" + str(self.contador)] = VidInter(self.frame,self.videoPath,self.x,self.y,self.canvas,self.contador,self)
          
        globals()["button_detection" + str(self.contador)]= BottInter(self.canvas,"Video Speed Icon.png",0.5,0.8,'',partial(self.verGrafica,self.IdVideo))
        globals()["button_detection" + str(x)].modzise(95,50)
        globals()["button_detection" + str(x)].create()
        self.window= globals()["button_detection" + str(x)].return_panel()

        self.IdVia = History_Videos[x][3]
        conexionSlow.cursorSlow.execute(f"SELECT VIA FROM VIAS WHERE IDVIA={self.IdVia}")
        self.Via = conexionSlow.cursorSlow.fetchone()
        self.Via = self.Via[0]

        self.Ciudad = History_Videos[x][4]
        self.Direccion = History_Videos[x][5]
        self.Fecha = History_Videos[x][6]

        self.text= f"ID: {self.IdVideo} - {self.Via} - {self.Ciudad} - {self.Direccion}\n{self.Fecha} - {self.UsuarioVideo}"
        self.canvas.create_text(self.x+160,self.y+250,font=('Helvetica', 11, 'bold'), text=self.text)

        self.canvas.create_window(self.x+390,self.y+245, window=self.window, anchor=CENTER)
        
        if (self.x==0):
          self.x=500
        else:
          self.x=0
        self.contador+=1
        if (self.contador % 2 ==0):
          self.y+=300
      conexionSlow.cerrarBaseDeDatosSlow()
    
    self.create_video()

    self.canvas.config(yscrollcommand=self.scrollbar.set, scrollregion = self.canvas.bbox("all"))
    
    self.scrollbar.configure(command= self.canvas.yview )

  def verGrafica(self,idVideo):
    conexionSlow = bD.ConexionBaseDeDatosSlow()
    carpetaGraficas = ArchivosYCarpetas.Carpeta("Graficas")
    if not carpetaGraficas.existeCarpeta:
      carpetaGraficas.crearCarpeta()
    conexionSlow.cursorSlow.execute(f"SELECT GRAFICA FROM DETECCIONYVIDEOS WHERE IDVIDEO={idVideo}")
    self.graficaPath = f"Graficas\\GraficaVideo-{idVideo}.png"
    '''
    r = conexionSlow.cursorSlow.fetchone()[0]
    graficaBinaria = str(r).strip()
    graficaImagenBin = Imagenes.ImagenHexaDecimalStr(graficaBinaria)
    graficaImagenBin.aImagen(self.graficaPath)
    '''
    conexionSlow.cerrarBaseDeDatosSlow()
    self.paginaVerGrafica = verGrafica(idVideo,self.graficaPath,master=self.master,app=self)
    self.frame.pack_forget()
    self.paginaVerGrafica.start_page()
    
  
  def create_video(self):
     for x in range(len(History_Videos)):
      global id
      globals()["video" + str(x)].create_label()
      globals()["video" + str(x)].show()
      globals()["video" + str(x)].create()
      globals()["video" + str(x)].action()
        
  def Open_menu(self,event=None):
    global ac
    self.name="history"
    self.Menu = menu(self.name,root=self.frame, app=self, additional=self.canvas)
    if (ac== False):
    
      self.Menu.start_page()
      ac=True

class verGrafica(info):

  def __init__(self,idVideo,graficaPath, master=None, app=None):
      self.idVideo = idVideo
      self.graficaPath = graficaPath
      super().__init__(master, app)
  
  def own_widgets(self):
    self.iminfo= ImInter(self.frame,"History Icon.png", 0.82,0.06) 
    self.iminfo.sizeImage(80,80)
    self.iminfo.create()

    self.Text=f"Ver Gráfica\nVideo ID:{self.idVideo}"
    self.Title1 = textInter(self.frame,self.Text,30,0.5,0.23)
    self.Title1.create_Tittle()

    self.imgGrafica = ImInter(self.frame,self.graficaPath, 0.495,0.56)
    self.imgGrafica.sizeImage(488,756)
    self.imgGrafica.create()

  def Open_menu(self,event=None):
    global ac
    self.name="history"
    self.Menu = menu(self.name,root=self.frame, app=self)
    if (ac==False):
      self.Menu.start_page()
      ac=True
  
  def go_back(self):
    global ac
    ac=False
    self.frame.pack_forget()
    self.paginaAnterior = history()
    self.frame.pack_forget()
    self.paginaAnterior.start_page()

#Datos

def tomarInfoUsuario():
  global idUsuario,usuario,nombreUsuario,apellidoUsuario,tipoDocumento,numeroDocumento,imagenPerfilPath
  global tipoSangre,jefe,policiasAsignados,asignacion,rol,numeroCuadrante,cuadrante
  global ciudad,departamento,horario,estado,direccion,celular,correo,fondo
  conexionSlow = bD.ConexionBaseDeDatosSlow()
  conexionSlow.cursorSlow.execute(f"SELECT * FROM USUARIOS WHERE IDUSUARIO={idUsuario}")
  listaInfoUsuario = conexionSlow.cursorSlow.fetchall()
  usuario = f"{listaInfoUsuario[0][1]}"
  nombreUsuario = f"{listaInfoUsuario[0][3]}"
  apellidoUsuario = f"{listaInfoUsuario[0][4]}"
  tipoDocumento = f"{listaInfoUsuario[0][5]}"
  numeroDocumento = int(listaInfoUsuario[0][6])
  imagenPerfil = listaInfoUsuario[0][7]
  tipoSangre = f"{listaInfoUsuario[0][8]}"
  jefe = int(listaInfoUsuario[0][9])
  policiasAsignados =f"{listaInfoUsuario[0][10]}"
  asignacion = f"{listaInfoUsuario[0][11]}"
  rol = f"{listaInfoUsuario[0][12]}"
  numeroCuadrante = int(listaInfoUsuario[0][13])
  cuadrante = f"{listaInfoUsuario[0][14]}"
  ciudad = f"{listaInfoUsuario[0][15]}"
  departamento = f"{listaInfoUsuario[0][16]}"
  horario = f"{listaInfoUsuario[0][17]}"
  estado = f"{listaInfoUsuario[0][18]}"
  direccion = f"{listaInfoUsuario[0][19]}"
  celular = int(listaInfoUsuario[0][20])
  correo = f"{listaInfoUsuario[0][21]}"
  fondo = f"{listaInfoUsuario[0][22]}"
  carpetaImgPerfil = ArchivosYCarpetas.Carpeta("RecursosGraficos\\ImagenesPerfil")
  if not carpetaImgPerfil.existeCarpeta:
    carpetaImgPerfil.crearCarpeta()
  imagenPerfil = Imagenes.ImagenHexaDecimalStr(imagenPerfil)
  imagenPerfilPath = f"RecursosGraficos\\ImagenesPerfil\\imagenPerfil-{idUsuario}.png"
  try:
    os.remove(imagenPerfilPath)
  except FileNotFoundError:
    pass
  imagenPerfil.aImagen(imagenPerfilPath)

def ordenarListaPaquete(lista):
  listaOr = []
  tam = len(lista)
  for i in range (0,tam):
    minAct = minListaPaquete(lista)
    listaOr.append(minAct)
    lista.remove(minAct)
  return listaOr

def minListaPaquete(lista):
  minLista = lista[0]
  numListaMinId = minLista[0]
  for i in lista:
    listaActual = i
    numListaActual = listaActual[0]
    if numListaActual<numListaMinId:
      numListaMinId = numListaActual
      minLista = listaActual
  return minLista

#Crea Ventana

def elUsuario(usuario):
  global idUsuario, infoUsuario
  global root, ac, id, play, ancho, alto, History_Videos, vias
  
  root = Tk()

  ac=False  
  id = 1
  play=False
  root.title("SLOW")
  ancho = root.winfo_screenwidth()
  alto = root.winfo_screenheight()
  root.geometry(f"{ancho}x{alto}+0+0")
  root.resizable(False,False)
  root.iconbitmap("RecursosGraficos\\Logo_Slow_Icon_Map.ico")
  root.configure(bg='white')

  idUsuario = usuario
  conexionSlow = bD.ConexionBaseDeDatosSlow()
  conexionSlow.cursorSlow.execute(f"SELECT NOMBRE,APELLIDO FROM USUARIOS WHERE IDUSUARIO={idUsuario}")
  nombreUsuario = conexionSlow.cursorSlow.fetchall()
  nombreUsuario = str(nombreUsuario[0][0]+" "+nombreUsuario[0][1]).upper()
  root.title(f"SLOW - USUARIO: {nombreUsuario}")
  tomarInfoUsuario()

  conexionSlow = bD.ConexionBaseDeDatosSlow()
  if rol=="JEFE":
    listaPoliciasAsignados = policiasAsignados.split(sep=",")
    listaPoliciasAsignados.append(idUsuario)
    videosInicial = []
    for i in listaPoliciasAsignados:
      conexionSlow.cursorSlow.execute(f"SELECT * FROM DETECCIONYVIDEOS WHERE IDUSUARIO={i}")
      videosPolicia = conexionSlow.cursorSlow.fetchall()
      for j in videosPolicia:
        videosInicial.append(j)
    History_Videos = ordenarListaPaquete(videosInicial)
  else:
    conexionSlow.cursorSlow.execute(f"SELECT * FROM DETECCIONYVIDEOS WHERE IDUSUARIO={idUsuario}")
    History_Videos = conexionSlow.cursorSlow.fetchall()
  conexionSlow.cerrarBaseDeDatosSlow()
  app = App(root)
  root.mainloop()