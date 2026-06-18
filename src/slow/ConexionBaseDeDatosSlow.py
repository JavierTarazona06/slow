from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

import pymysql

from .paths import CONFIG_DIR


@dataclass(frozen=True)
class DatabaseSettings:
    host: str = "localhost"
    port: int = 3306
    user: str = "root"
    password: str = "root"
    db: str = "slow"


def _clean_config_value(value: str) -> str:
    return value.strip().strip(",").strip('"').strip("'")


def load_database_settings(config_path: Path = CONFIG_DIR / "database.txt") -> DatabaseSettings:
    """Load database settings from environment variables or config/database.txt."""
    values = {
        "host": os.getenv("SLOW_DB_HOST"),
        "port": os.getenv("SLOW_DB_PORT"),
        "user": os.getenv("SLOW_DB_USER"),
        "password": os.getenv("SLOW_DB_PASSWORD"),
        "db": os.getenv("SLOW_DB_NAME"),
    }

    if config_path.exists():
        for line in config_path.read_text(encoding="utf-8").splitlines():
            if "=" not in line or line.strip().startswith("#"):
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            if key in values and values[key] is None:
                values[key] = _clean_config_value(value)

    return DatabaseSettings(
        host=values["host"] or "localhost",
        port=int(values["port"] or 3306),
        user=values["user"] or "root",
        password=values["password"] or "root",
        db=values["db"] or "slow",
    )

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
        print("BD: Slow conectada")

    def abrirBasedeDatosSlow(self):
        settings = load_database_settings()
        self.conexionSlow = pymysql.connect(
            host=settings.host,
            port=settings.port,
            user=settings.user,
            password=settings.password,
            db=settings.db
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
        self.cursorSlow.execute('''
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
                GRAFICA LONGBLOB,
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
            VIA VARCHAR(200) UNIQUE,
            IMAGENVIA LONGBLOB,
            LIMITEVELOCIDAD FLOAT,
            MULTA FLOAT,
            PRIMARY KEY (IDVIA))
        ''')
        self.reiniciarBaseDeDatosSlow()

    def crearTablaVehiculos (self):
        self.cursorSlow.execute('''
            CREATE TABLE IF NOT EXISTS VEHICULOS (
                IDVEHICULO INT AUTO_INCREMENT,
                IDVIDEO INT,
                CAPTURA LONGBLOB,
                TIPOVEHICULO VARCHAR (200),
                PLACA VARCHAR (8),
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

def main():
    """Create the SLOW database tables."""
    conexionSlow = ConexionBaseDeDatosSlow()
    print(conexionSlow)
    conexionSlow.crearTablaUsuarios()
    conexionSlow.crearTablaVias()
    conexionSlow.crearTablaDeteccionYVideos()
    conexionSlow.crearTablaVehiculos()
    conexionSlow.cerrarBaseDeDatosSlow()

if __name__ == "__main__":
    main()
