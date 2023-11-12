import random

preguntas = [
    {
        "pregunta": "¿Cuánto es 5 + 9?",
        "respuestas": ["14", "12", "15", "13"]
    },
    {
        "pregunta": "¿Cuánto es 7 x 8?",
        "respuestas": ["56", "48", "60", "49"]
    },
    {
        "pregunta": "¿Cuánto es 20 - 7?",
        "respuestas": ["13", "15", "12", "10"]
    },
    {
        "pregunta": "¿Cuánto es 18 / 3?",
        "respuestas": ["6", "5", "4", "7"]
    },
    {
        "pregunta": "¿Cuánto es 3^2?",
        "respuestas": ["9", "6", "5", "12"]
    },
    {
        "pregunta": "¿Cuánto es 4 * 6 - 5?",
        "respuestas": ["19", "15", "21", "14"]
    },
    {
        "pregunta": "¿Cuánto es 9 + 17?",
        "respuestas": ["26", "25", "24", "27"]
    },
    {
        "pregunta": "¿Cuánto es 12 / 4?",
        "respuestas": ["3", "4", "2", "5"]
    },
    {
        "pregunta": "¿Cuánto es 11 - 8?",
        "respuestas": ["3", "4", "2", "5"]
    },
    {
        "pregunta": "¿Cuánto es 10 x 5?",
        "respuestas": ["50", "45", "55", "40"]
    }
]

def mezclar_respuestas(respuestas):
    respuestas_mezcladas = respuestas[:]
    random.shuffle(respuestas_mezcladas)
    return respuestas_mezcladas

for i in range(20):
    examen = f"Examen-{i + 1}.txt"
    with open(examen, "w") as file:
        file.write(f"Examen {i + 1} de matemáticas básicas\n\n")
        preguntas_mezcladas = random.sample(preguntas, k=10)
        for j, pregunta in enumerate(preguntas_mezcladas):
            file.write(f"Pregunta {j + 1}: {pregunta['pregunta']}\n")
            respuestas_mezcladas = mezclar_respuestas(pregunta['respuestas'])
            for k, respuesta in enumerate(respuestas_mezcladas):
                file.write(f"   {k + 1}. {respuesta}\n")
            file.write("\n")
