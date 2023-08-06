value = float(input("type is value for hours = "))

hours = float(input("type for hours = "))

def wage():
    result = value * hours
    return result
resulted = wage()

def ir():
    result = wage() * 0.11
    return result
resultedir = ir()

def inss():
    result = wage() * 0.08
    return result
resultedinss = inss()
def sin():
    result = wage() * 0.05
    return result
resultedsin = sin()

def liquid():
    result = wage() - inss() - sin() - ir()
    return result
resultedliquid = liquid()

print("your salary will be = ",resulted)
print("pay for INSS = ", resultedinss)
print("pay for IR = ", resultedir)
print("pay for SIN = ", resultedsin)
print("Resulted liquit = ", resultedliquid)