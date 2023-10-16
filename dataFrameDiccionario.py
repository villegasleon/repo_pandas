import pandas as pd
#Vamos a considerar un Dataframe a partir de un diccionario,
#como data=diccionario, index=filas, columns= columnas

data= {'NOMBRE':['Maria','Jose', 'David', 'Ivan'],
       'CARRERA':['Auditoria', 'Informatica', 'Derecho','Idiomas'],
        'CORREO':['MARIA@GMAIL.OM','jose@gmail.com','david@gmail.com','ivan@gmail.com'],
        'TELEFONO':[7778878,'4454545','98989898','323232323']}
#ahora vamos a llamar dataframe, ya no trabajamos con series
#un dateframe es algo parecido a un diccionario pero diferentes tidpos de data, en este caso traia
estudiantes = pd.DataFrame(data)

print(estudiantes)

#Dataframe a partir d euna lista


