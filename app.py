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
lista_juegos.nuevo_juego('Animal Croosing New Horizons','2020','Q714.90','Simulación','Aventura','','https://media.vandal.net/t200/65557/animal-crossing-new-horizons-202011012375667_1.jpg','https://todasgamers.com/wp-content/uploads/2020/02/BANNER-TEST-AC.png','Animal Croosing New Horizons es un videojuego de simulación desarrollado y publicado por Nintendo para la consola Nintendo Switch, lanzado el 20 de marzo de 2020. Es la novena entrega de la saga Animal Croosing, el jugador asume el papel de un personaje personalizable que se moviliza en una isla desierta, esto tras comprarle un pack de vacaciones a Tom Nook.')
lista_juegos.nuevo_juego('Mario Kart 8 Deluxe','2017','Q714.90','Carreras','Arcade','','https://media.vandal.net/m/45256/mario-kart-8-deluxe-201742811181_45.jpg','https://todasgamers.com/wp-content/uploads/2017/07/mario-kart-deluxe-8.png','Mario Kart 8 Deluxe es la nueva versión del juego de carreras más popular, originalmente lanzado para Wii U y ahora para Nintendo Switch. Desarrollado por Nintendo, es la undécima entrega de la serie Mario Kart, lanzado el 28 de abril de 2017. Contiene modos de juegos entre ellos, Grand Prix, Contrarreloj, Carrera VS, Multijugador y modo Batalla.')
lista_juegos.nuevo_juego('Super Smash Bros Ultimate','2018','Q705.00','Lucha','Plataformas','Crossover','https://media.vandal.net/t200/58489/super-smash-bros-ultimate-2018112212474987_1.jpg','https://www.gameinformer.com/sites/default/files/styles/full/public/2018/07/10/73c738be/smashbrosultimatebanner.jpg','Super Smash Bros Ultimate es un videojuego de lucha de la serie Super Smash Bross, desarrollado por Bandai Namco Games y Sora Ltd y publicado por Nintendo. Fue lanzado el 7 de diciembre de 2018 para la consola Nintendo Switch. Presenta varios luchadores de diferentes franquicias haciendo al juego más divertido, entr ellas Mario, Metroid, Sonic the Hedgehog, Pac-Man, Solid Snake y Mega Man.')
lista_juegos.nuevo_juego('Fifa 2021','2015','Q400.00','Deporte','Simulación','','https://media.vandal.net/t200/86853/fifa-21-202092911423764_1.jpg','https://juntozstgsrvproduction.blob.core.windows.net/cms-images/1940x470_banner%20fifa%202021%20%20version%20desktop_%2029877.jpg','Es un videojuego de simulación de fútbol del año 2020 para las consolas PS5, Xbox One y será el primer videojuego de la serie FIFA para Google Stadia, el jugador Kylian Mbappé fue elegido para ser la portada del FIFA 21 y como embajadores estarán Alexander-Arnold, Haaland y Jao Félix. Saldrá en octubre y las consolas de próxima generación salen a fin de año')
lista_juegos.nuevo_juego('Plantas vs Zombies Garden Warfare 2','2015','Q250.00','Accion','Aventura','','https://media.vandal.net/t200/31447/plants-vs-zombies-garden-warfare-2-20162258593_1.jpg','https://assets.vg247.com/current//2013/12/plants_vs_zombies_garden_warfare.jpg','Plantas vs Zombies: Garden Warfare 2 es la secuela del divertido título de acción multijugador protagonizado por las plantas y los zombis de PopCap Games y Electronic Arts para PC, Playstation 4 y Xbox One. Lo más divertido es que se puede jugar multijador online.')
lista_juegos.nuevo_juego('Watch Dogs Legion','2015','Q550.50','Accion','Simulación','Lucha','https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/cover_290x414/public/media/image/2020/02/watch-dogs-legion-portada-ficha-1866043.jpg?itok=9QL6djQC','https://www.beahero.gg/wp-content/uploads/2020/07/watchdogs-legion-hero-banner-01-ps4-us-10jun19.jpg','Es un videojuego perteneciente al género de acción y aventura desarrollado por Ubisoft Toronto y publicado por Ubisoft con lanzamiento oficial el 29 de octubre de 2020. Es la tercera entrega de la serie Watch Dogs y la secuela de Watch Dogs 2.')
lista_juegos.nuevo_juego('Rare Replay','2015','Q200.00','Recopilatorio','Acción','Arcade','https://media.vandal.net/t200/31611/rare-replay-201584121134_1.jpg','https://lh3.googleusercontent.com/proxy/wCHn3cZZpb52BcAg6QkFcvf-4_k6wvXBg_wzlqfujk01E8QpDiuklDJg6cElpcPM_bUr3_B3WMyvbvW1xOKDAsSFccMKHgWUJ0-Id6K66nJ56RCzVpkrKB0VtRqNj63cve_vVgnjBFUFxoY','RARE Replay es un videojuego que recopila 30 videojuegos que conmemoran los 30 años de historia de la tan conocida Rare y su predecesor Ultimate Play The Game. La compilación fue de varias ídeas que Rare consideró para celebrar su 30 aniversario. Inspirada por los fanáticos, las próximas características de compatibilidad con versiones anteriores de XBOX ONE.')
lista_juegos.nuevo_juego('Call of Duty Black Ops IV','2015','Q350.50','Disparos','Acción','','https://media.vandal.net/t200/57391/call-of-duty-black-ops-iiii-20181012104839_1.jpg','https://www.ubergizmo.com/wp-content/uploads/2018/05/call-of-duty-black-ops-4.jpg','Es un videojuego de acción en primera persona, desarollada por Treyarch y distribuido por Activisión, para las plataformas Playstation 4, Xbox One y Microsoft Windows. El videojuego es el décimo quinto título de la franquicia Call of Duty, tambiés es el cuarto título de la serie Black Ops y se ambienta después de Call of Duty: Black Ops 2 y antes de Call of Duty: Black Ops 3')

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