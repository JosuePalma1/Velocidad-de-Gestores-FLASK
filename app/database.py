from sqlalchemy import create_engine
from app import db
from config import Config
import time
import logging
from sqlalchemy import text
from datetime import datetime

def test_connection(db_type):
    try:
        engine = get_db_connection(db_type)
        connection = engine.connect()
        print(f"Conexión exitosa a {db_type}")
        connection.close()
        return True
    except Exception as e:
        print(f"Error de conexión a {db_type}: {str(e)}")
        return False
def get_db_connection(db_type):
    if db_type == 'mysql':
        return create_engine(Config.MYSQL_URI)
    elif db_type == 'postgres':
        return create_engine(Config.POSTGRES_URI)
    elif db_type == 'oracle':
        return create_engine(Config.ORACLE_URI)
    elif db_type == 'sqlserver':
        return create_engine(Config.SQLSERVER_URI)
    else:
        raise ValueError("Unsupported database type")

def test_connection(db_type):
    try:
        engine = get_db_connection(db_type)
        connection = engine.connect()
        connection.close()
        return True
    except:
        return False

def delete_all_products(db_type):
    engine = get_db_connection(db_type)
    try:
        with engine.connect() as connection:
            # Comenzar una transacción
            trans = connection.begin()
            try:
                # Ejecutar el DELETE con el comando correcto según el gestor
                if db_type == 'oracle':
                    connection.execute(text("DELETE FROM producto"))
                elif db_type == 'mysql':
                    connection.execute(text("DELETE FROM producto"))
                elif db_type == 'postgres':
                    connection.execute(text("DELETE FROM producto"))
                elif db_type == 'sqlserver':
                    connection.execute(text("DELETE FROM producto"))
                
                # Confirmar la transacción
                trans.commit()
                return True
            except Exception as e:
                # Si hay error, hacer rollback
                trans.rollback()
                logging.error(f"Error al eliminar registros en {db_type}: {str(e)}")
                return False
    except Exception as e:
        logging.error(f"Error de conexión en {db_type}: {str(e)}")
        return False

def insert_products_ldm(db_type, product_data, duration=5):
    engine = get_db_connection(db_type)
    start_time = time.time()
    count = 0
    try:
        # Preparar la consulta SQL según el tipo de base de datos
        if db_type == 'oracle':
            query = text("""
                INSERT INTO producto (id, descripcion, precio, fecha)
                VALUES (:id_producto, :descripcion, :precio, TO_DATE(:fecha, 'YYYY-MM-DD'))
            """)
            # Convertir los tipos de datos para Oracle
            product_data = product_data.copy()
            product_data['id_producto'] = int(product_data['id_producto'])
            product_data['precio'] = float(product_data['precio'])
        else:
            query = text("""
                INSERT INTO producto (id, descripcion, precio, fecha)
                VALUES (:id_producto, :descripcion, :precio, :fecha)
            """)

        while time.time() - start_time < duration:
            with engine.connect() as connection:
                connection.execute(query, product_data)
                connection.commit()
            count += 1
        return count
    except Exception as e:
        logging.error(f"Error en insert_products_ldm para {db_type}: {str(e)}")
        return 0

def insert_products_sp(db_type, product_data, duration=5):
    engine = get_db_connection(db_type)
    start_time = time.time()
    count = 0
    try:
        # Preparar los datos según el tipo de base de datos
        if db_type == 'oracle':
            product_data = product_data.copy()
            product_data['id_producto'] = int(product_data['id_producto'])
            product_data['precio'] = float(product_data['precio'])
            product_data['fecha'] = datetime.strptime(product_data['fecha'], '%Y-%m-%d')
            query = text("""
                BEGIN
                    PA_INSERTARPRODUCTO(:id_producto, :descripcion, :precio, :fecha);
                END;
            """)
        elif db_type == 'mysql':
            query = text("CALL PA_INSERTARPRODUCTO(:id_producto, :descripcion, :precio, :fecha)")
        elif db_type == 'postgres':
            query = text("SELECT PA_INSERTARPRODUCTO(:id_producto, :descripcion, :precio, :fecha)")
        elif db_type == 'sqlserver':
            query = text("EXECUTE PA_INSERTARPRODUCTO :id_producto, :descripcion, :precio, :fecha")

        while time.time() - start_time < duration:
            with engine.connect() as connection:
                connection.execute(query, product_data)
                connection.commit()
            count += 1
        return count
    except Exception as e:
        logging.error(f"Error en insert_products_sp para {db_type}: {str(e)}")
        return 0