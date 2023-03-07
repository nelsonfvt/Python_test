import pandas as pd
import numpy as np

def process_df(kh_file,es_df,quiz):
    #Cargando resultados de Kahoot
    kh_df = pd.read_excel(kh_file, sheet_name='Final Scores',header=2)
    regs=len(kh_df)
    bns = [0.0] * regs
    kh_df.insert(3, 'Bonus', bns)
    kh_df['Player'] = kh_df['Player'].astype(str)
    kh_df['Player'] = kh_df['Player'].str.strip()
    
    # asignando 50 al podio
    kh_df.loc[kh_df['Rank'] < 4,'Bonus'] = 5.0
    #kh_df['Grade'] = kh_df['Rank'].apply(lambda x: 50 if x<4 else 0)
    
    # sacando puntajes restantes a un arreglo
    np_arr = kh_df.loc[kh_df['Rank'] > 3,'Total Score (points)'].to_numpy()
    
    # calculando percentiles
    perc = np.percentile(np_arr,[25, 50, 75])
    print('Percentiles (25 - 50 - 75):')
    print(perc)
    lim_max = kh_df.loc[kh_df['Rank'] == 3,'Total Score (points)'].to_numpy()

    # asignando notas segun percentiles
    kh_df.loc[ (kh_df['Total Score (points)'] < lim_max[0]) & (kh_df['Total Score (points)'] >= perc[2]), 'Bonus' ] =3.0
    kh_df.loc[ (kh_df['Total Score (points)'] < perc[2]) & (kh_df['Total Score (points)'] >= perc[1]), 'Bonus' ] =1.0
    kh_df.loc[ (kh_df['Total Score (points)'] < perc[1]) & (kh_df['Total Score (points)'] >= perc[0]), 'Bonus' ] =0.0
    kh_df.loc[ kh_df['Total Score (points)'] < perc[0], 'Bonus' ] =0.0

    for i in range(0,regs):
        nota = kh_df.iloc[[i]]['Correct Answers'].values[0]
        nota = nota * 10.0
        nota = nota + kh_df.iloc[[i]]['Bonus'].values[0]
        code = kh_df.iloc[[i]]['Player'].values[0]
        print('Codigo:', str(code), 'Nota: ', str(nota))
        es_df.loc[ es_df['CODIGO'] == code , quiz] = nota

    return es_df

#Rutina Principal
#archivos con Scores
file_scores = ['G1.xlsx','G2.xlsx','G3.xlsx']

#archivo listado
file_ests='PDS2023-1.xlsx'

#Quiz a asinar nota
quiz = 'Q1'

#Cargando lista de estudiantes
es_df = pd.read_excel(file_ests, sheet_name='Corte1', header=2)
es_df.dropna(subset=['CODIGO'], inplace=True) # eliminar filas vacias
#print(es_df.dtypes)
es_df['CODIGO'] = es_df['CODIGO'].astype(int)
es_df['CODIGO'] = es_df['CODIGO'].astype(str)

for i in file_scores:
    print('procesando: ', i)
    es_df = process_df(i, es_df, quiz)

print('Guandando resultado -> out.xlsx')
#print(es_df.dtypes)
es_df.to_excel('out.xlsx')