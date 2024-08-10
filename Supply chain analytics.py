#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the libraries
import pandas as pd
import numpy as np


# In[2]:


# import datasets 
df_orders = pd.read_csv('orders_and_shipments.csv',encoding='ISO-8859-1')
df_inventory = pd.read_csv('inventory.csv') 
df_fulfillment = pd.read_csv('fulfillment.csv')


# In[3]:


df_orders.head()


# In[4]:


df_inventory.head()


# In[5]:


df_fulfillment.head()


# In[6]:


df_orders.isna().sum()


# In[7]:


df_inventory.isna().sum()


# In[8]:


df_fulfillment.isna().sum()


# In[9]:


df_orders.duplicated().sum()


# In[10]:


df_inventory.duplicated().sum()


# In[11]:


df_fulfillment.duplicated().sum()


# In[12]:


df_orders.info()


# In[13]:


df_inventory.info()


# In[14]:


df_fulfillment.info()


# In[15]:


# using strip fn removing unwanted spaces from columns name
dataframes = [df_inventory, df_orders, df_fulfillment]

for df in dataframes:
  df.columns = df.columns.str.strip()


# In[16]:


df_orders.columns


# In[17]:


df_inventory.columns


# In[18]:


df_fulfillment.columns


# In[20]:


df_orders.columns


# In[21]:


df_orders['Discount %'].sample(30)


# In[22]:


# Convert the '-' values to 0 in the 'Discount %' column and then change the data type from object to float
df_orders['Discount %'] = df_orders['Discount %'].replace('  -  ', 0).astype(float)


# In[23]:


df_orders.columns


# In[24]:


# Make new columns: Order Datetime and Shipment Datetime
df_orders['Order Datetime'] = pd.to_datetime(df_orders['Order Year'].astype(str) + '-' + df_orders['Order Month'].astype(str) + '-' + df_orders['Order Day'].astype(str) + ' ' + df_orders['Order Time'])
df_orders['Shipment Datetime'] = pd.to_datetime(df_orders['Shipment Year'].astype(str) + '-' + df_orders['Shipment Month'].astype(str) + '-' + df_orders['Shipment Day'].astype(str))

# Displaying the result
df_orders[['Order Datetime', 'Shipment Datetime']].head()


# In[25]:


# Drop unnecessary columns
df_orders.drop(columns=['Order Year', 'Order Month', 'Order Day', 'Order Time',
                        'Shipment Year', 'Shipment Month', 'Shipment Day'], inplace=True)


# In[26]:


df_orders['Customer Country'].unique()


# In[27]:


#replace the special characters in the Customer Country column
df_orders['Customer Country'] = df_orders['Customer Country'].replace({
    'Dominican\xa0Republic': 'Dominican Republic',
    'Cote d\x92Ivoire': 'Cote d Ivoire', # Added a comma at the end of this line
    'Perú': 'Peru',
    'Algeria\xa0': 'Algeria',
    'Israel\xa0':'Israel',
    'Benín': 'Benin'
})
df_orders['Customer Country'].unique()


# In[28]:


df_orders['Order Processing Time'] = (df_orders['Shipment Datetime'] - df_orders['Order Datetime']).dt.days
df_orders['Order Processing Time'] = df_orders['Order Processing Time'].apply(lambda x: 0 if x == -1 else x)

df_orders.sample(5)


# In[29]:


# Final Check
df_orders.info()


# In[30]:


df_inventory.info()


# In[31]:


df_fulfillment.info()


# In[32]:


# Export DataFrames to CSV
df_orders.to_csv('orders_and_shipment.csv', index=False)
df_inventory.to_csv('inventory.csv', index=False)
df_fulfillment.to_csv('fulfillment.csv', index=False)


# In[ ]:




