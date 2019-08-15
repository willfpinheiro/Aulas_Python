# cont = 1
# while True:
#     print(cont, '- ', end='')
#     cont += 1

#usando f string e break
# n = s = 0
# while True:
#     n = int(input('Digite um numero: 1'))
#     if n == 999:
#         break
#     s += n
# print('A some é: {}'.format(s))
# print(f'A soma é {s}')

nome = 'jose'
idade = 22
salario = 1000.45123
print(f'O {nome:20} tem {idade:-^20} anos e seu salario é {salario:.3f}')  #PYTHON 3.6+
print('O {} tem {} anos'.format(nome, idade)) #PYTHON 3
