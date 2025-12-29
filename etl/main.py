from extract import extract_csv

def run_etl():

    #================================================#
    #            TODO: EXTRAER (EXTRACT)             #
    #================================================#
    
    df_students, df_grades = extract_csv()
    print(f'Archivo de estudiantes:\n {df_students}')
    print("===" * 20)
    print(f'Archivo de notas:\n {df_grades}')

    
run_etl()