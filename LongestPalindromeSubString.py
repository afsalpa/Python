class LongestPalindromeSubSting:

    def expand(inp : str, l: int, r :int) -> str:
        while (l >=0 and r < len(inp) and inp[l] == inp[r]):
            l-=1;
            r+=1;
        return inp[l+1:r]

    inp = "aacabdkacaa"
    result = ""
    for l in range(len(inp)):
        sub1 = expand(inp, l, l)
        if (len(sub1) > len(result)):
            result = sub1
        sub2 = expand(inp, l, l + 1)
        if (len(sub2) > len(result)):
            result = sub2
    print(result)
