point1 = float(input("Enter is number = "))
point2 = float(input("Enter other number = "))
point3 = float(input("Enter other number = "))

media = (point1 + point2 + point3)/3

count_above_average = 0

if point1 > media:
    count_above_average += 1
if point2 > media:
    count_above_average += 1
if point3 > media:
    count_above_average += 1

print("The is media will be = ", media)
print("number of numbers that are above the average will be", count_above_average)



