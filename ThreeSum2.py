class ThreeSum2:

    def findThreeSum(nums : list[int]) -> int:
        print(nums)
        nums.sort()
        print('After sorting', nums)
        result = []

        for i, v in enumerate(nums):
            
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = v + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                   result.append([v, nums[l], nums[r]])
                   l += 1
                   while nums[l] == nums[l-1] and l <  r:
                       l += 1
        return result

    #print(findThreeSum([-1,0,1,2,-1,-4]))

    print(findThreeSum([0,0,0,0]))