
'''2. Faça um Programa que peça um número correspondente a um
 determinado ano e em seguida informe se este ano é ou não bissexto.
 ATENÇÃO ATENÇÃO
 ATENÇÃO ATENÇÃO
 ATENÇÃO ATENÇÃO
 ATENÇÃO ATENÇÃO
 é preciso fazer mais cálculos para descobrir se o ano é bissexto,
 pois existem alguns casos de especiais que devemos tratar,
 façam esses casos especiais
 Dica: a melhor ferramenta no mundo da TI são os buscadores (e.g. Google, Bing)
 '''

ano = int(raw_input("Digite um ano qualquer: "))

if ano % 4 == 0 and ano % 100 != 0:
        print "Ano bissexto"
elif ano % 400 == 0:
        print "Ano bissexto"
else:
    print "Ano normal"
