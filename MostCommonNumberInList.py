class MostCommonNumberInList:

    def findMostCommonNumber( l : list[int]) -> int:
        #l.sort()
        seen = {}
        maxVal = 0
        maxOcc = 0
        for r in range(len(l)):

            if l[r] in seen:
                val = seen[l[r]]
                seen[l[r]] = val + 1
            else: 
                seen[l[r]] = 1
            
            checMax = max(maxOcc, seen[l[r]])
            if checMax > maxOcc:
                maxOcc = checMax
                maxVal = l[r]
        
        return maxVal
    
    print(findMostCommonNumber([1,3,1,3,2,1]))
            


