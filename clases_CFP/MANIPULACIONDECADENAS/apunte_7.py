"""
    Copiando y Pegando cadenas con Pyperclip:
El módulo pyperclip contiene las funciones copy() y paste() que pueden recibir o enviar texto 
del portapapeles de nuestra computadora.
Este módulo no viene incluido con Python. Para instalarlo habrá que ejecutar el comando pip 
install pyperclip en el símbolo de sistema.
"""
import pyperclip

pyperclip.copy('hola Leon, hola Lucio hermosos!')
print(pyperclip.paste())