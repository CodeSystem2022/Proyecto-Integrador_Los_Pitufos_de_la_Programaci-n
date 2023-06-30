import psycopg2
conexion= psycopg2.connect(user= 'postgres',password= 'admi',host='127.0.0.1',port='5432', database='HOTEL'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM hotel WHERE habitacion IN %s'
            entrada = input('Digite el numeros de registro a eliminar: ')
            valores = (tuple(entrada.split(', ')),) 
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()