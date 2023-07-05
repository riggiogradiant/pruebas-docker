# lector.py

# Leer las frases desde el archivo
with open("frases.txt", "r") as file:
    phrases = file.readlines()

# Imprimir las frases por terminal
print("Frases leídas:")
for phrase in phrases:
    print(phrase.strip())
