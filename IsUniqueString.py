class IsUniqueString:

    def uniqueCheck(inp): 
        charSet = []
        for x in inp:
            if x in charSet:
                return False
            charSet.append(x)
        return True
    resp = uniqueCheck("aeeesd")
    print(resp)