# texto = 'Ana'
# numero_inteiro = 10
# numero_real = 5.6
# dado_boleano = True

# # print() -> Mostrar ou imprimir dados no console
# # Utilizmos aspas conforme o exemplo abaixo é possivel que utilizando aspas triplas não gera erro, porém não gera erro. (forma não oficial).
# '''
# adkjaldkjf
# jkjalskdf
# jkalsdjfl
# jaklsdjflk
# '''

# print(texto)
# print(numero_inteiro)
# print(numero_real)
# print(dado_boleano)

# #type -  verificar o tipo de dado.

# print(type(texto))
# print(type(numero_inteiro))
# print(type(numero_real))
# print(type(dado_boleano))

# # concatenar == juntar textos, variáveis, resultados

# text = type(texto)
# inteiro = type(numero_inteiro)
# real = type(numero_real)
# boleano = type(dado_boleano)

# print('Essa variável ->', texto, 'é da', text)
# print('Essa variável ->', numero_inteiro, 'é da', inteiro)
# print('Essa variável ->', numero_real, 'é da', real)
# print('Essa variável ->', dado_boleano, 'é da', boleano)


# print(f'Essa variável ->, {texto}, é da, {text}')
# print(f'Essa variável ->, {numero_inteiro}, é da, {inteiro}')
# print(f'Essa variável ->, {numero_real}, é da, {real}')
# print(f'Essa variável ->, {dado_boleano}, é da, {boleano}')


# ----------------------------------------------------------------

# nome = 'Fernando'
# nome = 'Jr'
# print(nome)

# NOME = 'Caio' #NÃO ALTERE
# NOME = 'Karol'
# # print(NOME)

# def nome():
#     name = 'Maria'
#     return name

# NOME = nome()


# print(NOME)

# print(10//10)

# nome = input('Digite seu nome: ')
# print(nome)

# numero1 = int(input('>>'))
# numero2 = int(input('>>'))
# nome = input('nome')
# calcular = numero1 + numero2

# print('Resultado', calcular, nome)


# x = 10
# text = bool(numero)
# n = text + 1
# print(n)

# print('Calculo: ((x/y)*z))')

# operacao = str(input('>>'))
# numero1 = int(input('>>')) 
# numero2 = int(input('>>'))
# numero3 = int(input('>>'))

# calcular =  ((numero1 / numero2)* numero3)
# soma = numero1 + numero2 + numero3
# print('Resultado: ((x/y)*z))', calcular)
# print('Resultado: ((x/y)*z))', soma)


# n1 = float(input('Digite um número:'))
# n2 = float(input('Digite um número:'))

# print(f'''
# Resultado da soma: {n1=n2},
# Resultado da subtração: {n1-n2},
# Resultado da divisão: {n1/n2},
# Resultado da multiplicação: {n1*n2},
# '''
# )

# numero =  10

# numeros = [10,2,3,5,'a',True,8.0]

# print(numeros[0])

# -----------------------------------------------------

# lista = [10,15,3,1,5]
# indice = lista[0]
# indice2 = lista[1]

# print(indice + indice2)

# numeros1 = list(range(1,11))
# print(numeros1)


# # Comprimento == len()
# # lista = [10,15,3,2,5]
# # print(len(lista))

# # add == append()

# # lista.append(10)
# # print(lista)

# # variavel = '10000'
# # print(len(variavel))

# # Transformar uma variavel em uma lista do tipo str
# variavel = 'text'
# lista2 = list(variavel)
# print(lista2)
# cria_sequencia = list(range(1, 101))
# soma = sum(cria_sequencia)
# print(soma)

# # max e min
# menor = min(cria_sequencia)
# print(menor)

# maior = min(cria_sequencia)
# print(maior)

# lista3 =  [6456, 56, 45, 1, 89]
# organizar = sorted(lista3)
# print(organizar)


# # pop() -> remover um indice
# lista3 .pop(0)
# print(lista3)

# lista3.remove(89)

# ----------------------------------


# Tuplas
# listas imutáveis
# Usamos parenteses


# lista = [1, 33]

# lista[0] = 22

# print(lista)

# tupla2 = tuple(lista)
# print(tupla2)

# tupla = (1,2,150,6,9,9,9,9)
# print(tupla[2])
# # conta a quantidade de valores
# # que foi declarado no parenteses
# contador = tupla.count(9)

# # verifica o indice do valor
# indice = tupla.index(9)
# print(contador, indice)

# # tamanho len()
# print(len(tupla))

# # max e min

# maior = max(tupla)
# menor = min(tupla)
# print(menor, maior)

# ordenar = sorted(tupla)
# print(ordenar)


# tupla4 = (1,4546,1,89,3,4,656)
# sorted(tupla4)
# numero = tupla4[1]
# a,b,c,d,e,f,g = tupla4

# print(a+b+c+d+e+f+g)
# print(sum(tupla4))

# CONJUNTOS {}
# TRABALHA COM COLCHETES

# nome = {1,5,150,56,89,78}
# conjunto2 = {1,6,6}

# diferenca = conjunto2 ^ nome
# nome.symmetric_difference(conjunto2)
# print(nome.difference(conjunto2))
# print(diferenca)


# conjunto4 =  set([1,56,6]
# remove = conjunto4.discard)


# # vai verificar o que tem nos 2 cojuntos
# intersecção = nome & conjunto2
# print(intersecção)

# print(nome, conjunto2)

# print(nome.union(conjunto2))

# ------------------------------------------
# Dicionario
# dicionario={
# 'nome': 'Pedro',
# 'idade': 25,
# 'endereco': 'Rua 100',
# 'curso': 'Python60h',

# }

# print(dicionario['endereco'])

# print(dicionario['curso'])

# ---------------------------------------------
# DESAFIO

dicionario={
'Aluno': 'Andre','curso': 'Python60h','nota': 10,
'Aluno': 'Adriano','curso': 'Python60h','nota': 8,
'Aluno': 'Anderson','curso': 'Python60h','nota': 7,
}

print(dicionario.keys()'Aluno'])
print(dicionario.keys['nota'])






