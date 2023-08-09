basebigger = float(input("Enter is base bigger = "))
basesmaller = float(input("Enter is base Small = "))
height = float(input("Enter is height = "))

def Area():
    calc = (basebigger + basesmaller) * height /2 
    return calc

result = Area()

print("The area is Trapezium is = ", result)