'''
#TODO: Transformar y limpiar archivos
#TODO: VALIDAR SI LAS ID EXISTEN  ---COMPLETADO
#TODO: LIMPIAR NOMBRES Y CIUDADES ---COMPLETADO
#TODO: RELLENAR EDADES FALTANTES CON EL PROMEDIO --COMPLETADO
#TODO: UNIR ESTUDIANTES + NOTAS
#TODO: CALCULAR: PROMEDIO POR ESTUDIANTE / ESTADO(APROBADO/DESAPROBADO)

'''

# === LIBRERIAS === #
import pandas as pd
# ================= #

#================================================#
#                  TRANSFORM                     #
#================================================#

# VALIDAR SI LAS ID EXISTEN:
def id_verify(df_students, df_grades):
    grades_id = set(df_grades['student_id'])

    valid_id = df_students['student_id'].isin(grades_id)

    id_valido = df_students[valid_id].copy()
    id_novalido = df_students[~valid_id].copy()

    if not id_valido.empty:
        print(f'La id {id_valido} \nsi existe.\n')
    else:
        print("La id no existe o es incorrecta\n")
    return id_valido, id_novalido

#LIMPIAR NOMBRES, CIUDADES, EDADES
def clean_city_name(df):
    print(f'\n--- Limpiando datos vacios en columna CITY/NAME/AGE ---\n')


    #Ver si hay elemento nulo y reemplazar por valor 'No especifica ciudad'
    df['city'] = df['city'].fillna('Sin ciudad')
    df['name'] = df['name'].fillna('Sin nombre')
    df['age'] = df['age'].fillna(df['age'].mean()).astype(int)
    
    #Primero vamos a transformar todo el nombre de ciudad a una sola forma.
    #Si el nombre es pura mayuscula o minuscula, lo llevaremos a Esta Forma.
    df['city'] = df['city'].astype(str).str.title() # --> Capitaliza cada palabra en esa columna
    df['name'] = df['name'].astype(str).str.title()
    df['age'] = df['age'].astype(int)
    return df

#UNIR ESTUDIANTES + NOTAS / CALCULAR PROMEDIO POR ESTUDIANTE Y ESTADO
def join_csv(df_students, df_grades):
    
    # --- CALCULAR PROMEDIO POR ESTUDIANTE
    df_average = df_grades.groupby('student_id')['grade'].mean().reset_index() #Calcula el promedio
    df_average.columns = ['student_id', 'average']

    # --- UNIMOS ESTUDIANTES CON PROMEDIOS

    df_complete = pd.merge(
        df_students,
        df_average,
        on='student_id',
        how='left'
    )    



    # --- CALCULAR EL ESTADO (APROBADO / DESAPROBADO)
    print(df_complete)

    return df_complete                   