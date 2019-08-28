print(10 / 3) #gives a floating point value
print(10 // 3) #gives a integer value
print(10 ** 3) #gives 10 to the power of 3
print(10 % 3) #gives the remainder
print(round(3.5))

import math
print(math.factorial(4))
print(math.ceil(3.6))
print(math.floor(3.6))

#if elif else
x = 400
y = 300
z = 500

if x > y:
    if x > z:
        print("x is the greatest integer")
    else:
        print("z is the greatest integer")
else:
    if y>z:
        print("y is the greatest")
    else:
        print('z is the greatest')