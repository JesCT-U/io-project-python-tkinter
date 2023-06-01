import tkinter as tk

# Elimina la pagina para que no se ponga una debajo de la otra
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

# Funcion que crea la pantalla inicio
def home_page():
    home_frame = tk.Frame(main_frame)

    lb = tk.Label(home_frame, 
                  text="Investigación de operaciones\n\n", 
                  font=('Bold', 25))
    lb.pack()
    lb_names = tk.Label(home_frame, text='Omar Tubac\nJesús Capriel\nWilliam Hernandez',
                        font=('Bold', 20))
    lb_names.pack()

    home_frame.pack(pady=20)


# Funcion que crea la pantalla Nor Oeste
def noro_page():
    noro_frame = tk.Frame(main_frame)

    lb = tk.Label(noro_frame, 
                  text="Metodó de la esquina Noroeste\n", 
                  font=('Bold', 20))
    lb.pack()
    
    noro_frame.pack()

# Funcion que crea la pantalla Asignacion
def asig_page():
    asig_frame = tk.Frame(main_frame)

    lb = tk.Label(asig_frame, 
                  text="Metodó de asignación\n", 
                  font=('Bold', 20))
    lb.pack()

    asig_frame.pack()

# Funcion que ocualta todos los indicadores
def hide_indicators():
    asig_indicate.config(bg='#c3c3c3')
    noro_indicate.config(bg='#c3c3c3')
    home_indicate.config(bg='#c3c3c3')

# Funcion que cambia el color del indicador si se presiona el boton
# Tambien ejecuta las funciones que crean las pantallas
def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()

### Ventana principal ###
root = tk.Tk()
root.geometry('600x400')
root.title("IO")


### Frames ###
## Frame lateral para las opciones
options_frame = tk.Frame(root, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)

# Boton e indicador para inicio
home_btn = tk.Button(options_frame, text="Inicio", font=('Bold', 12),
                     fg='#158aff', bd=0, bg='#c3c3c3', 
                     command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10, y=50)

home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3, y=50, width=5, height=30)

# Boton e indicador para metodo Nor Oeste
noro_btn = tk.Button(options_frame, text="Noroeste", font=('Bold', 12),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(noro_indicate, noro_page))
noro_btn.place(x=10, y=100)

noro_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
noro_indicate.place(x=3, y=100, width=5, height=30)

# Boton e indicador para metodo de Asignacion
asig_btn = tk.Button(options_frame, text="Asignación", font=('Bold', 12),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(asig_indicate, asig_page))
asig_btn.place(x=10, y=150)

asig_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
asig_indicate.place(x=3, y=150, width=5, height=30)


## Frame principal
main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)

root.mainloop()