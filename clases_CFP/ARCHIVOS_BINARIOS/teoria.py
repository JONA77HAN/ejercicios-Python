#1.Escribiendo una variable en el archivos misdatos
import shelve
gatos = ['Sofia', 'Pooka', 'Simon']
shelfArc = shelve.open('misdatos.dat')
shelfArc['nombresGatos'] = gatos.copy()
shelfArc.close()


#2.Leyendo y escribiendo del archivo misdatos
import shelve
shelfArc = shelve.open('misdatos')
gatos = shelfArc['nombresGatos'].copy()
print(gatos)
gatos.append(input('Gato nuevo: '))
shelfArc['nombresGatos'] = gatos.copy()
shelfArc.close()

