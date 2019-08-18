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
