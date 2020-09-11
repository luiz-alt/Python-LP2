'''
Quest ̃ao 4: Crie um programa que leia o nome de 5 pessoas e os armazena em
uma lista. Em seguida, construa uma fun ̧c ̃ao que recebe como parˆametros essa
lista e uma posi ̧c ̃ao ( ́ındice da lista) e devolve o nome contido naquela posi ̧c ̃ao.
B Essa fun ̧c ̃ao deve gerar uma exce ̧c ̃ao do tipo IndexError caso o  ́ındice n ̃ao
exista na lista.
'''

def error(lista):
    return lista[8]

nome = []
for i in range(5):
    nome_novo = input("Digite um nome: ")
    nome.append(nome_novo)

print(error(nome))

# Causando o erro IndexError, pois o indice da lista não existe.