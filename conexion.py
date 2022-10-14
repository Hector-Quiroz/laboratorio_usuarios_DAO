from psycopg2 import pool
from logger_base import log
import sys


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN = 1 # Minimo de conexiones
    _MAX = 5 # Maximo de conexiones
    _pool = None # Variable de pool

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None: # Si la conexion no existe entonces se ejecuta los procedimientos para su creacion
            try: # Manejo de excepciones
                cls._pool = pool.SimpleConnectionPool(cls._MIN, cls._MAX, # Asignamos la creacion del pool a nuestra variable de clase cls._pool
                                                      database=cls._DATABASE,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      host=cls._HOST
                                                      )
                log.debug(f'Creacion de POOL exitosa: {cls._pool}') # Imprimimos en consola con log la creacion exitosa del Pool
                return cls._pool # retornamos el Pool creado
            except Exception as e:
                log.error(f'Ocurrio un error: {e}') # Imprimimos el error con log.error()
                sys.exit() # En caso de no poderse crear el pool cerramos el sistema, ya que es un error del que no se puede recuperar el mismo
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn() # El método getconn() nos permite obtener un objeto conexion del Pool del conexiones
        log.debug(f'Obtencion de CONEXION exitosa: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion) # El método putconn() nos permite liberar un objeto conexion que esta siendo utilizado
        log.debug(f'La conexion fue LIBERADA: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall() # El método closeall() libera y cierra todas las conexiones del Pool de conexiones
        log.debug(f'Las conexiones fueron CERRADAS:')


# PRUEBAS
if __name__ == '__main__':
    # Conexion.obtenerPool()
    conex = Conexion.obtenerConexion()
    Conexion.liberarConexion(conex)
    conex2 = Conexion.obtenerConexion()
    conex3 = Conexion.obtenerConexion()
    Conexion.cerrarConexiones()
