nome = "Edmilson"
sobrenome = "Correia"

print("Nome", nome+" "+sobrenome, sep=': ')

#FORMATAR VARIÁVEIS
idade = 8.55
print("Idade %d" % idade)
print("O Sinal %d printa a variável como Int")
print("Idade %f" % idade)
print("O Sinal %f printa a variável como Float")
print("Idade %.1f" % idade)
print("O Sinal %.1f printa a variável como Float exibindo apenas 1 casa após a virgula")

#CRIANDO UM ARQUIVO
'''
arquivo = open("Arquivo.txt", "a")
print("NOSSA SEGUNDA LINHA SALVA", file=arquivo)
arquivo.close()
'''