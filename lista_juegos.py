class Juegos:

    def __init__(self,id,nombre_juego,anio,precio,categoria1,categoria2,categoria3,imagen,baner,desc):
        self.id=id
        self.nombre_juego=nombre_juego
        self.anio=anio
        self.precio=precio
        self.categoria1=categoria1
        self.categoria2=categoria2
        self.categoria3=categoria3
        self.imagen=imagen
        self.baner=baner
        self.desc=desc

    
    def dump(self):
        return{
            'id':self.id,
            'nombre_juego':self.nombre_juego,
            'anio':self.anio,
            'precio':self.precio,
            'categoria1':self.categoria1,
            'categoria2':self.categoria2,
            'categoria3':self.categoria3,
            'imagen':self.imagen,
            'baner':self.baner,
            'desc':self.desc
        }