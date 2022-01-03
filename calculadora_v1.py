# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("Selecione o número da operação desejada: ")

print(""" 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
""")

def opSoma(num1,num2):
    return print(num1 + num2)
def opSub(num1,num2):
    return print(num1 - num2)
def opMult(num1,num2):
    return print(num1 * num2)
def opDiv(num1,num2):
    return print(num1 / num2)

operacao = int(input("Digite a opção desejada: "))

if operacao == 1:
    print("Você selecionou operação de Soma, aguarde!!")
    x = float(input("Informe o primeiro número que deseja somar: "))
    y = float(input("Informe o segundo número que deseja somar: "))
    opSoma(x,y)

elif operacao == 2:
    print("Você selecionou a operação de subtração, aguarde!!")    
    x = float(input("Informe o primeiro número que deseja subtrair: "))
    y = float(input("Informe o segundo número que deseja subtrair: "))
    opSub(x,y)

elif operacao == 3:
    print("Você selecionou a operação de multiplicação, aguarde!!")
    x = float(input("Informe o primeiro número que deseja multiplicar: "))
    y = float(input("Informe o segundo número que deseja multiplicar: "))
    opMult(x,y)

elif operacao == 4:
    print("Você selecionou a operação de divisã0, aguarde!!")
    x = float(input("Informe o primeiro número que deseja dividir: "))
    y = float(input("Informe o segundo número que deseja dividir: "))
    opDiv(x,y)

elif operacao >= 5:
    "Você escolheu uma operação inválida"