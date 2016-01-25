import math
def getAllPrimes(x):
    listOfPrimes = []
    limit = int(math.floor(math.sqrt(x)))
    primes = [1]*limit
    for i in range(2,limit):
        if primes[i] != 0:
            listOfPrimes.append(i)
            ii = 0
            while ii  < limit:
                primes[ii] = 0
                ii += i
    return listOfPrimes


value = 600851475143
pList = getAllPrimes(value)
for i in reversed(pList):
    if value % i == 0:
        print i
        break


