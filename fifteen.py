number = int(input("Enter the number = "))

def SP():
    if(number>0):
        return("His successor is =",number+1,"His anteccessor is =",number-1)
    else:
        return("not exist")
    

calc = SP()

print(calc)