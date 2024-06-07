from tkinter import *

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

    boton3 = Button(frame2, text="Calcular", width=30, height=2, command="")
    boton3.pack()#Falta hacer que cuando se de al boton se abra otra ventana igual pero con los controles anteriores
    
    infbox1.config(state="disabled")#esto es para desactivar el text
    

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
