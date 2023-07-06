class GenerateParanthesis:
    
    def generate(n):
        
        depth = {0:0}
        stack = []
        result = []

        def recur(openN, closeN,loopId):
            depth[0] = depth[0] + 1

            print("Current Depth", depth)
            if openN == closeN == n:
                result.append("".join(stack))
                print(loopId, "Maxed out")
            
            if openN < n:
                print(loopId, " Inside for appending (")
                stack.append("(")
                recur(openN + 1, closeN, str(openN + 1) + "_" +  str(closeN))
                stack.pop()
            
            if closeN < openN:
                print(loopId, " Inside for appending )")
                stack.append(")")
                recur(openN, closeN + 1, str(openN) + "_" + str(closeN + 1))
                stack.pop()
            depth[0] = depth[0] - 1
            print(loopId, "Exit")          
    
        print(recur(0,0,"0_0"))
        return result
    
    generate(3)
    

    
