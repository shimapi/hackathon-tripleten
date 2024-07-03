#%% ################################################# Importar librerias #############################################################################
import datetime as dt
import pandas as pd
#%% ################################################# Leer CSV limpio ################################################################################
df_online_retail_feat_eng = pd.read_csv('./datasets/intermediate/df_online_retail_feat_eng.csv')
print(df_online_retail_feat_eng)
#%% ################################################# Preparación de datos ###########################################################################

# Asegurarse de que la columna de fecha esté en el formato datetime
df_online_retail_feat_eng['invoice_date'] = pd.to_datetime(df_online_retail_feat_eng['invoice_date'])
#%% ################################################# Calcular las métricas RFM ###########################################################################
# Establecer la fecha de referencia para el análisis
current_date = df_online_retail_feat_eng['invoice_date'].max() + dt.timedelta(days=1)

# Calcular Recency, Frequency y Monetary para cada cliente
rfm = df_online_retail_feat_eng.groupby('customer_id').agg({
    'invoice_date': lambda x: (current_date - x.max()).days,
    'invoice_no': 'nunique',
    'total_sales': 'sum'
}).reset_index()

# Renombrar las columnas
rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']
#%% ################################################# Asignar puntajes RFM #################################################################################
# Asignar puntajes de 1 a 5 para cada métrica
rfm['R'] = pd.qcut(rfm['recency'], 5, labels=False, duplicates='drop') + 1
rfm['F'] = pd.qcut(rfm['frequency'], 5, labels=False, duplicates='drop') + 1
rfm['M'] = pd.qcut(rfm['monetary'], 5, labels=False, duplicates='drop') + 1

# Crear el puntaje RFM combinando los puntajes individuales
rfm['RFM_Score'] = rfm['R'].astype(str) + rfm['F'].astype(str) + rfm['M'].astype(str)
#%% ################################################# Segmentar los clientes ################################################################################
# Definir una función para segmentar los clientes
def segment_rfm(df):
    if df['RFM_Score'] in ['555', '554', '545', '554']:
        return 'Best Customers'
    elif df['RFM_Score'] in ['544', '543', '534', '535']:
        return 'Loyal Customers'
    elif df['RFM_Score'] in ['445', '444', '443', '434']:
        return 'Potential Loyalists'
    elif df['RFM_Score'] in ['344', '343', '334', '333']:
        return 'New Customers'
    elif df['RFM_Score'] in ['244', '243', '234', '233']:
        return 'Promising'
    elif df['RFM_Score'] in ['144', '143', '134', '133']:
        return 'Need Attention'
    elif df['RFM_Score'] in ['111', '112', '121', '122']:
        return 'At Risk'
    else:
        return 'Others'

# Aplicar la función de segmentación
rfm['Segment'] = rfm.apply(segment_rfm, axis=1)
#%% Convertir el dataframe a CSV
rfm.to_csv('./datasets/intermediate/rfm.csv', index=False)
#%% ################################################# Unir dataframes rfm y original ################################################################################
# Realizar la unión de los DataFrames
df_online_retail_rfm = pd.merge(df_online_retail_feat_eng, rfm, on='customer_id', how='left')
#%% Convertir el dataframe a CSV
df_online_retail_rfm.to_csv('./datasets/intermediate/df_online_retail_rfm.csv', index=False)