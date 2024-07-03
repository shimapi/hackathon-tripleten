#%% ################################################# Importar librerias #############################################################################
import pandas as pd

#%% ################################################# Leer CSV limpio ################################################################################
df_online_retail_cleaned = pd.read_csv('./datasets/intermediate/df_online_retail_cleaned.csv')
#%% ################################################# Preparar el dataset ################################################################################

# Convertir los datos a datetime
df_online_retail_cleaned['invoice_date'] = pd.to_datetime(df_online_retail_cleaned['invoice_date'])

# Eliminar la columna de descripción original
df_online_retail_cleaned.drop(columns=['description'], axis=1, inplace=True)
#%% ################################################# Crear columnas a partir de fechas ################################################################################
# Crear columnas día, mes y año a partir de la fecha
df_online_retail_cleaned['day'] = df_online_retail_cleaned.invoice_date.dt.day
df_online_retail_cleaned['month'] = df_online_retail_cleaned.invoice_date.dt.month
df_online_retail_cleaned['year'] = df_online_retail_cleaned.invoice_date.dt.year

#%% ################################################# Crear columnas a partir de las ventas ############################################################################
# Total de ventas por factura
df_online_retail_cleaned['total_sales'] = df_online_retail_cleaned['quantity'] * df_online_retail_cleaned['unit_price']

# Agrupar por ventas totales por cliente y renombrar la columna
sales_per_customer = df_online_retail_cleaned.groupby('customer_id').agg(sales_per_customer=('total_sales', 'sum')).reset_index()

# Unir el total de ventas por cliente con el dataFrame original
df_online_retail_cleaned = df_online_retail_cleaned.merge(sales_per_customer, on='customer_id', how='left')
#%% ################################################# No. de Facturas por cliente #####################################################################################
# Agrupar las facturas por cliente y renombrar la columna
invoices_per_customer = df_online_retail_cleaned.groupby('customer_id').agg(invoices_per_customer=('invoice_no', 'count')).reset_index()

# Unir las facturas por cliente con el dataFrame original
df_online_retail_cleaned = df_online_retail_cleaned.merge(invoices_per_customer, on='customer_id', how='left')
#%% ################################################# valor prom. de factura por cliente ##############################################################################
df_online_retail_cleaned['avg_sales_per_customer'] = df_online_retail_cleaned['sales_per_customer'] / df_online_retail_cleaned['invoices_per_customer']

#%% Convertir el dataframe a CSV
df_online_retail_cleaned.to_csv('./datasets/intermediate/df_online_retail_feat_eng.csv', index=False)