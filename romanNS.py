def romanNS(n):
    digits = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i,c in enumerate(n):
        if (i+1) == len(n) or digits[c] > digits[n[i+1]]:
            result += digits[c]
        else:
            result -= digits[c]
    return result

n=input('->')
print(romanNS(n))
