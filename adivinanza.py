import random

def jugar():
    intentos = 0
    numero_secreto = random.randint(1, 100)

    print("¡Bienvenido al juego de adivinanza de números! Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    while intentos < 7:
        intento = int(input("Introduce tu intento: "))

        if intento < numero_secreto:
            print('¡Demasiado bajo!')
        elif  intento > numero_secreto:
            print('¡Demasiado alto!')
        else:
            print('¡Felicidades! Adivinaste el número en', intentos+1, 'intentos.')
            return
        intentos +=1
    print('Lo siento, has perdido. El número secreto era', numero_secreto)
jugar()
