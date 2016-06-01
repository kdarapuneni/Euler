limit = 999
found = False;
palindromes = []
for i in reversed(range(100,1000)):
    for y in reversed(range(100,1000)):
        num = str(i*y)
        if(num == num[::-1]):
            palindromes.append(int(num))

print max(palindromes)
