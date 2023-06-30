from datetime import datetime

# Definir una clase para representar una habitación
class Habitacion:
    def __init__(self, numero, tipo, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.disponible = disponible
        self.estado = 'libre'  # Estado inicial: libre
        self.reserva = None  # Reserva  inicial: ningunaS

    # Método para cambiar el estado de la habitación
    def cambiar_estado(self, estado):
        self.estado = estado

    # Método para agregar una reserva a la habitación
    def agregar_reserva(self, fecha_llegada, fecha_salida):
        self.reserva = (fecha_llegada, fecha_salida)

    # Método para verificar si la habitación está reservada en una fecha específica
    def esta_reservada(self, fecha):
        if self.reserva is None:
            return False
        fecha_llegada, fecha_salida = self.reserva
        return fecha_llegada <= fecha <= fecha_salida

# Crear una lista de habitaciones del hotel
num_habitaciones = 5  # Número total de habitaciones
habitaciones = []

# Inicializar las habitaciones del hotel
for i in range(1, num_habitaciones + 1):
    habitacion = Habitacion(i, "Tipo")
    habitaciones.append(habitacion)

# Función para mostrar el estado actual de todas las habitaciones
def mostrar_estado_habitaciones():
    print('Estado de las habitaciones:')
    for habitacion in habitaciones:
        print(f'Habitación {habitacion.numero}: {habitacion.estado}')

# Método para verificar el estado actual de las habitaciones
def verificar_estado_habitaciones():
    estado_habitaciones = {}
    for habitacion in habitaciones:
        estado_habitaciones[habitacion.numero] = habitacion.estado
    return estado_habitaciones
def solicitar_fecha(mensaje):
    while True:
        fecha_str = input(mensaje)
        try:
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
            return fecha
        except ValueError:
            print('Fecha inválida. Introduce la fecha en formato dd/mm/yyyy.')#

# Menú principal


def elegir_habitacion():
    while True:
        num_habitacion = input('Introduce el número de habitación: ')
        tipo_habitacion = input('Introduce el tipo de habitación (individual, doble o suite): ')

        for habitacion in habitaciones:
            if habitacion.numero == int(num_habitacion) and habitacion.tipo.lower() == tipo_habitacion.lower():
                return habitacion

        print('Habitación no encontrada o tipo de habitación incorrecto. Inténtalo nuevamente.')
# Función para verificar la disponibilidad de las habitaciones en las fechas especificadas
def verificar_disponibilidad_habitaciones(fecha_llegada, fecha_salida):
    disponibilidad = {}
    for habitacion in habitaciones:
        if habitacion.esta_reservada(fecha_llegada) or habitacion.esta_reservada(fecha_salida):
            disponibilidad[habitacion.numero] = 'No disponible'
        else:
            disponibilidad[habitacion.numero] = 'Disponible'

    return disponibilidad
    print('Habitación no encontrada o tipo de habitación incorrecto. Inténtalo nuevamente.')

# ...

while True:
    print('--- Menú ---')
    print('1. Mostrar estado de las habitaciones')
    print('2. Verificar disponibilidad de habitaciones')
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

# Función para solicitar una fecha al usuario
def solicitar_fecha(mensaje):
    while True:
        fecha_str = input(mensaje)
        try:
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
            return fecha
        except ValueError:
            print('Fecha inválida. Introduce la fecha en formato dd/mm/yyyy.')
