import pandas as pd

#creacion de series a partir de un diccionario
materias= pd.Series({'Matematicas':60, 'Fisica':100, 'Quimica':78})

#print(materias)

 #acceder a los valores de un elemento
print(materias[['Matematicas','Fisica']])