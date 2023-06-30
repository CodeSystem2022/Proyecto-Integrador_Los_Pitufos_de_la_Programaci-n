import psycopg2  # Esto es para poder conectarnos a Postgre
#Insertar un registro
conexion = psycopg2.connect(user='postgres', password='admi', host='127.0.0.1', port='5432', database='test_basesdatos')
try:
    with conexion:
        with conexion.cursor() as cursor:
            # Placeholder
            sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES (%s, %s,%s)'
            valores= ('Carlos', 'Lara','clara@mail.com') #Es una tupla
            cursor.execute(sentencia, valores)#De esta manera ejecutamos la sentencia
            registros_insertados = cursor.rowcount  # Recuperamos todos los registros que sera una lista
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
