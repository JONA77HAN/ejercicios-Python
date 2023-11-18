import random
import string
import zipfile

# Preguntas de provincias argentinas y sus capitales
preguntas = {
    "Buenos Aires": ["La Plata", "Córdoba", "Rosario", "Mar del Plata"],
    "Córdoba": ["Córdoba", "Mendoza", "Rosario", "La Plata"],
    "Santa Fe": ["Santa Fe", "Rosario", "La Plata", "Córdoba"],
    "Mendoza": ["Mendoza", "La Plata", "Córdoba", "Rosario"],
    # Agrega más preguntas de provincias y capitales de Argentina
}

# Función para generar un examen con preguntas y respuestas
def generar_examen():
    examen = []
    provincias = list(preguntas.keys())
    
    for _ in range(10):
        provincia = random.choice(provincias)
        respuesta_correcta = preguntas[provincia][0]
        opciones = preguntas[provincia][:]
        random.shuffle(opciones)
        
        examen.append((f"¿Cuál es la capital de {provincia}?", opciones.index(respuesta_correcta) + 1))
    
    return examen

# Función para guardar el examen en un archivo de texto
def guardar_examen(numero, examen):
    nombre_archivo = f"examen_{numero}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for i, pregunta in enumerate(examen, 1):
            archivo.write(f"Pregunta {i}: {pregunta[0]}\n")
            for j, opcion in enumerate(preguntas[pregunta[0][16:]], 1):
                archivo.write(f"{string.ascii_uppercase[j - 1]}. {opcion}\n")
            archivo.write("\n")

# Función para guardar las respuestas del examen
def guardar_respuestas(numero, examen):
    nombre_archivo = f"respuestas_{numero}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"Respuestas del Examen {numero}:\n")
        for i, pregunta in enumerate(examen, 1):
            archivo.write(f"Pregunta {i}: {string.ascii_uppercase[pregunta[1] - 1]}\n")

# Generar 20 exámenes y guardarlos
for i in range(1, 21):
    examen = generar_examen()
    guardar_examen(i, examen)
    guardar_respuestas(i, examen)

# Comprimir los archivos de exámenes en un archivo zip
with zipfile.ZipFile('preguntas.zip', 'w') as preguntas_zip:
    for i in range(1, 21):
        preguntas_zip.write(f"examen_{i}.txt")

# Comprimir los archivos de respuestas en un archivo zip
with zipfile.ZipFile('respuestas.zip', 'w') as respuestas_zip:
    for i in range(1, 21):
        respuestas_zip.write(f"respuestas_{i}.txt")
