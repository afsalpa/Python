class FindTwoNumberMultiplication:

    def findNumbers(l : list[int], target : int) -> list[int]:
        print(l)
        enum = enumerate(l)
        for x in range(len(l)):
            div = int(target / l[x]) 
            if div in l:
                return [l[x], div]
    
    print(findNumbers([2,4,1,6,5,40,-1], -1))