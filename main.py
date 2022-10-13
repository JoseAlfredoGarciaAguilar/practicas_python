nombre = 'Alfredo'
edad = 22
texto = 'Hola Mundo, soy ' + nombre + ' y tengo ' + str(edad) + ' años'

for k in range(5):
    print(texto)

for i in range(10):
    print('Cuenta: ' + str(i+1))

str = 'Rammstein'
for word in str:
    print('Las letras son: ', word)

print('==========\n')
for word in range(len(str)):
    print('Letra en el Index {0} es = {1}'.format(word, str[word]))

for f in range(1,11):
    print(f)

for f in range(1,11):
    mult = 7 * f
    print(f'7 x {f} = {mult}')