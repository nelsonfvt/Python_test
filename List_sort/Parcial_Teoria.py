import pandas as pd
import numpy as np

#Rutina Principal
#archivos con Calificaciones
Parcial = 'Parcial-calificaciones.xlsx'

#archivo listado general de estudiantes
file_ests='PDS2023-1.xlsx'

#Cargando lista de estudiantes por codigo
es_df = pd.read_excel(file_ests, sheet_name='Corte1', header=2)
es_df.dropna(subset=['CODIGO'], inplace=True) # eliminar filas vacias
#print(es_df.dtypes)
es_df['CODIGO'] = es_df['CODIGO'].astype(int)
es_df['CODIGO'] = es_df['CODIGO'].astype(str)
regs = len(es_df)

#Cargando lista de estudiantes por correo
ml_df = pd.read_excel(file_ests,sheet_name='Listado', header=0)
ml_df.dropna(subset=['CODIGO'], inplace=True)
ml_df['CODIGO'] = ml_df['CODIGO'].astype(int)
ml_df['CODIGO'] = ml_df['CODIGO'].astype(str)

#Organizar lista de correos de acuerdo con los códigos
ml_df = ml_df.set_index('CODIGO')
ml_df = ml_df.reindex(index=es_df['CODIGO'])
ml_df = ml_df.reset_index()
#print(ml_df)

#Cargando calificaciones de parcial
nt_df = pd.read_excel(Parcial)
nt_df.dropna(subset=['Dirección de correo'], inplace=True)

#Organizar lista de notas de acuerdo con los correos organizados
nt_df = nt_df.set_index('Dirección de correo')
print(nt_df)
nt_df = nt_df.reindex(index=ml_df['CORREO'])
nt_df = nt_df.reset_index()

#Extraer nombres y calificaciones
out_df = nt_df[["Apellido(s)" ,"Nombre", "Calificación/50.00" ]]
#out_df['Calificación/10.00'] =  out_df['Calificación/10.00'].apply(lambda x: x*5.0)
print(out_df)
out_df.to_excel('Notas_parcial.xlsx')