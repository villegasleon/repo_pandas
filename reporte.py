import pandas as pd

data = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv',
                   #indexamos por Person ID
                   index_col='Person ID'
                   )
#print(data)

# Preguntas que buscamos responder con este conjunto
# Las preguntas que buscaremos responder con este conjunto de datos son las siguientes:

# ¿Quiénes tienen peor calidad del sueño, hombres o mujeres?

# ¿Existe una relación entre la calidad del sueño de las personas y su profesión?

# ¿La actividad física afecta al sueño?

# ¿Qué profesión presenta la peor calidad de sueño?

# ¿Cuál profesión tienen a las personas con el mayor nivel de estrés y el mayor índice de masa corporal?

# ¿En qué rango de edades se encuentran la mayor cantidad de trastornos del sueño?

# La cantidad de pasos al día, ¿afecta la calidad del sueño? ¿al índice de masa corporal?

# Con estas preguntas comenzaremos a hacer nuestro análisis buscando extraer la mayor cantidad de información que
# se pueda del conjunto, es importante señalar que en este proyecto solamente haremos análisis de datos utilizando 
# la librería Pandas.

#PRIMERO ANALIZAMOS LA INFORMACION QUE TENEMOS . Por ejemplo data.info para ver el resumen que es lo q tiene data
info=data.info()
print(info)
#TENEMOS OTRA FUNCION que nos regresa un resumen especifico de las columnas donde se almacenan datos numericos
resumen=data.describe()
print(resumen)

#Aanalisis de edades
#que numero de mujeres y hombres se les hizo esta encuesta?
genero = data['Gender'].value_counts()
print(genero)

#vamos a conocer el promedio d ela edades de este conjunto de datos
edadesProm = data['Age'].mean()
print(edadesProm)

#vamos a agregar una columna a nuestro conjunto de datos, donde nos diga si la persona es adulto <40 o adulto viejo>40
#si es menos de 40 le vamos a dar un nombre a la columna q vamos a agregar, la vamos a llamar Age_group, y aqui van a exisitir 2 clasificaciones : Adult y Older Adult
data.loc[data['Age']<=40, 'Age_group']= 'Adult'
data.loc[data['Age']>=41, 'Age_group']= 'Older Adult'
print(data)

#Ahora contaremos cuantos son Older Adult y cuantos son Adult
data_resume_age = data['Age_group'].value_counts()
print(data_resume_age)

#Agrupar en base a sexo, por promedio de edades, teniendo promedio y desviacion std
promEdadesXSexo= data.groupby('Gender')['Age'].agg(['mean','std'])
print(promEdadesXSexo)

#Analisis de las ocupaciones
ocupacion=data.groupby('Occupation')['Gender'].value_counts()
print(ocupacion)

#Tiempo maximo de sueño
suenoMax= data['Sleep Duration'].min(),data['Sleep Duration'].max()
print('EStos con los valores minimos y maximos de sueño : ', suenoMax)

#Quien tiene mejor calidad de sueño, hombres o mujeres, mediante un groupBy y doble corchete para poner 
#las 2 columnas con las q quiero discriminar
calidadSueno= data.groupby('Gender')[['Sleep Duration', 'Quality of Sleep']].mean()
print(calidadSueno)

#disticnion por la ocupacion y ordenamos con .sort()
calidadSuenoXOcupa= data.groupby('Occupation')[['Sleep Duration', 'Quality of Sleep']].mean()
calidadSuenoOcupOrdenado=calidadSuenoXOcupa.sort_values(by='Quality of Sleep')
print(calidadSuenoOcupOrdenado)

#indice de masa corporal por ocupaciones y genero
masaCorporal= data.groupby(['Occupation', 'Gender'])['BMI Category'].value_counts()
#ordenamos los datos para q sean mas legibles
masaCorporalOrder=masaCorporal.sort_values()
print(masaCorporalOrder)







