hardness = float(input("Enter hardness: "))
carbon = float(input("Enter carbon content: "))
tensile = float(input("Enter tensile strength: "))

a1 = hardness > 50
a2 = carbon < 0.7
a3 = tensile > 5600

if a1 and a2 and a3:
    grade = 10
elif a1 and a2:
    grade = 9
elif a2 and a3:
    grade = 8
elif a1 and a3:
    grade = 7
elif a1 or a2 or a3:
    grade = 6
else:
    grade = 5
print("Grade of steel:", grade)
