'''
#TODO: Extraer y leer los archivos CSV

'''

# === LIBRERIAS === #

import pandas as pd
from pathlib import Path
# ================= #

# === PATHS === #
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Funcion para leer archivo, error: si no existe el archivo 

def extract_csv():
    '''
    Docstring for extract_csv
    '''
    print('Cargando archivos...')
    
    try:
        # --- CREANDO DATAFRAMES DE CADA ARCHIVO

        df_students = pd.read_csv(DATA_DIR / 'students.csv')
        df_grades = pd.read_csv(DATA_DIR / 'grades.csv')

        print('Todos los archivos cargados correctamente.')
    except FileNotFoundError as e:
        print(f'Archivos no cargados por error: {e}')

    return df_students, df_grades

df_students, df_grades = extract_csv()
print(f'Archivo de estudiantes:\n {df_students}')
print()
print(f'Archivo de notas:\n {df_grades}')