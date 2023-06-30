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
            sentencia = 'SELECT * FROM hotel WHERE habitacion IN (1, 2)' #Placeholder
            llaves_primarias=((1, 2, 3),)#asi se escribe una tupla
            cursor.execute(sentencia, llaves_primarias)#De esta manera ejecutamos la setencia
            registros = cursor.fetchall()#Recuperamos todos los registros que sera una lista
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
