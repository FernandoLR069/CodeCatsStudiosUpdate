import pyodbc
from django.conf import settings

def get_db_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={settings.DATABASES['default']['HOST']};"
        f"DATABASE={settings.DATABASES['default']['NAME']};"
        f"UID={settings.DATABASES['default']['USER']};"
        f"PWD={settings.DATABASES['default']['PASSWORD']};"
    )
    return pyodbc.connect(conn_str)

def sp_crear_mensaje(nombres, telefono, correo, mensaje):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("{CALL spCrearMensaje (?, ?, ?, ?)}", (nombres, telefono, correo, mensaje))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()


def sp_ver_mensajes():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("EXEC spVerMensajes")
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()
        conn.close()


def sp_ver_mensaje_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("EXEC spVerMensajeId @id=?", id)
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()
        conn.close()


def sp_eliminar_mensaje(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("EXEC spEliminarMensaje @id=?", id)
        conn.commit()
    finally:
        cursor.close()
        conn.close()

