import pandas as pd
import numpy as np

#Rutina Principal
#archivos con Scores
Parcial = 'Parcial-calificaciones.xlsx'

#archivo listado
file_ests='PDS2022-1.xlsx'

#Cargando lista de estudiantes por codigo
es_df = pd.read_excel(file_ests, sheet_name='Corte1', header=1)
es_df.dropna(subset=['Codigo'], inplace=True) # eliminar filas vacias
#print(es_df.dtypes)
es_df['Codigo'] = es_df['Codigo'].astype(int)
es_df['Codigo'] = es_df['Codigo'].astype(str)
regs = len(es_df)

#Cargando lista de estudiantes por correo
ml_df = pd.read_excel(file_ests,sheet_name='Listado', header=1)
ml_df.dropna(subset=['Codigo'], inplace=True)
ml_df['Codigo'] = ml_df['Codigo'].astype(int)
ml_df['Codigo'] = ml_df['Codigo'].astype(str)

#Cargando calificaciones de parcial
nt_df = pd.read_excel(Parcial)

es_df['Ex_Pr'] = es_df.loc
es_df.loc[ (ml_df['Correo'] == nt_df['Dirección de correo']) , ''] 

for i in range(0,regs):
    print('a')