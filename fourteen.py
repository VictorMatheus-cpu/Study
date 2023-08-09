ph = int(input("Enter the PH = "))

def PH():
    if(ph>7):
        return("solution is basic")
    elif(ph==7):
        return("solution is neutra")
    else:
        return("solution is acid")

result = PH()

print(result)