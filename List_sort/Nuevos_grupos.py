import pandas as pd
import numpy as np

#Nombre de archivo - en el mismo folder
Listado = "Lista1.xlsx"

#Cargando archivo
est_df = pd.read_excel(Listado,sheet_name='Hoja1',header=0)
est_df.dropna() # removiendo filas vacias o NaN

n_ests = len(est_df)
n_part = 3 # numero de integrantes
n_grups = n_ests // n_part
n_sobra = n_ests % n_part
print('numero de grupos: ' + str(n_grups))
print('sobran: ' + str(n_sobra))

# formando cada grupo
estudiantes = est_df #copiando el dataframe ???
grupos = [] # lista de los grupos
sh_nomb = []
for g in range(0,n_grups):
    part = estudiantes.sample(n = n_part)
    part_codes = part['CODIGO']
    # retira la muestra del dataframe
    for e in part_codes:
        estudiantes = estudiantes[estudiantes['CODIGO'] != e]
    grupos.append(part)
    sh_nomb.append('grupo_' + str(g+1))


writer = pd.ExcelWriter(r"Out2.xlsx")
_ = [A.to_excel(writer,sheet_name="{0}".format(sh_nomb[i]),index=False) for i, A in enumerate(grupos)]
writer._save()
