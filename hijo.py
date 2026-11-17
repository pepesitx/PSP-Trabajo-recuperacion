import os
import sys

# Actividades 2, 3 y 5
nombre = sys.argv[1]
pid = os.getpid()

if len(sys.argv) > 2:
    numero = sys.argv[2]
    print(f"Hola {nombre}, soy el proceso hijo {numero} con PID {pid}")
else:
    print(f"Hola {nombre}, soy el primer proceso hijo con PID {pid}")
