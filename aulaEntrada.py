'''
nome = input("Digite seu nome: ")

saudacao = "Olá, " + nome

print(saudacao)
'''

'''
Testa se de fato conseguimos converter o input para int
Se der errado, então avisa o usuário.
Se der certo executa a conta.
'''

try:
    num1 = int(input("Digite o primeiro número: ")) # testa a conversão
    num2 = int(input("Digite o segundo número: "))
except:
    print("Você precisa digitar números inteiros")
else:
    print(num1 + num2)