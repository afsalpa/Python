class MergeTwoSortedArray:

    def mergeTwoArrays(num1 : list[int], num2 : list[int]) -> list[int]:

        result = []
        length = max(len(num1), len(num2))

        for v in range(length):
            if v < len(num1):
                result.append(num1[v])
            if v < len(num2):
                result.append(num2[v])
        return result

    print(mergeTwoArrays([1,2,4],[1,3,4]))
    print(mergeTwoArrays([],[0]))
    print(mergeTwoArrays([],[]))