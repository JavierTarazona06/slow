import pymysql

class ConexionBaseDeDatosSlow():
    '''
    4 Bases de datos para el funcionamiento de Slow más un diccionario self.recursosGraficos con claves como los nombres de las imágenes
    y los valores como las rutas de las mismas para usar en la interfaz gráfica de slow.
    Nota: Inicializar (conectar) sólo una vez ya que esta es la base de datos inicial de Slow.
    Es decir, no crear mas instancias ya que se dirige al mismo host con la base de datos slow, por lo tanto no es necesario.
    '''
    '''
    Encriptar: En Insert: values (usuario,aes_encrypt('clave','claveDeLaClave'))
    Desencriptar: En Select: SELECT aes_decrypt(clave,'claveDeLaCLave')
    '''
    def __init__(self):
        self.abrirBasedeDatosSlow()
        self.recursosGraficos = {"LOGOSLOWICO":"S:\\\RecursosGraficos\\\Logo_Slow_Icon_Map.ico",
        "LOGOSLOW":'S:\\\RecursosGraficos\\\Logo_Slow.png',
        "DEVOLVER":'S:\\\RecursosGraficos\\\DEVOLVER.png',
        "MENU":'S:\\\RecursosGraficos\\\MENU.png',
        "RECARGAR":'S:\\\RecursosGraficos\\\RECARGAR.png',
        "ELIMINAR":'S:\\\RecursosGraficos\\\ELIMINAR.png',
        "MULTA":'S:\\\RecursosGraficos\\\MULTA.png',
        "AVATAR":'S:\\\RecursosGraficos\\\AVATAR.png',
        "CANDADO":'S:\\\RecursosGraficos\\\CANDADO.png',
        "OJOCLAVECERRADO":'S:\\\RecursosGraficos\\\OJOCLAVECERRADO.png',
        "OJOCLAVEABIERTO":'S:\\\RecursosGraficos\\\OJOCLAVEABIERTO.png',
        "TARJETADOCUMENTO":'S:\\\RecursosGraficos\\\TARJETADOCUMENTO.png',
        "CORREO":'S:\\\RecursosGraficos\\\CORREO.png',
        "ROL":'S:\\\RecursosGraficos\\\ROL.png',
        "CLAVE":'S:\\\RecursosGraficos\\\CLAVE.png',
        "POLICIA":'POLICIA NACIONAL',
        "ESCUDOPOLICIA":'S:\\\RecursosGraficos\\\ESCUDOPOLICIA.png',
        "PAIS":'REPÚBLICA DE COLOMBIA',
        "BANDERAPAIS":'S:\\\RecursosGraficos\\\BANDERAPAIS.png',
        "INFORMACION":'S:\\\RecursosGraficos\\\INFORMACION.png',
        "ACTUALIZARDATOS":'S:\\\RecursosGraficos\\\ACTUALIZARDATOS.png',
        "REGISTRARVIDEOS":'S:\\\RecursosGraficos\\\REGISTRARVIDEOS.png',
        "VEHICULOSVIAS":'S:\\\RecursosGraficos\\\VEHICULOSVIAS.png',
        "HISTORICO":'S:\\\RecursosGraficos\\\HISTORICO.png',
        "PERFILDEFECTO":'S:\\\RecursosGraficos\\\PERFILDEFECTO.png',
        "VIADEFECTO":'S:\\\RecursosGraficos\\\VIADEFECTO.png'}
        print("BD: Slow conectada")

    def abrirBasedeDatosSlow(self):
        self.conexionSlow = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            db="slow"
        )
        self.cursorSlow = self.conexionSlow.cursor()
        print("BBDD: Slow Abierta Exitosamente")

    def __str__(self):
        self.infoServidor = self.conexionSlow.get_server_info()
        self.cursorSlow.execute("SELECT DATABASE()")
        self.bd = self.cursorSlow.fetchone()
        return f"Información del servidor: {self.infoServidor}. Base de Datos: {self.bd}"

    def eliminarTabla(self,tabla):
            self.cursorSlow.execute(f"DROP TABLE {tabla}")

    def crearTablaUsuarios(self):
        self.cursorSlow.execute = ('''
            CREATE TABLE IF NOT EXISTS USUARIOS (
            IDUSUARIO INT AUTO_INCREMENT,
            USUARIO VARCHAR(200) UNIQUE,
            CLAVE LONGBLOB,
            NOMBRE VARCHAR(150),
            APELLIDO VARCHAR(150),
            TIPODOCUMENTO ENUM ('C.C','C.E','T.P'),
            NUMERODOCUMENTO BIGINT UNIQUE,
            IMAGENPERFIL LONGBLOB,
            TIPOSANGRE ENUM ('A+','A-','B+','B-','AB+','AB-','O+','O-'),
            JEFE INT,
            POLICIASASIGNADOS TEXT,
            ASIGNACION VARCHAR(150) DEFAULT 'TRÁNSITO',
            ROL ENUM ('JEFE','POLICIA'),
            NUMEROCUADRANTE INT,
            CUADRANTE VARCHAR(150),
            CIUDAD VARCHAR(200),
            DEPARTAMENTO VARCHAR(200),
            HORARIO VARCHAR(100),
            ESTADO ENUM ('ACTIVO','DESACTIVADO'),
            DIRECCION TEXT,
            CELULAR BIGINT,
            CORREO VARCHAR(200),
            FONDO ENUM ('CLARO','OSCURO'),
            PRIMARY KEY (IDUSUARIO)
            )
        ''')
        self.reiniciarBaseDeDatosSlow()

    def crearTablaDeteccionYVideos(self):
        self.cursorSlow.execute('''
            CREATE TABLE IF NOT EXISTS DETECCIONYVIDEOS (
                IDVIDEO INT AUTO_INCREMENT,
                IDUSUARIO INT,
                VIDEO TEXT,
                IDVIA INT,
                CIUDAD VARCHAR (200),
                DIRECCION TEXT,
                FECHA DATE,
                PRIMARY KEY (IDVIDEO),
                CONSTRAINT FK_IDUSUARIO2 FOREIGN KEY (IDUSUARIO) REFERENCES USUARIOS (IDUSUARIO),
                CONSTRAINT FK_IDVIA FOREIGN KEY (IDVIA) REFERENCES VIAS (IDVIA)
            )
        ''')
        self.reiniciarBaseDeDatosSlow()

    def crearTablaVias(self):
        self.cursorSlow.execute('''
        CREATE TABLE IF NOT EXISTS VIAS(
            IDVIA INT AUTO_INCREMENT,
            VIA VARCHAR (200) UNIQUE,
            IMAGENVIA LONGBLOB,
            LIMITEVELOCIDAD FLOAT,
            IDUSUARIO INT,
            MULTA FLOAT,
            PRIMARY KEY (IDVIA),
            CONSTRAINT FK_IDUSUARIO FOREIGN KEY (IDUSUARIO) REFERENCES USUARIOS (IDUSUARIO))
        ''')
        self.reiniciarBaseDeDatosSlow()

    def crearTablaVehiculos (self):
        self.cursorSlow.execute('''
            CREATE TABLE IF NOT EXISTS VEHICULOS (
                IDVEHICULO INT AUTO_INCREMENT,
                IDVIDEO INT,
                CAPTURA LONGBLOB,
                TIPOVEHICULO VARCHAR (200),
                PLACA VARCHAR (8) UNIQUE,
                VELOCIDAD FLOAT,
                IDVIA INT,
                VELOCIDADEXCEDIDA BOOLEAN,
                MULTA FLOAT,
                IDUSUARIO INT,
                PRIMARY KEY (IDVEHICULO),
                CONSTRAINT FK_IDUSUARIO3 FOREIGN KEY (IDUSUARIO) REFERENCES USUARIOS (IDUSUARIO),
                CONSTRAINT FK_IDVIA2 FOREIGN KEY (IDVIA) REFERENCES VIAS (IDVIA),
                CONSTRAINT FK_IDVIDEO FOREIGN KEY (IDVIDEO) REFERENCES DETECCIONYVIDEOS (IDVIDEO)
            )
        ''')
        self.reiniciarBaseDeDatosSlow()

    def cerrarBaseDeDatosSlow(self):
        self.conexionSlow.commit()
        self.cursorSlow.close()
        self.conexionSlow.close()
        print("BBDD: Slow Cerrada Exitosamente")

    def reiniciarBaseDeDatosSlow(self):
        self.cerrarBaseDeDatosSlow()
        self.abrirBasedeDatosSlow()

    def prueba(self):
        self.cursorSlow.execute('''
        CREATE TABLE IF NOT EXISTS PRUEBA (
            USUARIO INT AUTO_INCREMENT,
            CLAVE LONGBLOB,
            HOBBY VARCHAR (200) NOT NULL,
            PRIMARY KEY (USUARIO)
        )
        ''')
        self.reiniciarBaseDeDatosSlow()
        #self.cursorSlow.execute("INSERT INTO PRUEBA (CLAVE,HOBBY) VALUES (aes_encrypt('tenis','clave'),'tenis')")
        self.cursorSlow.execute("SELECT USUARIO, aes_decrypt(CLAVE,'clave'),HOBBY FROM PRUEBA")
        lista = self.cursorSlow.fetchall()
        for i in lista:
            print(i)

def main():
    conexionSlow = ConexionBaseDeDatosSlow()
    print(conexionSlow)
    conexionSlow.crearTablaUsuarios()
    conexionSlow.crearTablaDeteccionYVideos()
    conexionSlow.crearTablaVias()
    conexionSlow.crearTablaVehiculos()
    conexionSlow.cerrarBaseDeDatosSlow()

main()

#conexionSlow = ConexionBaseDeDatosSlow()
#conexionSlow.cursorSlow.execute('''INSERT INTO USUARIOS (
            #USUARIO,CLAVE,NOMBRE,APELLIDO,TIPODOCUMENTO,NUMERODOCUMENTO,
#            IMAGENPERFIL,TIPOSANGRE,JEFE,POLICIASASIGNADOS,ASIGNACION,ROL,
#            NUMEROCUADRANTE,CUADRANTE,CIUDAD,DEPARTAMENTO,HORARIO,ESTADO,
#            DIRECCION,CELULAR,CORREO,FONDO
 #      ) VALUES (
  #          'prueba',AES_ENCRYPT('prueba','clave'),'PRUEBA','PRUEBA','C.C',1,
  #          'IMAGENPERFIL','O+','1','POLICIA PRUEBA 1, POLICIA PRUEBA 2','TRÁNSITO','POLICIA',
  #          1,'CUADRANTE CENTRAL','BOGOTÁ','BOGOTÁ D.C','7:00 - 12:00 Y 14:00 A 18:000','ACTIVO',
  #          'CRA 60 NO. 4725 BRR. MARAVILLA CASA 2',3333333333,'prueba@prueba.com','CLARO'
  #      )''')
#conexionSlow.cerrarBaseDeDatosSlow()