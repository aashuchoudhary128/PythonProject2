class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)

class Manager(Employee):
    def show(self):
        print("\n--- Manager Details ---")
        self.display()

managers = []
for i in range(2):
    print(f"\nEnter details for Manager {i+1}")
    m = Manager()
    m.get_data()
    managers.append(m)

print("\n===== All Managers =====")
for m in managers:
    m.show()