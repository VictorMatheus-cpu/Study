weight = float(input("Enter is Weight in KG = "))
height = float(input("Enter is Height in CM = "))

def IMC():
    imc = weight / (height**2)
    if (imc<18.5):
        return("You IMC =", imc ,"is underweight")
    elif (imc<=24.9):
        return("You IMC =", imc ,"You have the ideal weight")
    else:
        return("You IMC =", imc ,"is overweight ")

calc = IMC()

print(calc)