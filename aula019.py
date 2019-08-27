# Dicionarios - adiciona indices literais
# Tuplas - ()
# Listas - []
# Dicionarios - {}

# Pode ser declara como:
dados = dict()
# ou
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print (dados['idade'])
# Append não funciona no dicionario, para adicionar uma nova informação, precisa usar o:
dados['sexo'] = 'M'
# Para deletar um elemento, desssa forma sera eliminado tanto as informações quanto a coluna
del dados['idade']
filme = {'Titulo':'Star wars',
         'ano':1977,
         'diretor':'George Lucas'
}
# Diferença entre VALOR X CHAVE X ITEM
# Valor é o conteudo de cada coluna
print(filme.values())
#Chaves é o nome de cada coluna
print (filme.keys())
# Item é tudo
print(filme.items())

for chave, valor in filme.itens():
    print(f'O {chave} é {valor}')
