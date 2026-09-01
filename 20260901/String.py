frase = 'Eu amo python'
print(frase)
lista = frase.split()
print(lista)

primeira_palavra = lista[0]
print(primeira_palavra)
letra = primeira_palavra[0]
print(letra)

frase = 'Eu amo python'
print('\nImprimindo palavra a palavra')
for palavra in frase.split():
    print(palavra)

print('\nImprimindo letra a letra')
for letra in frase:
    print(letra)

if 'Python' in frase:
    print('Tem Python na frase')

print('\nSlicing de uma string')
frase = 'Eu amo Python'
lista_palavras = frase.split()
print(lista_palavras)
amor = lista_palavras[0:2]
print(amor)

print('\nSlicing de uma frase - dividindo em letras')
indices = '0123456789123'
frase = 'Eu amo python'
print(frase[0:2])
print(frase[0:6])
print(frase[7:])
print(frase[::-1])