
def imprime_ate(num):
    if num == 0:
        print "somente valor 0"
        return
    else:
        print "imprimindo ate {number}".format(number=num)
        for value in range(num+1):
            print value

if __name__ == "__main__":
    var = int(raw_input("valor: "))
    imprime_ate(var)
