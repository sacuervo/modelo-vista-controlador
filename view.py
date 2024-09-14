class View:
    def show_customers(self, customers): # Mostrar lista de clientes
        if not customers:
            print("Todavía no hay clientes.")
        for customer in customers: # Atravesar lista de clientes
            print(f"Customer: {customer['Nombre']}, mascota: {customer['nombre_mascota']}") # Imprimir clientes

    def get_customer_details(self): # Recibe los datos del cliente y mascota por parte del cliente
        name = input("Ingrese nombre de cliente: ")
        pet_name = input("Ingrese nombre de mascota: ")
        return name, pet_name

    def show_message(self, message): # Mostrar mensaje de salida al usuario
        print(message)
