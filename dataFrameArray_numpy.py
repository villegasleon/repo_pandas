import pandas as pd
import numpy as np

#aqui utilizamos libreria numpy que es np con su funcion random y randn, es aqui donde le definimos que 
#queremos 4 filas x 3 columnas 
df = pd.DataFrame(np.random.randn(4,3), columns=['a','b','c'])
print(df)