import pandas as pd

#aqui podemos ver la informacion que tiene el archivo csv
df = pd.read_csv('ModalidadVirtual.csv')

#print(df)

print(df['carrera'][1])

#filtrar datos por edad
filtrar=df['edad']>23
#tomaremos el dataframe q ya tenemos pero filtrando para q nos devuelva los datos de quienes superan los 23
df_filtrar= df[filtrar]
print(df_filtrar)


