# c = 1
# while c < 10:
#     print(c)
#     c += 1
# print('fim')
#
# while c != 0:
#     c = int(input('Digite um valor: '))
#
# r = 'S'
# while r == 'S':
#     r = str(input('Quer continuar? [S/N]')).upper()
# print('Fim')
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} pares e {} impares'.format(par, impar))