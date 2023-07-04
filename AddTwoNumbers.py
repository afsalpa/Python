class AddTwoNumbers:
    def addTwoNumbs(a : list[int], b: list[int]) -> list[int]:
        idx : int
        dict = {}
        
        finalRange = len(a) if len(a) > len(b) else len(b)
        aRange = len(a)
        bRange = len(b)

        for idx in range(finalRange):            
            if idx < aRange:
                if idx == 0:
                    numb1 = str(a[idx])
                else:
                    numb1 = str(a[idx]) + numb1
            if idx < bRange:
                if idx == 0:
                    numb2 = str(b[idx])
                else:
                    numb2 = str(b[idx]) + numb2

            print(numb1)
            print(numb2)
        sumVal = int(numb1) + int(numb2)
        sumList = [int(x) for i,x in enumerate(str(sumVal))]        
        print(sumList)
        reversed_list = sumList[::-1]
        print(reversed_list)
        return sumList.reverse()

    resp = addTwoNumbs([2,4,3], [5,6,4])
    print(resp)

    resp = addTwoNumbs([9,9,9,9,9,9,9], [9,9,9,9])
    print(resp)
    