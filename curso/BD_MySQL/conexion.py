import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '123456',
        db = 'condominio'
    )

    if conexion.is_connected():
        print("Conexion exitosa.")
        infoServer = conexion.get_server_info()
        print("Info del servidor:", infoServer)
except Error as ex:
    print("Error durante la conexion:", ex)

finally:
    if conexion.is_connected():
        conexion.close() #cerro la conexion de la bd.
        print("la conexion ha finalizado")