# === IMPORTS === #
import pandas as pd
import sqlite3
from pathlib import Path

# === PATHS === #
BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "outputs"


def load_csv(csv_path, db_path=OUT_DIR / 'students.db', table='students_grades'):
    """
    Guardar CSV en una base de datos SQlite
    
    Args:
    csv_path: ruta del archivo csv
    db_path: ruta de la base de datos
    table: nombre tabla de la base de datos
    """

    try:
        #Leer el csv
        df = pd.read_csv(csv_path)

        print(f'\n CSV cargado: {len(df)} filas, {len(df.columns)} columnas \n')
        print(f'Columnas: {list(df.columns)}')

        #Conectar con la base de datos
        connect = sqlite3.connect(db_path)

        #Guardar el DataFrame en la base de datos
        #if_exists = 'replace' -> sobreescrible la tabla si existe
        #if_exists = 'append' -> añade los datos si la tabla existe

        df.to_sql(table, connect, if_exists='replace', index=False)

        print(f"\n✓ Datos guardados en la base de datos '{db_path}'\n")
        print(f"Tabla: {table}")

        #Verificar que se guardo correctamente
        cursor = connect.cursor()
        cursor.execute(f'SELECT COUNT(*) FROM {table}')
        count = cursor.fetchone()[0]
        print(f'\nRegistros en la tabla: {count}')

        connect.close()
        '''
        connect = sqlite3.connect('estudiantes.db')
        df = pd.read_sql_query("SELECT COUNT(*) as total FROM estudiantes", connect)
        count = df['total'][0]
        connect.close()
        print(f"Registros: {count}")
        '''
        return True
    
    except FileNotFoundError as e:
        print(f'Error: {e}')
        return False
    except Exception as e:
        print(f'Error: {e}')
        return False