class TwoSum:

    def findTwoSum(arrayList, target):
        for x in range(len(arrayList) -1 ):
            for y in range(x+1, len(arrayList)):
                if (int(arrayList[x]) + int(arrayList[y])) == target:
                    return [x,y]
        return -1

    
    resp = findTwoSum(["3","2","3"],6)
    print(resp)