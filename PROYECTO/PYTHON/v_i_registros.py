import psycopg2  # Esto es para poder conectarnos a Postgre
#Insertar varios registros
conexion = psycopg2.connect(user='postgres', password='admi', host='127.0.0.1', port='5432', database='test_basesdatos')
try:
    with conexion:
        with conexion.cursor() as cursor:
            # Placeholder
            sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES (%s, %s,%s)'
            valores = (
                ('Carlos', 'Lara', 'clara@mail.com'),
                ('Marcos', 'Canto','mcantos@mail.com'),
                ('Marcelo','Cuenca','mcuenca@mail.com')
                )  # Es una tupla de tuplas
            # De esta manera ejecutamos la sentencia
            cursor.executemany(sentencia, valores)
            # Recuperamos todos los registros que sera una lista
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
