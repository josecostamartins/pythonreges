def duplo(x):
    print "Duplicando"
    return x * 2

def somando(y, z):
    print "Somando"
    return y + z

if somando(20, duplo(10)) == 0 and somando(-25, duplo(5)) < 0:
    print "Sim! numero final: {numero}".format(numero=somando(duplo(3), 0))
else:
    print "Nao! numero final: {numero}".format(numero=somando(duplo(3), 0))

