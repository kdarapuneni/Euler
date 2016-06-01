import math
import numpy as np
def getAllMultiples(limit):
    Sum = sum(np.asarray(range(1,11)))
    sumFactors = [1]*limit
    for i in range(2,11):
        ii = i
        while ii  < limit:
            sumFactors[ii] += i
            ii += i

    for i in range(1, limit):
        if sumFactors[i] == Sum:
            return i
    return 0
        

smallestMultiple = getAllMultiples(20000)
print smallestMultiple

