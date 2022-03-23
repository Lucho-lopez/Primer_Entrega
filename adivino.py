## Adivina adivinador....
import random
numero_aleatorio = random.randrange(101)
gane = False
print("Tenés 5 intentos para adivinar un entre 0 y 100")
intento = 1
while intento < 6 and not gane:
    numero_Ingresado = int(input('Ingresa tu número: '))
    if numero_Ingresado == numero_aleatorio:
        print(f'Ganaste! y necesitaste {intento} intentos!!!')
        gane = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
        intento += 1
numero_Ingresado = int(input('Ingresa tu número: '))
if numero_Ingresado == numero_aleatorio:
    print(f'Ganaste! y necesitaste {intento} intentos!!!')
    gane = True
else:
    print(f'\n Perdiste :(\n El número era: {numero_aleatorio}')
