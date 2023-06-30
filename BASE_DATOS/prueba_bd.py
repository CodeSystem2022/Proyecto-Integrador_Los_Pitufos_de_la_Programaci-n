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
            sentencia = 'SELECT * FROM HOTEL WHERE habitacion =%s' #Placeholder
            habitacion= input('Digite un numero para el habitacion: ')
            cursor.execute(sentencia, (habitacion))#De esta manera ejecutamos la setencia
            registros = cursor.fetchone()#Recuperamos todos los registros que sera una lista
            print(registros)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

#www.psycopg.org/docs/usage.html