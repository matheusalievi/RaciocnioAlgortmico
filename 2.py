cont = 0
soma_medias = 0
while cont < 3:
    nome = str(input("Digite o nome do aluno: "))
    n1 = float(input(f"Digite a primeira nota do {nome} : "))
    n2 = float(input(f"Digite a segunda nota do {nome} : "))
    n3 = float(input(f"Digite a terceira nota do {nome}: "))
    n4 = float(input(f"Digite a última nota do {nome} :"))
    media = (n1 + n2 + n3 + n4) / 4
    soma_medias += media
    print("Média anual: ", media)
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    cont += 1
    media_total = soma_medias / cont
print(f"A média total é: {media_total:.12f}")


print("Testando alterações da atividade no Git!")