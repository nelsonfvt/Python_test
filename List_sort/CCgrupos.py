import pandas as pd
import numpy as np
import random

#Cargar lista de estudiantes por codigo
ests_file = 'VM2022-2.xlsx'
ests_df = pd.read_excel(ests_file,sheet_name = 'Listado', header=0)
ests_df.dropna(subset = ['CODIGO'], inplace = True)
#ests_df.drop(ests_df.columns[[4 ,5]], axis=1, inplace=True)
ests_df['CODIGO'] = ests_df['CODIGO'].astype(int)
ests_df['CODIGO'] = ests_df['CODIGO'].astype(str)

temas = ['Tema 1', 'Tema 2', 'Tema 3']
rela_codes = ['1803486', '1803212', '1803264', '1803169']
print(rela_codes)

n_temas = len(temas)
n_ests = len(ests_df)
n_rel = len(rela_codes)
n_grups = n_rel
n_part = n_ests // n_grups
n_sobra = n_ests % n_grups
print('numero de participantes por grupo: ' + str(n_part))
print('y sobran: ' + str(n_sobra))

relatores = ests_df.loc[ ests_df['CODIGO'].isin(rela_codes)]

for i in rela_codes:
    ests_df = ests_df[ests_df['CODIGO'] != i]

sesion_list = []
sh_nomb = []
cont = 0

for i in temas:
    grupos_sesion = pd.DataFrame()
    estudiantes = ests_df
    for e in rela_codes:
        rel = relatores[relatores['CODIGO'] == e]
        est_sample = estudiantes.sample(n=n_part-1)
        codes = est_sample['CODIGO']
        for c in codes:
            estudiantes = estudiantes[estudiantes['CODIGO'] != c]
        grupo = pd.concat([rel,est_sample])
        grupos_sesion = pd.concat([grupos_sesion,grupo])
    sesion_list.append(grupos_sesion)
    sh_nomb.append(i)


writer = pd.ExcelWriter(r"ListaCC.xlsx")
_ = [A.to_excel(writer,sheet_name="{0}".format(sh_nomb[i])) for i, A in enumerate(sesion_list)]
writer.save()