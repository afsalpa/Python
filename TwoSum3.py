class TwoSum3:

    def findTwoSum(inp, target):
        seen = {}

        for x in range(len(inp)):
            diff =  target - inp[x]
            if diff in seen:
                return [seen[diff], x]
            seen[inp[x]] = x
    
    print(findTwoSum([2,7,11,15], 9))
    print(findTwoSum([3,2,4], 6))
    print(findTwoSum([3,3], 6))