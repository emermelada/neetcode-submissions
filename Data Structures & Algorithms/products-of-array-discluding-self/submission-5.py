class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        zeros =0

        for i in range(len(nums)):
            if nums[i] != 0:
                allzero = False
                total *= nums[i]
            else:
                zeros += 1

        if zeros > 1:
            total = 0        

        for i in range(len(nums)):
            if zeros > 0:
                if nums[i] == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // nums[i])

        return res