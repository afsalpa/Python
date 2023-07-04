import sys
class ReverseInteger:

    def reverseIneger(n):
        print(n)
        max = 2**31
        
        negative = False
        if "-" in str(n):
            n = int(str(n).replace("-",""))
            negative = True
        s = str(n)
        reverse = int(s[::-1])
        
        if reverse <= -max or reverse >= max:
            return 0 
        else:
            if negative:
                return "-" + str(reverse)
            else:
                return reverse
        
    print(reverseIneger(123))
    print(reverseIneger("-123"))
    print(reverseIneger("120"))