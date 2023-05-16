def validaEntrada(valor, minimo, maximo):
    if (valor >= minimo and valor <= maximo):
        return True
    return False

while True:
    numeroFigurinhaAlbum = int(input('Quantas figurinhas tem no album? '))
    if (validaEntrada(numeroFigurinhaAlbum, 1, 100)):
        break

while True:
    numeroDeFigurinhasCompradas = int(input('Quantas figurinhas foram compradas? '))
    if (validaEntrada(numeroDeFigurinhasCompradas, 1, 300)):
        break

album = []

for posicaoAlbum in range(numeroFigurinhaAlbum):
    album.append(0)

for figurinha in range(numeroDeFigurinhasCompradas):
    while True:
        numeroDaFigurinha = int(input('Qual o numero da figurinha? '))
        if (validaEntrada(numeroDaFigurinha, 1, numeroFigurinhaAlbum)):
            album[numeroDaFigurinha - 1] = album[numeroDaFigurinha - 1] + 1
            break

totalFigurinhaQueFalta = numeroFigurinhaAlbum
for posicaoAlbum in range(numeroFigurinhaAlbum):
    if (album[posicaoAlbum] > 0):
        totalFigurinhaQueFalta = totalFigurinhaQueFalta - 1

print('---------------------------------')
print('Ainda faltam :', totalFigurinhaQueFalta, 'figurinhas no seu album')
