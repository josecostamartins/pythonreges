num1 = int(raw_input("Informe o primeiro numero: "))
num2 = int(raw_input("Informe o segundo numero: "))
operation = raw_input("Informe a operacao, opcoes: *, /, +, -: ")

result = 0
if operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
elif operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2

if result % 2 == 0:
    if result > 0:
        print result, "par", "positivo"
        #"{}, {}, {}".format(result, "par", "positivo")
    else:
        print "{}, {}, {}".format(result, "par", "negativo")
else:
    if result > 0:
        print "{}, {}, {}".format(result, "impar", "positivo")
    else:
        print "{}, {}, {}".format(result, "impar", "negativo")

