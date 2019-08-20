#Listas Compostas ( listas 2)
# #ex 1
# teste = list()
# teste.append('will')
# teste.append(40)
# galera = list()
# galera.append(teste[:]) #Utilizando da copia para que não duplique a informação
# teste[0] = 'maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['joao', 22], ['ana', 33], ['joaquim', 40], ['maria', 19]]
galera = list()
dado = list()
totmaior = totmenor = 0
#ler os dados
for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')