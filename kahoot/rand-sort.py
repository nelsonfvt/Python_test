import pandas as pd

#Cargando archivo estudiantes
lista_full = pd.read_csv('Listado_estudiantes.csv',header=None)
lin_es=len(lista_full)
print('numero de estudiantes: '+str(lin_es))

# Cargando archivo relatores
relatores = pd.read_csv('Relatores.csv',header=None)
lin_re = len(relatores)
print('numero de relatores: '+str(lin_re))

#Numero de grupos y estudiantes por grupo
est_disp=lin_es-lin_re
#print('Estudiantes para hacer grupos: '+str(est_disp))
n_integrantes = est_disp//lin_re
print('numero de integrantes por grupo: '+str(n_integrantes))
n_sobrantes = est_disp%lin_re
print('... y sobran: '+str(n_sobrantes))

estudiantes = lista_full
rel_cod = relatores[0]
for i in rel_cod:
    estudiantes = estudiantes[estudiantes[0] != i]

grupos = []
for g in range(0,lin_re):
    rel=relatores.iloc[g].to_frame().transpose()
    ests=estudiantes.sample(n=n_integrantes)
    ests_codes = ests[0]
    for e in ests_codes:
        estudiantes = estudiantes[estudiantes[0] != e]
    grupo = pd.concat([rel,ests])
    grupos.append(grupo)


for s in range(0, len(estudiantes)):
    #print(estudiantes.iloc[s].to_frame().transpose())
    est = estudiantes.iloc[s].to_frame().transpose()
    grupos[s]= grupos[s].append(est,ignore_index=True)

for g in range(0,lin_re):
    filename = "grupo_"+str(g+1)+".csv"
    grupos[g].to_csv(filename, header=['código','Apellidos','Nombres','correo'])