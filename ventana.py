import tkinter as tk

def centrar_ventana(ventana, ancho, alto):
    # Obtiene el ancho y alto de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    
    # Calcula la posición x e y para centrar la ventana
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    
    # Establece la geometría de la ventana
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

def centrar_ventana_emergente(ventana_padre, ventana_emergente, ancho, alto):
    # Obtiene la posición y el tamaño de la ventana principal
    ventana_padre.update_idletasks()
    ancho_padre = ventana_padre.winfo_width()
    alto_padre = ventana_padre.winfo_height()
    x_padre = ventana_padre.winfo_x()
    y_padre = ventana_padre.winfo_y()
    
    # Calcula la posición x e y para centrar la ventana emergente en la ventana principal
    x = x_padre + (ancho_padre // 2) - (ancho // 2)
    y = y_padre + (alto_padre // 2) - (alto // 2)
    
    # Establece la geometría de la ventana emergente
    ventana_emergente.geometry(f'{ancho}x{alto}+{x}+{y}')

def crear_ventana_emergente():
    # Crea una ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Ventana Emergente")
    
    # Define el tamaño de la ventana emergente
    ancho_ventana_emergente = 300
    alto_ventana_emergente = 200
    
    # Llama a la función para centrar la ventana emergente
    centrar_ventana_emergente(ventana, ventana_emergente, ancho_ventana_emergente, alto_ventana_emergente)

# Crea una instancia de Tkinter
ventana = tk.Tk()
ventana.title("Ventana Principal")

# Define el tamaño de la ventana principal
ancho_ventana = 400
alto_ventana = 300

# Llama a la función para centrar la ventana principal
centrar_ventana(ventana, ancho_ventana, alto_ventana)

# Crea un botón para abrir la ventana emergente
boton = tk.Button(ventana, text="Abrir Ventana Emergente", command=crear_ventana_emergente)
boton.pack(pady=20)

# Inicia el bucle principal de Tkinter
ventana.mainloop()
