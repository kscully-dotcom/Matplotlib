# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:22:13 2024

@author: billy
"""

import os

import pandas as pd
import matplotlib.pyplot as plt

dpi = 300

# if you are on windows, you are going to have to change the file path to
# windows style
project_dir = r'C:/Users/billy/Documents/Homework/Data Visualization/Matplotlib/'
data_dir = project_dir + r'Data/'
output_dir = project_dir + r'Output/'

df1_filename = 'esteelauder_products.csv'
df1 = pd.read_csv(data_dir + df1_filename, encoding='ISO-8859–1')

df1 = df1.iloc[:-1,:]
product_name = df1['product_name']
# product_type = df1['product_type']
product_decription = df1['product_decription']
product_purpose = df1['product_purpose']
df1['cost_per_unit'] = df1['cost_per_unit'].replace('[\$,]', '', regex=True).astype(float)
# cost_per_unit = df1['cost_per_unit']
cost_range = df1['cost_range']
print(df1.dtypes)

# # Histogram of prices
avg_cost_per_product = df1.groupby('product_type', as_index=False)['cost_per_unit'].mean()
avg_cost_per_product.sort_values(by='cost_per_unit', ascending=True, inplace=True)
cost_per_unit = avg_cost_per_product['cost_per_unit']
product_type = avg_cost_per_product['product_type']

total_cost_per_product = df1.groupby('product_type', as_index=False)['cost_per_unit'].sum()
total_cost_per_product.sort_values(by='cost_per_unit', ascending=True, inplace=True)
cost_per_unit = total_cost_per_product['cost_per_unit']
product_type = total_cost_per_product['product_type']

product_count = df1.groupby('product_type', as_index=False)['cost_per_unit'].count()
product_count.sort_values(by='cost_per_unit', ascending=True, inplace=True)
cost_per_unit = product_count['cost_per_unit']
product_type = product_count['product_type']

fig, [ax0, ax1, ax2] = plt.subplots(3,1,figsize=(80,40))
ax0.barh(product_type, cost_per_unit, data=product_count)
ax0.set_title('Average Cost per Estee Lauder Product', fontsize=24)
ax0.set_xlabel('Average Cost', fontsize=18)
ax0.set_ylabel('Product Type', fontsize=18, labelpad=1.5)
ax0.set_yticklabels(list(product_type.values), fontsize=16)

ax1.barh(product_type, cost_per_unit, data=total_cost_per_product)
ax1.set_title('Total Cost per Estee Lauder Product', fontsize=24)
ax1.set_xlabel('Total Cost', fontsize=18)
ax1.set_ylabel('Product Type', fontsize=18, labelpad=1.5)
ax1.set_yticklabels(list(product_type.values), fontsize=16)

ax2.barh(product_type, cost_per_unit, data=total_cost_per_product)
ax2.set_title('Estee Lauder Product Availablility', fontsize=24)
ax2.set_xlabel('Count of Product Type', fontsize=18)
ax2.set_ylabel('Product Type', fontsize=18, labelpad=1.5)
ax2.set_yticklabels(list(product_type.values), fontsize=16)

plot1_filename = 'Product Type.png'
fig.savefig(output_dir + plot1_filename, dpi=dpi)