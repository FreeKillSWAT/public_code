import tkinter as tk


ventana = tk.Tk()
ventana.title("Mi aplicación")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Bienvenido a mi aplicación")
etiqueta.pack()

boton = tk.Button(ventana, text="Haz clic aquí")
boton.pack(side="left", padx=10, pady=10)

campo_texto = tk.Entry(ventana)
campo_texto.pack(side="left", padx=10, pady=10)
"""

root = tk.Tk()

def say_hello():
    print("Hello, World!")

button = tk.Button(root, text="Click me!", command=say_hello)
button.pack()

root.mainloop()
"""