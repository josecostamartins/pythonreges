def remove_ultimo(minha_lista):
        minha_lista.pop()
        return minha_lista

a = [1, 2, 3, 4, 5, 6]
b = remove_ultimo(a[:])
c = remove_ultimo(b)
print a
print b
print c


print "Resposta: alternativa E"
