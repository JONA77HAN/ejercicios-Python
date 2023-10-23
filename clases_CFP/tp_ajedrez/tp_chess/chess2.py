from random import randint
piezas_blancas = {
    'pb' : int(randint(0,8))*'♟',
    'cb' : int(randint(0,2))*'♞' ,
    'ab' : int(randint(0,2))*'♝',
    'tb' : int(randint(0,2))*'♜',
    'rb' : int(randint(0,1))*'♛',
    'Rb' : '♚'
}
piezas_negras = {
    'pn' : int(randint(0,8))*'♟',
    'cn' : int(randint(0,2)),
    'an' : int(randint(0,2)),
    'tn' : int(randint(0,2)),
    'rn' : int(randint(0,1)),
    'Rn' : 1
}
print(piezas_blancas['cb'])
print(piezas_negras['pn'])

# Generacion de fichas aleatorias 
peon_blanco = int(randint(0, 8))*'♟'
caballo_blanco = int(randint(0, 2))*'♞' 
alfil_blanco = int(randint(0, 2))*'♝'
torre_blanca = int(randint(0, 2))*'♜'
reina_blanca = int(randint(0, 1))*'♛'
rey_blanco = 1*'♚'
# Negras: 
peon_negro = int(randint(0, 8))*'♙' 
caballo_negro = int(randint(0, 2))*'♘'
alfil_negro = int(randint(0, 2))*'♗'
torre_negra = int(randint(0, 2))*'♖'
reina_negra = int(randint(0, 1))* '♕'
rey_negro = 1*'♔'