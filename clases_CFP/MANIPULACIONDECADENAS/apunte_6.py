import os
spam = 'SpamSpamCerdoSpamHuevosSpamSpam'
print(spam.strip('ampS'))
pollo = 'laskikicosaskikiquekikiquierokikisonkikimikikifamilia'
print(pollo.strip('kiki'))

frase_trunca = 'cual+ de estas fr++ase +es la +m+as ++rara?'
frase_limpia = frase_trunca.replace('+','')
print(frase_limpia)