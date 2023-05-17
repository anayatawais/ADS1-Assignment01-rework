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

# selecting rows based on condition
tmar_df = tmar_df[tmar_df['Country Name'].isin(options)]
# Plotting the pie chart for above dataframe
tmar_df.groupby(['Country Name']).sum().plot(
    kind='pie', y='2021', autopct='%1.0f%%', figsize=(8, 8))
plt.title('Terrestrial and marine protected areas')
# Grouped barchart for School enrollment, primary and secondary
educ_df = data[data['Indicator Name'].str.contains('School enrollment, primary and secondary')]
educ_df = educ_df.reset_index()
options = ['Sub-Saharan Africa', 'Finland', 'Indonesia', 'France', 'Argentina','Germany', 'Mexico']
  
# selecting rows based on condition
educ_df = educ_df[educ_df['Country Name'].isin(options)]
educ_df = educ_df[['Country Name','1996','1999','2000','2002','2004','2006','2010']]
grouped_df = educ_df.groupby(['Country Name']).sum()
plot_df = grouped_df[['1996', '1999', '2000', '2002', '2004', '2006', '2010']]# Set the years as the x-axis labels
years = list(plot_df.columns)
x = np.arange(len(years))
# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.1
for i, country in enumerate(plot_df.index):
    plt.bar(x + i * bar_width, plot_df.loc[country], bar_width, label=country)

# Add labels, title, and legend
plt.xlabel('Years')
plt.ylabel('School enrollment, primary and secondary (gross), gender parity index (GPI)')
plt.xticks(x + bar_width * len(plot_df) / 2, years)
plt.title('Year-wise representation of GPI')
plt.legend()

# Display the plot
plt.show()
