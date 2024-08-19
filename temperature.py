fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celsius = float(input("Enter the temperature in celsius: "))


convert1 : float = (fahrenheit - 32) / 1.8
print(fahrenheit, "->", convert1, "Celsius")

convert2:  float = (celsius*1.8) + 32
print(celsius, "->", convert2, "Fahrenheit")
