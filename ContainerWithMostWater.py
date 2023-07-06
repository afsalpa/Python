class ContainerWithMostWater:

    def findContainerWithMostWater(inp):
        l = 0 
        r = len(inp) - 1 
        maxWidth = 0
        print(inp)
        
        while l < r:
            width = (r - l ) * min(inp[l], inp[r])
            print(width, l , r )
            maxWidth = max(maxWidth, width)

            if(inp[l] < inp[r]):
                l+=1
            else:
                r-=1
        return maxWidth

    print(findContainerWithMostWater([1,8,6,2,5,4,8,3,7]))