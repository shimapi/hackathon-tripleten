import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
# Configurar pandas para mostrar todas las columnas
pd.set_option('display.max_columns', None)
df=pd.read_csv('C:/USers/Usuario/hackathon-tripleten/datasets/intermediate/df_online_retail_cleaned.csv')

## prueba a/b : medir la diferencia entre las dos regiones con mas ventas de la tienda online
# Calcular las ventas totales por región
ventas_por_region = df.groupby('region')['quantity'].sum().sort_values(ascending=False)

# Obtener las dos regiones más vendidas
top_2_regiones = ventas_por_region.index[:2]
print(f"Las dos regiones más vendidas son: {top_2_regiones[0]} y {top_2_regiones[1]}")
# Filtrar los datos para las dos regiones más vendidas
df_top_2 = df[df['region'].isin(top_2_regiones)]

# Crear una columna 'grupo' basada en la región
df_top_2['grupo'] = df_top_2['region'].apply(lambda x: 'A' if x == top_2_regiones[0] else 'B')
# Calcular el ingreso total por fila
df_top_2['total_revenue'] = df_top_2['unit_price'] * df_top_2['quantity']

# Calcular el ingreso total por cliente en cada grupo
ventas_por_usuario = df_top_2.groupby(['grupo', 'customer_id'])['total_revenue'].sum().reset_index()

# Dividir los datos en los dos grupos
ventas_grupo_a = ventas_por_usuario[ventas_por_usuario['grupo'] == 'A']['total_revenue']
ventas_grupo_b = ventas_por_usuario[ventas_por_usuario['grupo'] == 'B']['total_revenue']

print(f"Ventas por usuario en el Grupo A:\n{ventas_grupo_a.describe()}")
print(f"Ventas por usuario en el Grupo B:\n{ventas_grupo_b.describe()}")
 
 #eliminar los datos atipicos
def eliminar_outliers(ventas):
    Q1 = ventas.quantile(0.25)
    Q3 = ventas.quantile(0.75)
    IQR = Q3 - Q1
    filtro = (ventas >= (Q1 - 1.5 * IQR)) & (ventas <= (Q3 + 1.5 * IQR))
    return ventas[filtro]

# Eliminar outliers en cada grupo
ventas_grupo_a_filtradas = eliminar_outliers(ventas_grupo_a)
ventas_grupo_b_filtradas = eliminar_outliers(ventas_grupo_b)

print(f"Ventas por usuario en el Grupo A (sin outliers):\n{ventas_grupo_a_filtradas.describe()}")
print(f"Ventas por usuario en el Grupo B (sin outliers):\n{ventas_grupo_b_filtradas.describe()}")

from scipy.stats import ttest_ind

# Realizar una prueba t para comparar las ventas por usuario entre los dos grupos
t_stat, p_value = ttest_ind(ventas_grupo_a_filtradas, ventas_grupo_b_filtradas)

print(f"Estadístico t: {t_stat}")
print(f"Valor p: {p_value}")

if p_value < 0.05:
    print("La diferencia es estadísticamente significativa.")
else:
    print("No hay suficiente evidencia para afirmar que la diferencia es significativa.")
