from tkinter import *
from tkinter import ttk
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
    
def llenartabla2(tabla3):
    transiciones=[
        ["q0","(q1,B,R)","(q4,B,R)","(q7,B,R)"],
        ["q1","(q1,0,R)","(q1,1,R)","(q2,B,L)"],
        ["q2","(q3,B,L)"],
        ["q3","(q3,0,L)","(q3,1,L)","(q0,B,R)"],
        ["q4","(q4,0,R)","(q4,1,R)","(q5,B,L)"],
        ["q5","","(q6,B,L)"],
        ["q6","(q6,0,L)","(q6,1,L)","(q0,B,R)"],
        ["q7"]
    ]
    for datos in transiciones:
        tabla3.insert("", "end", values=datos)

def Procedimiento(infbox2,cadena,ventana2,funcion,grafo,boton4):
    continuar=True
    if len(cadena)==1:
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
                x.append(f"➞")
                x.append(cadena[0][1][i])
            else:
                x.append(cadena[0][1][i])
        
        final=True
        for i in x:
            if i ==f"➞":
                final=False
       
        if final: x.append(f"➞")
        z=""
        for i in x:
            z+=str(i)
        z="BBB"+z+"BBB"
        infbox2.delete("1.0", END)
        infbox2.insert("1.0", z)
        cadena.pop(0)
    else:
        if cadena[0][2]=="Aceptado":
            if cadena[0][1]:
                decision="Aceptada"
                finalizar(ventana2,decision)
                imagen1 = PhotoImage(file=f"img/q7.png")
                imagen_redimensionada4 = imagen1.subsample(5, 5)
                grafo.config(image=imagen_redimensionada4)
                funcion.config(text=f"                                                                                                                                           ")
                grafo.image = imagen_redimensionada4
                boton4.config(state="disabled")
            
                x=[]
                for i in range(len(cadena[0][1])):
                    if i==cadena[0][0]:
                        x.append(f"➞")
                        x.append(cadena[0][1][i])
                    else:
                        x.append(cadena[0][1][i])
                
                final=True
                for i in x:
                    if i ==f"➞":
                        final=False
            
                if final: x.append(f"➞")
                z=""
                for i in x:
                    z+=str(i)
                z="BBB"+z+"BBB"
                infbox2.delete("1.0", END)
                infbox2.insert("1.0", z)
                cadena.pop(0)
            else:
                boton4.config(state="disabled")
                decision="Rechazada"
                finalizar(ventana2,decision)
        else:
            boton4.config(state="disabled")
            if len(cadena[0][1]) > 1:
                if cadena[0][1][1]==0:
                    imagen1 = PhotoImage(file=f"img/q5.png")
                else:
                    imagen1 = PhotoImage(file=f"img/q2.png")
                imagen_redimensionada4 = imagen1.subsample(5, 5)
                grafo.config(image=imagen_redimensionada4)
                grafo.image = imagen_redimensionada4  
            x=[]
            for i in range(len(cadena[0][1])):
                if i==cadena[0][0]:
                    x.append("➞")
                    x.append(cadena[0][1][i])
                else:
                    x.append(cadena[0][1][i])
            
            final=True
            for i in x:
                if i =="➞":
                    final=False
        
            if final: x.append("➞")
            z=""
            for i in x:
                z+=str(i)
            z="BBB"+z+"BBB"
            infbox2.delete("1.0", END)
            infbox2.insert("1.0", z)
            cadena.pop(0)
            decision="Rechazada"
            ventana2.after(300,finalizar(ventana2,decision))
            

def calcular_cadena(ventana,infbox1):
    ventana.withdraw()
    datos = infbox1.get("1.0", END).strip()
    cadena=realizar(datos)
    ventana2 = Toplevel(root)
    ventana2.title("Calcular Cadena")
    ancho_ventana_emergente = 1100
    alto_ventana_emergente = 700
    centrar_ventana_emergente(root, ventana2, ancho_ventana_emergente, alto_ventana_emergente)
    
    ventana2.config(bg="white")
    frame3=Frame(ventana2)
    frame3.pack(fill="both", expand=True)
    frame3.config(bg="#013252")
    frame3.config(bd=21)

    grafo = Label(frame3)
    grafo.pack()
    grafo.place(x=5,y=5)

    infbox2 = Text(frame3, width=50, height=2,font=("Arial", 17, "bold italic"))  
    infbox2.pack( expand=True, padx=10, pady=10)
    infbox2.config(relief="solid")
    infbox2.place(x=30,y=530)
  
    funcion=Label(frame3,bg="#013252",fg="white",font=("Arial", 12, "bold italic"))
    funcion.pack()
    funcion.place(x=290,y=590)

    funciones=Label(frame3,text="FUNCIONES DE TRANSICIÓN",bg="#013252",fg="white",font=("Arial", 12, "bold italic"))
    funciones.pack()
    funciones.place(x=755,y=120)
    tabla3 = ttk.Treeview(frame3, columns=("Estados","0","1","B"), show="headings")
    tabla3.heading("Estados", text="Estados")
    tabla3.column("Estados", width=50)  
    tabla3.heading("0", text="0")
    tabla3.column("0", width=90) 
    tabla3.heading("1", text="1")
    tabla3.column("1", width=90)  
    tabla3.heading("B", text="B")
    tabla3.column("B", width=90)  
    tabla3.grid(row=0, column=0, padx=10, pady=10)  
    tabla3.tag_configure("custom_font", font=("Helvetica", 17))
    tabla3.place(x=720,y=150)

    llenartabla2(tabla3)

    boton4 = Button(frame3, text="Siguiente paso", width=30, height=2, command=lambda:Procedimiento(infbox2,cadena,ventana2,funcion,grafo,boton4))
    boton4.pack()
    boton4.place(x=250,y=620)
    Procedimiento(infbox2,cadena,ventana2,funcion,grafo,boton4)
    
    

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
