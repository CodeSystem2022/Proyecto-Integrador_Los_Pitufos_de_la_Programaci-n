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
            sentencia='DELETE FROM HOTEL WHERE habitacion =%s'
            entrada=input('Digite el numeros de registro a eliminar(separados por coma): ')
            valores= (entrada,)#Tuplca necesita la , para ser una tupla
            cursor.execute(sentencia, valores)
            # Recuperamos todos los registros que sera una lista
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
