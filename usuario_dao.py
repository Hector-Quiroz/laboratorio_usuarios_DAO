'''
Las consultas (queries) deben estar bien escritas y los parametros posicionales/comodines (placeholders) igualmente para que to-do funcione
La estructura de la mayoria de los métodos DAO es bastante parecida, solo hay que ajustar la variable de valores a el orden los parametros y cambiar la consulta
'''

from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario


class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username = %s, password = %s WHERE id_usuario  = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
            print('Impresion exitosa'.center(50, '-'))
        except Exception as e:
            log.error(f'Ocurrio un error: {e}')

    @classmethod # La estr
    def insertar(cls, usuario):
        try:
            with CursorDelPool() as cursor:
                valores = (usuario.username, usuario.password)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Registros insertados: {cursor.rowcount}')
                print('Insercion exitosa'.center(50, '-'))
        except Exception as e:
            log.error(f'Ocurrio un error-----: {e}')

    @classmethod
    def actualizar(cls, usuario):
        try:
            with CursorDelPool() as cursor:
                valores = (usuario.username, usuario.password, usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Usuario actualizado: {usuario}')
                log.debug(f'Registros insertados: {cursor.rowcount}')
                print('Actualizacion exitosa'.center(50, '-'))
        except Exception as e:
            log.error(f'Ocurrio un error <-----: {e}')

    @classmethod
    def eliminar(cls, usuario):
        try:
            with CursorDelPool() as cursor:
                valores = (usuario.id_usuario,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Usuario ELIMINADOS: {usuario}')
                log.debug(f'Registros insertados: {cursor.rowcount}')
                print('Eliminacion exitosa'.center(50, '-'))

        except Exception as e:
            log.error(f'Ocurrio un error <-----: {e}')

# PRUEBAS
# if __name__ == '__main__':
# ELIMINAR
# usu = Usuario(id_usuario=5)
# UsuarioDAO.eliminar(usu)

# ACTUALIZAR
# usu = Usuario(username='Aquiles', password='654', id_usuario=5)
# UsuarioDAO.actualizar(usu)

# INSERTAR
# usu = Usuario(username='Grecia', password='456')
# UsuarioDAO.insertar(usu)

# SELECCIONAR
# UsuarioDAO.seleccionar()
