import pandas as pd
import numpy as np

#Cargar lista de estudiantes por codigo
ests_file = 'PDS2022-2.xlsx'
ests_df = pd.read_excel(ests_file,sheet_name = 'Listado', header=1)
ests_df.dropna(subset = ['CODIGO'], inplace = True)
ests_df.drop(ests_df.columns[[4 ,5]], axis=1, inplace=True)
ests_df['CODIGO'] = ests_df['CODIGO'].astype(int)
ests_df['CODIGO'] = ests_df['CODIGO'].astype(str)
#print(ests_df['CODIGO'])

n_temas = 4 #primer corte
n_ests = len(ests_df)
n_part = 5
n_grups = n_ests // n_part
n_sobra = n_ests % n_part
print('numero de grupos: ' + str(n_grups))
print('numero de estudiantes sobrantes: ' + str(n_sobra))


estudiantes = ests_df
grupos = []
sh_nomb = []
# formando cada grupo
for g in range(0,n_grups):
    part = estudiantes.sample(n = n_part)
    part_codes = part['CODIGO']
    for e in part_codes:
        estudiantes = estudiantes[estudiantes['CODIGO'] != e]
    grupo = part
    grupos.append(grupo)
    sh_nomb.append('grupo_' + str(g+1))

writer = pd.ExcelWriter(r"Out2.xlsx")
_ = [A.to_excel(writer,sheet_name="{0}".format(sh_nomb[i])) for i, A in enumerate(grupos)]
writer.save()