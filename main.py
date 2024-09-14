from controller import CustomerController

def main():
    controller = CustomerController() # Inicializar objeto controlador

    while True: # Ciclo de menú principal
        print("\n1. Agregar cliente")  # Agregar un nuevo cliente
        print("2. Ver clientes")  # Ver lista de clientes
        print("3. Salir")  # Salir del programa

        choice = input("Elija una opción: ")

        if choice == "1":
            controller.add_customer()  # Llamar al controlador para agregar un cliente
        elif choice == "2":
            controller.show_customers()  # Llamar al controlador para mostrar clientes
        elif choice == "3":
            print("Hasta pronto!")
            break  # Romper el ciclo y terminar el programa
        else:
            print("Opción errada. Por favor intente nuevamente.")

if __name__ == "__main__":
    main()
