#!/usr/bin/python3

import sys
import pandas as pd
import matplotlib.pyplot as plt

filename = sys.argv[1]
headers = ['timestamp','msin', 'mcc','mnc', 'country', 'network']
df = pd.read_csv(filename,  names=headers)

df['country'].value_counts().plot(kind='barh', title='mcc count')
plt.show()

df['network'].value_counts().plot(kind='barh', title='mnc count')
plt.show()

df['msin'].value_counts().head(20).plot(kind='barh', title='msin top 20 (salted and hashed)')
plt.show()


