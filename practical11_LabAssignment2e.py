import matplotlib.pyplot as plt

companies = ['IBM', 'Amdocs']
values = [1000, 700]

plt.bar(companies, values)

plt.title('IBM vs Amdocs Recruitment')
plt.ylabel('Employees')

plt.show()