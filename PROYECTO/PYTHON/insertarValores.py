import psycopg2 
conexion = psycopg2.connect(user='postgres', password='admi', host='127.0.0.1', port='5432', database='HOTEL')
try: 
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO hotel(habitacion, tipohabitacion, fecha, estado)VALUES (%s, %s, %s, %s)'
            valores= ('6', 'Simple', '30-06-2023', 'true')
            cursor.execute(sentencia, valores)
            registros= cursor.rowcount
            print(f'Habitacion registrada: {registros}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
