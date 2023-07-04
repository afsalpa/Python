class LongestPalindromeSubSting:

    def findLongPal(inp : str) -> bool:
        inpList =  [*inp]
        return inpList == inpList[::-1]
    
    def checkPalindrome(inp : str):
        inpList =  [*inp]
        return inpList == inpList[::-1]

    print(findLongPal("abscd"))