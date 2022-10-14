# Implementacion de toda la vida de una clase POO

class Usuario:
    def __init__(self, id_usuario = None, username = None, password = None): # Es importante colocar los parametros de esta forma ya que no siempre se mandaran todos ellos
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'ID usuario: {self._id_usuario} | Usuario: {self._username} | Contraseña: {self._password}'

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @id_usuario.setter
    def id_usuario(self, nuevoID):
        self._id_usuario = nuevoID

    @username.setter
    def username(self, nuevoUsername):
        self._username = nuevoUsername

    @password.setter
    def password(self, nuevaPassword):
        self._password = nuevaPassword