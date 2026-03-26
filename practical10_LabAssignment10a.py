import pandas as pd

df = pd.DataFrame({
    'title': ['Book A','Book B','Book C','Book D','Book E'],
    'author': ['Author 1','Author 2','Author 1','Author 3','Author 2'],
    'edition': [1,2,1,3,1],
    'year': [2018,2020,2015,2022,2019],
    'publisher': ['Pub X','Pub Y','Pub X','Pub Z','Pub Y'],
    'price': [250,300,200,500,150]
})

print(df)

a = input("Author: ")
print(df[df['author'] == a])

p = input("Publisher: ")
print(df[df['publisher'] == p])

print(df[df['price'] == df['price'].min()][['title','price']])
print(df[df['price'] == df['price'].max()][['title','price']])

print(df.sort_values('year')[['title','year']])