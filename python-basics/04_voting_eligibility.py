age = int(input("Enter age: "))

if age < 0 or age > 120:
    print("Invalid age entered.")
elif age >= 18:
    print("Eligible for voting.")
else:
    print("Not eligible for voting.")
