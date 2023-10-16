import pandas as pd

#aqui generamos un dataFrame a partir de una lista de datos, ahi mismo le vamos a pasar el nombre que llevaran las columnas
df = pd.DataFrame([['Maria',27],['David',34],['Ana',18], ['JOse',17]],columns=['NOMBRE','EDAD'])

print(df)