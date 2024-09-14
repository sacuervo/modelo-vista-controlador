class Model:
    def __init__(self):
        self.customers = [] # Lista que almacenará información de clientes en forma de diccionario

    def add_customer(self, name, pet_name):
        self.customers.append({'nombre': name, 'nombre_mascota': pet_name}) # Añadir nuevo cliente a la lista

    def get_customers(self):
        return self.customers # Regresa referencia a lista de lcientes
