# Escreva um programa que leia 10 inteiros e armazene-os em uma lista "a".

a = []

for i in range(10):
    numeros = int(input(f"Digite o número {i + 1}: "))
    a.append(numeros)

print("\nNúmeros registrados na lista 'a' : ")
for numeros in a:
    print(numeros)

# Exer 5

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

maior = max(numeros)
impares = [n for n in numeros if n % 2 != 0]
menor_impar = min(impares) if impares else None

soma = sum(numeros)
media = soma / len(numeros)

print("\nResultados:")
print("Maior número:", maior)
if menor_impar is not None:
    print("Menor número ímpar:", menor_impar)
else:
    print("Nenhum número ímpar na lista.")
print("Somatório dos números:", soma)
print("Média dos números:", media)