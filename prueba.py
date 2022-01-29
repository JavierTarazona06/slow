from tkinter import *

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

ej2()