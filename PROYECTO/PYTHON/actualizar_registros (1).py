import psycopg2 as bd # Esto es para poder conectarnos a Postgre
# Insertar varios registros
conexion= bd.connect(
    user= 'postgres',
    password= 'admin',
    host='127.0.0.1',
    port='5432',
    database='HOTEL'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE hotel SET tipohabitacion=%s, fecha=%s,  estado=%s'
            valores = ('Suite', '20/02/2022', 'false')# Es una tupla de tuplas
            # De esta manera ejecutamos la sentencia
            cursor.execute(sentencia, valores)
            # Recuperamos todos los registros que sera una lista
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
