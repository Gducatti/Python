#Tupla
#É tambem uma coleção
#ela é IMUTAVEL: GABRIELA - nasce e morre do mesmo jeito

print('TUPLA')
minhaTupla = ('sol', 'agua', 'natureza')
print(minhaTupla)

print('\nTipos de dados diferentes')
outraTupla = tuple(('a', 45, True))
print(type(outraTupla))
print(outraTupla)

print('\nAcessando pela posição')
print(f'1a posição: {minhaTupla[0]}')
print(f'2a posição: {minhaTupla[1]}')
print(f'Última posição: {minhaTupla[-1]}')

print('\nPegadinha 1')
#Não faz sentido criar uma tupla vazia, pois não podemos acrescentar elementos
tuplaVazia = ()
print(tuplaVazia)

print('\nPegadinha - Tupla de um elemento precisa de virgula')
tuplaUmFalsa = ('sol')
print(tuplaUmFalsa)
print(type(tuplaUmFalsa))

tuplaUm = ('sol',)
print(tuplaUm)
print(type(tuplaUm))

print('\nAchando a posição de um elemento')
minhaTupla = ('sol', 'agua', 'natureza', 'sol')
print(minhaTupla)
print(f'A agua esta na posição: {minhaTupla.index('agua')}')
print(f'O 1a sol esta na posição: {minhaTupla.index('sol')}')
print(f'O proximo sol esta na posição: {minhaTupla.index('sol', 1)}')

minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print(f'O 1a sol esta na posição: {minhaTupla.index('sol')}')
print(f'O 2o sol esta na posição: {minhaTupla.index('sol', minhaTupla.index('sol') +1)}')
#A partir da 2a ocorrencia não é mais legivel
print(f'O 3o sol esta na posição: {minhaTupla.index('sol', minhaTupla.index('sol') +1) +1}')

print('\nPercorrendo a coleção toda')
minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print(minhaTupla)
for item in minhaTupla:
    if item == 'sol':
        print(item)

('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print('\nAchando a posição dos sois')
for indice, item in enumerate(minhaTupla):
    if item == 'sol':
        print(f'posição {indice}: {minhaTupla[indice]}')

print('\nMatriz de tuplas')
matrizTupla = (('café', 'Banho'), ('Almoço', 'Academia'), ('Aula', 'Series'))
print(matrizTupla)
print(matrizTupla[2][1])

#Unpacking - atribuição multipla
print('\nUnpacking')
pessoa = ('Patricia', 'Casada', 54)
nome, estado_civil, idade = pessoa
print(nome)
print(estado_civil)
print(idade)

print('\nConversão para gambiarra')
minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago' 'sol')
print(minhaTupla)
#Acrescentar um elemento ???? não tem append
#como fazer
temp = list(minhaTupla)
temp.append('chuva')
print(type(temp))
minhaTupla = tuple(temp)
print(minhaTupla)
del temp