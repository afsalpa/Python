class GenerateParanthesis2:

    def generateParanthesis(num):

        result = []
        stack = []

        def backtracking(o, c):

            if o == c == num:
                result.append("".join(stack))
            
            if o < num:
                stack.append("(")
                backtracking(o + 1, c)
                stack.pop()
            
            if c < o:
                stack.append(")")
                backtracking(o, c + 1)
                stack.pop()        
            
            return ",".join(result)

        return backtracking(0,0)
    
    print(generateParanthesis(3))

            
