# Aplicación de Alarma

## Descripción
Aplicación de Alarma es una herramienta elegante desarrollada en Python con una interfaz gráfica intuitiva. Permite a los usuarios configurar alarmas personalizadas con títulos y mensajes específicos, ofreciendo un diseño moderno con modos claro y oscuro.

## Características
- Interfaz gráfica de usuario intuitiva
- Configuración de hora y minutos para la alarma
- Personalización del título y mensaje de la alarma
- Modos claro y oscuro intercambiables
- Notificaciones del sistema y alerta sonora

## Requisitos del Sistema
- Python 3.x
- Bibliotecas: tkinter, plyer, Pillow (PIL)

## Instalación
1. Asegúrate de tener Python 3.x instalado.
2. Clona este repositorio o descarga el código fuente.
3. Instala las dependencias:

Plyer:
```bash
pip install plyer
```

Pillow:
```bash
pip install Pillow
```

## Uso
1. Navega al directorio del proyecto.
2. Ejecuta el script principal:


```bash
python aplicacion_alarma.py
```
3. Usa la interfaz para configurar tu alarma:
- Establece hora y minutos
- Ingresa título y mensaje
- Haz clic en "Iniciar Alarma"

## Estructura del Proyecto
- `aplicacion_alarma.py`: Script principal con la lógica de la aplicación
- `Imagenes/Iconos/`: Iconos para los modos claro y oscuro

## Características Técnicas
- Programación orientada a objetos
- Uso de hilos para temporización de alarmas
- Estilos personalizados con ttk
- Manejo de excepciones para validación de entrada

## Personalización
Modifica los estilos en el método `configurar_estilos()` para ajustar la apariencia de la aplicación según tus preferencias.