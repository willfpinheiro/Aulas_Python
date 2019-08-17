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

for c in range(0, len(lanche)):
      print(f'eu vou comer {lanche[c]}')

for comida in lanche:
     print(f'eu vou comer {comida}')

for pos, comida in enumerate(lanche):
     print(f'eu vou comer {comida} na posição {pos+1}')

print('Eu comi muito')