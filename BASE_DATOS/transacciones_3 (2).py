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
                conexion.autocommit= False #Esto no deberia estar
                cursor =conexion.cursor()
                sentencia= 'INSERT INTO hotel(tipohabitacion, fecha, estado) VALUES (%s, %s, %s)'
                valores= ('simple','11/06/2023', 'false')
                cursor.execute(sentencia, valores)
                
                sentencia='UPDATE hotel SET tipohabitacion=%s, fecha=%s, estado=%s WHERE habitacion=%s'
                valores= ('dobre', '12/06/2023', 'true', 1)
                cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()
    
print('Termina la transaccion')