from distutils import command
from tkinter import *
from tkinter import filedialog
from turtle import width
from PIL import ImageTk, Image
import cv2
import imutils
import ConexionBaseDeDatosSlow as bD


# interfaz principal
class App:
  def __init__(self, root=None):
    self.root = root
    self.frame =Frame(self.root,bg='white',width=1366,height=768)
    self.PosBottonY=0.65
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

    self.imWelcome= ImInter(self.frame,"GOBIERNO DE COLOMBIA TITL.png", 0.5,0.3)
    self.imWelcome.create()
    self.create_botton_info(0.2)
    self.create_botton_datos(0.35)
    self.create_botton_video(0.5) 
    self.create_botton_vias(0.65) 
    self.create_botton_history(0.8)

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
    'Vehículo/ Vías',self.make_page_vias)
    self.BottVias.modzise(170)
    self.BottVias.create()

    self.open_create_text(self.BottVias)

  def create_botton_history(self,positiony):

    self.positiony=positiony
    self.BottHistory = BottInter(self.frame,"History Icon.png",self.positiony,self.PosBottonY,
    'Hisrórico',self.make_page_history)
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
    self.page_info = info(master=self.root, app=self)
    self.frame.pack_forget()
    self.page_info.start_page()
  # ir a interfaz de datos
  def make_page_date(self):
    self.page_date = Date(master=self.root, app=self)
    self.frame.pack_forget()
    self.page_date.start_page()
  
  def make_page_video(self):
    self.page_video = video(master=self.root, app=self)
    self.frame.pack_forget()
    self.page_video.start_page()
  
  def make_page_vias(self):
    self.page_vias = Vias(master=self.root, app=self)
    self.frame.pack_forget()
    self.page_vias.start_page()
  
  def make_page_history(self):
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
    self.frame = Frame(self.master,bg='white',width=1366,height=768)
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

    self.BottReturn = BottInter(self.frame,"Return Arrow Icon.png",0.4,0.94, None,self.go_back)
    self.BottReturn.modzise(70,70)
    self.BottReturn.create()
    
    self.BottMenu = BottInter(self.frame,"Menu icon.png",0.5,0.94,None,None,self)
    
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
    self.paragraph1 = textInter(self.frame,self.Text,12,0.5,0.47)
    self.paragraph1.create_paragraph()

    self.Text="Los roles disponibles dentro de Slow son el de polícia o jefe de polícia. La diferencia está en que el jefe de polícia podrá editar vías y vehículos mientras que\n el subordinado solo las podrá ver. Asi mismo, el jefe podrá ver los vídeos subidos por sus polícias asigandos."
    self.paragraph2 = textInter(self.frame,self.Text,12,0.5,0.59)
    self.paragraph2.create_paragraph()
    
    self.Text="El usuario puede actualizar sus datos en la aplicación, registrar (subir) videos para utilizar la función de detección de la velocidad de los vehículos, ver tipos\n de vehículos y vías junto con las restricciones (el jefe las puede editar) y por último el histórico de los videos subidos (el jefe puede ver los del equipo)."
    self.paragraph3 = textInter(self.frame,self.Text,12,0.5,0.71)
    self.paragraph3.create_paragraph()

    self.Text="Para detectar la velocidad de vehículos en movimiento se requiere subir a la aplicación un video grabado en ángulo picado en cámara alta que enfoque\n la carretera o calle donde se desea detectar de velocidad."
    self.paragraph4 = textInter(self.frame,self.Text,12,0.5,0.83)
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

    self.Datos = ImInter(self.frame,"Datos.png", 0.5,0.55) 
    self.Datos.sizeImage(425,1200)
    self.Datos.create()

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
    self.inDate = ImInter(self.frame,"Vias Icon.png", 0.82,0.06)
    self.inDate.sizeImage(80,80)
    self.inDate.create()

    self.Tittle_Vias= ImInter(self.frame,"Vias.png", 0.35,0.25) 
    self.Tittle_Vias.sizeImage(80,120)
    self.Tittle_Vias.create()

    self.police = ImInter(self.frame,"in.png", 0.2,0.1) 
    self.police.sizeImage(100,100)
    self.police.create()

    self.Autopista = ImInter(self.frame,"Autopista.png", 0.15,0.37) 
    self.Autopista.sizeImage(90,240)
    self.Autopista.create()

    self.Arterias = ImInter(self.frame,"Arterias.png", 0.15,0.5) 
    self.Arterias.sizeImage(90,240)
    self.Arterias.create()

    self.Principales = ImInter(self.frame,"Principales.png", 0.15,0.63) 
    self.Principales.sizeImage(90,240)
    self.Principales.create()

    self.Locales = ImInter(self.frame,"Locales.png", 0.15,0.76) 
    self.Locales.sizeImage(90,240)
    self.Locales.create()

    self.Textos = ImInter(self.frame,"Textos.png", 0.4,0.56) 
    self.Textos.sizeImage(400,240)
    self.Textos.create()

    self.Textos2 = ImInter(self.frame,"Textos2.png", 0.75,0.56) 
    self.Textos2.sizeImage(400,600)
    self.Textos2.create()

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
    'Hisrórico',None)
    self.Bottvelo.modzise(50,50)
    self.Bottvelo.create()
    
    self.open_create_text(self.Bottvelo)

  def create_botton_velo2(self,positiony):

    self.positiony=positiony
    self.Bottvelo2 = BottInter(self.frame,"velocidadInstantanea2.png",self.positiony, 0.7,
    'Hisrórico',None)
    self.Bottvelo2.modzise(50,50)
    self.Bottvelo2.create()
    
    self.open_create_text(self.Bottvelo2)

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

      self.Menu = menu(self.name,root=self.frame, app=self)
      
    
      self.Menu.start_page()
      ac=True




class graficas:
    pass


class tablagraficas:
  pass
# grevy
class guardarVehiculo(info):
  pass


#Crea imagenes 
class ImInter:

  def __init__(self, frame,objeto,relx,rely,bg=True):
    self.frame = frame
    self.objeto = objeto
    self.relx = relx
    self.rely = rely
    self.bg=bg
    self.open = Image.open(self.objeto)
    
  #muestra la imagen creada
  def show(self):

    self.panel.place(relx = self.relx,rely=self.rely,anchor = CENTER)
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
  sizex=130
  sizey=130
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
      self.rely += 0.12
    else:
      self.rely=RELY

    self.panel= Label(self.frame, text = self.texto,bg= 'white',font =('Helvetica 15 underline italic'))

    
    self.show()

class textInter(ImInter):

  def __init__(self, frame,texto,size,relx,rely):
    self.frame = frame
    self.texto = texto
    self.relx = relx
    self.rely = rely
    self.size=size
  def create_Tittle(self):
    self.panel=Label(self.frame, text = self.texto,bg= 'white',font=('Helvetica', self.size, 'bold'))
    self.show()
  def create_paragraph(self):
    self.panel=Label(self.frame, text = self.texto,bg= 'white',font=('Helvetica', self.size))
    self.show()


class VidInter(ImInter):
  def __init__(self, frame,objeto,x,y,canvas,variable):

    self.frame = frame
    self.objeto = objeto
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
        globals()["video" + str(self.contador)] = VidInter(self.frame,self.name_video,self.x,self.y,self.canvas,self.contador)
        
        self.text= self.via+" - "+self.ciudad + " - " + self.fecha
        self.canvas.create_text(self.x+160,self.y+230,font=('Helvetica', 11, 'bold'), text=self.text)
        
        self.canvas.create_text(self.x+50,self.y+250,font=('Helvetica', 11), text=self.direccion)
        
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
    self.canvas.bind('<Enter>', self._bind_to_mousewheel)
    self.canvas.bind('<Leave>', self._unbind_from_mousewheel)

  
  def _on_mousewheel(self,event):
    self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

  def _bind_to_mousewheel(self,event):
    self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)      

  def _unbind_from_mousewheel(self,event):
    self.canvas.unbind_all("<MouseWheel>")
  
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
    if (ac== False):

      self.Menu = menu(self.name,root=self.frame, app=self, additional=self.canvas)
    
      self.Menu.start_page()
      ac=True

class Lista(object):
  pass

#Datos

def tomarInfoUsuario():
  global idUsuario
  global infoUsuario
  conexionSlow = bD.ConexionBaseDeDatosSlow()
  conexionSlow.cursorSlow.execute(f"SELECT * FROM USUARIOS WHERE IDUSUARIO={idUsuario}")
  listaInfoUsuario = conexionSlow.cursorSlow.fetchall()
#Crea Ventana

def elUsuario(usuario):
  global idUsuario
  global infoUsuario
  idUsuario = usuario
  root.title(f"SLOW - {str(idUsuario)}")
  infoUsuario = tomarInfoUsuario()
  app = App(root)
  root.mainloop()

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
'''
if __name__ == '__main__':
  root = Tk()
  ac=False  
  id = 1
  play=False
  root.title("Slow")
  root.geometry('1366x768')
  root.configure(bg='white')

  History_Videos =  [(1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","10/10/2021"),
                    (1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","11/10/2021"),
                    (1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","12/10/2021"),
                    (1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","13/10/2021"),
                    (1,"/home/runner/POO/video2.mp4","CARRETERA","Bogotá D.C","km 7 - Tunja","14/10/2021"),
                    ]
  
  
  app = App(root)
  root.mainloop()
'''