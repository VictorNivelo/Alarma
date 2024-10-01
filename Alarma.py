import os
import time
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from plyer import notification
import winsound
import threading
from PIL import Image, ImageTk


class AplicacionAlarma(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alarma")
        self.geometry("400x500")
        self.configure(bg="#f5f5f5")
        self.resizable(False, False)
        self.estilo = ttk.Style(self)
        self.estilo.theme_use("clam")
        self.modo_oscuro = False
        self.crear_widgets()

    def crear_widgets(self):
        marco_principal = ttk.Frame(self, padding="30 30 30 30", style="MarcoP.TFrame")
        marco_principal.pack(expand=True, fill=tk.BOTH)
        etiqueta_titulo = ttk.Label(
            marco_principal,
            text="Configurar Alarma",
            font=("Roboto", 28, "bold"),
            style="Titulo.TLabel",
        )
        etiqueta_titulo.pack(pady=(0, 30))
        marco_tiempo = ttk.Frame(marco_principal, style="Tiempo.TFrame")
        marco_tiempo.pack(pady=(0, 30))
        self.var_hora = tk.StringVar(value="00")
        self.var_minuto = tk.StringVar(value="00")
        entrada_hora = ttk.Entry(
            marco_tiempo,
            textvariable=self.var_hora,
            width=2,
            font=("Roboto", 64),
            justify="center",
            style="Tiempo.TEntry",
        )
        entrada_hora.pack(side=tk.LEFT, padx=(0, 10))
        ttk.Label(
            marco_tiempo, text=":", font=("Roboto", 64), style="Tiempo.TLabel"
        ).pack(side=tk.LEFT)
        entrada_minuto = ttk.Entry(
            marco_tiempo,
            textvariable=self.var_minuto,
            width=2,
            font=("Roboto", 64),
            justify="center",
            style="Tiempo.TEntry",
        )
        entrada_minuto.pack(side=tk.LEFT, padx=(10, 0))
        ttk.Label(
            marco_principal, text="Título de la alarma", style="Etiqueta.TLabel"
        ).pack(anchor=tk.W, pady=(20, 5))
        self.var_titulo = tk.StringVar(value="Mi alarma")
        entrada_titulo = ttk.Entry(
            marco_principal,
            textvariable=self.var_titulo,
            font=("Roboto", 12),
            style="Entrada.TEntry",
        )
        entrada_titulo.pack(fill=tk.X)
        ttk.Label(marco_principal, text="Mensaje", style="Etiqueta.TLabel").pack(
            anchor=tk.W, pady=(20, 5)
        )
        self.var_mensaje = tk.StringVar(value="¡Es hora de despertar!")
        entrada_mensaje = ttk.Entry(
            marco_principal,
            textvariable=self.var_mensaje,
            font=("Roboto", 12),
            style="Entrada.TEntry",
        )
        entrada_mensaje.pack(fill=tk.X)
        boton_iniciar = ttk.Button(
            marco_principal,
            text="Iniciar Alarma",
            command=self.iniciar_alarma,
            style="Iniciar.TButton",
        )
        boton_iniciar.pack(pady=(40, 0), fill=tk.X)
        ruta_iconos = os.path.join("Imagenes", "Iconos")
        self.icono_claro = ImageTk.PhotoImage(
            Image.open(os.path.join(ruta_iconos, "Modo_claro.png")).resize((24, 24))
        )
        self.icono_oscuro = ImageTk.PhotoImage(
            Image.open(os.path.join(ruta_iconos, "Modo_oscuro.png")).resize((24, 24))
        )
        self.boton_tema = ttk.Button(
            self,
            image=self.icono_oscuro,
            command=self.cambiar_tema,
            style="Tema.TButton",
        )
        self.boton_tema.place(relx=0.90, rely=0.01)
        self.configurar_estilos()

    def configurar_estilos(self):
        self.estilo.configure("MarcoP.TFrame", background="#f5f5f5")
        self.estilo.configure(
            "Titulo.TLabel",
            background="#f5f5f5",
            foreground="#333333",
            font=("Roboto", 28, "bold"),
        )
        self.estilo.configure("Tiempo.TFrame", background="#f5f5f5")
        self.estilo.configure(
            "Tiempo.TEntry",
            fieldbackground="#ffffff",
            foreground="#333333",
            insertcolor="#333333",
            borderwidth=0,
            relief="flat",
        )
        self.estilo.configure(
            "Tiempo.TLabel", background="#f5f5f5", foreground="#333333"
        )
        self.estilo.configure(
            "Etiqueta.TLabel",
            background="#f5f5f5",
            foreground="#555555",
            font=("Roboto", 12),
        )
        self.estilo.configure(
            "Entrada.TEntry",
            fieldbackground="#ffffff",
            foreground="#333333",
            insertcolor="#333333",
            borderwidth=0,
            relief="flat",
        )
        self.estilo.configure(
            "Iniciar.TButton",
            background="#4CAF50",
            foreground="#ffffff",
            font=("Roboto", 14, "bold"),
            borderwidth=0,
            relief="flat",
            padding=(10, 15),
        )
        self.estilo.map("Iniciar.TButton", background=[("active", "#45a049")])
        self.estilo.configure("Tema.TButton", background="#f5f5f5", relief="flat")

    def cambiar_tema(self):
        self.modo_oscuro = not self.modo_oscuro
        if self.modo_oscuro:
            self.configure(bg="#1e1e1e")
            self.estilo.configure("MarcoP.TFrame", background="#1e1e1e")
            self.estilo.configure(
                "Titulo.TLabel", background="#1e1e1e", foreground="#ffffff"
            )
            self.estilo.configure("Tiempo.TFrame", background="#1e1e1e")
            self.estilo.configure(
                "Tiempo.TEntry",
                fieldbackground="#2d2d2d",
                foreground="#ffffff",
                insertcolor="#ffffff",
                relief="flat",
                borderwidth=0,
            )
            self.estilo.configure(
                "Tiempo.TLabel", background="#1e1e1e", foreground="#ffffff"
            )
            self.estilo.configure(
                "Etiqueta.TLabel", background="#1e1e1e", foreground="#cccccc"
            )
            self.estilo.configure(
                "Entrada.TEntry",
                fieldbackground="#2d2d2d",
                foreground="#ffffff",
                insertcolor="#ffffff",
                relief="flat",
                borderwidth=0,
            )
            self.boton_tema.configure(image=self.icono_claro)
        else:
            self.configure(bg="#f5f5f5")
            self.estilo.configure("MarcoP.TFrame", background="#f5f5f5")
            self.estilo.configure(
                "Titulo.TLabel", background="#f5f5f5", foreground="#333333"
            )
            self.estilo.configure("Tiempo.TFrame", background="#f5f5f5")
            self.estilo.configure(
                "Tiempo.TEntry",
                fieldbackground="#ffffff",
                foreground="#333333",
                insertcolor="#333333",
                relief="flat",
                borderwidth=0,
            )
            self.estilo.configure(
                "Tiempo.TLabel", background="#f5f5f5", foreground="#333333"
            )
            self.estilo.configure(
                "Etiqueta.TLabel", background="#f5f5f5", foreground="#555555"
            )
            self.estilo.configure(
                "Entrada.TEntry",
                fieldbackground="#ffffff",
                foreground="#333333",
                insertcolor="#333333",
                relief="flat",
                borderwidth=0,
            )
            self.boton_tema.configure(image=self.icono_oscuro)

    def iniciar_alarma(self):
        try:
            if not self.var_hora.get().strip():
                raise ValueError(
                    "Por favor, introduce una hora válida (no puede estar vacía)."
                )
            hora = int(self.var_hora.get())
            minuto = int(self.var_minuto.get())
            titulo = self.var_titulo.get()
            mensaje = self.var_mensaje.get()
            if hora < 0 or hora > 23:
                raise ValueError("Por favor, introduce una hora válida (0 a 23).")
            if minuto < 0 or minuto > 59:
                raise ValueError("Por favor, introduce un minuto válido (0 a 59).")
            if not titulo.strip():
                raise ValueError("El título de la alarma no puede estar vacío.")
            if not mensaje.strip():
                raise ValueError("El mensaje de la alarma no puede estar vacío.")
            threading.Thread(
                target=self.configurar_alarma,
                args=(hora, minuto, titulo, mensaje),
                daemon=True,
            ).start()
            messagebox.showinfo(
                "Alarma configurada",
                f"La alarma está configurada para las {hora:02d}:{minuto:02d}.",
            )
        except ValueError as ve:
            messagebox.showerror("Error en los datos", str(ve))

    def configurar_alarma(self, hora, minuto, titulo, mensaje):
        ahora = datetime.now()
        tiempo_alarma = datetime(ahora.year, ahora.month, ahora.day, hora, minuto)
        if tiempo_alarma <= ahora:
            tiempo_alarma = tiempo_alarma.replace(day=tiempo_alarma.day + 1)
        diferencia_tiempo = tiempo_alarma - ahora
        time.sleep(diferencia_tiempo.total_seconds())
        notification.notify(title=titulo, message=mensaje, app_icon=None, timeout=10)
        winsound.Beep(1000, 1000)
        messagebox.showinfo("Alarma", f"{titulo}\n{mensaje}")


if __name__ == "__main__":
    app = AplicacionAlarma()
    app.mainloop()
