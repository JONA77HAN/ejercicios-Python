import os
os.path.join('Usuarios', 'Documentos', 'Spam.docx')
misArchivos = ['cuentas.txt', 'detalles.csv', 'invitación.docx']
for nombreArch in misArchivos:
    print(os.path.join('C:\\Usuarios\\Alan', nombreArch))

os.getcwd()
os.chdir('C:\\Windows\\System32')
os.getcwd()
os.chdir('C:\\EstaCarpetaNoExiste')