class LongestSubstringWithOutRepeating:

    # solving problem in O(n)
    # solving problem window solution 

    def findLongestSubsString(inp: str) -> int:
        if str is None:
            return 0 

        l : int = 0
        seen = {}
        length : int = 0

        # loop runs only once to find the solution
        for r in range(0, len(inp)):
            c = inp[r]
            print(c, r)
            print("l index", l)
            if c in seen and seen[c] >= l:  
                l = seen[c] + 1
                print("Inside if", l)
            else:
                length = max(length, r - l +  1)
                print("Inside else", length)
            seen[c] = r
            print(seen)

        return length

    print(findLongestSubsString("abcabcbb"))
