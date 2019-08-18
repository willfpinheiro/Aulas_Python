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


