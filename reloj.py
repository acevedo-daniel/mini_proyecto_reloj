import tkinter as tk
import tkinter.ttk as ttk # Importamos ttk para el Notebook y los estilos

class AdvancedClock:
    def __init__(self, master):
        """
        Constructor de la aplicación AdvancedClock.
        Configura la ventana principal y aplica estilos personalizados a las pestañas
        (ttk.Notebook) para un diseño plano y moderno.
        """
        self.master = master
        master.title('Advanced Clock') # Título de la ventana
        master.geometry('450x400')   # Tamaño inicial de la ventana (ancho x alto)
                                     # Ancho ajustado para que las pestañas se vean más centradas.
        master.resizable(False, False) # Impide que el usuario redimensione la ventana

        # --- Configuración de Estilos para ttk.Notebook (Pestañas) ---
        # Usamos ttk.Style para personalizar la apariencia de los widgets temáticos.
        style = ttk.Style()
        style.theme_use('default') # Establece el tema base.

        # Estilo general del contenedor del Notebook (el área que rodea las pestañas y el contenido)
        style.configure('TNotebook', 
                        background='#003366', # Color de fondo del Notebook (azul oscuro)
                        borderwidth=0,        # Sin borde alrededor del Notebook principal
                        padding=[5, 5, 5, 0]  # Espacio interno del Notebook (izq, arr, der, ab)
                       )
        
        # Estilo de las Pestañas individuales (las etiquetas "Reloj", "Alarma", etc.)
        style.configure('TNotebook.Tab', 
                        background='#003366',    # Fondo de las pestañas no seleccionadas (azul oscuro)
                        foreground='white',     # Color del texto de las pestañas no seleccionadas
                        padding=[40, 15],       # Relleno interno de cada pestaña [horizontal, vertical]
                                                # Esto hace que las pestañas sean más anchas y altas.
                        font=('Helvetica', 12, 'bold'), # Fuente del texto de las pestañas (se recomienda 'Helvetica' o 'Arial')
                        relief='flat',          # Elimina el efecto 3D de botón de las pestañas (las hace planas)
                        borderwidth=0,          # Elimina el borde visible de las pestañas
                        bordercolor='#003366',  # Color del borde (igual que el fondo para que se "funda")
                        focuscolor='#003366'    # Color del contorno de enfoque (igual que el fondo para que sea invisible)
                       )
        
        # Mapeo de estilos: Define cómo cambian las propiedades de las pestañas en diferentes estados
        style.map('TNotebook.Tab',
            background=[('selected', '#FFD700'), # Fondo de la pestaña cuando está seleccionada (dorado)
                        ('active', '#004488')],   # Fondo cuando el mouse está sobre la pestaña (azul más claro)
            foreground=[('selected', 'black')],   # Color del texto de la pestaña seleccionada (negro)
            bordercolor=[('selected', '#FFD700')] # Borde de la pestaña seleccionada coincide con su fondo
        )
        # --- Modificación Avanzada del Layout de la Pestaña ---
        # Esta es la parte crucial para eliminar el "cuadro blanco" de enfoque.
        # Redefine la estructura interna de cómo se dibuja una pestaña,
        # eliminando el componente 'TNotebook.focus' que es el responsable de ese contorno.
        style.layout("TNotebook.Tab",
                     [("TNotebook.tab", {"sticky": "nswe", "children":
                                         [("TNotebook.padding", {"sticky": "nswe", "children":
                                                                 [("TNotebook.label", {"sticky": ""})]
                                                                })]
                                        })]
                    )
        
        # --- Creación del Widget Notebook (Pestañas) ---
        self.notebook = ttk.Notebook(master)
        # Empaqueta el notebook para que ocupe todo el espacio disponible en la ventana
        self.notebook.pack(expand=True, fill='both', padx=5, pady=5)

        # --- Creación de los Frames (Contenedores) para cada Pestaña ---
        # Cada Frame es el contenido de una pestaña. Se les asigna un color de fondo claro.
        self.clock_frame = tk.Frame(self.notebook, bg='#E0FFFF') # Azul muy claro
        self.notebook.add(self.clock_frame, text='Reloj') # Añade el frame como una pestaña con el texto "Reloj"

        self.alarm_frame = tk.Frame(self.notebook, bg='#FFE0E0') # Rojo muy claro
        self.notebook.add(self.alarm_frame, text='Alarma')

        self.stopwatch_frame = tk.Frame(self.notebook, bg='#E0FFE0') # Verde muy claro
        self.notebook.add(self.stopwatch_frame, text='Cronómetro') 

        # --- Llamadas a Métodos de Configuración de Funcionalidades ---
        # Estos métodos se implementarán en futuras fases para añadir los widgets
        # y la lógica específica de cada función (reloj, alarma, cronómetro).
        # self._setup_digital_clock()
        # self._setup_alarm()
        # self._setup_stopwatch()

# --- Punto de Entrada de la Aplicación ---
if __name__ == '__main__':
    root = tk.Tk() # Crea la ventana principal de Tkinter
    app = AdvancedClock(root) # Crea una instancia de nuestra aplicación de reloj
    root.mainloop() # Inicia el bucle principal de eventos de Tkinter, manteniendo la ventana abierta