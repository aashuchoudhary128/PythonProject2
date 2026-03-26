import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM',
             'Deloitte', 'Capgemini', 'Amdocs']

recruitment = [1200,1500,1800,1000,900,1100,700]

plt.pie(recruitment, labels=companies, autopct='%1.1f%%')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Doughnut Chart')
plt.show()