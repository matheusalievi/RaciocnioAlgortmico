# 1) Escreva os algoritmos em Python.

# a) Tabuada do 5 usando while:

i = 1

while i <= 10:
    print(f"5 x {i} = {5 * i}")
    i += 1

# b) Tabuada do 5 usando for

i = 1

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}") 

# 2) Soma dos números ímpares até um limite:
# Peça ao usuário para inserir um número inteiro positivo. Em seguida, some todos os números ímpares até esse limite usando um loop (while).

num = int(input("Digite um número inteiro positivo: "))
contador = 0
soma = 0

while contador <= num:
    if contador % 2 != 0:
        soma += contador
        print(contador)
    contador += 1
print("A soma dos números ímpares até", num, "é: ", soma)

# 3) Tabuada de dois números específicos: 
# Solicite ao usuário dois números inteiros. Após isso, imprima a tabuada correspondente a esses números de 1 a 10 utilizando um loop
# (for).

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

i = 1

for i in range(1, 11):
    print(f"{num1} x {i} = {num1 * i} / {num2} x {i} = {num2 * i}") 

# 4) Contagem regressiva: Inicie uma contagem regressiva a partir de um número especificado pelo usuário até 0, empregando um loop (while).

num = int(input("Digite um número: "))
contador = 0

while contador <= num:
    print(num - contador)
    contador += 1

    #5) Média de uma lista de números: Peça ao usuário para fornecer uma lista de números e então calcule a média desses números utilizando um loop (for).

entrada = input("Digite uma lista de números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)
print(f"A média dos números é: {media}")

# 6) Peça ao usuário para inserir um número inteiro positivo e calcule o fatorial desse número utilizando um loop (for).


numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Número inválido! Por favor, digite um número inteiro positivo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}")

# 7) Verificar se um número é primo: Solicite ao usuário um número inteiro e, em seguida, determine se ele é primo ou não utilizando um loop (for).

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print(f"{numero} não é primo.")
else:
    eh_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")

# 8) Imprimir os primeiros N termos da sequência de Fibonacci: Solicite ao usuário um número inteiro N e então imprima os primeiros N termos 
# da sequência de Fibonacci utilizando um loop (while).

n = int(input("Digite a quantidade de termos da sequência de Fibonacci que deseja ver: "))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    a, b = 0, 1
    contador = 0

    print("Sequência de Fibonacci:")
    while contador < n:
        print(a, end=' ')
        a, b = b, a + b
        contador += 1