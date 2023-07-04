class PalindromeNumber:
    def findPalindromeNumber(x : int) -> bool:
        reverse = str(x)
        reverse = reverse[::-1]
        return x == int(reverse)
    
    print(findPalindromeNumber(121))
    print(findPalindromeNumber(123))
    print(findPalindromeNumber(12521))