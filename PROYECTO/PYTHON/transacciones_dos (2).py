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
    #conexion.autocommit= False (Esto no deberia estar)
    cursor =conexion.cursor()
    sentencia= 'INSERT INTO hotel(tipohabitacion, fecha, estado) VALUES (%s, %s, %s)'
    valores= ('simple','12/06/2023', 'true')
    cursor.execute(sentencia, valores)
    
    sentencia='UPDATE hotel SET tipohabitacion=%s, fecha=%s, estado=%s WHERE habitacion=%s'
    valores= ('doble', '10/10/2023', 'true', 1)
    cursor.execute(sentencia, valores)

    conexion.commit()#Hacemos el commit manualmente
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()