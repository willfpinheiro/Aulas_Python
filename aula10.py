#Condição
def aula10():
    t = int(input('Quantos anos tem seu carro? '))
    if t<=3:
        print('carro novo')
    else:
        print('carro velho')
    print('FIM-')

#ou
def aula10a():
    print('carro novo' if t<=3 else 'carro velho')

def aula10b():
    nome = str(input('Qual o seu nome? '))
    if nome == 'Gustavo':
        print('Que nome lindo voce tem')
    print('Bom dia, {}'.format(nome))

def aula10c():
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    m = (n1+n2)/2
    print('A sua media foi {:.1f}'.format(m))
    if m>= 6.0:
        print('Sua media foi boa')
    else:
        print('Sua media foi ruim. Estude mais!')
aula10c()
