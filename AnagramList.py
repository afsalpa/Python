class AnagramList:
    
    def findAnagram(inputArray):
        print(inputArray)
        stringDict = dict()
        for currentString in inputArray:
            arrayString = [*currentString]
            arrayString.sort()
            sortedString = "".join(arrayString)
            if sortedString in stringDict.keys() == False:
                stringDict[sortedString] = []
            else:
                list1 = stringDict.get(sortedString)

                if list1 != None:
                    list1.append(currentString)
                else:
                    list1 = [currentString]

                stringDict[sortedString] = list1
        return stringDict.values()

    inputVals = ["eat","tea","tan","ate","nat","bat"]
    resp = findAnagram(inputVals)
    print(resp)