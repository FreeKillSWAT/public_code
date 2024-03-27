import tkinter as tk

class SearchBox:
    def __init__(self, master, search_callback):
        self.master = master
        self.search_callback = search_callback

        # Crear el Entry para ingresar el nombre de usuario a buscar
        self.search_entry = tk.Entry(self.master)
        self.search_entry.pack(side="left", fill="x", padx=10, pady=5)

        # Crear el botón de búsqueda de usuario
        self.search_button = tk.Button(self.master, text="Buscar Usuario", command=self.search)
        self.search_button.pack(side="left", padx=10, pady=5)

    def search(self):
        username = self.search_entry.get()
        self.search_callback(username)