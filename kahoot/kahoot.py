import pandas as pd
import numpy as np

def process_df(kh_file,es_df,quiz):
    #Cargando resultados de Kahoot
    kh_df = pd.read_excel(kh_file, sheet_name='Final Scores',header=2)
    regs=len(kh_df)
    grds = [0] * regs
    kh_df.insert(3, 'Grades', grds)
    
    # asignando 50 al podio
    kh_df.loc[kh_df['Rank'] < 4,'Grades'] = 50
    #kh_df['Grade'] = kh_df['Rank'].apply(lambda x: 50 if x<4 else 0)
    
    # sacando puntajes restantes a un arreglo
    np_arr = kh_df.loc[kh_df['Rank'] > 3,'Total Score (points)'].to_numpy()
    
    # calculando percentiles
    perc = np.percentile(np_arr,[25, 50, 75])
    lim_max = kh_df.loc[kh_df['Rank'] == 3,'Total Score (points)'].to_numpy()

    # asignando notas segun percentiles
    kh_df.loc[ (kh_df['Total Score (points)'] < lim_max[0]) & (kh_df['Total Score (points)'] >= perc[2]), 'Grades' ] =45
    kh_df.loc[ (kh_df['Total Score (points)'] < perc[2]) & (kh_df['Total Score (points)'] >= perc[1]), 'Grades' ] =38
    kh_df.loc[ (kh_df['Total Score (points)'] < perc[1]) & (kh_df['Total Score (points)'] >= perc[0]), 'Grades' ] =30
    kh_df.loc[ kh_df['Total Score (points)'] < perc[0], 'Grades' ] =25

    for i in range(0,regs):
        nota = kh_df.iloc[[i]]['Grades'].values[0]
        code = kh_df.iloc[[i]]['Player'].values[0]
        #print('Codigo:', str(code), 'Nota: ', str(nota))
        es_df.loc[ es_df['Codigo'] == code , quiz] = nota

    return es_df


#archivos con Scores
file_scores = ['Muestreo y cuantificación G1.xlsx','Muestreo y cuantificación G2.xlsx','Muestreo y cuantificación G3.xlsx']
#archivo listado
file_ests='PDS2022-1.xlsx'
#Quiz a asinar nota
quiz = 'Q1'

#Cargando lista de estudiantes
es_df = pd.read_excel(file_ests, sheet_name='Corte1', header=1)
es_df.dropna(subset=['Codigo'], inplace=True) # eliminar filas vacias
es_df['Codigo'] = es_df['Codigo'].astype(int)
es_df['Codigo'] = es_df['Codigo'].astype(str)

for i in file_scores:
    es_df = process_df(i, es_df, quiz)

es_df.to_excel('out.xlsx')