def validaIdade(idade):
    if (idade > 5 and idade < 100):
        return True
    return False

while True:
    cibele = int(input('Qual a idade da cibele? '))
    if (validaIdade(cibele)):
        break

while True:
    camila = int(input('Qual a idade da camila? '))
    if (validaIdade(camila)):
        break

while True:
    celeste = int(input('Qual a idade da celeste? '))
    if (validaIdade(celeste)):
        break
print('---------------------------------')
print('A idade da cibele é:', cibele)
print('A idade da camila é:', camila)
print('A idade da celeste é:', celeste)
