import datetime
import math
import random
import time
import pygame


def ex001():
    print('Ola, mundo!')


def ex002():
    a = input('Digite seu some: ')
    # msg = ('Seja bem vindo '+a)
    # print(msg)
    msg = "Seja bem vindo, "
    print('{}{}'.format(msg, a))


def ex003():
    a = int((input('Digite um valor: ')))
    b = int((input('Digite um outro valor: ')))
    soma = a + b
    print('A soma entre {} e {} é {}'.format(a, b, soma))


def ex004():
    a = input('Digite algo: ')
    print('O tipo primitivo é: ', type(a))
    print('Só tem espaços: ', a.isspace())
    print('É um numero: ', a.isnumeric())
    print('É alfabetico?', a.isalpha())
    print('É alfanumerico? ', a.isalnum())


def ex005():
    a = int(input('Digite um numero: '))
    print('O valor anterior é: {}\n e o valor posterio é: {}'.format(a - 1, a + 1))


def ex006():
    a = int(input('Digite um numero: '))
    print('O dobro é: {}\nO triplo é: {}\nA raiz quadrada é: {}'.format(a * 2, a * 3, pow(a, (1 / 2))))


def ex007():
    a = int(input('Coloque a primeira nota do aluno: '))
    b = int(input('Coloque a segunda nota do aluno: '))
    print('A media do aluno é: {}'.format((a + b) / 2))


def ex008():
    a = float(input('Coloque o numero em metros: '))
    print('O numero convertido em cm é: {:.2f}\nO numero convertido em ml: {:.2f}'.format(a * 100, a * 1000))


def ex009():
    a = int(input('qual a tubuada que você deseja fazer?'))
    b = ('-' * 10)
    print(b)
    print('{}*1={}\n{}*2={}\n{}*3={}\n{}*4={}\n{}*5={}\n{}*6={}\n{}*7={}\n{}*8={}\n{}*9={}'
          .format(a, a * 1, a, a * 2, a, a * 3, a, a * 4, a, a * 5, a, a * 6, a, a * 7, a, a * 8, a, a * 9))
    print(b)


def ex010():
    a = float(input('Digite o valor em Reais: '))
    print('Você pode comprar com R${}, a quantia de ${}'.format(a, a / 3.27))


def ex011():
    a = float(input('Coloque a altura da parede: '))
    b = float(input('Coloque a largura da parede: '))
    mq: float = a * b
    print('Com a altura de {} e a largura de {}, você tera {:.2f}m², precisando utilizar {:.2f}L de tinta.'.format(a, b,
                                                                                                                   mq,
                                                                                                                   mq / 2))


def ex012():
    a = float(input('Valor do produto: R$'))
    print('O valor de R${} com 5% de desconto fica R${}'.format(a, a - (a * 0.05)))


def ex013():
    a = float(input('Valor do salario que será aumentado: R$'))
    print('O salario mudará de R${} para R${} com o ajuste de 15%.'.format(a, a + (a * 0.15)))


def ex014():
    a = float(input('Coloque a temperatura em Celsius: '))
    print('A temperatura {:.2f}ºC em: \nFahrenheit é {:.2f}ºF\nE em Kelvin é {:.2f}K'.format(a, (a * 9 / 5) + 32,
                                                                                             (a + 273.15)))


def ex015():
    a = int(input('Quantos dias o carro ficou alugado: '))
    b = float(input('Quantos quilometros rodados: '))
    d = a * 60
    k = b * 0.15
    print('O carro rodou {:.3f}KM durante {} dias, valor devido é de: R${:.2f}'.format(b, a, d + k))


def ex016():
    a = float(input('Coloque um numero: '))
    print('O valor inteiro é: {}'.format(math.trunc(a)))
    print('O valor inteiro é: {}'.format(int(a)))


def ex017():
    a = float(input('Coloque o Cateto oposto: '))
    b = float(input('Coloque o cateto adjacente: '))
    print('A hipotenusa é {:.3f}'.format(math.hypot(a, b)))
    print('A hipotenusa é: {:.3f}'.format((a ** 2 + b ** 2) ** (1 / 2)))


def ex018():
    a = float(input('Coloque o angulo: '))
    print('O seno é: {:.3f}\nA tangente é: {:.3f}\nO cosseno é: {:.3f}'
          .format(math.sin(math.radians(a)), math.tan(math.radians(a)), math.cos(math.radians(a))))


def ex019():
    a = input('Nome do primeiro aluno: ')
    b = input('Nome do segundo aluno: ')
    c = input('Nome do terceiro aluno: ')
    d = input('Nome do quarto aluno: ')
    print('O aluno que irá apagar o quadro será: {}'.format(random.choice([a, b, c, d])))


def ex020():
    a = input('Nome do primeiro aluno: ')
    b = input('Nome do segundo aluno: ')
    c = input('Nome do terceiro aluno: ')
    d = input('Nome do quarto aluno: ')
    lista = [a, b, c, d]
    print('A ordem de apresentação será: \n{}'.format(random.sample(lista, 4)))
    random.shuffle(lista)
    print('A ordem aleatoria é de: {}'.format(lista))


def ex021():
    pygame.mixer.init()
    pygame.mixer.music.load('Kalimba.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(100)
    input('Agora você escuta?')
    pygame.event.wait()
    # playsound.playsound('Kalimba.mp3')


def ex022():
    a = str(input('Qual o seu nome? ')).strip()
    nome = a.split()
    print('Em maiusculo '.format(a.upper()))
    print('Em minusculo'.format(a.lower()))
    print('Quantidade de letras: '.format(len(''.join(nome))))  # len(a) - a.count(' ')
    print(len(nome[0]))  # a.find(' ')


def ex023():
    a = input('Digite o numero em milhar: ')
    print('unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(a[3], a[2], a[1], a[0]))


def ex023RC1():
    a = int(input('Digite um numero: '))
    m = a // 1000 % 10
    c = a // 100 % 10
    d = a // 10 % 10
    u = a // 1 % 10
    print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(m, c, d, u))


def ex024():
    a = str(input('Digite o nome da cidade: ')).strip()
    frase = a.upper()
    b = frase.split()
    c = b[0]
    print('SANTO' in c)
    # print(a[:5].upper() == 'SANTO')


def ex025():
    a = input('Digite o nome da pessoa: ').strip()
    frase = a.upper()
    print('SILVA' in frase)
    # print('SILVA' in a.upper())


def ex026():
    a = str(input('Digite uma frase: ')).upper().strip()
    print('Letra A aparece {} vezes'.format(a.count('A')))
    print('A letra A aparece pela primeira vez na sequencia {}'.format(a.find('A') + 1))
    print('A letra A aparece pela ultima vez na {} sequencia'.format(a.rfind('A') + 1))


def ex027():
    a = input('Digite seu nome completo: ').strip()
    a = a.title()
    b = a.find(' ')
    c = a.rfind(' ')
    print('Seu primeiro nome é: {}e seu ultimo nome é:{}'.format(a[:b], a[c:]))
    # nome = a.split()
    # print('Seu primeiro nome é {} e seu ultimo nome é {}'.format(nome[0], nome[len(nome)-1]))


def ex028():
    print('-+-' * 20)
    a = int(input('Qual o numero a maquina escolheu entre 0 e 5?'))
    b = random.randint(0, 5)
    print('Processando...')
    time.sleep(2)
    if a == b:
        print('Parabens, você acertou')
    else:
        print('O valor era {}. Tente na proxima'.format(b))


def ex029():
    a = float(input('Qual a velociadde do carro?'))
    if a <= 80:
        print('Parabens, continue salvando vidas')
    else:
        print('Você esta dirigindo acima da velocidade permitida\n'
              'irá pagar uma multa no valor de {:.2f}R$'.format((a - 80) * 7))


def ex030():
    a = float(input('Digite um numero: '))
    if (a % 2) == 0:
        print('Esse numero é par')
    else:
        print('Esse numero é impar')


def ex031():
    a = float(input('Quantos KM tem sua viagem? '))
    if a <= 200:
        print('Você ira pagar {}R$ pela viagem de {}KM'.format((a * 0.5), a))
    else:
        print('Você irá pagar {}R$ pela viagem de {}KM'.format((a * 0.45), a))


def ex032():
    a = int(input('Qual o ano quer saber se é bissexto(0 para ano atual): '))
    if a == 0:
        a = datetime.date.today().year
    if a % 400 == 0:
        print('Ano bissexto')
    else:
        print('Ano não bissexto')


def ex033():
    a = int(input('Primeiro numero: '))
    b = int(input('Segundo numero: '))
    c = int(input('Terceiro numero: '))
    if a > b > c:
        maior = a
        menor = c
    elif a > c > b:
        maior = a
        menor = b
    elif c > b > a:
        maior = c
        menor = a
    elif c > a > b:
        maior = c
        menor = b
    elif b > a > c:
        maior = b
        menor = c
    elif b > c > a:
        maior = b
        menor = a
    else:
        maior = 'inexistente'
        menor = 'inexistente'
    print('O maior é {} e o menor é {}'.format(maior, menor))


def ex034():
    a = float(input('Quanto é o salario que deseja aumentar: '))
    if a >= 1250:
        print('O salario irá aumentar para: {:.2f}R$'.format(a + (a * 0.10)))
    else:
        print('O salario irá aumentar para: {:.2f}R$'.format(a + (a * 0.15)))


def ex035():
    a = float(input('Primeira reta: '))
    b = float(input('Segunda reta: '))
    c = float(input('Terceira reta: '))
    if (a + b) > c and (a + c) > b and (c + b) > a:
        print('Com essas medidas é possivel fazer um triangulo')
    else:
        print('Com essas medidas não é possivel fazer um triangulo')


def ex036():
    a = float(input('Qual o valor da casa: '))
    b = float(input('Qual o seu salario: '))
    c = int(input('Tempo para pagamento: '))
    if (a / (c * 12)) >= (b * 0.3):
        print('O emprestimo não pode ser dado.')
    else:
        print('O emprestimo pode ser concedido, e o valor das parcelas será de R${:.2f}'.format((a / (c * 12))))


def ex037():
    a = int(input('Qual o numero deseja converter?\n'))
    b = int(input('Para binario digite 1\n'
                  'Para Octal digite 2\n'
                  'Para Hexadecimal digite 3'))
    if b == 1:
        print('O numero {} em binario é: {}'.format(a, bin(a)[2:]))
    elif b == 2:
        print('O numero {} em octal é: {}'.format(a, oct(a)[2:]))
    elif b == 3:
        print('O numero {} em hexadecimal é: {}'.format(a, hex(a)[2:]))
    else:
        print('Numero não reconhecido')


def ex038():
    a = float(input('Digite o primeiro numero: '))
    b = float(input('Digite o segundo numero: '))
    if a > b:
        print('O primeiro valor é maior')
    elif b > a:
        print('O segundo valor é maior')
    else:
        print("Não existe valor maior, os dois são iguais")


def ex039():
    a = int(input('Ano de nascimento: '))
    b = datetime.date.today().year
    c = b - a
    if c < 18:
        print('Você deve se alistar, faltam {} anos, que será no ano de {}'.format(18 - c, a + (18 - c)))
    elif c == 18:
        print('Ja esta na hora de se alistar')
    else:
        print('Ja passou {} anos do prazo de alistamento, este foi em {}'.format(c - 18, a + 18))


def ex040():
    a = float(input('Primeira nota: '))
    b = float(input('Segunda nota: '))
    if (a + b) / 2 < 5:
        print('reprovado')
    elif 7 > (a + b) / 2 >= 5:
        print('Recuperção')
    else:
        print('Aprovado')


def ex041():
    a = int(input('Qual o ano de nascimento: '))
    b = datetime.date.today().year - a
    print(b)
    if b < 10:
        print('mirin')
    elif b <= 14:
        print('infantil')
    elif b <= 19:
        print('junior')
    elif b <= 25:
        print('Sênior')
    else:
        print('Master')


def ex042():
    a = float(input('Primeira reta: '))
    b = float(input('Segunda reta: '))
    c = float(input('Terceira reta: '))
    if (a + b) > c and (a + c) > b and (c + b) > a:
        print('Com essas medidas é possivel fazer um triangulo', end='')
        if a == b == c:
            print('E forma um Triangulo equilatero')
        elif a == b or a == c or b == c:
            print('E forma um Triangulo Isoceles')
        elif a != b != c != a:
            print('E forma um triangulo escaleno')
    else:
        print('Com essas medidas não é possivel fazer um triangulo')


def ex043():
    a = float(input('Qual o peso: (Kg)'))
    b = float(input('Qual a altura: (m)'))
    c = a / (b ** 2)
    print(c)
    if c < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= c < 25:
        print('Peso ideal')
    elif 25 <= c < 30:
        print('Sobrepeso')
    elif 30 <= c < 40:
        print('Obesidade')
    else:
        print('Obesidade morbida')


def ex044():
    print('{:=^40}'.format(' Lojas Will '))
    a = float(input('Valor do produto: '))
    b = int(input('Entre com a forma de pagamento\n'
                  '1 - Dinheiro/cheque à vista\n'
                  '2 - cartão à vista\n'
                  '3 - 2X no cartão\n'
                  '4 - 3X ou mais no cartão\n'))
    if b == 1:
        print('O valor será: {:.2f}R$'.format(a - (a * 0.1)))
    elif b == 2:
        print('O valor será: {:.2f}R$'.format(a - (a * 0.05)))
    elif b == 3:
        print('O valor será: {:.2f}R$'.format(a))
    elif b == 4:
        print('O valor será: {:.2f}R$'.format(a + (a * 0.20)))
    else:
        print('Forma de pagamento incorreta')


def ex045():
    print('Vamos Jogar Jokenpo')
    a = random.randint(0, 2)
    itens = ('Pedra', 'Papel', 'Tesoura')
    b = int(input('Escolha sua mão\n'
                  '0 - Pedra\n'
                  '1 - Papel\n'
                  '2 - Tesoura\n'))
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PÔ')
    time.sleep(1)
    if b != 0 and b != 1 and b != 2:
        print('Opção invalida')
    elif a == b:
        print('Maquina escolheu {} e você escolheu {}'.format(itens[a], itens[b]))
        print('Empate')
    elif a == 0 and b == 1 or a == 1 and b == 2 or a == 2 and b == 0:
        print('Maquina escolheu {} e você escolheu {}'.format(itens[a], itens[b]))
        print('Parabéns, você venceu')
    else:
        print('Maquina escolheu {} e você escolheu {}'.format(itens[a], itens[b]))
        print('Eu ganhei, maquina no comando')
    ex045()

def ex046():
    for c in range(10, -1, -1):
        print(c)
        time.sleep(1)
    print('{:=^40}'.format(' BUM '))


def ex047():
    for c in range(0, 50):
        if c % 2 == 0:
            print('Esse numero é par: {}'.format(c))


def ex048():
    s = 0
    for c in range(1, 501):
        if c % 2 == 1 and c % 3 == 0:
            s += c
    print(s)


def ex049():
    print('{:*^40}'.format(' Tabuada '))
    n = int(input('Vamos fazer a multiplicação do número: '))
    for c in range(0, 10):
        m = n * c
        print('{} x {} = {}'.format(n, c, m))


def ex050():
    s = 0
    for c in range(0, 6):
        n = int(input('Digite um numero: '))
        if n % 2 == 0:
            s += n
    print('A soma dos pares é igual {}'.format(s))


def ex051():
    print(('{:*^40}'.format('Calculo de um PA')))
    t = int(input('Qual o primeiro termo: '))
    r = int(input('Qual a razão: '))
    for c in range(0, 10):
        print('Termo {} igual {}'.format(c + 1, t))
        t += r


def ex052():
    n = int(input('Digite um numero inteiro: '))
    t = 0
    for c in range(1, n + 1):
        if n % c == 0:
            print('\033[33m {}'.format(c), end=' ')
            t += 1
        else:
            print('\033[31m {}'.format(c), end=' ')

    if t == 2:
        print('\n\033[mNumero primo')
    else:
        print('\n\033[mNumero não é primo')
    ex052()


def ex053():
    t = 0
    a = input('Digite uma frase: ').strip().upper()
    palavras = a.split()
    junto = ''.join(palavras)
    m = junto[::-1]
    for c in range(0, len(junto)):
        # if b[c] == b[((len(m)-1)-c)]: Posso fazer uma varredura inversa na palavra
        if junto[c] == m[c]:
            t += 1
    print('A frase digitada é {} e o inverso é {}'.format(junto,m))
    if t == len(junto) or junto == m:
        print('Este frase é polindromo')
    else:
        print('Não é um polindrome')

def ex054():
    menor = 0
    maior = 0
    for c in range(1, 8):
        nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
        if nasc > 2019:
            print('Data invalida, favor coloque uma data antes de 2019'
                  'Essa Variavel nao será usada')
        elif datetime.date.today().year - nasc < 21:
            menor += 1
        else:
            maior += 1
    print('Temos {} maiores de idade e {} menores'.format(maior, menor))


def ex055():
    maior = float(0)
    menor = float(0)
    for c in range(1, 6):
        peso = float(input('Coloque um peso da {}º: '.format(c)))
        if c == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print('O maior peso é {} e o menor é {}'.format(maior, menor))


def ex056():
    idade = [0, 0, 0, 0]
    velho = 1
    quan_mulher = 0
    homem = 'Não foi citado '
    # soma = 0
    for c in range(1, 5):
        print('--- {}º Pessoa ---'.format(c))
        nome = input('Qual o nome: ').strip()
        idade[c] = int(input('Qual a idade: '))
        gen = int(input('Qual seu genero: 0 - Mulher \n1 - Homem \n2 - Outro'))
        if gen == 1 and idade[c] >= velho:
            homem = nome
        if idade[c] < 20 and gen == 0:
            quan_mulher = quan_mulher + 1
    #soma = idade[c]+ soma
    media = (sum(idade)) / 4
    print('''A idade media das pessoas informadas é {}
    O homem mais velho é {}
    Temos {} mulheres com menos de 20'''.format(media, homem, quan_mulher))


def ex057():
    s = ' '
    while s not in 'SN':
      s = str(input('Deseja sair? [S/N]')).upper().strip()


def ex058():
    print('-+-' * 20)
    user = int(input('Qual o numero a maquina escolheu entre 0 e 5?'))
    maq = random.randint(0, 5)
    print('Processando...')
    time.sleep(2)
    acertou = 'nao acertou'
    conterro = 1
    while acertou != 'acertou':
        if user == maq:
            acertou = 'acertou'
        else:
            print('Tente novamente')
            user = int(input('Qual o numero a maquina escolheu entre 0 e 5?'))
            conterro += 1
    print('Parabens, você acertou com {} tentativas'.format(conterro))

def ex059():
    print('Entre com os variaveis')
    num1 = float(input('Numero 1: '))
    num2 = float(input('Numero 2: '))
    result = 0
    var = 0
    while var != 5:
        var = int(input('''
        [1] - Somar
        [2] - Multiplicar
        [3] - Maior
        [4] - Novos Numeros
        [5] - Sair do programa'''))
        if var == 1:
            print('O valor da operação é {}'.format(num1+num2))
        elif var == 2:
            print('O valor da operação é {}'.format(num1 * num2))
        elif var == 3:
            if num2 == num1:
                print('Numeros iguais')
            elif num2 > num1:
                print('O numero {} é maior que {}'.format(num2, num1))
            else:
                print('O numero {} é maior que o numero {}'.format(num1, num2))
        elif var == 4:
            num1 = float(input('Numero 1: '))
            num2 = float(input('Numero 2: '))
        elif var == 5:
            print('Saindo do sistema tenha um bom dia')
        else:
            print('Opção invalida')

def ex060():
    num = int(input('Digite um numero: '))
    cont = num
    print('{}!'.format(num), end=' = ')
    while cont != 0:
        print('{}'.format(cont), end='x')
        cont -= 1

ex060()