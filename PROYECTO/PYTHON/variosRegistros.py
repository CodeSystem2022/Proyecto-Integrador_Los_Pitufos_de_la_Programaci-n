import psycopg2 
conexion = psycopg2.connect(user='postgres', password='admi', host='127.0.0.1', port='5432', database='HOTEL')
try: 
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM hotel WHERE habitacion IN %s'
            entrada= input('Digite las habitaciones que desee buscar: ')
            llaves=(tuple(entrada.split(', ')),)
            cursor.execute(sentencia, llaves)
            registros= cursor.fetchall()
            for registro in registros:
                print(registros)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
