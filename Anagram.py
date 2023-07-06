class Anagram:

    def checkAnagram(a :str, b :str) -> str:
        a = a.upper()
        b = b.upper()
        print(a," ", b)
        aList=[*a]
        bList=[*b]        
        aList.sort()
        bList.sort()
        return aList == bList
    
    print(checkAnagram("welcome", "Comewel"))