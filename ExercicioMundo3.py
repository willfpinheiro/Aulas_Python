import random
def ex072():
    numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    print(numero[0])
    while True:
        num = int(input(f'Digite um valor entre 0 e 20: '))
        if 0 <= num < len(numero):
            break
        print('Tente Novamente. ', end='')
    print(f'Voce digitou o numero {numero[num]}')


def ex073():
    brasileirao = ('Palmeiras', 'remo', 'tuna', 'paysandu', 'Aguia de maraba', 'tabajara', 'Grêmio', 'Cruzeiro', 'Atlético', 'Paranaense', 'Flamengo', 'Corinthians', 'Santos', 'Vasco da Gama', 'Bahia', 'Fluminense', 'São Paulo', 'Botafogo', 'Internacional', 'Atlético', 'Chapecoense')
    print('-=' * 20)
    print(f'Os 5 primeiros colocados são: {brasileirao[0:5]}')
    print('-=' * 20)
    print(f'Os 4 ultimos são: {brasileirao[-4:]}')
    print('-=' * 20)
    print(f'Em ordem alfabetica: {sorted(brasileirao)}')
    print('-=' * 20)
    print(f'A Chapecoense esta na {brasileirao.index("Chapecoense")-1}ª colocação')
    print('-=' * 20)


def ex074():
    numrand = ((random.randint(0, 10)), (random.randint(0,10)), random.randint(0,10), random.randint(0,10), random.randint(0,10))
    print(f'Os valores sorteados foram: ', end='')
    for n in numrand:
        print(f'{n} ', end='')
    print(f'\nO maior é {max(numrand)}\nO menor é {min(numrand)}')


def ex075():
    count = 0
    num = (int(input("Digite um valor: ")), int(input("Digite outro valor: ")), int(input("Digite mais um valor: ")), int(input("Digite o ultimo valor: ")))
    print(f'O numero 9 repetiu {num.count(9)} vezes')
    if 3 not in num:
        print('O numero 3 não foi digitado')
    else:
        print(f'O primeiro 3 apareceu na posição: {num.index(3)+1}')
    print('Os numeros pares foram: ', end='')
    for c in num:
        if c % 2 == 0:
            print(c, end=' ')
            count += 1
    if c == 3 and count == 0:
        print('Nenhum')


def ex076():
    num = ('Pão', 0.40, 'Açucar', 1, 'farinha', 2.40, 'Note', 1999.99)
    print('-' * 30)
    print('{: ^30}'.format('Listagem de Preços'))
    print('-' * 30)
    for pos, c in enumerate(num):
        if pos % 2 == 0:
            print(f'{c:.<20}', end='')
        else:
            print(f'R${c: >8.2f}')


def ex077():
    times = ('Palmeiras', 'remo', 'tuna', 'paysandu', 'Aguia de maraba', 'tabajara', 'Gremio', 'Cruzeiro', 'Atletico', 'Paranaense', 'Flamengo', 'Corinthians', 'Santos', 'Vasco da Gama', 'Bahia', 'Fluminense', 'Sao Paulo', 'Botafogo', 'Internacional', 'Atletico', 'Chapecoense')
    for palavras in times:
        print(f'\nNa palavra {palavras.upper()} temos: ', end='')
        for letras in palavras:
            if letras.lower() in 'aeiou':
                print(letras, end=' ')

def ex078():
    lista = []
    for cont in range(0, 5):
        lista.append(int(input(f'Digite o valor na posição {cont}: ')))
    print('=-'*50)
    print(f'Voce digitou os valores {lista}')
    print(f'O maior valor digitado na lista foi {max(lista)} nas posições: ', end='')
    for n, maior in enumerate(lista):
        if maior == max(lista):
            print(f'{n}...', end=' ')
    print(f'\nO menor valor digitado na lista foi {min(lista)}, nas posições: ', end='')
    for i, menor in enumerate(lista):
        if menor == min(lista):
            print(f'{i}...', end=' ')


def ex079():
    valores = []
    cont = 'S'
    while True:
        if cont == 'N':
            break
        elif cont == 'S':
            n = int(input('Digite um: '))
            if n in valores:
                print('Numero ja inserido')
            else:
                valores.append(n)
                print('Valor adicionado com sucesso')
            cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        else:
            print('Letra invalida')
            cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    valores.sort()
    print(f'esse deu ceroto{valores}')
ex079()