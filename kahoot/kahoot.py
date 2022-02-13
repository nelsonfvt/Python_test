import pandas as pd

#Cargando resultados de Kahoot
#print('Ingrese nombre de archivo:')
#kh_sc=input()
kh_df = pd.read_excel( 'Muestreo y cuantificacion G1.xlsx', sheet_name='Final Scores',header=2)
regs=len(kh_df)
grds = [0] * regs
gr_df = kh_df[["Rank","Player"]]
gr_df.insert(2, 'Grade', grds)
print(gr_df)

gr_df.loc[kh_df["Rank"] < 4,"Grade"] = 50
df = kh_df[kh_df["Rank"] > 3,"Total Score (point)"]
print(df)