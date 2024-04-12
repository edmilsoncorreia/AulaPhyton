'''
nome = input("Digite seu nome: ")

saudacao = "Olá, " + nome

print(saudacao)
'''

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
except:
    print("Você precisa digitar números inteiros")
else:
    print(num1 + num2)