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
    'Rn' : 1*'♔'
}
