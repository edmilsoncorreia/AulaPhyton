nota = 100
presenca = 10

if nota < 70 or presenca < 70:
    print("Você não Passou!")
    if nota < 70:
        print("Melhore sua Nota")
    if presenca < 70:
        print("Melhore sua Presença")

else:
    print("Você Passou!")
    if nota == 100 and presenca == 100:
        print("Você Passou com Louvor!")