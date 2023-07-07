class FindCommonElements:

    def findCommonElement(l : list[int], r : list[int]) -> list[int]:

        result = set()
        for x in range(len(r)):
            if r[x] in l:
                result.add(r[x])
        return result
    
    result = findCommonElement([1,3,4,6,7,9], [1,2,4,5,9,10])
    print(result)
