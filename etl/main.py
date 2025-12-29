from extract import extract_csv
from transform import id_verify
def run_etl():

    #================================================#
    #            TODO: EXTRAER (EXTRACT)             #
    #================================================#
    
    df_students, df_grades = extract_csv()
    print(f'Archivo de estudiantes:\n {df_students}')
    print("===" * 20)
    print(f'Archivo de notas:\n {df_grades}')

    #================================================#
    #            TODO: TRANSFORM (VALIDATE)          #
    #================================================#

    print(f'\nComprobando id en los archivos...\n')
    id_valido, id_novalido = id_verify(df_students, df_grades)

    print(id_valido, id_novalido)

run_etl()