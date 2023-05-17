# este menú vamos a usar input para que el usuario ingresa datos
def menu():
    print('Hola, Silvana Inmobiliaria para servirte')
    print('1. agregar datos personales')
    print('2. agregar inmueble') 
    
    print('3. salir')

def app():
    while True:
        menu() 
        opcion = input('Ingrese una opción: ') 
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion == 3:
                break

            if opcion == 1:
                print('Agregar datos personales')
            elif opcion == 2:
                print('Agregar características del inmueble')
            else:
                print('Ingrese una opción válida')

                 
        else:
            print('Error: Ingresa un número')

app()