from pulp import * # Libreria para resolver problemas de programacion lineal
import tkinter as tk
from tkinter import ttk

class Asignacion:
    def __init__(self, root): # root = frame asig_frame
        self.root = root
        
        form_param = tk.Frame(root) # Frame de datos para generar la tabla
        
        tk.Label(form_param, text="Destinos: ").grid(row=0, column=0) # Etiqueta numero de destinos
        self.destinos_txt = tk.Entry(form_param, width=8)
        self.destinos_txt.grid(row=0, column=1) # textbox numero de destinos
        tk.Label(form_param, text="Tareas: ").grid(row=1, column=0) # Etiqueta numero de tareas
        self.tareas_txt = tk.Entry(form_param, width=8)
        self.tareas_txt.grid(row=1, column=1) # textbox numero de tareas

        tk.Button(form_param, text="Crear tabla"
                  , command=lambda: self.create_table()).grid(row=2,column=0, columnspan=2)

        form_param.pack()

    def create_table(self): # Funcion que crea la tabla
        rows = int(self.destinos_txt.get()) # Obtener numero de destinos
        cols = int(self.tareas_txt.get()) # Obtener numero de tareas

        destinos = [f"Tarea {i+1}" for i in range(rows)] # Genera lista nombres de destinos
        tareas = [f"Destino {i+1}" for i in range(cols)] # Genera lista nombres de tareas

        if 'table_frame' in self.root.children:
            self.root.children['table_frame'].destroy() # Eliminar frame existente (si hay alguno)

        table_frame = tk.Frame(self.root,  name='table_frame') # Frame para la tabla
        table_frame.pack()

        inputs_costos = [] # Lista para almacenar los costos
        for i, destino in enumerate(destinos):
            tk.Label(table_frame, text=destino).grid(row=i+1, column=0) # Etiqueta nombre del destino
            for j, tarea in enumerate(tareas):
                tk.Label(table_frame, text=tarea).grid(row=0, column=j+1) # Etiqueta nombre de tarea
                input_costo = tk.Entry(table_frame, width=8) # Campo de entrada costo
                input_costo.grid(row=i+1, column=j+1)
                inputs_costos.append(input_costo) # Agregar el campo costo a la lista

        solve_button = tk.Button(table_frame, text="Resolver", #Llama a la funcion solve_asignation()
                                    command=lambda: self.solve_asignation(destinos, tareas, inputs_costos))
        solve_button.grid(row=rows+1, column=0, columnspan=cols+1, pady=(10, 0))

    def solve_asignation(self, destinos, tareas, inputs_costos):
        costos = {} # Diccionario para almacenar los costos de asignacion
        for i, destino in enumerate(destinos):
            for j, tarea in enumerate(tareas):
                costo = float(inputs_costos[i*len(tareas) + j].get())  # Obtener costo
                costos[(destino, tarea)] = costo  # Asignar el costo al par (destino, tarea)

        prob = LpProblem("Problema de asignación", LpMinimize)  # Crear un problema de asignación utilizando PuLP

        x = LpVariable.dicts("x", [(destino, tarea) for destino in destinos for tarea in tareas], lowBound=0, cat='Continuous')
        # Crear variables de decisión para las asignaciones utilizando PuLP

        prob += lpSum([costos[(destino, tarea)] * x[(destino, tarea)] for destino in destinos for tarea in tareas])
        # Definir la función objetivo: minimizar la suma de los costos de asignación multiplicados por las variables de decisión

        for destino in destinos:
            prob += lpSum([x[(destino, tarea)] for tarea in tareas]) == 1
            # Restricción: cada destino debe tener asignada exactamente una tarea

        for tarea in tareas:
            prob += lpSum([x[(destino, tarea)] for destino in destinos]) == 1
            # Restricción: cada tarea debe estar asignada a exactamente un destino

        prob.solve()  # Resolver el problema

        asignaciones = []  # Lista asignaciones
        for destino in destinos:
            for tarea in tareas:
                if x[(destino, tarea)].varValue == 1:  # Verificar si la variable de decisión es igual a 1 (asignada)
                    asignaciones.append((destino, tarea))  # Agregar la asignación a la lista
        
        if 'result_frame' in self.root.children:
            self.root.children['result_frame'].destroy() # Eliminar frame si existe

        result_frame = tk.Frame(self.root, name='result_frame')  # Frame para mostrar los resultados
        result_frame.pack()

        tk.Label(result_frame, text="Asignaciones: ").grid(row=0, column=0)
        for i, asignacion in enumerate(asignaciones):
            tk.Label(result_frame, text=f"{asignacion[0]} -> {asignacion[1]}").grid(row=i+1, column=0)
            # Etiqueta para cada asignación en una nueva fila

        new_button = tk.Button(result_frame, text="Nuevo", command=self.reiniciar_app)
        new_button.grid(row=len(asignaciones)+1, column=0, pady=(10, 0))
        # Botón para reiniciar la aplicación

    def reiniciar_app(self):
        if 'table_frame' in self.root.children:
            self.root.children['table_frame'].destroy()  # Eliminar marco existente (si hay alguno)
        if 'result_frame' in self.root.children:
            self.root.children['result_frame'].destroy()  # Eliminar marco existente (si hay alguno)

        self.create_table()  # Reiniciar la aplicación llamando a la función crear_tabla()
