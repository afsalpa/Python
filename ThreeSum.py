class ThreeSum:

    def findThreeSum(inp : list[int]):
        print(inp)
        result = []
        inp.sort()
        print(inp)

        for i , v in enumerate(inp):
            
            if i > 0 and inp[i] == inp[i-1]:
                continue
            
            l , r = i+1, len(inp) -1

            while l < r :
                sum = v + inp[l] + inp[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                elif  sum == 0:
                    result.append([v,inp[l],inp[r]])
                    l += 1
                    while inp[l] == inp[l -1] and l < r:
                        l += 1
        return result
                


    print(findThreeSum([-1,0,1,2,-1,-4]))