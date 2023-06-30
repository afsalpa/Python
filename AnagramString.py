class AnagramString:

    def findAnagaramString(a, b):
        inp1 = [*a]
        inp1.sort()
        inp2 = [*b]
        inp2.sort()
        print(inp2)
        return inp1 == inp2

    resp = findAnagaramString("ate", "we")
    print(resp)