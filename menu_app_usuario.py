from usuario import Usuario
from usuario_dao import UsuarioDAO

op = None

while op != 5:
    print('1) Listar usuarios')
    print('2) Agregar usuario')
    print('3) Actualizar usuario')
    print('4) Eliminar usuario')
    print('5) Salir')
    op = int(input('Ingrese la opcion: '))

    if op == 1:
        UsuarioDAO.seleccionar()
    elif op == 2:
        user = input('Ingrese el usuario: ')
        pas = input('Ingrese la contraseña: ')
        obj = Usuario(username=user, password=pas)
        UsuarioDAO.insertar(obj)
    elif op == 3:
        id = int(input('Ingrese el ID: '))
        user = input('Ingrese el usuario: ')
        pas = input('Ingrese la contraseña: ')
        obj = Usuario(username=user, password=pas, id_usuario=id)
        UsuarioDAO.actualizar(obj)
        print('')
    elif op == 4:
        id = int(input('Ingrese el ID: '))
        obj = Usuario(id_usuario=id)
        UsuarioDAO.eliminar(obj)
