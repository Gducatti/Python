#EX01
#Exercício 1 Crie a tupla notas = (7.5, 8.0, 6.5, 9.0) e imprima a primeira nota e a última nota, usando
#índice positivo para a primeira e índice negativo para a última.

notas = tuple((7.5, 8.0, 6.5, 9.0))
print(f'A primeira nota é {notas[0]}')
print(f'A ultima nota é {notas[-1]}')

#EX02
#Exercício 2 Dada a tupla numeros = (12, 45, 7, 23, 9, 31) , calcule a soma de todos os elementos
#percorrendo a tupla com um for (sem usar a função sum ) e imprima o total.

numeros = ((12, 45, 7, 23, 9, 31))
total = 0
for numero in numeros:
    total += numero
print(f'O total da soma dos numeros é {total}')

#EX03
#3 Escreva uma função contar_pares que receba uma tupla de números inteiros e retorne
#quantos desses números são pares.

def conta_pares(numeros: tuple):
    total = 0
    for numero in numeros:
        if numero % 2 == 0:
            total += 1
    return total

print(f'Total de numeros pares: {conta_pares((12,5,7,24,9,31))}')

#EX04
#Crie duas tuplas de nomes de produtos, produtos_loja1 = ("Caneta", "Caderno", "Mochila")
#e produtos_loja2 = ("Estojo", "Régua") . Concatene as duas tuplas em uma única tupla todos_produtos e
#imprima o resultado.

produtos_loja1 = tuple(('Caneta', 'Caderno', 'Mochila'))
produtos_loja2 = tuple(('Estojo', 'Régua'))
todos_produtos = tuple([produtos_loja1 + produtos_loja2])
print(todos_produtos)

#EX05
tupla = (3, 15, 7, 42, 8, 19, 4, 26, 11)
print(tupla[0:4])
print(tupla[6:9])
print(tupla[::-1])