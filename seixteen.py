def celsiusinFahrenheit(temperature):
    return temperature * 9/5 + 32

def celsiusinKelvin(temperature):
    return temperature + 273.15

def fahrenheitincelsius(temperature):
    return (temperature - 32) * 5/9

def fahrenheitinkelvin(temperature):
    return (temperature -32) * 5/9 + 273.15

def kelvinincelsius(temperature):
    return temperature - 273.15

def kelvininfahrenheit(temperature):
    return (temperature - 273.15) * 9/5 + 32
print("Choose temperature scale: ")
print("1 : celsius")
print("2 : kelvin")
print("3 : fahrenheit")

choice = int(input("Enter number the option choose = "))
temperature = float(input("Enter the Temperature = "))

if (choice == 1):
    print("The Temperature",temperature, "The Result of Celsius in Fahrenheit is : ", celsiusinFahrenheit(temperature),"The result of Celsius in kelvin is = ", celsiusinKelvin(temperature))
elif (choice == 2):
     print("The Temperature",temperature, "The Result of kelvin in Fahrenheit is : ", kelvininfahrenheit(temperature),"The result of kelvin in celsius is = ", kelvinincelsius(temperature))
elif (choice == 3):
     print("The Temperature in Fahrenheit",temperature, "The Result of Fahrenheit in celsius is : ", fahrenheitincelsius(temperature),"The result of Fahrenheit in kelvin is = ", fahrenheitinkelvin(temperature))
else:
    print (" not exist ")



