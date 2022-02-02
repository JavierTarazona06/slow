from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as MessageBox
from tkinter import ttk
from PIL import ImageTk, Image
import cv2
from functools import partial
import imutils
import ConexionBaseDeDatosSlow as bD
import Imagenes, ArchivosYCarpetas, os
from tkinter import messagebox


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

  def common_widgets(self):
  
    self.imSlow= ImInter(self.frame,"Logo_ SLOW.png", 0.5,0.1) 
    self.imSlow.create()

    self.imPolice= ImInter(self.frame,"Policia Nacional Logo.png", 0.1,0.1)
    self.imPolice.create()

    self.imColombia= ImInter(self.frame,"Colombia Slogan.png", 0.9,0.1)
    self.imColombia.create()

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

    self.police = ImInter(self.frame,"in.png", 0.2,0.1) 
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
        numeroDocumento = int(numeroDocumentoN)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"El Número de Documento debe ser un Número.")
    if numeroDocumento <= 99999:
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
      for i in listaPoliciasAsignadosN:
        try:
          idPolicia = int(i)
        except ValueError:
          return messagebox.showerror(messageBoxTit,"Recuerde ingresar solo los ID válidos de Slow para\nlos policías asignados separados por comas")
        conexionSlow.cursorSlow.execute(f"SELECT IDUSUARIO FROM USUARIOS WHERE IDUSUARIO='{idPolicia}' AND ROL='POLICIA'")
        policiaEncontrado = conexionSlow.cursorSlow.fetchall()
        if len(policiaEncontrado)==0:
          return messagebox.showerror(messageBoxTit, f"No existe el ID del policía {idPolicia}. Ingresar uno existente o crear uno nuevo")
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
        celular = int(celularN)
      except ValueError:
        return messagebox.showerror(messageBoxTit,"El Número de Celular debe ser un Número.")
      if celular <= 0:
        return messagebox.showerror(messageBoxTit,"El Número de Celular debe ser un Número mayor a 0.")
    correoN = str(self.correoEntrada.get())
    if correoN == "":
      return messagebox.showerror(messageBoxTit,messageBoxContent+"Correo")
    if (correo.find("@policia.gov.co")==-1):
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
      messagebox.showinfo("Información Slow", "Información Guardada Exitosamente.\nCierre sesión y vuelva a ingresar para ver los cambios")
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
    self.iminfo= ImInter(self.frame,"Video Speed Icon.png", 0.8,0.06) 
    self.iminfo.sizeImage(70,110)
    self.iminfo.create()

    self.Button_file = BottInter(self.frame,"Boton.png",0.33,0.78,None,self.Open_File)
    self.Button_file.modzise(370,60)
    self.Button_file.create()

    self.Button_life = BottInter(self.frame,"Boton_life.png",0.67,0.78,None)
    self.Button_life.modzise(370,60)
    self.Button_life.create()

    self.Text="Registrar Video"
    self.Title1 = textInter(self.frame,self.Text,30,0.5,0.23)
    self.Title1.create_Tittle()

    self.Text="A continuación puede registrar el video arrastrándolo o seleccionándolo desde la carpeta"
    self.paragraph1 = textInter(self.frame,self.Text,16,0.5,0.36)
    self.paragraph1.create_paragraph()

  def Open_File(self):
    self.File= filedialog.askopenfile(title="Abrir Archivo",initialdir="C:/",
    filetypes=(("MP4 video","*.mp4"),
    ("Windows video file (avi)","*.avi"),("Todos los Archivos","*.*")))

    if bool(self.File)!=0:  
      self.make_page_detection()        
    
  
  def make_page_detection(self):
    self.page_detection = detection(self.File,master=self.master, app=self)
    
    self.frame.pack_forget()
    self.page_detection.start_page()
    


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

    self.canvas = Canvas(self.frame, bg='white')
    self.canvas.place(relx = 0.5,rely=0.58,anchor = CENTER, relheight=0.63,relwidth=0.7)

    self.scrollbar = Scrollbar(self.canvas,bg='white')
    self.scrollbar.place(relx = 0.99,rely=0.5,anchor = CENTER, relheight=1)

    self.inDate = ImInter(self.frame,"Vias Icon.png", 0.82,0.06)
    self.inDate.sizeImage(80,80)
    self.inDate.create()

    self.Tittle_Vias= ImInter(self.frame,"Vias.png", 0.35,0.25) 
    self.Tittle_Vias.sizeImage(80,120)
    self.Tittle_Vias.create()

    self.police = ImInter(self.frame,"in.png", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

#    self.Autopista = ImInter(self.frame,"Autopista.png", 0.15,0.37) 
#    self.Autopista.sizeImage(90,240)
#    self.Autopista.create()

#    self.Arterias = ImInter(self.frame,"Arterias.png", 0.15,0.5) 
#    self.Arterias.sizeImage(90,240)
#    self.Arterias.create()
#
#    self.Principales = ImInter(self.frame,"Principales.png", 0.15,0.63) 
#    self.Principales.sizeImage(90,240)
#    self.Principales.create()
 
#    self.Locales = ImInter(self.frame,"Locales.png", 0.15,0.76) 
#    self.Locales.sizeImage(90,240)
#    self.Locales.create()
 
#    self.Textos = ImInter(self.frame,"Textos.png", 0.4,0.56) 
#    self.Textos.sizeImage(400,240)
#    self.Textos.create()
 
#    self.Textos2 = ImInter(self.frame,"Textos2.png", 0.75,0.56) 
#    self.Textos2.sizeImage(400,600)
#    self.Textos2.create()

  

    self.BottVehiculos = BottInter(self.frame,"Vehiculos.png",0.7,0.25, None,self.go_vehiculos)
    self.BottVehiculos.modzise(130,70)
    self.BottVehiculos.create()


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

    self.police = ImInter(self.frame,"in.png", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

    self.inVe = ImInter(self.frame,"Ve_guardados.png", 0.6,0.25)
    self.inVe.sizeImage(80,120)
    self.inVe.create()

    self.inVe2 = ImInter(self.frame,"Vehiculos2.png", 0.5,0.6)
    self.inVe2.sizeImage(425,1200)
    self.inVe2.create()

    self.BottVehiculos = BottInter(self.frame,"ViasImage.png",0.4,0.25, None,self.go_Vias)
    self.BottVehiculos.modzise(130,70)
    self.BottVehiculos.create()

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
  def own_widgets(self):
    self.inDate = ImInter(self.frame,"deteccionimage.png", 0.82,0.06)
    self.inDate.sizeImage(80,120)
    self.inDate.create()

    self.police2 = ImInter(self.frame,"in.png", 0.2,0.1) 
    self.police2.sizeImage(100,100)
    self.police2.create()

    self.BottGuardar = BottInter(self.frame,"GuardarBoton.png",0.5,0.8, None,None)
    self.BottGuardar.modzise(190,60)
    self.BottGuardar.create()

    self.Bottsnapshot2 = BottInter(self.frame,"velocidadInstantanea2.png",0.7,0.7, 'Velocidad Instantánea',None)
    self.Bottsnapshot2.modzise(50,50)
    self.Bottsnapshot2.create()

    self.create_botton_velo(0.3) 
    self.create_botton_velo2(0.7) 

  def create_botton_velo(self,positiony):

    self.positiony=positiony
    self.Bottvelo = BottInter(self.frame,"velocidadInstantanea.png",self.positiony, 0.7,
    'Velocidad instantanea',self.make_page_graficas)
    self.Bottvelo.modzise(50,50)
    self.Bottvelo.create()
    
    self.open_create_text(self.Bottvelo)

  def create_botton_velo2(self,positiony):

    self.positiony=positiony
    self.Bottvelo2 = BottInter(self.frame,"velocidadInstantanea2.png",self.positiony, 0.7,
    'Velocidad promedio',self.make_page_graficas2)
    self.Bottvelo2.modzise(50,50)
    self.Bottvelo2.create()
    
    self.open_create_text(self.Bottvelo2)

  def make_page_graficas(self):
    self.page_graficas = Graficas(master=self.master, app=self)
    self.frame.pack_forget()
    self.page_graficas.start_page()

  def make_page_graficas2(self):
    self.page_graficas2 = Graficas2(master=self.master, app=self)
    self.frame.pack_forget()
    self.page_graficas2.start_page()

  def open_create_text(self,botton):
    
    self.botton=botton
    self.botton.createText()

  def __init__(self,video,master=None,app=None):
    self.video=video
    super().__init__(master,app)
  
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

  def make_agregar_vehiculo(self):
    self.page_agregar_vehiculo = guardarVehiculo(master=self.master, app=self)
    self.frame.pack_forget()
    self.page_agregar_vehiculo.start_page()

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
class guardarVehiculo(info):
  def __init__(self,idusuario=None, idvideo=None,velocidad=None,velocidad_excedida=None, captura=None, master=None, app=None):
    self.captura_carro=captura
    self.idusuario = idusuario
    self.idvideo= idvideo
    self.velocidad=velocidad
    self.velocidad_excedida=velocidad_excedida

    super().__init__(master,app)


  def own_widgets(self):
    #estos son como ejemplo
    self.idusuario = 1
    self.idvideo= 10
    self.velocidad=40.5
    self.velocidad_excedida=True

    self.iminfo= ImInter(self.frame,"Video Speed Icon.png", 0.8,0.06) 
    self.iminfo.sizeImage(70,110)
    self.iminfo.create()

    self.Text="Guardar Vehículo"
    self.Title1 = textInter(self.frame,self.Text,30,0.5,0.23)
    self.Title1.create_Tittle()
    

    self.Text="ID Video "
    self.Title_id_video = textInter(self.frame,self.Text,16,0.15,0.3,'w')
    self.Title_id_video.create_Tittle()
    self.id_video= IntVar(self.frame, value=self.idvideo)
    self.entrada_vehiculo = Entry(self.frame,textvariable=self.id_video,width=10,
     font = ('comics Sans MS',18))
    self.entrada_vehiculo.place(relx = 0.34,rely=0.3,anchor ='w')

    
    self.Text="Captura:"
    self.Title_captura = textInter(self.frame,self.Text,16,0.6,0.3,'w')
    self.Title_captura.create_Tittle()

    self.mostrar_captura= ImInter(self.frame,"captura.png", 0.7,0.45)
    self.mostrar_captura.create()

    self.Text="Tipo de Vehículo:"
    self.Title_tipo_vehiculo = textInter(self.frame,self.Text,16,0.15,0.38,'w')
    self.Title_tipo_vehiculo.create_Tittle()
    self.tipo_vehiculo= StringVar()
    self.entrada_tipo_video = Entry(self.frame,textvariable=self.tipo_vehiculo,width=10, font = ('comics Sans MS',18))
    self.entrada_tipo_video.place(relx = 0.34,rely=0.38,anchor ='w')

    self.Text="PLACA:"
    self.Title_placa = textInter(self.frame,self.Text,16,0.15,0.45,'w')
    self.Title_placa.create_Tittle()
    self.placa= DoubleVar(self.frame,value=self.velocidad)
    self.entrada_placas = Entry(self.frame,textvariable=self.placa,width=10, font = ('comics Sans MS',18))
    self.entrada_placas.place(relx = 0.34,rely=0.45,anchor ='w')

    self.Text="Velocidad (km/h):"
    self.Title_velocidad = textInter(self.frame,self.Text,16,0.15,0.53,'w')
    self.Title_velocidad.create_Tittle()
    if self.velocidad_excedida:
      self.velocidad= StringVar(self.frame,value="Sí")
    else:
      self.velocidad= StringVar(self.frame,value="No")
    self.entrada_velocidad = Entry(self.frame,textvariable=self.velocidad,width=10, font = ('comics Sans MS',18))
    self.entrada_velocidad.place(relx = 0.34,rely=0.53,anchor ='w')


    self.Text="Vía:"
    self.Title_via = textInter(self.frame,self.Text,16,0.15,0.61,'w')
    self.Title_via.create_Tittle()
    self.via= StringVar()

    self.opciones_vias = ttk.Combobox(self.frame, width=10, font = ('comics Sans MS',18),textvariable = self.via)
    self.opciones_vias['value'] = vias
    self.opciones_vias.place(relx = 0.34,rely=0.61,anchor ='w')
    self.opciones_vias.current(0) 

    self.Text="Velocidad Excedida:"
    self.Title_velocidad_excedida = textInter(self.frame,self.Text,16,0.15,0.69,'w')
    self.Title_velocidad_excedida.create_Tittle()
    self.velocidad_excedida= StringVar()
    self.entrada_velocidad_excedida = Entry(self.frame,textvariable=self.velocidad_excedida,width=10, font = ('comics Sans MS',18))
    self.entrada_velocidad_excedida.place(relx = 0.34,rely=0.69,anchor ='w')
    
    self.Text="Multa:"
    self.Title_multa = textInter(self.frame,self.Text,16,0.6,0.61,'w')
    self.Title_multa.create_Tittle()
    self.multa= StringVar()
    self.entrada_multa = Entry(self.frame,textvariable=self.multa,width=10, font = ('comics Sans MS',18))
    self.entrada_multa.place(relx = 0.71,rely=0.61,anchor ='w')


    self.Text="ID Usuario:"
    self.Title_id_usuario = textInter(self.frame,self.Text,16,0.6,0.69,'w')
    self.Title_id_usuario.create_Tittle()
    self.id_usuario= IntVar(self.frame, value=self.idusuario)
    self.entrada_id_usuario = Entry(self.frame,textvariable=self.id_usuario,width=10, font = ('comics Sans MS',18))
    self.entrada_id_usuario.place(relx = 0.71,rely=0.69,anchor ='w')


    self.Button_guardar = BottInter(self.frame,"Boton_guardar.png",0.5,0.8,None, self.make_guardar_vehiculo)
    self.Button_guardar.modzise(250,60)
    self.Button_guardar.create()

    self.canvas = Canvas(self.frame,bg="white",width=3,height=370,relief=FLAT)
    self.canvas.create_line(1.5, 0, 1.5, 370)
    self.canvas.place(relx = 0.5,rely=0.5,anchor = CENTER)
  


  def make_guardar_vehiculo(self):
    if (self.vehiculo.get()!="" and self.placas.get()!="" and self.velocidad.get()!="" and self.via.get()!="" and self.limite_velocidad.get()!=""):
      print(self.vehiculo.get())
      #self.page_agrega = guardarVehiculo(master=self.master, app=self)
      #self.frame.pack_forget()
      #self.page_agregar_vehiculo.start_page()
    else:
      self.mensaje()
    
  
  def mensaje(self):
    MessageBox.showinfo("Información","Por favor, rellene todas las casillas.")
    
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
      self.frame2 = imutils.resize(self.frame2, width=440)
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
        if (History_Videos[x][0]==id and x!= self.variable):
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
    self.canvas.place(relx = 0.5,rely=0.58,anchor = CENTER, relheight=0.63,relwidth=0.7)

    
    self.scrollbar = Scrollbar(self.canvas,bg='white')
    self.scrollbar.place(relx = 0.99,rely=0.5,anchor = CENTER, relheight=1)

    
    self.y = 0
    self.x = 0
    self.contador=0

    for x in range(len(History_Videos)):
      global id

      if (History_Videos[x][0]==id):
       
        
        self.name_video = History_Videos[x][1]
        self.via = History_Videos[x][2]
        self.ciudad = History_Videos[x][3]
        self.direccion = History_Videos[x][4]
        self.fecha = History_Videos[x][5]

        globals()["video" + str(self.contador)] = VidInter(self.frame,self.name_video,self.x,self.y,self.canvas,self.contador,self)
        
        globals()["button_detection" + str(self.contador)]= BottInter(self.canvas,"Video Speed Icon.png",0.5,0.8,'',partial(self.make_page_detection,self.name_video))
        globals()["button_detection" + str(x)].modzise(95,50)
        globals()["button_detection" + str(x)].create()
        self.window= globals()["button_detection" + str(x)].return_panel()

        self.text= self.via+" - "+self.ciudad + " - " + self.fecha
        self.canvas.create_text(self.x+160,self.y+230,font=('Helvetica', 11, 'bold'), text=self.text)
        self.canvas.create_text(self.x+50,self.y+250,font=('Helvetica', 11), text=self.direccion)

        
        self.canvas.create_window(self.x+390,self.y+245, window=self.window, anchor=CENTER)

        
        if (self.x==0):
          self.x=500
        else:
          self.x=0
        self.contador+=1
        if (self.contador % 2 ==0):
          self.y+=300
    
    self.create_video()

    self.canvas.config(yscrollcommand=self.scrollbar.set, scrollregion = self.canvas.bbox("all"))
    
    self.scrollbar.configure(command= self.canvas.yview )

  def make_page_detection(self,name_video):
    self.name_video_detection= name_video
    self.page_detection = detection(self.name_video_detection, master=self.master, app=self)
    self.frame.pack_forget()
    self.page_detection.start_page()
    
  
  def create_video(self):
     for x in range(len(History_Videos)):
      global id
      if (History_Videos[x][0]==id):
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

  History_Videos =  [(1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","10/10/2021"),
                    (1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","11/10/2021"),
                    (1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","12/10/2021"),
                    (1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","13/10/2021"),
                    (1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","14/10/2021"),
                    ]
  vias= ["Autopista/Carretera", "Arterias", "Principales", "Locales y Especiales"]

  idUsuario = usuario
  conexionSlow = bD.ConexionBaseDeDatosSlow()
  conexionSlow.cursorSlow.execute(f"SELECT NOMBRE,APELLIDO FROM USUARIOS WHERE IDUSUARIO={idUsuario}")
  nombreUsuario = conexionSlow.cursorSlow.fetchall()
  nombreUsuario = str(nombreUsuario[0][0]+" "+nombreUsuario[0][1]).upper()
  root.title(f"SLOW - USUARIO: {nombreUsuario}")
  tomarInfoUsuario()
  app = App(root)
  root.mainloop()