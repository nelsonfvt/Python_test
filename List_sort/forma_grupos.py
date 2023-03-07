import pandas as pd
import numpy as np
import random

#Cargar lista de estudiantes por codigo
ests_file = 'PDS2023-1.xlsx'
#ests_file = 'VM2022-2.xlsx'
ests_df = pd.read_excel(ests_file,sheet_name = 'Listado', header=0)
ests_df.dropna(subset = ['CODIGO'], inplace = True)
#ests_df.drop(ests_df.columns[[4 ,5]], axis=1, inplace=True)
ests_df['CODIGO'] = ests_df['CODIGO'].astype(int)
ests_df['CODIGO'] = ests_df['CODIGO'].astype(str)

temas = ['Teorema de muestreo y Aliasing','Cuantificación de señales y error de cuantificación','Sistemas LTI','Función de transferencia de sistemas LTI','Aplicación de Tda Z para análisis de señales y sistemas','Análisis de Fouier para señales de tiempo discreto','DFT y FFT']
random.shuffle(temas)
print(temas)

n_temas = len(temas)
n_ests = len(ests_df)
n_part = 5
n_grups = n_ests // n_part
n_sobra = n_ests % n_part
print('numero de grupos: ' + str(n_grups))

estudiantes = ests_df
grupos = []
sh_nomb = []
cont = 0
# formando cada grupo
for g in range(0,n_grups):
    tm = pd.DataFrame([temas[cont]],columns = ['Tema'])
    cont += 1
    if cont == len(temas):
        cont = 0
    part = estudiantes.sample(n = n_part)
    part_codes = part['CODIGO']
    for e in part_codes:
        estudiantes = estudiantes[estudiantes['CODIGO'] != e]
    grupo = pd.concat([tm, part])
    grupos.append(grupo)
    sh_nomb.append('grupo_' + str(g+1))

for s in range(0, len(estudiantes)):
    grupos[s] = pd.concat([grupos[s], estudiantes.iloc[s].to_frame().transpose()]) 

writer = pd.ExcelWriter(r"Out2.xlsx")
_ = [A.to_excel(writer,sheet_name="{0}".format(sh_nomb[i])) for i, A in enumerate(grupos)]
writer.save()