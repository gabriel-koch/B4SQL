# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 01:30:24 2017

@author: Hugo
Edited by: Koch
"""
import math
import matplotlib #importa o módulo matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
import pandas as pd  #importa o módulo 'pandas' e chama de 'pd'

#dados = pd.read_csv(r'bank\\bank.csv', delimiter = ";" )
#dados2 = dados.iloc[:,5].abs() #extrai a coluna 5 e coloca os valores em módulo

#Se for arquivo em Excel (.xlsx)

df = pd.ExcelFile(r"C:\\Users\\R210.R210-07\\Desktop\\João Paulo\\Unifesp\\DOADOR_RECEPTOR.xlsx").parse('DOADOR_RECEPTOR_GAP')   # 'bank' é o nome da pasta que fica na parte de baixo do aruivo excel
dados=[]
dados.append(df['doa_rgct_1'])      # 'balance' é o nome da coluna
dados2 = [abs(x) for x in dados] # converte os valores em módulo


#coloca em dados2
# dados2 = dados2.set(str) #Converte os dados em string


prim_dig = [] #cria variável para a quantidade de repetições para cada dígito
seg_dig = []
terc_dig = []

dig_prec = [] #inicia variável para o percentual de cada dígito
dig_prec2 = []

"""
Aqui os números ainda estão como string (texto)

No python as strings podem ser interpretadas como uma sequência de letras
Como são vários valores e cada valor é uma linha temos uma tabela de letras.

Assim vamos extrair no loop for a seguir o primeiro dígito de cada linha
"""

for i in range(len(dados2)): #repete o número de vezes igual à quantidade de valores (linhas)
    if dados2[i][0] != '0': #retira valores iguais a zero (válido para este caso)
        prim_dig.append(dados2[i][0]) #vai incrementando as linhas e retira a o primeiro dígito

for n in range(9):
    dig_prec.append(0)  #inicializa lista com o percentual para cada dígito
    
    
"""
A seguir um loop para verificar cada um dos primeiros dígitos
e compará-los com 1,2,3,4,5,6,7,8,9.
Para cada comparação soma 1 e armazena na repectiva posição do vetor dig_prec
Ao final tem-se jm vetor dig_prec com o valor da quentidade de cada número(1,2,3 etc.)

Exemplo: dig_prec = [30, 20, 15, 10...]
Ou seja, existem 30 repetições do número 1, 20 repetições do número 2 e assim por diante.
"""
for j in range(len(prim_dig)): #repete o número de vezes igual à quantidade de valores armazenados em prim_dig
    for m in range(9): #repete o número de vezes igual a 9 (de 1 a 9)
        if prim_dig[j]==str(m+1): #Compara cada valor de prim_dig com 1, depois 2, e assim por diante
            dig_prec[m] = dig_prec[m]+1 #exemplo: se for 3 soma 1 na posição 3 da lista dig_prec
"""
A seguir vamos dividir esta quantidade pelo número total de valores 
(lembrando que foram extraídos os valores que eram apenas 0 dos dados originais).
Assim obteremos a porcentagem.
"""
for j in range(len(dig_prec)):
    dig_prec[j]=dig_prec[j]/len(prim_dig)

"""
Converteremos os dados em uma tupla para fazermos operações com a biblioteca pyplot
"""
dig_prec = tuple(dig_prec)

bar_width = 0.35 #Define a largura da barra do gráfico
eixo_x = [float(i+1) for i in range(9)] #Cria lista com valores de 1 a 9
eixo_x2 = [x+bar_width for x in eixo_x] #Cria lista com valores de 1.35 a 9.35  -> serão utilizados com o eixo x

eixo_x = tuple(eixo_x) #transforma as listas em Tuplas
eixo_x2 = tuple(eixo_x2)

#Cria o conjunto com os valores de Benford
numbers = [int(n) for n in range(1, 10)] #Cria lista de 1 a 10
benford = [math.log10(1 + 1 / d) for d in numbers] #Cria lista com os valores de Benford com d variando de 1 a 10
benford = tuple(benford) #transforma a lista em tupla

#Cria os gráficos a partir das tuplas criadas
fig = plt.figure()
ax = fig.add_subplot(211) # configura para o subplot 1
fig.subplots_adjust(hspace=.5) #ajusta o espaço entre os subplots
rects1 = ax.bar(eixo_x, dig_prec, bar_width) #plota a porcentagem ref ao prim dígito
rects2 = ax.bar(eixo_x2, benford, bar_width, color='r') #plota a porcentagem de Benford
ax.set_title('Primeiro dígito') # Título deste subplot
ax.legend((rects1[0], rects2[0]), ('Dados', 'Benford')) #Cria legenda

"""
Agora iniciaremos os passos para extrair o segundo dígito.
Faremos isto apenas para um determinado conjunto suspeito.
Se o conjunto suspeito mudar, altere a variável alg_susp.
"""
alg_susp = 3 #Algarismo suspeito. Exemplo: Suspeita-se que os valores que começam com 3 estão fora do padrão de Benford

for i in range(len(dados2)): #repete o número de vezes igual à quantidade de valores (linhas)
    if dados2[i][0] != '0': #retira valores iguais a zero (válido para este caso)
        if dados2[i][0] == '3':
            if len(dados2[i])<2:
                seg_dig.append(0)
            else:
                seg_dig.append(dados2[i][1]) #vai incrementando as linhas e retira a o segundo dígito
"""
#Seguimos o mesmo raciocínio utilizado para o primeiro dígito.
"""

for n in range(10):
    dig_prec2.append(0)  #inicializa lista com o percentual para cada  dígito (agora incluímos o 0)

for j in range(len(seg_dig)): #repete o número de vezes igual à quantidade de valores armazenados em prim_dig
    for m in range(10): #repete o número de vezes igual a 9 (de 1 a 9)
        if seg_dig[j]==str(m): #Compara cada valor de seg_dig com 1, depois 2, e assim por diante
            dig_prec2[m] = dig_prec2[m]+1 #exemplo: se for 3 soma 1 na posição 3 da lista dig_prec2
            
for j in range(len(dig_prec2)):
    dig_prec2[j]=dig_prec2[j]/len(seg_dig)
    
benford2 = [0.11968,0.11389,0.10882,0.10433,0.10031,0.09668,0.09337,0.09035,0.08757,0.08500] #Cria lista com os valores de Benford com d variando de 0 a 10
benford2 = tuple(benford2) #transforma a lista em tupla
eixo_x = [float(i+1) for i in range(10)] #Cria lista com valores de 1 a 10
eixo_x2 = [x+bar_width for x in eixo_x] #Cria lista com valores de 1.35 a 10.35  -> serão utilizados com o eixo x
eixo_x = tuple(eixo_x) #transforma as listas em Tuplas
eixo_x2 = tuple(eixo_x2)

ax2 = fig.add_subplot(212)
rects3 = ax2.bar(eixo_x, dig_prec2, bar_width)
rects4 = ax2.bar(eixo_x2, benford2, bar_width, color='r')
ax2.set_title('Segundo dígito')