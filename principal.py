import os
import subprocess
import sys

nombre = "Pedro González Hernández"

# Actividad 1
print(f"Alumno: {nombre}")
print(f"PID del proceso principal: {os.getpid()}")

# Actividades 2 y 3
hijo = subprocess.Popen([sys.executable, "hijo.py", nombre])
print(f"Primer hijo lanzado con PID: {hijo.pid}")

# Actividad 4
retorno = hijo.wait()
print(f"Primer hijo (PID {hijo.pid}) finalizado con codigo de retorno: {retorno}")

# Actividad 5
hijos = []

for i in range(1, 4):
    proceso = subprocess.Popen([sys.executable, "hijo.py", nombre, str(i)])
    hijos.append((i, proceso))
    print(f"Hijo {i} lanzado con PID: {proceso.pid}")

for i, proceso in hijos:
    codigo = proceso.wait()
    print(f"Hijo {i} (PID {proceso.pid}) finalizado con codigo de retorno: {codigo}")
