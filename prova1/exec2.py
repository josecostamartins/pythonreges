def verifica_numero(numero):
	
	if numero > 0:
		return "P"
	else:
		return "N"


valor = int(raw_input("Informe o valor: ") or 0)
print verifica_numero(valor)
