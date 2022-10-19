#Gilmar Adriel Gonzalez Romero SMIS061221
#Sofía Gissell Hernandez Ascencio SMIS015421
from tkinter import *
from tokenize import Double
from PIL import Image, ImageFilter, ImageTk

#Creamos la ventana
vent1 = Tk()
vent1.title("Pupuseria Niña MARI")
vent1.geometry("600x600")
vent1.config(bg= "pink")
#se configuran las imagenes 
queso= Image.open(r"C:\Users\adrie\Documents\Adriel UGB\CICLO III\PROGRAMACION III\IMAGENES\Q.jpg")
queso=queso.filter(ImageFilter.SHARPEN)
render=ImageTk.PhotoImage(queso)
reducida = queso.resize((100,100), Image.Resampling.LANCZOS)
render= ImageTk.PhotoImage(reducida)

revuelta= Image.open(r"C:\Users\adrie\Documents\Adriel UGB\CICLO III\PROGRAMACION III\IMAGENES\descarga.jpg")
revuelta=revuelta.filter(ImageFilter.SHARPEN)
render1=ImageTk.PhotoImage(revuelta)
reducida = revuelta.resize((100,100), Image.Resampling.LANCZOS)
render1= ImageTk.PhotoImage(reducida)

fq= Image.open(r"C:\Users\adrie\Documents\Adriel UGB\CICLO III\PROGRAMACION III\IMAGENES\FQ.jpg")
fq=fq.filter(ImageFilter.SHARPEN)
render2=ImageTk.PhotoImage(fq)
reducida1 = fq.resize((100,100), Image.Resampling.LANCZOS)
render2= ImageTk.PhotoImage(reducida1)

fq= Image.open(r"C:\Users\adrie\Documents\Adriel UGB\CICLO III\PROGRAMACION III\IMAGENES\FQ.jpg")
fq=fq.filter(ImageFilter.SHARPEN)
render2=ImageTk.PhotoImage(fq)
reducida1 = fq.resize((100,100), Image.Resampling.LANCZOS)
render2= ImageTk.PhotoImage(reducida1)

soda= Image.open(r"C:\Users\adrie\Documents\Adriel UGB\CICLO III\PROGRAMACION III\IMAGENES\Gaseosas.png")
soda=soda.filter(ImageFilter.SHARPEN)
render3=ImageTk.PhotoImage(soda)
reducida1 = fq.resize((100,100), Image.Resampling.LANCZOS)
render3= ImageTk.PhotoImage(reducida1)

soda= Image.open(r"C:\Users\adrie\Documents\Adriel UGB\CICLO III\PROGRAMACION III\IMAGENES\Gaseosas.png")
soda=soda.filter(ImageFilter.SHARPEN)
render3=ImageTk.PhotoImage(soda)
reducida2 = soda.resize((100,100), Image.Resampling.LANCZOS)
render3= ImageTk.PhotoImage(reducida2)

choco= Image.open(r"C:\Users\adrie\Documents\Adriel UGB\CICLO III\PROGRAMACION III\IMAGENES\chocolate.jpg")
choco=choco.filter(ImageFilter.SHARPEN)
render4=ImageTk.PhotoImage(choco)
reducida3 = choco.resize((100,100), Image.Resampling.LANCZOS)
render4= ImageTk.PhotoImage(reducida3)

fres= Image.open(r"C:\Users\adrie\Documents\Adriel UGB\CICLO III\PROGRAMACION III\IMAGENES\frescos.jpg")
fres=fres.filter(ImageFilter.SHARPEN)
render5=ImageTk.PhotoImage(fres)
reducida4 = fres.resize((100,100), Image.Resampling.LANCZOS)
render5= ImageTk.PhotoImage(reducida4)

#Funciones para los radiobuttons
opcion=IntVar()
bebida=IntVar()
domicilio=IntVar()

def pupusas():
    global especialidad
    global pup
    o=opcion.get()

    if o==1:
        pup=0.7
        especialidad = "Queso"
    elif o==2:
        pup=0.65
        especialidad = "F/Q"
    elif o==3:
        pup=0.6
        especialidad = "Revuelta"
    else :
        pup=0
        especialidad = ""

def bebidas():
    global tipo
    global bebid
    b=bebida.get()
    if b==4:
        bebid=0.75
        tipo="gaseosa"
    elif b==5:
        bebid=0.5
        tipo="chocolate"
    elif b==6:
        bebid=0.60
        tipo="fresco"
    else :
        bebid=0

def domic():
    global delivery
    d=domicilio.get()
    if d == 1:
        delivery=1.5
    elif d==2:
        delivery=0
 


def total():
    totpup=float(cantidad.get())*pup

    total=totpup+bebid+delivery

    print("Producto     Cantidad      Precio" )
    print(especialidad,"          ",cantidad.get(),"          ","$",totpup)
    print(tipo,"      ","-","      ","$",bebid)
    print("domicilio","      ","-","      ","$",delivery)
    print("total                   ","$",total)





#Se agregan los radio buttons junto con sus posiciones
radio1=Radiobutton(vent1, text="QUESO" , value=1 ,command=pupusas, variable=opcion)
radio2=Radiobutton(vent1, text="F/Q" , value=2, command=pupusas, variable=opcion)
radio3=Radiobutton(vent1, text="REVUELTAS" , value=3,command=pupusas , variable=opcion)
radio4=Radiobutton(vent1, text="GASEOSAS" , value=4 ,command=bebidas, variable=bebida)
radio5=Radiobutton(vent1, text="CHOCOLATE" , value=5 ,command=bebidas, variable=bebida)
radio6=Radiobutton(vent1, text="REFRESCOS" , value=6,command=bebidas , variable=bebida)
radio7=Radiobutton(vent1, text="SI" , value=1 ,command=domic, variable=domicilio)
radio8=Radiobutton(vent1, text="NO" , value=2,command=domic ,variable=domicilio)

radio1.place(x=50, y=150)
radio2.place(x=250, y=150)
radio3.place(x=450, y=150)
radio4.place(x=50, y=330)
radio5.place(x=250, y=330)
radio6.place(x=450, y=330)
radio7.place(x=100, y=500)
radio8.place(x=150, y=500)

#Se agrega el boton de imprimir factura y el entry para saber cuantas pupusas se ordenaron 
cantidad=StringVar()
btn=Button(vent1, text="Imprimir Factura", command=total)
cant=Entry(vent1, font=10, bg="white", textvariable=cantidad)
btn.place(x=450, y=500)
lb8=Label(vent1,text="Cantidad", background="lightblue")
lb8.place(x=400, y=190)
cant.place(x=460, y=185, width=100)

#Se crean los labels donde iran las imagenes 
lab=Label(vent1,text="Especialidades de pupusas", background="lightblue")
lab.place(x=240, y=10)
lab1=Label(vent1, image=render)
lab1.place(x=50, y=40)
lab2=Label(vent1, image=render2)
lab2.place(x=250, y=40)
lab3=Label(vent1, image=render1)
lab3.place(x=450, y=40)
lab4=Label(vent1,text="Bebidas", background="lightblue")
lab4.place(x=280, y=190)
lab5=Label(vent1, image=render3)
lab5.place(x=50, y=220)
lab6=Label(vent1, image=render4)
lab6.place(x=250, y=220)
lab7=Label(vent1, image=render5)
lab7.place(x=450, y=220)
lab8=Label(vent1,text="Domicilio", background="lightblue")
lab8.place(x=25, y=500)



vent1.mainloop()