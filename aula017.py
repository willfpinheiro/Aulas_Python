#Listas
# Tuplas x lista
# tuplas = ()
# Listas = []

# Adicionar um novo elemento na lista
# lista.append('asd') #adiciona um no final da lista
# lista.insert(0,'asd') #coloca o item na posição e arrasta os restantes

# Para deletar um item da lista
#remover pela chave
# del lista[3]
# lista.pop(3) #normalmente usado para remover o ultimo item da lista
# lista.pop()
#remover pelo conteudo
# lista.remove('conteudo') #caso não esteja na lista retornara erro
# Ex de como resolver:
# if conteudo in lista:
#     lista.remove('conteudo')

#Criar um lista
# valores = list(range(4, 11))

#Ordenar uma lista
# valores.sort()
# valores.sort(reverse=True) #de forma decrecente

#Tamanho de uma lista
# len(valores)

num = [2, 3, 5, 1]
num[2] = 1
num.append(7) #adicionar no fim da
num.sort()
print(num)
num.sort(reverse=True)
num.insert(2, 100)
num.pop(4)
print(num)