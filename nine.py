kg = 50
value = 4.00

total = float(input("type total kg = "))

excesso = total - kg
def calckg():
    if (kg>0):
        multe = excesso * value
        return multe
    else:
        multe = 0.0

multe = calckg()
print("value of multe will be = ",multe)