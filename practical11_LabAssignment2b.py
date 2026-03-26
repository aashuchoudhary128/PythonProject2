import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM',
             'Deloitte', 'Capgemini', 'Amdocs']

recruitment = [1200,1500,1800,1000,900,1100,700]

plt.pie(recruitment, labels=companies, autopct='%1.1f%%')

plt.title('Recruitment Distribution')
plt.show()