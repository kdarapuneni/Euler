x = 1
y = 2

total= 2;
while(x + y < 4000000):
    yTemp = x+y
    x = y
    y = yTemp
    if y%2 == 0:
        total += y
print total
