from tkinter import *
from Functions import realizar
def on_cerrar_ventana():
    root.destroy()

def centrar_ventana(ventana, ancho, alto):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

def centrar_ventana_emergente(ventana_padre, ventana_emergente, ancho, alto):
    ventana_padre.update_idletasks()
    ancho_padre = ventana_padre.winfo_width()
    alto_padre = ventana_padre.winfo_height()
    x_padre = ventana_padre.winfo_x()
    y_padre = ventana_padre.winfo_y()
    
    x = x_padre + (ancho_padre // 2) - (ancho // 2)
    y = y_padre + (alto_padre // 2) - (alto // 2)
    
    ventana_emergente.geometry(f'{ancho}x{alto}+{x}+{y}')
def cerrar(ventana2,ventana3):
    ventana2.withdraw()
    ventana3.withdraw()
def finalizar(ventana2,decision):
    ventana3 = Toplevel(root)
    ventana3.title("resultado")
    ancho_ventana_emergente = 200
    alto_ventana_emergente = 100
    centrar_ventana_emergente(root, ventana3, ancho_ventana_emergente, alto_ventana_emergente)
    
    frame4=Frame(ventana3)
    frame4.pack(fill="both", expand=True)
    frame4.config(bd=21)
    resultado=Label(frame4,text=f"La cadena fue: {decision}", font=("Arial", 9, "bold italic"))
    resultado.pack()

    boton5 = Button(frame4, text="Finalizar", width=15, height=1, command=lambda:cerrar(ventana2,ventana3))
    boton5.pack()#Falta hacer que cuando se de al boton se abra otra ventana igual pero con los controles anteriores
    

def Procedimiento(infbox2,cadena,ventana2,funcion,grafo):
    continuar=True
    if len(cadena)==1:
        print(cadena[0][2])
        continuar=False
    if continuar:
        imagen1 = PhotoImage(file=f"img/q{cadena[0][3].estadoActual}.png")
        imagen_redimensionada4 = imagen1.subsample(5, 5)
        grafo.config(image=imagen_redimensionada4)
        grafo.image = imagen_redimensionada4  # Mantener referencia
        funcion.config(text=f"δ(q{cadena[0][3].estadoActual},{cadena[0][3].entrada})=(q{cadena[0][3].estado},{cadena[0][3].remplazo},{cadena[0][3].movimiento})")
        x=[]
        for i in range(len(cadena[0][1])):
            if i==cadena[0][0]:
                x.append("q")
                x.append(cadena[0][1][i])
            else:
                x.append(cadena[0][1][i])
        
        final=True
        for i in x:
            if i =="q":
                final=False
       
        if final: x.append("q")
        z=""
        for i in x:
            z+=str(i)
        z="BBB"+z+"BBB"
        infbox2.delete("1.0", END)
        infbox2.insert("1.0", z)
        cadena.pop(0)
    else:
        if cadena[0][2]=="Aceptado":
            decision="Aceptada"
            finalizar(ventana2,decision)
            imagen1 = PhotoImage(file=f"img/q7.png")
            imagen_redimensionada4 = imagen1.subsample(5, 5)
            grafo.config(image=imagen_redimensionada4)
            grafo.image = imagen_redimensionada4
        else:
            decision="Rechazada"
            finalizar(ventana2,decision)

def calcular_cadena(ventana,infbox1):
    ventana.withdraw()
    datos = infbox1.get("1.0", END).strip()
    cadena=realizar(datos)
    ventana2 = Toplevel(root)
    ventana2.title("Calcular Cadena")
    ancho_ventana_emergente = 700
    alto_ventana_emergente = 700
    centrar_ventana_emergente(root, ventana2, ancho_ventana_emergente, alto_ventana_emergente)
    
    ventana2.config(bg="white")
    frame3=Frame(ventana2)
    frame3.pack(fill="both", expand=True)
    frame3.config(bg="#013252")
    frame3.config(bd=21)

    grafo = Label(frame3)
    grafo.pack()

    infbox2 = Text(frame3, width=50, height=2,font=("Arial", 17, "bold italic"))  
    infbox2.pack( expand=True, padx=10, pady=10)
    infbox2.config(relief="solid")
  
    funcion=Label(frame3)
    funcion.pack()

    Procedimiento(infbox2,cadena,ventana2,funcion,grafo)

    boton4 = Button(frame3, text="Siguiente paso", width=30, height=2, command=lambda:Procedimiento(infbox2,cadena,ventana2,funcion,grafo))
    boton4.pack()
    
    

def abrir_ventana_emergente():
    ventana = Toplevel(root)
    ventana.title("Calcular Cadena")
    ancho_ventana_emergente = 500
    alto_ventana_emergente = 200
    centrar_ventana_emergente(root, ventana, ancho_ventana_emergente, alto_ventana_emergente)

    ventana.config(bg="white")
    frame2=Frame(ventana)
    frame2.pack(fill="both", expand=True)
    frame2.config(bg="#013252")
    frame2.config(bd=21)

    infbox1 = Text(frame2, width=50, height=2,font=("Arial", 17, "bold italic"))  # Ajuste estos valores según sea necesario
    infbox1.pack( expand=True, padx=10, pady=10)
    infbox1.config(relief="solid")

    boton3 = Button(frame2, text="Calcular", width=30, height=2, command=lambda:calcular_cadena(ventana,infbox1))
    boton3.pack()#Falta hacer que cuando se de al boton se abra otra ventana igual pero con los controles anteriores
    
    

root = Tk()
root.title("Registro de horas extracurriculares")
root.config(bg="black")
ancho_ventana = 400
alto_ventana = 300

centrar_ventana(root, ancho_ventana, alto_ventana)

frame = Frame(root)
frame.pack(fill="both", expand=True)
frame.config(bg="#013252")
frame.config(bd=21)

label = Label(frame, text="Máquina de Turing que calcula \n palíndromos pares de 0 y 1", font=("Arial", 17, "bold italic"), fg="white")
label.config(bg="#013252")
label.pack()

boton = Button(frame, text="CALCULAR CADENA", width=30, height=2,command=abrir_ventana_emergente)
boton.pack()
boton.place(x=70, y=120)

boton2 = Button(frame, text="Salir", width=30, height=2, command=on_cerrar_ventana)
boton2.pack()
boton2.place(x=70, y=170)


root.protocol("WM_DELETE_WINDOW", on_cerrar_ventana)
root.mainloop()
