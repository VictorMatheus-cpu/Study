number = int(input("enter this number = "))

def days():
    if (number==1):
        return("Sabado")
    elif(number==2):
        return("Domingo")
    elif(number==3):
        return("Segunda")
    elif(number==4):
        return("Terça")
    elif(number==6):
        return("Quarta")
    elif(number==7):
        return("Quinta")
    elif(number==8):
        return("Sexta")
    else:
        return("Not exist")
day = days()

print("the chosen day is = ",day)