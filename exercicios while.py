import time

def exc1():
    n1=0
    soma=0

    while n1<101:
        soma+=n1
        print(n1)
        n1+=1
    print('a soma de todos os numeros: ',soma)

def exc2():
    soma = 0
    quant = 0
    contador = 1

    while contador <= 50:
        numero = int(input(f"Digite o {contador}º número: "))

        if numero > 0:
            soma += numero
        elif numero < 0:
            quant += 1

        contador += 1

    print(f"\nSoma dos números positivos: {soma}")
    print(f"Quantidade de números negativos: {quant}")

def exc3():
    n1=7

    while n1<1000:
        print(n1)
        n1+=7

def exc4():
    n1=86
    soma=0
    while n1<907:
        soma+=n1
        print(n1)
        n1+=2
    print(soma)

def exc5():
    n1=int(input('insira um numero: '))
    cont=1
    n2=0

    while cont<=n1:
        print(f'+{cont}')
        n2+=cont
        cont+=1
    print(f'={n2}')

def exc6():
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    resultado = 1
    contador = 0

    while contador < abs(expoente):
        resultado *= base
        contador += 1

    if expoente < 0:
        resultado = 1 / resultado

    print(f"{base} elevado a {expoente} é igual a {resultado}")

def exc7():
    n1=int(input('vc deseja que imprima a tabuada de 1 ate: '))
    tabuada=1
    multi=0
    result=0

    while tabuada<=n1:
        while multi<10:
            multi+=1
            result=tabuada*multi
            print(f'{tabuada}x{multi}={result}')
        tabuada+=1
        multi=0

def exc8():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B (maior que A): "))

    if B <= A:
        print("Erro: B deve ser maior que A.")
    else:
        soma = 0
        numero = A + 1 

        while numero < B:
            if numero % 2 == 0:  
                soma += numero ** 3 
            numero += 1

        print(f"A soma dos cubos dos números pares entre {A} e {B} é: {soma}")

def exc9():
    n1=int(input('insira o valor depositao na poupanca: '))
    mes=1
    juros=0.5/100

    while mes<=12:
        rend=n1*juros
        n1+=rend
        print(f"Mês {mes}: R$ {n1:.2f}") #.2f serve para deixar o numers apos a virgula bem mais bonitos e formatados corretamente
        mes+=1
    print(f"\nValor final após 12 meses: R$ {n1:.2f}")

def exc10():
    n1=int(input('Digite um Numero: '))
    divi=0
    i=1

    while i<n1:
        if n1%i==0:
            divi+=1
        i+=1

    if divi == 2:
        print(f"{n1} é um número primo.")
    else:
        print(f"{n1} NÃO é um número primo.")

def exc11():
    mil=1000
    cont=0
    divi=0
    result=0

    while cont<50:
        divi+=1
        result=mil/divi
        print(f'{mil}÷{divi}={result:.2f}')
        cont+=1
        mil-=3

def exc12():
    n1=int(input('insira um numero: '))
    fat=1
    cont=1
    soma=0

    while cont<=n1:
        fat*=cont
        soma+=fat
        print(f'{fat}x{cont}={soma}')
        cont+=1
    print(f'o fatorial e: {fat}')

def exc13():
    n1=int(input('digite o numero de Termos: '))
    r=int(input('digitie o numero de Razoes: '))
    p1=int(input('Digite o primeiro termo: '))
    cont=0

    soma=0
    termo=p1

    while cont<n1:
        print(termo)
        soma+=termo
        termo+=r
        cont+=1
    print(f'soma dos termos = {soma}')

n1=int(input('Escolha uma atividade de 1 a 13: '))

match n1:
    case 1:
        print('Some os números de 1 a 100 e imprima o valor.')
        time.sleep(2)
        exc1()
    case 2:
        print('Construa um Algoritmo que, para um grupo de 50 valores inteiros, determine: \na) A soma dos números positivos; \nb) A quantidade de valores negativos;')
        time.sleep(2)
        exc2()
    case 3:
        print('Faça um algoritmo que imprima os múltiplos positivos de 7, inferiores a 1000;')
        time.sleep(2)
        exc3()
    case 4:
        print('Faça um algoritmo que imprima todos os números pares compreendidos entre 85 e 907. O algoritmo deve também calcular a soma destes valores.')
        time.sleep(2)
        exc4()
    case 5:
        print('Escreva um programa que pergunte ao usuário um número e após, imprima na tela a soma total de 1 até o número lido. Exemplo: 5: 1 + 2 + 3 + 4 + 5 = 15')
        time.sleep(2)
        exc5()
    case 6:
        print('Faça um programa que peça dois números, base e expoente, calcule e imprima o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.')
        time.sleep(2)
        exc6()
    case 7:
        print('Construa um programa que exiba a tabuada de 1 até N, onde N é informado pelo usuário. ex: Até a tabuada de 3, irá imprimir as tabuadas de 1, 2 e 3.')
        time.sleep(2)
        exc7()
    case 8:
        print(' Faça um programa para calcular e imprimir a soma dos cubos dos números pares compreendidos entre A e B (B > A). A e B são lidos pelo teclado.')
        time.sleep(2)
        exc8()
    case 9:
        print('Faça um programa que receba um valor que foi depositado na poupança e exiba o valor com rendimento mês a mês durante o período de um ano. Considere fixo o juros da poupança em 0,5% a. m.')
        time.sleep(2)
        exc9()
    case 10:
        print('Número primo é aquele que só é divisível por ele mesmo e pelo número 1. Faça um programa que peça um número inteiro ao usuário e determine se o número informado é primo ou não.')
        time.sleep(2)
        exc10()
    case 11:
        print('Faça um programa que calcule o resultado dos 50 primeiros números da seguinte sequência: \n1000 ÷ 1 - 997 ÷ 2 + 994 ÷ 3 - 991 ÷ 4 + ...')
        time.sleep(2)
        exc11()
    case 12:
        print('Escreva um programa que determine o fatorial de um número. Para este problema, tem-se como entrada o valor do número do qual se deseja calcular o fatorial. O fatorial de 0 é igual a 1. O fatorial de um número N(N!) é definido conforme a seguir:\nN! = 1 × 2 × 3 × 4 × ... × (N - 1) × N')
        time.sleep(2)
        exc12()
    case 13:
        print('Construa um programa para exibir os termos de uma progressão aritmética, tendo como entrada o número de termos, a razão e o primeiro termo. Não utilizar vetor. Este programa também irá mostrar a soma dos termos')
        time.sleep(2)
        exc13()
    case _:
        print('numero invalido tente novamente')