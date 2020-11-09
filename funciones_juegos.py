from juegos import juegos
import json

class funciones_juegos:

    def __init__(self):
        self.lista_juegos=[]
        self.cantidadJuegos=0
        self.id=0
        self.resultado=0

    def nuevo_juego(self,nombre_juego,anio,precio,categoria1,categoria2,categoria3,imagen,baner,desc):
        self.lista_juegos.append(juegos(self.cantidadJuegos,nombre_juego,anio,precio,categoria1,categoria2,categoria3,imagen,baner,desc))
        self.cantidadJuegos  += 1
        return True

    def cargar_codigo(self,id):
        for juego in self.lista_juegos:
            if juego.id==id:
                return juego.dump()    
        return None

    def cargar_juegos(self):
        return json.dumps([juegos.dump() for juegos in self.lista_juegos])

    def buscar_juego(self,categoria1_juego):
        for buscar_juego in self.lista_juegos:
            if buscar_juego.categoria1==categoria1_juego:
                return buscar_juego.dump()
        return None

    def editar_juegos(self,id,nombre_juego,anio,precio,categoria1,categoria2,categoria3,imagen,baner,desc):   
        try:
            for juegos_mod in self.lista_juegos:
                if juegos_mod.id==id:
                    juegos_mod.editarjuegos(id,nombre_juego,anio,precio,categoria1,categoria2,categoria3,imagen,baner,desc)
                    return True
            return False
        except ValueError:
            return "Error"

    def eliminar_juegos(self,id):
        try:
            for elim_juego in self.lista_juegos:
                if elim_juego.id==id:
                    return self.lista_juegos.remove(elim_juego)
                else:
                    self.id += 1
            return False
        except ValueError:
            return "Error"
