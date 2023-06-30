# Proyecto-Integrador_Los_Pitufos_de_la_Programación



***Aquí se encuentra el código del proyecto correspondiente al team Los pitufos de la Programación, el cual esta basado en crear una app para el registro remoto de los hoteles dandole facilidad y dinamismo a esta acción.
Esto genera una experiencia confortable tanto para el empresario dueño del hotel como para el cliente que quiere facildades a la hora de disfrutar su estadia en el recinto.***
Para dicho proyecto se utilizo:
Python como lenguaje del código hya que posee una sintaxis amplia y legible.
PostgreSQL como base de datos debido a su gran rendimiento y flexibilidad.


**Desarrolladores:

Santiago Mañas

Luciano Quinteros

Ezequiel Garcia

Jorge de la Plata

Maira Gimenez

Mayra Manzaneda

Ana Castello

Luciana Baigorria**


from datetime import datetime
import psycopg2

class Habitacion:
    def __init__(self, numero, tipo, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.disponible = disponible
        self.estado = 'libre'  
        self.reserva = None  

    def cambiar_estado(self, estado):
        self.estado = estado

    def agregar_reserva(self, fecha_llegada, fecha_salida):
        self.reserva = (fecha_llegada, fecha_salida)

    def esta_reservada(self, fecha):
        if self.reserva is None:
            return False
        fecha_llegada, fecha_salida = self.reserva
        return fecha_llegada <= fecha <= fecha_salida


num_habitaciones = 6 
habitaciones = []

# Inicializar las habitaciones del hotel
for i in range(1, 2):
    habitacion = Habitacion(i, "suite")
    habitaciones.append(habitacion)
for i in range(2, 4):
    habitacion = Habitacion(i, "doble")
    habitaciones.append(habitacion)
for i in range(4, 6):
    habitacion = Habitacion(i, "simple")
    habitaciones.append(habitacion)

# Mostrar el estado actual de todas las habitaciones
def mostrar_estado_habitaciones():
    print('Estado de las habitaciones:')
    for habitacion in habitaciones:
        print(f'Habitación {habitacion.numero}: {habitacion.estado}')

# Verificar el estado actual de las habitaciones
def verificar_estado_habitaciones():
    estado_habitaciones = {}
    for habitacion in habitaciones:
        estado_habitaciones[habitacion.numero] = habitacion.estado
    return estado_habitaciones

# Verificar la disponibilidad de las habitaciones en un rango de fechas
def verificar_disponibilidad_habitaciones(fecha_llegada, fecha_salida):
    disponibilidad_habitaciones = {}
    for habitacion in habitaciones:
        if habitacion.esta_reservada(fecha_llegada) or habitacion.esta_reservada(fecha_salida):
            disponibilidad_habitaciones[habitacion.numero] = 'No disponible'
        else:
            disponibilidad_habitaciones[habitacion.numero] = 'Disponible'
    return disponibilidad_habitaciones

# Solicitar una fecha al usuario
def solicitar_fecha(mensaje):
    while True:
        fecha_str = input(mensaje)
        try:
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
            return fecha
        except ValueError:
            print('Fecha inválida. Introduce la fecha en formato dd/mm/yyyy.')

# Método para elegir una habitación
def elegir_habitacion():
    while True:
        num_habitacion = input('Introduce el número de habitación: ')
        tipo_habitacion = input('Introduce el tipo de habitación (simple, doble o suite): ')

        for habitacion in habitaciones:
            if habitacion.numero == int(num_habitacion) and habitacion.tipo.lower() == tipo_habitacion.lower():
                return habitacion

        print('Habitación no encontrada o tipo de habitación incorrecto. Inténtalo nuevamente.')

# Menú principal
while True:
    print('--- Menú ---')
    print('1. Mostrar estado de las habitaciones')
    print('2. Disponibilidad con fechas ')
    print('3. Agregar reserva')
    print('4. Salir')

    opcion = input('Selecciona una opción: ')

    if opcion == '1':
        mostrar_estado_habitaciones()
    elif opcion == '2':
        fecha_llegada = solicitar_fecha('Introduce la fecha de llegada (dd/mm/yyyy): ')
        fecha_salida = solicitar_fecha('Introduce la fecha de salida (dd/mm/yyyy): ')

        disponibilidad = verificar_disponibilidad_habitaciones(fecha_llegada, fecha_salida)

        print('Disponibilidad de habitaciones:')
        for habitacion, estado in disponibilidad.items():
            print(f'Habitación {habitacion}: {estado}')
    elif opcion == '3':
        fecha_llegada = solicitar_fecha('Introduce la fecha de llegada (dd/mm/yyyy): ')
        fecha_salida = solicitar_fecha('Introduce la fecha de salida (dd/mm/yyyy): ')

        habitacion_elegida = elegir_habitacion()
        if habitacion_elegida is not None:
            habitacion_elegida.agregar_reserva(fecha_llegada, fecha_salida)
            habitacion_elegida.cambiar_estado('reservada')
            print(f'Reserva agregada para la Habitación {habitacion_elegida.numero}')
        else:
            print('No hay habitaciones disponibles para reservar.')
    elif opcion == '4':
        break
    else:
        print('Opción inválida. Introduce un número válido.')
