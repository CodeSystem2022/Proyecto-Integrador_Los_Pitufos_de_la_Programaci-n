import psycopg2  # Esto es para poder conectarnos a Postgre
# Insertar varios registros
conexion = psycopg2.connect(user='postgres', password='admi',
                            host='127.0.0.1', port='5432', database='test_basesdatos')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre= %s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Roldan', 'rcarlos@mail.com', 1)# Es una tupla de tuplas
            # De esta manera ejecutamos la sentencia
            cursor.execute(sentencia, valores)
            # Recuperamos todos los registros que sera una lista
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
