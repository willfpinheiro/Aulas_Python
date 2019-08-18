import random
def ex072():
    numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    print(numero[0])
    a = ''
    while True:
        num = int(input(f'{a}Digite um valor entre 0 e 20: '))
        if 0 <= num < len(numero):
            break
        else:
            a = 'Tente Novamente. '
    print(f'Voce digitou o numero {numero[num]}')


def ex073():
    brasileirao = ('Palmeiras', 'remo', 'tuna', 'paysandu', 'Aguia de maraba', 'tabajara', 'Grêmio', 'Cruzeiro', 'Atlético', 'Paranaense', 'Flamengo', 'Corinthians', 'Santos', 'Vasco da Gama', 'Bahia', 'Fluminense', 'São Paulo', 'Botafogo', 'Internacional', 'Atlético', 'Chapecoense')
    print('-='*20)
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
    print(f'Os valores sorteados foram {numrand}')
    for c in range(0, 5):
        if c == 0:
            menor = numrand[c]
            maior = numrand[c]
        if numrand[c] < menor:
            menor = numrand[c]
        if numrand[c] > maior:
            maior = numrand[c]
    print(f'O maior é {maior}\nO menor é {menor}')


def ex075():
    count = 0
    num = (int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")))
    print(f'O numero 9 repetiu {num.count(9)} vezes')
    if num.count(3) == 0:
        print('O numero 3 não foi digitado')
    else:
        print(f'O primeiro 3 apareceu na posição: {num.index(3)+1}')
    print('Os numeros pares foram: ', end='')
    for c in range(0, 4):
        if num[c] % 2 == 0:
            print(num[c], end=' ')
            count += 1
    if c == 3 and count == 0:
        print('Nenhum')

def ex076():
    num = ('Pão', 0.40, 'Açucar', 1.95, 'farinha', 2.40, 'Note', 1999.99)
    print('-' * 30)
    print('{: ^30}'.format('Listagem de Preços'))
    print('-' * 30)
    for pos, c in enumerate(num):
        if pos % 2 == 0:
            print(f'{c:.<20}', end='')
        else:
            print(f'R${c: >8}')

def ex077():
    palavras = ('Palmeiras', 'remo', 'tuna', 'paysandu', 'Aguia de maraba', 'tabajara', 'Gremio', 'Cruzeiro', 'Atletico', 'Paranaense', 'Flamengo', 'Corinthians', 'Santos', 'Vasco da Gama', 'Bahia', 'Fluminense', 'Sao Paulo', 'Botafogo', 'Internacional', 'Atletico', 'Chapecoense')
    for c in range(0, len(palavras)):
        separada = str(palavras[c]).upper().strip()
        print(separada)
        print(f'Na palavra {separada} temos: ')
ex077()