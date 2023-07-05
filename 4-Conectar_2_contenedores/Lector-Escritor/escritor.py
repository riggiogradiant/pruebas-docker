# escritor.py

# Importar módulo sys
import sys

# Pedir frases al usuario
phrases = []
while True:
    try:
        phrase = input("Ingresa una frase (o escribe 'salir' para finalizar): ")
        if phrase.lower() == "salir":
            break
        phrases.append(phrase)
    except EOFError:
        # Capturar el error EOFError y finalizar el bucle
        break

# Escribir las frases en un archivo
with open("frases.txt", "w") as file:
    for phrase in phrases:
        file.write(phrase + "\n")

print("Escritura completada.")
