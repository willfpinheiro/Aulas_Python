#Manipulação de string
# ºFatiamento
frase = 'Curso em video Python'
print(frase[9])
print(frase[9:14])
print(frase[9:21:2]) #do 9 ate o 20 pulando 2
print(frase[:15]) #do começo até o 14
print(frase[15:]) #do 15 até o final
print(frase[9::3])#do 9 ate o fim pulando 3

#Analise
print(len(frase)) #tamanho
print(frase.count('o'))#conta quantas vezes o o aparece
print(frase.count('o',0,13))#conta do 0 ao 13 a quantidade de o's
print(frase.find('deo'))#encontra o começo de deo
print(frase.find('Android'))#retorna -1 dizendo que nao foi encontrado
'curso' in frase #retorna verdadeiro ou falso

#Transformação
frase.replace('Python', 'Android')#substitui
frase.upper()#transforma tudo em maiusculo
frase.lower()#transforma tudo em minusculo
frase.capitalize()#coloca tudo em minusculo e a primeira letra fica maiuscula
frase.title()#Coloca cada palavra com a primeira letra em maiusculo
frase.strip()#remove espaços no começo e no fim da frase
frase.rstrip() #so da direita
frase.lstrip() #so da esquerda

#Divisão
frase.split() #separa uma frase em mini listas, dividindo pelos espaços
#junçao
'_'.join(frase) #Junta a frase, que ja foi separada, usando um string para unilas.
