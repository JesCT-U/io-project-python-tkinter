import tkinter as tk
import myLib.pl_noroeste as pl

class Noroeste:
    def __init__(self, root):
        self.root = root # root = frame asig_frame
        
        form_param = tk.Frame(root) # Frame para datos
        
        tk.Label(form_param, text="Origen: ").grid(row=0, column=0)
        self.origin_txt = tk.Entry(form_param, width=8) # textbox numero de origenes
        self.origin_txt.grid(row=0, column=1)
        tk.Label(form_param, text="Destino: ").grid(row=1, column=0)
        self.destination_txt = tk.Entry(form_param, width=8) # textbox numero de destinos
        self.destination_txt.grid(row=1, column=1)

        tk.Button(form_param, text="Crear tabla"
                  , command=lambda: self.create_table()).grid(row=2,column=0, columnspan=2)

        form_param.pack()

    def create_table(self): # Funcion que crea la tabla
        rows = int(self.origin_txt.get()) # Obtener numero de ofertas
        cols = int(self.destination_txt.get())# Obtener numero de demandas

        origins = [f"Origen {i+1}" for i in range(rows)] # Genera lista nombres de ofertas
        origins.append("Demanda")
        destinations = [f"Destino {i+1}" for i in range(cols)] # Genera lista nombres de demandas
        destinations.append("Oferta")

        if 'table_frame' in self.root.children:
            self.root.children['table_frame'].destroy() # Eliminar frame si existente

        table_frame = tk.Frame(self.root,  name='table_frame') # Frame para la tabla
        table_frame.pack()

        inputs_costos = [] # Lista para almacenar los costos
        for i, origin in enumerate(origins):
            inputs_costos.append([])
            tk.Label(table_frame, text=origin).grid(row=i+1, column=0) # Etiqueta nombre de origen
            for j, destination in enumerate(destinations):
                tk.Label(table_frame, text=destination).grid(row=0, column=j+1) # Etiqueta nombre de destino
                input_costo = tk.Entry(table_frame, width=8) # Campo de entrada costo
                input_costo.grid(row=i+1, column=j+1)
                inputs_costos[i].append(input_costo)

        solve_button = tk.Button(table_frame, text="Resolver",
                                    command=lambda: self.solve_noroeste(inputs_costos))
        solve_button.grid(row=rows+2, column=0, columnspan=cols+2, pady=(10, 0))

    def solve_noroeste(self, inputs_costos):
        mat_text = [] # Matriz para almacenar los valores de los inputs
        
        for i in range(len(inputs_costos)):
            mat_text.append([])
            for j in range(len(inputs_costos[0])):
                mat_text[i].append(inputs_costos[i][j].get())

        plNoroeste = pl.PLNoroeste(mat_text) # Objeto PL Noroeste creado por Jesus Capriel
        plNoroeste.solve() # Funcion para resorlver esquina Noroeste

        tk.Label(self.root, text="El resultado es " + str(plNoroeste.result)).pack()