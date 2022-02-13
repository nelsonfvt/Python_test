import pandas as pd
import numpy as np

#Cargando resultados de Kahoot
#print('Ingrese nombre de archivo:')
#kh_sc=input()
kh_df = pd.read_excel('Muestreo y cuantificación G1.xlsx', sheet_name='Final Scores',header=2)
regs=len(kh_df)
grds = [0] * regs
#Adicionar columna de notas
kh_df.insert(3, 'Grades', grds)

# asignando 50 a los primeros
kh_df.loc[kh_df['Rank'] < 4,'Grades'] = 50
#kh_df['Grade'] = kh_df['Rank'].apply(lambda x: 50 if x<4 else 0)

# sacando puntajes restantes a un arreglo
np_arr = kh_df.loc[kh_df['Rank'] > 3,'Total Score (points)'].to_numpy()

# calculando percentiles
perc = np.percentile(np_arr,[25, 50, 75])
lim_max = kh_df.loc[kh_df['Rank'] == 3,'Total Score (points)'].to_numpy()

# asingnado notas segun percentiles
kh_df.loc[ (kh_df['Total Score (points)'] < lim_max[0]) & (kh_df['Total Score (points)'] >= perc[2]), 'Grades' ] =45
kh_df.loc[ (kh_df['Total Score (points)'] < perc[2]) & (kh_df['Total Score (points)'] >= perc[1]), 'Grades' ] =38
kh_df.loc[ (kh_df['Total Score (points)'] < perc[1]) & (kh_df['Total Score (points)'] >= perc[0]), 'Grades' ] =30
kh_df.loc[ kh_df['Total Score (points)'] < perc[0], 'Grades' ] =25

#Cargando lista de estudiantes
es_df = pd.read_excel('PDS2022-1.xlsx', sheet_name='Corte1', header=1)

codes = kh_df['Player']
#print(codes)

#for i in codes:
    