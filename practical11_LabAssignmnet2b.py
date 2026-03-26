import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM',
             'Deloitte', 'Capgemini', 'Amdocs']

recruitment = [1200,1500,1800,1000,900,1100,700]

plt.bar(companies, recruitment)

plt.title('Company Recruitment')
plt.xlabel('Company')
plt.ylabel('Employees')

plt.xticks(rotation=30)
plt.show()