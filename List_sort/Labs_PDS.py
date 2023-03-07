import pandas as pd

def proc_lists(lab_itm,est_df):
    kh_df = pd.read_excel(lab_itm, sheet_name='Corte2',header=1)
    kh_df.dropna(subset=['Codigo'],inplace=True)
    kh_df['Codigo'] = kh_df['Codigo'].astype(int)
    kh_df['Codigo'] = kh_df['Codigo'].astype(str)
    kh_df['Codigo'].str.strip()
    regs=len(kh_df)

    for i in range(0,regs):
        nota = kh_df.iloc[[i]]['Nota'].values[0]
        code = kh_df.iloc[[i]]['Codigo'].values[0]
        est_df.loc[ est_df['Codigo'] == code , 'Def'] = nota

    return est_df


#archivos con LABs
#file_lab = ['LAB1.xlsx','LAB2.xlsx','LAB3.xlsx']
file_lab = ['LAB1.xlsx']
#archivo listado
file_ests='PDS2022-1.xlsx'
#Quiz a asinar nota
quiz = 'LAB'

#Cargando lista de estudiantes
es_df = pd.read_excel(file_ests, sheet_name='Corte1', header=1)
es_df.dropna(subset=['Codigo'], inplace=True) # eliminar filas vacias
es_df['Codigo'] = es_df['Codigo'].astype(int)
es_df['Codigo'] = es_df['Codigo'].astype(str)
es_df['Codigo'].str.strip()


for i in file_lab:
    print('procesando: ', i)
    es_df = proc_lists(i, es_df)

print('Guandando resultado -> out_lab.xlsx')
es_df.to_excel('out_lab.xlsx')