height = float(input("Enter height in meters (m): "))
weight = float(input("Enter weight in kilograms (kg): "))

bmi: float = weight / (height**2)
print("BMI:", bmi)
