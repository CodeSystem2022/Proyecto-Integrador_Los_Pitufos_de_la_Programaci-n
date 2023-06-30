import psycopg2 #Esto es para poder conectarnos a Postgre
#Crear registros
conexion= psycopg2.connect(
    user= 'postgres',
    password= 'admi',
    host='127.0.0.1',
    port='5432',
    database='test_basesdatos'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1, 2)' #Placeholder
            llaves_primarias=((1, 2, 3),)#asi se escribe una tupla
            cursor.execute(sentencia, llaves_primarias)#De esta manera ejecutamos la setencia
            registros = cursor.fetchall()#Recuperamos todos los registros que sera una lista
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()