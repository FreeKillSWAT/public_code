from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ldap_search import LDAPSearch

class ListView:
    def __init__(self, master, search_box):
        self.master = master
        self.search_box = search_box
        
        # Inicializar el objeto LDAPSearch
        self.ldap_search = LDAPSearch()

        # Crear el Treeview
        self.tree = ttk.Treeview(self.master, columns=("Usuario", "Nombre", "Estado"))
        self.tree.heading("#0", text="No.")
        self.tree.heading("#1", text="Usuario")
        self.tree.heading("#2", text="Nombre")
        self.tree.heading("#3", text="Estado")

        # Empaquetar el Treeview
        self.tree.pack(side="top", fill="both", expand=True)

        # Empaquetar las barras de desplazamiento dentro del Treeview
        self.scrollbar_y = ttk.Scrollbar(self.master, orient="vertical", command=self.tree.yview)
        self.scrollbar_x = ttk.Scrollbar(self.master, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.tree.pack(side="left", fill="both", expand=True)
        self.scrollbar_y.pack(side="right", fill="y")
        self.scrollbar_x.pack(side="bottom", fill="x")

    def populate_user_list(self):
        self.tree.delete(*self.tree.get_children())  # Limpiar la tabla antes de volver a poblarla
        users = self.ldap_search.search_users_in_group()
        if users:
            for i, user in enumerate(users, start=1):
                username = user['sAMAccountName'].value
                nombre = user['cn'].value
                enabled = user['userAccountControl'].value
                if int(enabled) == 66048 or int(enabled) == 512:  # Solo agregar usuarios habilitados al Treeview
                    self.tree.insert("", "end", text=str(i), values=(username, nombre, "Habilitado"))
                else:
                    self.tree.insert("", "end", text=str(i), values=(username, nombre, "Deshabilitado"))

    def filter_users(self, selected_option):
        users = self.ldap_search.search_users_in_group()
        self.tree.delete(*self.tree.get_children())  # Limpiar la tabla antes de volver a poblarla
        if users:
            for i, user in enumerate(users, start=1):
                username = user['sAMAccountName'].value
                nombre = user['cn'].value
                enabled = user['userAccountControl'].value
                if (selected_option == "Todos" or 
                    (selected_option == "Habilitado" and (int(enabled) == 66048 or int(enabled) == 512)) or
                    (selected_option == "Deshabilitado" and int(enabled) != 66048 and int(enabled) != 512)):
                    if int(enabled) == 66048 or int(enabled) == 512:
                        self.tree.insert("", "end", text=str(i), values=(username, nombre, "Habilitado"))
                    else:
                        self.tree.insert("", "end", text=str(i), values=(username, nombre, "Deshabilitado"))

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

class ButtonsOptions:
    def __init__(self, master, list_view):
        self.master = master
        self.list_view = list_view

        # Crear un Frame para agrupar los botones de búsqueda y filtrado
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side="top", fill="x", padx=10, pady=5)

        # Crear el botón de búsqueda general
        self.search_button = tk.Button(self.button_frame, text="Buscar Usuarios", command=self.list_view.populate_user_list)
        self.search_button.pack(side="left")

        # Crear el menú desplegable con las opciones de filtro
        self.selected_option = tk.StringVar(self.button_frame)
        self.selected_option.set("Todos")  # Establecer "Todos" como la opción seleccionada por defecto
        self.filter_menu = tk.OptionMenu(self.button_frame, self.selected_option, "Todos", "Habilitado", "Deshabilitado", command=self.filter_users)
        self.filter_menu.pack(side="left")

    def filter_users(self, selected_option):
        self.list_view.filter_users(selected_option)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x600")

    wrapper1 = tk.LabelFrame(root, text="Lista de Usuarios de Active Directory")
    wrapper1.pack(fill="both", expand="yes", padx=20, pady=20)

    wrapper2 = tk.LabelFrame(root, text="Opciones")
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=20)

    wrapper3 = tk.LabelFrame(root, text="Búsqueda")
    wrapper3.pack(fill="both", expand="yes", padx=20, pady=20)


    search_user = SearchBox(wrapper3, None)
    
    user_list_view = ListView(wrapper1, search_user)

    buttons_options = ButtonsOptions(wrapper2, user_list_view)

    root.mainloop()