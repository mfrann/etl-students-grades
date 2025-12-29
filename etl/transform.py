'''
#TODO: Transformar y limpiar archivos
#TODO: LIMPIAR NOMBRES Y CIUDADES
#TODO: RELLENAR EDADES FALTANTES CON EL PROMEDIO
#TODO: UNIR ESTUDIANTES + NOTAS
#TODO: CALCULAR: PROMEDIO POR ESTUDIANTE / ESTADO(APROBADO/DESAPROBADO)

'''

# === LIBRERIAS === #

import pandas as pd
# ================= #

#================================================#
#                  TRANSFORM                     #
#================================================#

#todo: validar si las id existen 

def id_verify(df_students, df_grades):
    grades_id = set(df_grades['student_id'])

    valid_id = df_students['student_id'].isin(grades_id)

    id_valido = df_students[valid_id].copy()
    id_novalido = df_students[~valid_id].copy()

    if not id_valido.empty:
        print("La id si existe.\n")
    else:
        print("La id no existe o es incorrecta\n")
    return id_valido, id_novalido

