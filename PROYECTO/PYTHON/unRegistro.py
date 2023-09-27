import psycopg2 
conexion = psycopg2.connect(user='postgres', password='admi', host='127.0.0.1', port='5432', database='HOTEL')
try: 
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM hotel WHERE habitacion = %s'
            habitacion=input('Digite la habitacion que desea ver: ')
            cursor.execute(sentencia, habitacion)
            registros= cursor.fetchone()
            print(registros)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
