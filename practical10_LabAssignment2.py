import pandas as pd

state = ['S1','S2','S3','S4','S5']
area = [100000,150000,90000,120000,110000]
pop = [5000000,8000000,3000000,7000000,6000000]

df = pd.DataFrame(list(zip(state, area, pop)), columns=['State','Area','Population'])

print(df)

print(df.loc[df['Area'].idxmax(), 'State'])
print(df.loc[df['Population'].idxmax(), 'State'])

df['Density'] = df['Population'] / df['Area']
print(df)

print(df.loc[df['Density'].idxmax(), 'State'])