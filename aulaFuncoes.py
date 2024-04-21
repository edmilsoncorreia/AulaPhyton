#DEFININDO FUNÇÕES
def PrimeiraFunc():
    print("Esta é minha primeira função")
    print("Ela é bem Simples")
    print("Somente Imprime algumas coisas")

PrimeiraFunc()

print("\n")

def Ola(nome):
    print("Olá, ",nome)
    print("Como você vai?")

Ola("Edmilson")

print("\n")


#FUNÇÕES COM RETORNO
print("FUNÇÕES COM RETORNO")

def adicionaDois(numero):
    numero += 2
    return numero
inteiro = 10
inteiro = adicionaDois(inteiro)

print(inteiro)

print("\n")

#FUNÇÕES COM MÚLTIPLOS ARGUMENTOS
print("FUNÇÕES COM MÚLTIPLOS ARGUMENTOS")

def Multiplica(n1, n2):
    return n1*n2

resultado = Multiplica(10, 2)
print(resultado)

print("\n")

#ARGUMENTOS COM VALOR PADRÃO
print("ARGUMENTOS COM VALOR PADRÃO")

def Multiplica2(n1 = 3, n2 = 3):
    return n1*n2

print(Multiplica2())
print(Multiplica2(20,2))

print("\n")

#NÚMERO VARIÁVEL DE ARGUMENTOS
print("NÚMERO VARIÁVEL DE ARGUMENTOS")

def multiplicaNumeros(*varArgs):
    total = 0
    for arg in varArgs:
        total *= arg
    return total

print(multiplicaNumeros(1,2,3,4,5))

print("\n")

print("EXPRESSÕES LAMBDA")
f = lambda x,y:x*y
print( f(2,4))

print('\n')

print("DOCUMENTANDO FUNÇÕES")
def somaTres(x):
    '''Soma 3 a variável passada como entrada'''
    x += 3

print(somaTres.__doc__)