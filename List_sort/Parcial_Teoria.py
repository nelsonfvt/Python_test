import pandas as pd
import numpy as np

#Rutina Principal
#archivos con Calificaciones
Parcial = 'Parcial-calificaciones.xlsx'

#archivo listado general de estudiantes
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

#Organizar lista de correos de acuerdo con los códigos
ml_df = ml_df.set_index('Codigo')
ml_df = ml_df.reindex(index=es_df['Codigo'])
ml_df = ml_df.reset_index()

#Organizar lista de notas de acuerdo con los correos organizados
nt_df = nt_df.set_index('Dirección de correo')
nt_df = nt_df.reindex(index=ml_df['Dirección de correo'])
nt_df = nt_df.reset_index()

#Extraer nombres y calificaciones
out_df = nt_df[["Apellido(s)" ,"Nombre", "Calificación/10.00" ]]
out_df['Calificación/10.00'] =  out_df['Calificación/10.00'].apply(lambda x: x*5.0)
print(out_df)
out_df.to_excel('Notas_parcial.xlsx')