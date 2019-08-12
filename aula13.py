for c in range(1, 6):
    print(c)
    print('fim')
for c in range(6, 1, -1):
    print(c)
for c in range(1, 6, 2):
    print(c)
for c in range(0, 7):
    print(c)
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio é {}'.format(s))