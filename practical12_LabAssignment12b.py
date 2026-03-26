import pandas as pd

data = {
    'Employee ID': [101, 102, 103, 104, 105],
    'Employee Name': ['Amit', 'Neha', 'Raj', 'Simran', 'John'],
    'Department': ['Automotive', 'IT', 'Automotive', 'HR', 'IT'],
    'Designation': ['Manager', 'Developer', 'Engineer', 'HR', 'Developer']
}

df = pd.DataFrame(data)

print("Employees in Automotive domain:")
print(df[df['Department'] == 'Automotive'])

emp_id = int(input("\nEnter Employee ID: "))
print(df[df['Employee ID'] == emp_id])

print("\nList of Developers:")
print(df[df['Designation'] == 'Developer'])