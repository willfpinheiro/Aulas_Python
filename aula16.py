#Variáveis compostas(Tuplas)
#Tuplas são variaveis composta
#AS TUPLAS SÃO IMUTAVEIS, NO PYTHON

# tuplas podem ser declaradas de 3 formas
# tupla = {'item1', 'item2'} ou ['item1', 'item2'] ou ('item1', 'item2') ou 'item1', 'item2'
lanche = ('Hamburguer', 'suco', 'cascalho', 'pudim')
print(lanche[1])
print(lanche[-1]) #Mostra o inverso
print(lanche[1:3]) #Mostra do um ate o 2, ignorando o 3
print(lanche[:2]) #mostra ate o 2
print(lanche[:-2]) #mostra o inverso ate o fim do inverso
print(lanche)
print(len(lanche))
#
# for c in range(0, len(lanche)):
#       print(f'eu vou comer {lanche[c]}')
#
# for comida in lanche:
#      print(f'eu vou comer {comida}')
#
# for pos, comida in enumerate(lanche):
#      print(f'eu vou comer {comida} na posição {pos+1}')
# print('Eu comi muito')

#Embaralhar uma tupla
# print(sorted(lanche))

#junçao de tuplas
# a = (2, 5, 8)
# b = (5, 9, 9, 8)
# c = a + b
# print(c)
# print(c.count(9)) #conta quantos x aparece a informação no ()
# print(c.index(8)) # Qual posição esta o valor
# print(c.index(8, 3)) #qual posição a partir de tal posição

#Tuplas no pyton aceita qualquer tipos na mesma tupla
pessoa = ('Will', 25, 'M', 75.2)
print(pessoa)

# Deletar tupla
# nao podendo deletar um elemento de dentro dela, somente ela por inteira
pessoa = ('Will', 25, 'M', 75.2)
del(pessoa)
print(pessoa)