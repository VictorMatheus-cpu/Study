day = int(input("Type is Days = "))
Km = int(input("Type is Km rotation = "))

def Calc():
    days = 30 * day
    ki = 0.1 * Km
    cl = days + ki
    des = cl * 0.1
    total = cl - des
    return total

total = Calc()

print ("The Total will bee = ", total)