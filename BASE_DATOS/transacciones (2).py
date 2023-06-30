import psycopg2 as bd #Esto es para poder conectarnos a Postgre
#Se crea para un Registro
conexion= bd.connect(
    user= 'postgres',
    password= 'admin',
    host='127.0.0.1',
    port='5432',
    database='HOTEL'
)
try:
    #conexion.autocommit= False #Esto no deberia estar
    cursor =conexion.cursor()
    sentencia= 'INSERT INTO hotel(tipohabitacion, fecha, estado) VALUES (%s, %s, %s)'
    valores= ('doble','14/06/2023', 'true')
    cursor.execute(sentencia, valores)
    #conexion.commit()#Hacemos el comit manualmente
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()