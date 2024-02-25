# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:22:13 2024

@author: billy
"""

import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dpi = 90

# if you are on windows, you are going to have to change the file path to
# windows style
project_dir = r'C:/Users/java/Documents/Homework/DataViz/Matplotlib/'
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
product_count = df1.groupby('product_type', as_index=False)['cost_per_unit'].count()
product_count.sort_values(by='cost_per_unit', ascending=True, inplace=True)
count_per_product = product_count['cost_per_unit']
product_type = product_count['product_type']

fig, ax0 = plt.subplots(figsize=(8,12))
fig.suptitle('Estee Lauder Product Breakdown', fontsize=18, fontweight='bold')

ax0.barh(product_type, count_per_product, data=product_count, color='#261820')
ax0.set_title('Average Cost per Estee Lauder Product Unit', fontsize=12)
ax0.set_xlabel('Average Cost', fontsize=12)
ax0.set_ylabel('Product Type', fontsize=12)
ax0.set_yticklabels(list(product_type.values), fontsize=12)

plot1_filename = 'Product Type.png'
fig.savefig(output_dir + plot1_filename, dpi=dpi, bbox_inches = "tight")

# Product Prices
avg_cost_per_product = df1.groupby('product_type', as_index=False)['cost_per_unit'].mean()
avg_cost_per_product.rename(columns={'cost_per_unit':'avg_cost'}, inplace=True)
avg_cost_per_unit = avg_cost_per_product['avg_cost']
avg_product_type = avg_cost_per_product['product_type']

total_cost_per_product = df1.groupby('product_type', as_index=False)['cost_per_unit'].sum()
total_cost_per_product.rename(columns={'cost_per_unit':'total_cost'}, inplace=True)
total_cost_per_unit = total_cost_per_product['total_cost']
total_product_type = total_cost_per_product['product_type']

prices = avg_cost_per_product.merge(total_cost_per_product, how='left', on='product_type')
prices.sort_values(by='total_cost', ascending=False, inplace=True)
product_type = prices['product_type']
avg_cost = prices['avg_cost']
total_cost = prices['total_cost']

fig, ax0 = plt.subplots(figsize=(10,8), sharex=True)

ax0.bar(product_type, avg_cost, data=prices, color='#040A2B', alpha=0.5)
ax0.set_xlabel('Product Type', fontsize=12)
ax0.set_ylabel('Average Cost per Unit', fontsize=12, labelpad=1.5, fontweight='bold', color='#040A2B')
ax0.set_title('Estee Lauder Prices', fontsize=18, fontweight='bold')
ax0.yaxis.set_major_formatter('${x:1.2f}')

plt.xticks(rotation=90)

ax1 = ax0.twinx()
ax1.bar(product_type, total_cost, data=prices, color='#D9B166', alpha=0.5)
ax1.set_ylabel('Total Cost of All Units',fontsize=12, fontweight='bold', color='#D9B166')
ax1.yaxis.set_major_formatter('${x:1.2f}')

plt.subplots_adjust(wspace=0, bottom=0.15)
          
plot1_filename = 'Product Prices.png'
fig.savefig(output_dir + plot1_filename, dpi=dpi,bbox_inches = "tight")

# Price Range by Product Name
df1[['low_range', 'high_range']] = cost_range.str.split(' - ', expand=True)
df1['low_range'] = np.where(df1['low_range'] == '(none)', None, df1['low_range'])
df1['low_range'] = df1['low_range'].replace('[\$,]', '', regex=True).astype(float)
df1['high_range'] = df1['high_range'].replace('[\$,]', '', regex=True).astype(float)
low_range = df1['low_range']
high_range = df1['high_range']
product_type = df1['product_type']


fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(high_range, low_range, alpha=0.5, color='#040A2B', s=100)
fig.suptitle('Price Range of Products', fontsize=18, fontweight='bold')
ax.set_xlabel('High Range of Prices', fontsize=12, labelpad=1.5)
ax.set_ylabel('Low Range of Prices', fontsize=12, labelpad=1.5)

print(product_type.unique())
labels_visible = ['serum',
                  'face cream',
                  'face lotion',
                  'treatment lotion',
                  'eye cream',
                  'face treatment',
                  'face cleanser',
                  'eye serum',
                  'mask',
                  'eye mask',
                  'sunscreen',
                  'resurfacing cream',
                  'toner',
                  'moisturizer',
                  'makeup remover',
                  'face massaging tool',
                  'hand cream',
                  'foundation',
                  'lipstick',
                  'concealer',
                  'mascara',
                  'eyeliner',
                  'blush',
                  'lip serum',
                  'lip balm',
                  'lip treatment',
                  'lip volumizer',
                  'highlighter',
                  'bronzer',
                  'primer',
                  'lip gloss',
                  'lip color',
                  'lip liner',
                  'eyeshadow',
                  'lash primer',
                  'eyebrow liner',
                  'eyebrow gel',
                  'multi-product set',
                  'eau de parfum',
                  'perfume',
                  'body lotion',
                  'body powder',
                  'eau fraiche',
                  'body oil',
                  'eau de toilette',
                  'body cream',
                  'body spray',
                  'cologne',
                  'solid perfume',
                  'body wash']

label_up = ['eau de parfum',
            'perfume',
            'serum',
            'solid perfume',
            'eye serum',
            'face massaging tool']

label_down = ['lip serum',
              'lip balm',
              'lip treatment',
              'lip color',
              'lash primer',
              'eyebrow gel']

labels = product_type
# create data labels
x_cutoff = 400
y_cutoff = 250

x_offset = (high_range.max() - high_range.min()) * .01
y_offset = (low_range.max() - low_range.min()) * .01

for index, label in labels.iteritems():
    
    if label in labels_visible:
        if label == "face cream":
            ax.annotate(label, (high_range[index], low_range[index] + y_offset * 1.5))
        elif label in label_up:
            ax.annotate(label, (high_range[index] + x_offset, low_range[index] + y_offset))
        elif label in label_down:
            ax.annotate(label, (high_range[index] + x_offset, low_range[index] - y_offset))
        else:
            ax.annotate(label, (high_range[index] + x_offset, low_range[index]))
            
plot1_filename = 'Product Price Ranges.png'
fig.savefig(output_dir + plot1_filename, dpi=dpi,bbox_inches = "tight")







