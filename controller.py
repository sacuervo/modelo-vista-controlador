# controller.py

from model import CustomerModel
from view import CustomerView

class CustomerController:
    def __init__(self):
        self.model = CustomerModel()
        self.view = CustomerView()

    def add_customer(self):
        name, pet_name = self.view.get_customer_details() # Utiliza método de vista para solicitar datos de cliente y mascota al modelo
        self.model.add_customer(name, pet_name) # Referencia a la lista del modelo para almacenar un nuevo cliente
        self.view.show_message(f"{name} y {pet_name} han sido agregados exitosamente.") # Utiliza método de vista para confirmar la adición del cliente

    def show_customers(self):
        customers = self.model.get_customers() # Utiliza método del modelo para referenciar los datos de los clientes
        self.view.show_customers(customers) # Muestra los datos de los clientes utilizando la referencia a sus datos
