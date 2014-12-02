# *-* encoding: utf-8 *-*
import random

# 11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de
# palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.

# primeiro passo: ler um arquivo e escolher uma palavra aleatória dele

arquivo = open("palavras.txt")  # abre o arquivo
palavras = arquivo.read().split("\n")  # eu poderia utilizar o método
                                       # readlines, mas ele mantém os \n
palavras.remove('')  # uma palavra vazia é adicionada ao final da lista, com essa linha nós removemos essa palavra

palavra = palavras[random.randint(1, len(palavras)) - 1]  # escolhemos uma palavra aleatória
forca = "_" * len(palavra)  # criamos uma variável que contém _ * tamanho da palavra escolhida
letras_digitadas = []  # guardamos as letras digitadas

# segundo passo: receber as letras do usuário 6 vezes
for tentativa in range(1, 7):
    print "Tentativa {}".format(tentativa)  # escrevemos na tela
    print forca  # escrevemos os traços na tela
    print  # espaço
    letra = raw_input("informe a letra: ")  # pedimos para o usuário informar a letra
    if letra in letras_digitadas:  # se o usuário já informou a letra, avisamos ele
        print "Letra já digitada"
    elif letra in palavra:  # se a letra existe na palavra mostramos ela
        indices = [i for i, x in enumerate(palavra) if x == letra] # guardamos as posicoes de onde essa letra aparece na palavra
        forca_temp = list(forca)  # transformamos a variavel forca em uma lista, assim podemos modificá-la
        for indice in reversed(indices):  # fazemos um loop para modificarmos todas as letras que são iguais
            forca_temp[indice] = letra  # modificamos os _ pela letra

        forca = "".join(forca_temp)  # transformamos a lista forca_temp em uma string novamente
        letras_digitadas.append(letra)  # adicionamos a letra digitada na lista de letras_digitadas
    else:
        print "Letra não consta na palavra" # informamos que a letra digitada não existe


print "A palavra é: " + "".join(palavra)
