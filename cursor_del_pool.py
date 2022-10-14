'''
El crear el cursor en otra clase nos permite segmentar la logica lo cual es bueno para su mantenimiento.
Se sobre-escriben los métodos __enter__ (Método especial que se ejecuta de manera automatica al utilizar la clausula with) y __exit__ (Lo mismo que __enter__ pero al terminar la ejecucion de la clausula with)
Para que el manejo de la conexion sea mucha más simple al implementar las funciones desde la clase DAO (Data Access Object - Patrón de diseño)
'''

from conexion import Conexion
from logger_base import log
import sys


class CursorDelPool:

    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self): # Método de entrada al ejecutar with
        self._conn = Conexion.obtenerConexion() # Obtenemos la conexion y la asignamos a la variable de clase cls._conn
        self._cursor = self._conn.cursor() # Obtenemos nuestro cursor de nuestra conexion
        log.debug(f'Cursor generado') # Mensaje de cursor generado
        return self._cursor # Retornamos el cursor

    def __exit__(self, tipoExcepcion, valorExcepcion, detalleExcepcion): # Método de salida al ejecutar with
        log.debug('Entrando en EXIT')
        if valorExcepcion: # Si existe una excepcion entonces...
            log.error(f'Ocurrio un error: {tipoExcepcion} | {valorExcepcion} | {detalleExcepcion}') # Imprimimos la excepcion
            self._conn.rollback() # Realizamos un rollback() con nuestra conexion
        else:
            self._conn.commit() # Si no existe una excepcion entonces realizamos la transaccion sobre la base de datos
            log.debug('COMMIT realizado con exito') # Imprimos el registro movimiento en consola
        self._cursor.close() # Siempre de cierra el cursor (como todos los recursos)
        Conexion.liberarConexion(self._conn) # Liberamos la conexion


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM persona')
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
