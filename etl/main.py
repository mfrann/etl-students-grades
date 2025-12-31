from extract import extract_csv
from transform import (
    id_verify,
    clean_city_name,
    join_csv
)
from tqdm import tqdm
import time
import pandas as pd

def run_etl():

    print('Comenzando con el proceso de ETL..\n')
    for i in tqdm(range(100), desc="Cargando"):
        time.sleep(0.02)
    print("===" * 20)
    #================================================#
    #            TODO: EXTRAER (EXTRACT)             #
    #================================================#
    print('--- Extrayendo los archivos CSV... ---\n')
    
    for i in tqdm(range(100), desc="Cargando"):
        time.sleep(0.02)
    
    df_students, df_grades = extract_csv()
    print('✓ Tablas cargadas correctamente\n')
    print("===" * 20)
    #================================================#
    #                TODO: TRANSFORM                 #
    #================================================#
    print('--- Comenzando proceso de transformacion... ---\n')
    for i in tqdm(range(100), desc="Cargando"):
        time.sleep(0.1)

    # --- COMPROBANDO ID VALIDA
    print(f'\n--- Comprobando id en los archivos... ---\n')
    for i in tqdm(range(100), desc="Cargando"):
        time.sleep(0.02)

    id_valido, id_novalido = id_verify(df_students, df_grades)
    #print(id_valido, id_novalido)
    print('✓ Archivos comprobados correctamente\n')
    print("===" * 20)

    # --- COMPLETANDO Y REVISANDO NULOS EN CITY/NAME
    print(f'\nCompletando los nulos en columna CITY/NAME/AGE...\n')
    for i in tqdm(range(100), desc="Cargando"):
        time.sleep(0.02)

    clean_city_name(df_students)
    print(f'Mostrando tabla limpia de estudiantes: \n{df_students}\n')
    print('✓ Archivo completado correctamente\n')
    print("===" * 20)

    # --- UNIENDO ARCHIVOS CSV
    print(f'\n--- Uniendo archivos csv... ---\n')
    for i in tqdm(range(100), desc="Cargando"):
        time.sleep(0.02)

    # --- FUNCION
    join_csv(df_students, df_grades)
    print('\n✓ Archivo unidos correctamente\n')
    print("===" * 20)

    print('\nPrograma finalizado\n')

    return df_students, df_grades

run_etl()