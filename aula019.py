# # Dicionarios - adiciona indices literais
# # Tuplas - ()
# # Listas - []
# # Dicionarios - {}
#
# # Pode ser declara como:
# dados = dict()
# # ou
# dados = {'nome':'Pedro', 'idade':25}
# print(dados['nome'])
# print (dados['idade'])
# # Append não funciona no dicionario, para adicionar uma nova informação, precisa usar o:
# dados['sexo'] = 'M'
# # Para deletar um elemento, desssa forma sera eliminado tanto as informações quanto a coluna
# del dados['idade']
# filme = {'Titulo':'Star wars',
#          'ano':1977,
#          'diretor':'George Lucas'}
# # Diferença entre VALOR X CHAVE X ITEM
# # Valor é o conteudo de cada coluna
# print(filme.values())
# #Chaves é o nome de cada coluna
# print (filme.keys())
# # Item é tudo
# print(filme.items())
#
# for chave, valor in filme.itens():
#     print(f'O {chave} é {valor}')

#Comando basicos de um dicionario

# pessoas = {'nomes': 'Will', 'sexo': 'M', 'idade': 22}
# print(f'{pessoas["nomes"]} tem {pessoas["idade"]} anos.') #Colocar aspas duplas pois ja possui aspa simples geral
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items()) #mostra graficamente um lista compasta por tuplas
#
# for k in pessoas.keys():
#     print(k)
# for v in pessoas.values():
#     print(v)
# # Não tem enumerate, tendo que usar o items()
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# # del pessoas['sexo']
# pessoas['nomes'] = 'Leandro'
# pessoas['peso'] = 70
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

#Colocando um dicionario em uma lista
estado = dict() # Declarando um dicionario
brasil = list() #Declarando uma lista
for c in range(0, 3):
    estado['Uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
     # brasil.append(estado[:]) dicionarios não permitem que seja feito a copia atravez do fatiamento
for e in brasil:
    print(e)
    for k, v in e.items():
        print(f'O campo {k} valor {v}.')
for e in brasil:
    for v in e.values():
        print(v, end='/ ')
    print()