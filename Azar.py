##import de random
import random

##
numeros = list(range(1,22))

numeros_jugador =[]

instrucciones = "Para jugar debes seleccionar 3 numeros del 1 al 21, el sistema seleccionara 3 numeros al azar, si aciertas a los 3 ganas"


def seleccion_numeros():
    numeros_jugador = []
    while len(numeros_jugador) < 3:
        try:
            n = int(input(f"Selecciona el número {len(numeros_jugador)+1}, del 1 al 21: "))
            if n in numeros and n not in numeros_jugador:
                numeros_jugador.append(n)
            else:
                print("Número inválido o repetido. Intenta nuevamente.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")
    return numeros_jugador

def jugar():
    numeros_jugador = seleccion_numeros()
    numeros_sorteados = random.sample(numeros, 3)
    
    print(f"\nTus números: {numeros_jugador}")
    print(f"Los números sorteados son: {numeros_sorteados}")
    
    aciertos = set(numeros_jugador).intersection(numeros_sorteados)
    if len(aciertos) == 3:
        print("¡Felicidades! Has acertado los 3 números y ganaste.")
    else:
        print(f"Has acertado {len(aciertos)} número(s): {list(aciertos)}. ¡Sigue intentando!")




#funcion menu
def menu_principal():
    """Muestra el menú principal del gestor de tareas"""
    flag = True
    while flag:
        print("\n--- Juego de Azar ---")
        print("1. Instrucciones")
        print("2. Jugar")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print(instrucciones)
        elif opcion == "2":
            jugar()
        elif opcion == "3":
            print("Gracias por usar el gestor de Tareas. ¡Hasta pronto!")
            flag = False
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")

#ejecutar el menu
if __name__ == "__main__":
    menu_principal()