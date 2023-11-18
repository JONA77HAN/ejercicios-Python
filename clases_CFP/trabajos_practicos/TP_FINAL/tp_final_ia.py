import random
import string
import zipfile

# Lista de preguntas con sus respuestas
preguntas = {
    "Buenos Aires": "La Plata",
    "Córdoba": "Córdoba",
    "Santa Fe": "Santa Fe",
    "Mendoza": "Mendoza",
    "Tucumán": "San Miguel de Tucumán",
    "Entre Ríos": "Paraná",
    "Salta": "Salta",
    "Chaco": "Resistencia",
    "Corrientes": "Corrientes",
    "Santiago del Estero": "Santiago del Estero",
    # Agregar más preguntas de geografía aquí
}

# Función para generar un examen con preguntas y respuestas
def generar_examen():
    examen = []
    provincias = list(preguntas.keys())
    
    # Seleccionar 10 provincias al azar
    seleccion_provincias = random.sample(provincias, 10)
    
    for provincia in seleccion_provincias:
        # Agregar la pregunta correcta
        pregunta = f"¿Cuál es la capital de {provincia}?"
        respuesta_correcta = preguntas[provincia]
        opciones = [respuesta_correcta]
        
        # Agregar 3 respuestas incorrectas (tomadas al azar)
        otras_opciones = list(preguntas.values())
        otras_opciones.remove(respuesta_correcta)
        opciones.extend(random.sample(otras_opciones, 3))
        
        # Mezclar las opciones
        random.shuffle(opciones)
        
        examen.append((pregunta, opciones.index(respuesta_correcta) + 1))  # Guardar la opción correcta
        
    return examen

# Función para generar un archivo de texto con el examen
def guardar_examen(numero, examen):
    nombre_archivo = f"examen_{numero}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for i, pregunta in enumerate(examen, 1):
            archivo.write(f"Pregunta {i}: {pregunta[0]}\n")
            for j, opcion in enumerate(pregunta[1]):
                archivo.write(f"{string.ascii_uppercase[j]}. {opcion}\n")
            archivo.write("\n")

# Función para generar el archivo de respuestas
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

# Comprimir los archivos de exámenes
with zipfile.ZipFile('preguntas.zip', 'w') as preguntas_zip:
    for i in range(1, 21):
        preguntas_zip.write(f"examen_{i}.txt")

# Comprimir los archivos de respuestas
with zipfile.ZipFile('respuestas.zip', 'w') as respuestas_zip:
    for i in range(1, 21):
        respuestas_zip.write(f"respuestas_{i}.txt")
