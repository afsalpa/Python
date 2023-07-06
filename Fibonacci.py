class Fibonacci:
    
    def findFibonacii(num : int) -> int:

        result = [int for i in range(num + 1)]
        if num == 0:
            return 0
        if num == 1:
            return 1
        
        result[0] = 0
        result[1] = 1

        for i in range(2, num + 1):
            result[i] = result[i-1] + result[i-2]
        
        return result[num]
    
    print(findFibonacii(4))
    
