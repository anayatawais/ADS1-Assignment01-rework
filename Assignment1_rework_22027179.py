# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:40:43 2023

@author: ALIENWARE-CERDAS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = 'API_climatechange.csv'
data = pd.read_csv(dataset)
popuag_df = data[data['Indicator Name'].str.contains('Population in urban agglomerations')]
popuag_df = popuag_df.reset_index()
options = ['Sub-Saharan Africa', 'Afghanistan', 'Australia', 'Japan', 'Argentina','Germany', 'Mexico']
# selecting rows based on condition
pop_df = popuag_df[popuag_df['Country Name'].isin(options)]
pop_df = pop_df.drop(['index','Country Code','Indicator Name','Indicator Code'], axis=1)
pop_df_grouped = pop_df.groupby(['Country Name']).sum().T

# Plot the graph
fig, ax = plt.subplots(figsize=(12, 8))
pop_df_grouped.plot(ax=ax)

# Set graph title and axis labels
ax.set_title('Population over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Population')

# Show the graph
plt.show()
# Pie chart for Terestrial and marine area
tmar_df = data[data['Indicator Name'].str.contains('Terrestrial and marine protected areas')]
tmar_df = tmar_df.reset_index()
tmar_df = tmar_df[['Country Name','2021']]
tmar_df = tmar_df.dropna()
options = ['Sub-Saharan Africa', 'Finland', 'Indonesia', 'France', 'Argentina','Germany', 'Mexico']
  
