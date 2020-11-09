class usuarios:

    def __init__(self,id,nombre,apellido,usuario,contra):

        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contra = contra


    def autenticar(self,usuario,contra):

        if self.usuario == usuario and self.contra == contra:
            return True
        return False

    def dump(self):
        return {

            'id': self.id,
            'nombre': self.nombre,
            'apellido':  self.apellido,
            'usuario': self.usuario,
            'contra':self.contra

        }
    
