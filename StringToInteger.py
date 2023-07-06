import math
class StringToInteger:
    def findMyAtoi(x) -> int:
        if len(x) > 200 and len(x) <= 0:
            return 0
        x = x.strip()
        max = 2**31
        num = 0
        i = 0
        sign = 1
        if x[i] == "+":
            i +=1 
        if x[i] == "-":
            i +=1;
            sign = -1
        while i < len(x) and x[i].isdigit():
            num = (num * 10 ) +  int(x[i])
            i+=1
        num = num * sign
        
        #num = max(min(num, 2 ** 31 - 1), -2 ** 31)

        return num

    # print(findMyAtoi("5355 test"))
    # print(findMyAtoi("-12355 testing one"))
    print(findMyAtoi("-91283472332"))



