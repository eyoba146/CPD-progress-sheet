class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        summ = 0
        for i in range(len(nums)):
            summ+=nums[i]
            running_sum.append(summ)
        return running_sum
