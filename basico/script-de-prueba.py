## Esto es un Script de Prueba
import sys
print(sys.argv)

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print("Error - Introduce los argumentos correctamente.")
    print('"repite_texto.py", "Texto a escribir", 4')
