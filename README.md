# Patrón modelo-vista-controlador. Guardería de mascotas 

## `model.py`

### Constructor:
- Inicializa instancias con una lista vacía de clientes
 
### `add_customer()`
- Añade nuevo cliente a la lista de clientes en forma de diccionario

### `get_customers()`
- Regresa referencia a la lista de clientes

## `view.py`

### `show_customers()`
- Recibe la lista de clientes como argumento, la atraviesa y muestra la información de cada cliente uno por uno

### `get_customer_details()`
- Recibe la información del un usuario mediante entrada de datos 

### `show_message()`
- Muestra mensaje de salida al usuario

## `controller.py`

### Constructor
- Inicializa la instancia con una referencia al modelo y otra referencia a la vista

### `add_customer`
- Utiliza métodos de la vista y el modelo para para solicitar datos de entrada y agregar un cliente. Posteriormente muestra una confirmación del proceso.

### `show_customers()`
- Utiliza metodo del modelo para referenciar la lista de clientes y mostrar sus datos 

## `main.py`
- Punto de entrada de la aplicación
- Muestra el menú principal
- Instancia el controlador