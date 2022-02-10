from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
import tkinter.filedialog as fd

def ej1():
    root = Tk()
    root.geometry("600x600+700+300")


    #Ejemplo usando un Entry y señales-evento
    def default(event):
        textoActual = caja.get()
        if textoActual == "Introducir el número 200 o el número 400":
            caja.delete(0, END)
            caja.config(fg = 'black')
        elif textoActual == "":
            caja.insert(0,"Introducir el número 200 o el número 400")
            caja.config(fg = 'grey')

    caja = Entry(root)
    caja.place(width=225, x=250,y=30)
    caja.config(fg = 'grey')
    caja.insert(0, 'Introducir el número 200 o el número 400')
    caja.bind("<FocusIn>", default)
    caja.bind("<FocusOut>", default)


    #Ejemplo usando un OptionMenu
    variable = StringVar(root)
    variable.set("200")
    menu = OptionMenu(root, variable, "200", "400")
    menu.place(x=380,y=75)
    etiqueta = Label(root, text="Seleccione un número:")
    etiqueta.place(x=250,y=80)


    root.mainloop()

def ej2():

    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )

    mylist = Listbox(root, yscrollcommand = scrollbar.set )
    for line in range(100):
        mylist.insert(END, "This is line number " + str(line))

    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )

    mainloop()

def ej3():
    #Import the required Libraries


    #Create an instance of tkinter frame
    win = Tk()

    #Set the geometry of tkinter frame
    win.geometry("750x270")

    #Create a canvas
    canvas= Canvas(win, width= 600, height= 400)
    canvas.pack()

    #Load an image in the script
    img= (Image.open("Boton.png"))

    #Resize the Image using resize method
    resized_image= img.resize((150,150), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    canvas.create_image(100,10, anchor=NW, image=new_image)

    win.mainloop()

def ej4():
    from PIL import ImageTk, Image


    root = tk.Tk()

    pic = fd.askopenfilename()

    img = Image.open(pic)

    o_size = img.size   #Tamaño original de la imagen
    f_size = (400, 400) #Tamaño del canvas donde se mostrará la imagen


    factor = min(float(f_size[1])/o_size[1], float(f_size[0])/o_size[0])
    width = int(o_size[0] * factor)
    height = int(o_size[1] * factor)

    rImg= img.resize((width, height), Image.ANTIALIAS)
    rImg = ImageTk.PhotoImage(rImg)
    print(rImg)
    canvas = tk.Canvas(root, width=f_size[0], height= f_size[1])
    canvas.create_image(f_size[0]/2, f_size[1]/2, anchor=tk.CENTER, image=rImg, tags="img")
    canvas.pack(fill=None, expand=False)

    root.mainloop()

def ej5():
    ventanaGrafica = Tk()
    ventanaGrafica.title("GraficaVideo-ID:5")
    ventanaGrafica.iconbitmap("RecursosGraficos\\Logo_Slow_Icon_Map.ico")
    ventanaGrafica.config(bg="white")
    ventanaGrafica.resizable(False,False)

    base = Frame(ventanaGrafica, bg="white").pack()

    imgGrafica = PhotoImage(file="Graficas\\GraficaVideo-1.png")
    labelImgGrafica = Label(base, image=imgGrafica, bg="white")
    labelImgGrafica.pack()

    ventanaGrafica.update()