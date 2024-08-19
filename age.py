birthYear = int(input("Enter your birth year: "))
currentYear = int(input("Enter the current year: "))
birthDay = input(
    "Birthday is passed this year or not: (Press Y for Yes & N for No) ")

age: int = currentYear - birthYear

if birthDay == "N":
    age -= 1

print(age)
