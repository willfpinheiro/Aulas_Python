import random
import time
def ex072():
    numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    print(numero[0])
    while True:
        num = int(input(f'Digite um valor entre 0 e 20: '))
        if 0 <= num < len(numero):
            break
        print('Tente Novamente. ', end='')
    print(f'Voce digitou o numero {numero[num]}')


def ex073():
    brasileirao = ('Palmeiras', 'remo', 'tuna', 'paysandu', 'Aguia de maraba', 'tabajara', 'Grêmio', 'Cruzeiro', 'Atlético', 'Paranaense', 'Flamengo', 'Corinthians', 'Santos', 'Vasco da Gama', 'Bahia', 'Fluminense', 'São Paulo', 'Botafogo', 'Internacional', 'Atlético', 'Chapecoense')
    print('-=' * 20)
    print(f'Os 5 primeiros colocados são: {brasileirao[0:5]}')
    print('-=' * 20)
    print(f'Os 4 ultimos são: {brasileirao[-4:]}')
    print('-=' * 20)
    print(f'Em ordem alfabetica: {sorted(brasileirao)}')
    print('-=' * 20)
    print(f'A Chapecoense esta na {brasileirao.index("Chapecoense")-1}ª colocação')
    print('-=' * 20)


def ex074():
    numrand = ((random.randint(0, 10)), (random.randint(0,10)), random.randint(0,10), random.randint(0,10), random.randint(0,10))
    print(f'Os valores sorteados foram: ', end='')
    for n in numrand:
        print(f'{n} ', end='')
    print(f'\nO maior é {max(numrand)}\nO menor é {min(numrand)}')


def ex075():
    count = 0
    num = (int(input("Digite um valor: ")), int(input("Digite outro valor: ")), int(input("Digite mais um valor: ")), int(input("Digite o ultimo valor: ")))
    print(f'O numero 9 repetiu {num.count(9)} vezes')
    if 3 not in num:
        print('O numero 3 não foi digitado')
    else:
        print(f'O primeiro 3 apareceu na posição: {num.index(3)+1}')
    print('Os numeros pares foram: ', end='')
    for c in num:
        if c % 2 == 0:
            print(c, end=' ')
            count += 1
    if c == 3 and count == 0:
        print('Nenhum')


def ex076():
    num = ('Pão', 0.40, 'Açucar', 1, 'farinha', 2.40, 'Note', 1999.99)
    print('-' * 30)
    print('{: ^30}'.format('Listagem de Preços'))
    print('-' * 30)
    for pos, c in enumerate(num):
        if pos % 2 == 0:
            print(f'{c:.<20}', end='')
        else:
            print(f'R${c: >8.2f}')


def ex077():
    times = ('Palmeiras', 'remo', 'tuna', 'paysandu', 'Aguia de maraba', 'tabajara', 'Gremio', 'Cruzeiro', 'Atletico', 'Paranaense', 'Flamengo', 'Corinthians', 'Santos', 'Vasco da Gama', 'Bahia', 'Fluminense', 'Sao Paulo', 'Botafogo', 'Internacional', 'Atletico', 'Chapecoense')
    for palavras in times:
        print(f'\nNa palavra {palavras.upper()} temos: ', end='')
        for letras in palavras:
            if letras.lower() in 'aeiou':
                print(letras, end=' ')

def ex078():
    lista = []
    for cont in range(0, 5):
        lista.append(int(input(f'Digite o valor na posição {cont}: ')))
    print('=-'*50)
    print(f'Voce digitou os valores {lista}')
    print(f'O maior valor digitado na lista foi {max(lista)} nas posições: ', end='')
    for n, maior in enumerate(lista):
        if maior == max(lista):
            print(f'{n}...', end=' ')
    print(f'\nO menor valor digitado na lista foi {min(lista)}, nas posições: ', end='')
    for i, menor in enumerate(lista):
        if menor == min(lista):
            print(f'{i}...', end=' ')

    #Outra forma, mais facil
    # numbers = list( )
    #
    # for n in range(0, 5):  # declarando variaveis com o laço
    #     numbers.append(int(input('Digite um valor: ')))
    #
    # print(f'''
    # O maior valor da lista: {max(numbers)} na posição {numbers.index(max(numbers))}
    # O menor valor da lista: {min(numbers)} ma posição {numbers.index(min(numbers))}''')


def ex079():
    valores = []
    cont = 'S'
    while True:
        if cont == 'N':
            break
        elif cont == 'S':
            n = int(input('Digite um valor: '))
            if n in valores:
                print('Numero ja inserido')
            else:
                valores.append(n)
                print('Valor adicionado com sucesso')
            cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        else:
            print('Letra invalida')
            cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    valores.sort()
    print(f'esse deu ceroto{valores}')

def ex080():
    valores = []
    for cont in range(0, 5):
        num = int(input('Digite um valor: '))
        if cont == 0 or num >= max(valores):
            valores.append(num)
            print('Valor adicionado no final da lista')
        # elif num <= min(valores):
        #     valores.insert(0, num)
        #     print('Adicionado na posição 0')
        else:
            contador = 0
            while True:
                if num < valores[contador]:
                    valores.insert(contador, num)
                    print(f'Adicionado na posição {contador}')
                    break
                contador += 1
    print('=-' * 30)
    print(valores)


def ex081():
    valores = []
    while True:
        valores.append(int(input('Digite um valor: ')))
        continuar = str(input('Desesa continuar? [S/N]')).upper().strip()[0]
        if continuar == 'N':
            break
    print(f'Você digitou {len(valores)} elementos')
    valores.sort(reverse=True)
    print(f'Os valores em ordem decrescente são {valores}')
    if 5 in valores:
        print('O valor 5 faz parte da lista')
    else:
        print('O valor 5 não faz parte da lista')


def ex082():
    padrao = list()
    par = list()
    impar = list()
    while True:
        padrao.append(int(input('Digite um valor: ')))
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if continuar == 'N':
            break
    padrao.sort()
    for v in padrao:
        if v % 2 == 0:
            par.append(v)
        elif v % 2 == 1:
            impar.append(v)
    print(f'A lista padrão é {padrao}')
    print(f'A lista par é {par}')
    print(f'A lista impar é {impar}')

def ex083():
    valores = str(input('Digite a expressão: '))
    pilha = []
    for simb in valores:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0: #Verifica se o tamanho da pilha esta maior que zero, para assim poder remover
                pilha.pop()
            else:
                pilha.append(')')
                break
    if len(pilha) == 0:
        print('Sua expressão esta certa')
    else:
        print('Sua expressão esta errada')
    print(pilha)


def ex084():
    galera = list()
    pessoa = list()
    cont = 0
    while True:
        pessoa.append(str(input('Nome: ')))
        pessoa.append(float(input('Peso: ')))
        if cont == 0:
            maior = menor = pessoa[1]
            cont += 1
        else:
            if maior < pessoa[1]:
                maior = pessoa[1]
            elif menor > pessoa[1]:
                menor = pessoa[1]
        galera.append(pessoa[:]) #Adiciona a lista temp na principal
        pessoa.clear() #Limpa a lista temp
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if continuar == 'N':
            break
    print('=-' * 30)
    print(f'Ao todo, você cadastrou {len(galera)} pessoas')
    print(f'O maior peso foi de {maior:.2f}. ', end=' ')
    for p in galera:
        if p[1] == maior:
            print(f'{p[0]}', end=' ')
    print()
    print(f'O menor peso foi de {menor:.2f}. ', end=' ')
    for p in galera:
        if p[1] == menor:
            print(f'{p[0]}', end='')

def ex085():
    numeros = [[], []] #Declarando um lista com duas listas internas
    for c in range(1, 8):
        n = int(input(f'Digite o {c}º valor: '))
        if n % 2 == 0: #separa os valores em par e adiciona na primeira posição da lista
            numeros[0].append(n)
        else: #separa os valores em impar e adiciona na posição 2 da lista
            numeros[1].append(n)
    print('=-' * 30)
    numeros.sort() #Organiza os valores
    print(f'Os valores pares digitados, foram: {numeros[0]}')
    print(f'Os valores impares digitados, foram: {numeros[1]}')


def ex086():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Declarção da matriz
    for linha in range(0, 3):
        for coluna in range(0, 3):
            matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    print(('=-') * 30)
    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f'[ {matriz[linha][coluna]:^5} ]', end='')
        print() #quebra a linha


def ex087():
    somapar = soma3 = 0
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Declarção da matriz
    for linha in range(0, 3):
        for coluna in range(0, 3):
            matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    print('=-' * 30)
    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f'[ {matriz[linha][coluna]:^5} ]', end='')
            if matriz[linha][coluna] % 2 == 0:
                somapar += matriz[linha][coluna]
        print()  # quebra a linha
    print('=-' * 30)
    #Varre a Matriz e verifica a coluna 3 e soma os valores da coluna 3
    # Depois varre a lista(linha) e verifica os pares para poder somar
    for valor in matriz:
        soma3 += valor[2]
    #     for c in range(0, 3):
    #         if valor[c] % 2 == 0:
    #             somapar += valor[c]
    print(f'A soma dos valores pares é: {somapar}')
    print(f'A soma dos itens da 3 coluna é: {soma3}')
    print(f'O maior valor da segunda linha é: {max(matriz[1])}')


def ex088():
    sena = []
    jogo = []
    n = int(input('Quantos jogos você quer fazer? '))
    print('=-' * 3, f'Sorteando {n} jogos', '=-' * 3)
    for j in range(0, n):
        for i in range(0, 6):
            while True:
                numero = random.randint(1, 60)
                if numero not in jogo:
                    jogo.append(numero)
                    break
        jogo.sort() #Ordena o jogo
        sena.append(jogo[:]) #adiciona o jogo na sena completa
        jogo.clear() #limpa o jogo
        print(f'Jogo {j+1}: {sena[j]}')
        time.sleep(1)
    # Fazendo o print rodando a lista
    # for i, l in enumerate(sena):
    #     print(f'Jogo {i+1}: {l}')
    print('Boa sorte!!!!')


def ex089():
    boletim = []
    nome = []
    notas = []
    media = []
    contnotas = 0
    while True:
        nome.append(str(input('Nome: ')))
        for a in range(1, 3):
            notas.append(float(input(f'Nota {a}: ')))
        m = (notas[0]+notas[1])/ 2
        boletim.append([nome[:], notas[:], m])
        notas.clear()
        nome.clear()
        media.clear()
        continuar = str(input('Deseja continuar: [S/N]')).upper().strip()[0]
        if continuar == 'N':
            break
    print("=-" * 30)
    print('No  Nome      Média')
    print('-' * 30)
    for cod, quadro in enumerate(boletim):
        print(f'{cod}  {quadro[0]}   {quadro[2]}')
    print('-' * 30)
    while contnotas is not 999:
        contnotas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if contnotas != 999:
            print(f'Notas da {boletim[contnotas][0]} sao {boletim[contnotas][1]}')
        else:
            break
    print('Finalizando....'
          'Volte sempre')
