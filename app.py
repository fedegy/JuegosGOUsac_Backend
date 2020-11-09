from flask import Flask, request, jsonify
from flask_cors import CORS
from usuarios import usuarios
from juegos import juegos
from funciones_usuarios import funciones_usuario
from funciones_juegos import funciones_juegos

app = Flask(__name__)
CORS(app)

lista_juegos=[]
lista_juegos=funciones_juegos()
administrador= funciones_usuario()
administrador.nuevo_usuario('Administrador','Maestro', 'admin','admin')
lista_juegos.nuevo_juego('Animal Croosing New Horizons','2020','$ 60.00','Simulación','Aventura','','https://media.vandal.net/t200/65557/animal-crossing-new-horizons-202011012375667_1.jpg','https://todasgamers.com/wp-content/uploads/2020/02/BANNER-TEST-AC.png','Animal Croosing New Horizons es un videojuego de simulación desarrollado y publicado por Nintendo para la consola Nintendo Switch, lanzado el 20 de marzo de 2020. Es la novena entrega de la saga Animal Croosing, el jugador asume el papel de un personaje personalizable que se moviliza en una isla desierta, esto tras comprarle un pack de vacaciones a Tom Nool.')
lista_juegos.nuevo_juego('Mario Kart 8 Deluxe','2017','$ 60.00','Carreras','Simulación','','https://media.vandal.net/m/45256/mario-kart-8-deluxe-201742811181_45.jpg','https://todasgamers.com/wp-content/uploads/2017/07/mario-kart-deluxe-8.png','Mario Kart 8 Deluxe es la nueva versión del juego de carreras más popular, originalmente lanzado para Wii U y ahora para Nintendo Switch. Desarrollado por Nintendo, es la undécima entrega de la serie Mario Kart, lanzado el 28 de abril de 2017. Contiene modos de juegos entre ellos, Grand Prix, Contrarreloj, Carrera VS, Multijugador y modo Batalla.')
lista_juegos.nuevo_juego('Super Smash Bros Ultimate','2018','$ 60.00','Lucha','Plataformas','Crossover','https://media.vandal.net/t200/58489/super-smash-bros-ultimate-2018112212474987_1.jpg','https://www.gameinformer.com/sites/default/files/styles/full/public/2018/07/10/73c738be/smashbrosultimatebanner.jpg','Super Smash Bros Ultimate es un videojuego de lucha de la serie Super Smash Bross, desarrollado por Bandai Namco Games y Sora Ltd y publicado por Nintendo. Fue lanzado el 7 de diciembre de 2018 para la consola Nintendo Switch. Presenta varios luchadores de diferentes franquicias haciendo al juego más divertido, entr ellas Mario, Metroid, Sonic the Hedgehog, Pac-Man, Solid Snake y Mega Man.')
lista_juegos.nuevo_juego('Fifa 2021','2015','150.50','Accion','Aventura','','https://media.vandal.net/t200/86853/fifa-21-202092911423764_1.jpg','https://juntozstgsrvproduction.blob.core.windows.net/cms-images/1940x470_banner%20fifa%202021%20%20version%20desktop_%2029877.jpg','Es un Juego')
lista_juegos.nuevo_juego('Plantas vs Zombies Garden Warfare 2','2015','150.50','Accion','Aventura','','https://media.vandal.net/t200/31447/plants-vs-zombies-garden-warfare-2-20162258593_1.jpg','https://assets.vg247.com/current//2013/12/plants_vs_zombies_garden_warfare.jpg','Es un Juego')
lista_juegos.nuevo_juego('Watch Dogs Legion','2015','150.50','Accion','Aventura','','https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/cover_290x414/public/media/image/2020/02/watch-dogs-legion-portada-ficha-1866043.jpg?itok=9QL6djQC','https://www.beahero.gg/wp-content/uploads/2020/07/watchdogs-legion-hero-banner-01-ps4-us-10jun19.jpg','Es un Juego')
lista_juegos.nuevo_juego('Rare Replay','2015','150.50','Accion','Aventura','','https://media.vandal.net/t200/31611/rare-replay-201584121134_1.jpg','https://www.elotrolado.net/w/images/d/d8/RARE_Replay_Banner.jpg','Es un Juego')
lista_juegos.nuevo_juego('Call of Duty Black Ops IV','2015','150.50','Accion','Aventura','','https://media.vandal.net/t200/57391/call-of-duty-black-ops-iiii-20181012104839_1.jpg','https://www.ubergizmo.com/wp-content/uploads/2018/05/call-of-duty-black-ops-4.jpg','Es un Juego')

@app.route('/login', methods=['POST'])
def login():

    if request.method == 'POST':
        result= {}
        usuario_admin = request.form.get('usuario_admin')
        contra_admin = request.form.get('contra_admin')

        usuario =administrador.autenticar(usuario_admin,contra_admin)

        if usuario is not False:
            result["res"] = 1
            return result
        return result


@app.route('/registrar_usuarios',methods=['POST'])
def registro_Usuarios():

    if request.method =='POST':
        result2={}
        nombre_get=request.form.get('nombre_usuarioget')
        apellido_get=request.form.get('apellido_usuarioget')
        usuario_get=request.form.get('usuario_adminget')
        contra_get=request.form.get('contra_get')

        nuevo=administrador.nuevo_usuario(nombre_get,apellido_get,usuario_get,contra_get)
        if nuevo is not False:
            result2["guardado"]=1
            return result2
        result2["guardado"]=0
        return result2

@app.route('/crear_nuevo_videojuego',methods=['POST'])
def crear_juego():

    if request.method =='POST':
        crear_juego={}
        nombre_juego=request.form.get('nombre_juegoget')
        anio_juego=request.form.get('anio_juegoget')
        precio_juego=request.form.get('precio_juegoget')
        categoria1_juego=request.form.get('categoria1_juegoget')
        categoria2_juego=request.form.get('categoria2_juegoget')
        categoria3_juego=request.form.get('categoria3_juegoget')
        imagen_juego=request.form.get('foto_juegoget')
        baner_juego=request.form.get('baner_juegoget')
        desc_juego=request.form.get('desc_juegoget')

        juegoCreado=lista_juegos.nuevo_juego(nombre_juego,anio_juego,precio_juego,categoria1_juego,categoria2_juego,categoria3_juego,imagen_juego,baner_juego,desc_juego)
        if juegoCreado is not False:
            crear_juego['juegocreado']=1
            return crear_juego
        crear_juego['juegocreado']=0
        return crear_juego

@app.route('/cargar_usuarios')
def usuarios_json():
    return administrador.mostrar_usuario()

@app.route('/recuperar_contrasena')
def recuperar():

    recuperado=str(request.args.get("usuario",None))
    contrasena = administrador.recuperar_contra(recuperado)
    
    if contrasena is not None:
        return {
            'contra': 1,
            'usuario':recuperado,
            'recuperar': contrasena
        }
    else:
        return {
            'contra': 0,
            'usuario':recuperado,
            'recuperar': 'No se encuentra el usuario'
        }

@app.route('/busqueda_de_juegos')
def buscar_juegoCategoria():
    
    buscarjuego=str(request.args.get("categoria1",None))
    juego_buscado=lista_juegos.buscar_juego(buscarjuego)
    
    if juego_buscado is not None:
        return { 
            'estado2':1,
            'categoria1': buscarjuego,
            'buscado': juego_buscado
        }
    else:
        return{
            'estado2':0,
            'categoria1': buscarjuego,
            'buscado': 'No se encuentra el Videojuego'
        }

@app.route('/editar_juegos',methods=['POST'])
def editar_juegos():
    if request.method=='POST':
        editar_juego={}
        id_mod=int(request.form.get('idjuego_modget'))
        nombre_mod=request.form.get('nombrejuego_modget')
        anio_mod=request.form.get('anio_modget')
        precio_mod=request.form.get('precio_modget')
        categoria1_mod=request.form.get('categoria1_modget')
        categoria2_mod=request.form.get('categoria2_modget')
        categoria3_mod=request.form.get('categoria3_modget')
        imagen_mod=request.form.get('foto_modget')
        baner_mod=request.form.get('baner_modget')
        desc_mod=request.form.get('desc_modget')

        mod_juego=lista_juegos.editar_juegos(id_mod,nombre_mod,anio_mod,precio_mod,categoria1_mod,categoria2_mod,categoria3_mod,imagen_mod,baner_mod,desc_mod)

        if mod_juego is not False:
            editar_juego["modificado"]=1
            return editar_juego
        editar_juego["modificado"]=0
        return editar_juego

@app.route('/eliminar_juego',methods=['POST','DELETE'])
def eliminar_juego():
    if request.method=='POST':
        elimin_juego={}
        id_eliminar=int(request.form.get('idjuego_elimget'))

        el_juego=lista_juegos.eliminar_juegos(id_eliminar)

        if el_juego is not False:
            elimin_juego["eliminado"]=1
            return elimin_juego
        elimin_juego["eliminado"]=0
        return elimin_juego


@app.route('/cargar_descripcionJuegos')
def cargar_juegos():

    id_juego = int(request.args.get("id", None))
    cargar_juegos = lista_juegos.cargar_codigo(id_juego)

    if cargar is not None:
        return {
            'estado': 1,
            'id': id_juego,
            'data': cargar_juegos
        }
    else:
        return {
            'estado': 0,
            'id': id_juego,
            'data': 'El Juego no se encuentra'
        }

@app.route('/carga_masiva',methods=['POST'])
def cargar():

    if request.method=='POST':
        result_json={}
        nombre_juego=request.json['nombre_juego']
        anio=request.json['anio']
        precio=request.json['precio']
        categoria1=request.json['categoria1']
        categoria2=request.json['categoria2']
        categoria3=request.json['categoria3']
        foto=request.json['foto']
        baner=request.json['baner']
        desc=request.json['desc']

        lista_j=lista_juegos.nuevo_juego(nombre_juego,anio,precio,categoria1,categoria2,categoria3,foto,baner,desc)

        if lista_j is not False:
            result_json["json"]=1
            return result_json
        result_json["json"]=0
        return result_json


@app.route('/cargar_listajuegos')
def cargar_listajuegos():
    return lista_juegos.cargar_juegos()

@app.route("/")
def index():
    return "Backend de Pagina"


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)