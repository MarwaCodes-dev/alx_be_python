FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temp = int(input("Enter the temperature to convert: "))
temp_kind = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()


def convert_to_celsius(fahrenheit):
    fahrenheit =(temp - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temp}°F is {fahrenheit}")
def convert_to_fahrenheit(celsius):
    celsius = (temp*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    print(f"{temp}°C is {celsius}")  

if temp_kind == "F":
    convert_to_celsius(temp)
elif temp_kind == "C":
    convert_to_fahrenheit(temp)
else:
    print("invalid operation")                 