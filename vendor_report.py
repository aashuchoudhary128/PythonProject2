# Lab Assignment 2
# Vendor Purchase Report

vendor_name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

monthly_purchases = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print("\nEnter Monthly Purchases:")
for month in months:
    amount = float(input(f"{month}: "))
    monthly_purchases.append(amount)

annual_total = sum(monthly_purchases)

print("\n----- Vendor Annual Purchase Report -----")
print("Vendor Name:", vendor_name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)
print("\nMonthly Purchases:")
for i in range(12):
    print(months[i], ":", monthly_purchases[i])

print("\nTotal Annual Purchase:", annual_total)
