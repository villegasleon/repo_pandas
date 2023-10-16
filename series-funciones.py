import pandas as pd

#para una suma de los valores contenidos en una lista

numeros= pd.Series([1,2,3,4,5,6,7,8,9])
print(numeros.sum())

#algunas propiedades elementales que tiene nuestra serie
print(numeros.describe())

#filtrar los valores mediante el valor por ejemplo en esta serie de materias, solo queremos
#obtener los que sean mayores de 6
serie = pd.Series({'Matematicas': 8, 'Economia': 6, 'Programacion':10, 'Fisica':5})

print(serie[serie>6])

#ordernar los datos ocn referencia al index
print(serie.sort_index)

#ordernar los datos  mediante sort
print(serie.sort_values(ascending=True))

#relacionar 2 listas diferentes con index y su valor
jugadores =['Cristiano','Messi', 'Benzama']
indices=['PSG', 'Manchester United','Real Madrid']
futbol= pd.Series(index=indices,data=jugadores)
print(futbol)



