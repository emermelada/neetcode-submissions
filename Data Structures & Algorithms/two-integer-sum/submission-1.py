class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            find = target - nums[i]
            if find in nums[i+1:]:
                return [i, nums.index(find, i +1)]