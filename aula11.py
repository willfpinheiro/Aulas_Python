"""\033[style:text:backm
Style
0 = none
1 = Bold
4 = underline
7 = Negative
Text (cores)
30 - branco
31 - vermelho
32 - verde
33 - amarelo
34 - azul
35 - lilas
36 - ciano
37 - cinza
Back
40 - branco
41 - vermelho
42 - verde
43 - amarelo
44 - azul
45 - lilas
46 - ciano
47 - cinza

\033[0:30:41m
\033[4:33:44m
\033[1:35:43m
\033[30:42m
\033[m letra branca fundo preto
\033[7:30m letra preta fundo branco"""
print('\033[4:35:46mOla mundo')
print('\033[4:35:46mOla mundo\033[m')
a= 'Will'
print('Ola prazer em conhecer, {}{}{}'.format('\033[1:35:43m',a,'\033[m'))
cores = {
    'limpa' : '\033[m',
    'azul' : '\033[34m'
}
print('Ola {}{}{}'.format(cores['azul'],a,cores['limpa']))

