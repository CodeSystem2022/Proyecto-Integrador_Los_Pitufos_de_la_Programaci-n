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
            # Placeholder
            sentencia = 'INSERT INTO hotel(tipohabitacion, fecha, estado)VALUES (%s, %s,%s)'
            valores= ('simple','12/06/2023', 'true') #Es una tupla
            cursor.execute(sentencia, valores)#De esta manera ejecutamos la sentencia
            registros_insertados = cursor.rowcount  # Recuperamos todos los registros que sera una lista
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
