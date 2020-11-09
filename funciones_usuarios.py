from usuarios import usuarios
import json


class funciones_usuario:

    def __init__(self):
        self.usuarios = []
        self.cantidadUsuarios = 0

    def nuevo_usuario(self,nombre,apellido,usuario_admin,contra_admin):
        self.usuarios.append(usuarios(self.cantidadUsuarios ,nombre,apellido,usuario_admin,contra_admin))
        self.cantidadUsuarios  += 1
        return True

    def mostrar_usuario(self):
        return json.dumps([usuario.dump() for usuario in self.usuarios])

    def autenticar(self,usuario_admin,contra_admin):
        for usuario in self.usuarios:
            if usuario.autenticar(usuario_admin,contra_admin) == True:                
                return usuario
        return False

    def recuperar_contra(self,usuario_admin):
        for usuario_contra in self.usuarios:
            if usuario_contra.usuario==usuario_admin:
                return usuario_contra.dump()
        
        return None
