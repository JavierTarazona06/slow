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

class DatabaseConnection:
    """MySQL connection helper for the SLOW application schema."""

    def __init__(self) -> None:
        self.open()
        print("BD: Slow conectada")

    def open(self) -> None:
        """Open a connection to the configured SLOW database."""
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

    abrirBasedeDatosSlow = open

    def __str__(self) -> str:
        self.infoServidor = self.conexionSlow.get_server_info()
        self.cursorSlow.execute("SELECT DATABASE()")
        self.bd = self.cursorSlow.fetchone()
        return f"Información del servidor: {self.infoServidor}. Base de Datos: {self.bd}"

    def drop_table(self, table: str) -> None:
        """Drop a database table by name."""
        self.cursorSlow.execute(f"DROP TABLE {table}")

    eliminarTabla = drop_table

    def create_users_table(self) -> None:
        """Create the users table if it does not exist."""
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
        self.reconnect()

    crearTablaUsuarios = create_users_table

    def create_detection_videos_table(self) -> None:
        """Create the detection/videos table if it does not exist."""
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
        self.reconnect()

    crearTablaDeteccionYVideos = create_detection_videos_table

    def create_roads_table(self) -> None:
        """Create the roads table if it does not exist."""
        self.cursorSlow.execute('''
        CREATE TABLE IF NOT EXISTS VIAS(
            IDVIA INT AUTO_INCREMENT,
            VIA VARCHAR(200) UNIQUE,
            IMAGENVIA LONGBLOB,
            LIMITEVELOCIDAD FLOAT,
            MULTA FLOAT,
            PRIMARY KEY (IDVIA))
        ''')
        self.reconnect()

    crearTablaVias = create_roads_table

    def create_vehicles_table(self) -> None:
        """Create the vehicles table if it does not exist."""
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
        self.reconnect()

    crearTablaVehiculos = create_vehicles_table

    def close(self) -> None:
        """Commit pending work and close the database connection."""
        self.conexionSlow.commit()
        self.cursorSlow.close()
        self.conexionSlow.close()
        print("BBDD: Slow Cerrada Exitosamente")

    cerrarBaseDeDatosSlow = close

    def reconnect(self) -> None:
        """Close and reopen the database connection."""
        self.close()
        self.open()

    reiniciarBaseDeDatosSlow = reconnect


ConexionBaseDeDatosSlow = DatabaseConnection


def initialize_schema() -> None:
    """Create the SLOW database tables."""
    database = DatabaseConnection()
    print(database)
    database.create_users_table()
    database.create_roads_table()
    database.create_detection_videos_table()
    database.create_vehicles_table()
    database.close()


def main() -> None:
    """CLI entry point for schema initialization."""
    initialize_schema()

if __name__ == "__main__":
    main()
