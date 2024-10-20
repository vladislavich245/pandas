import pandas as pd
df = pd.read_csv('GoogleApps.csv')
print(df[df['Type'] == 'Paid']['Price'].min())
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())

