class TwoSum2:

    def twoSum(nums : list[int], target : int) -> list[int]:
        values = {}
        print (list(enumerate(nums)))
        idx: int
        value : int
        for idx, value in enumerate(nums):
            diff = (int(target) - value)
            if diff in values:
                return [values.get(diff),idx]
            else: 
                values[int(value)] = int(idx)
                print(values)

    resp = twoSum(["3","2","3"],6)
    print(resp)