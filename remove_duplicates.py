class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        corrected_nums = []
        dictt = {}
        index = 0
        for i in range(len(nums)):
            if nums[i] in dictt:
                if nums[index] == nums[i]:
                    pass
            else:
                dictt[nums[i]] = 1
                corrected_nums.append(nums[i])
        for i in range(len(corrected_nums)):
            nums[i] = corrected_nums[i]
        return len(corrected_nums)
