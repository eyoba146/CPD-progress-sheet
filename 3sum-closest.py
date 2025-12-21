class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closests = []
        for i in range(len(nums)):
            middle, right = i+1,len(nums)-1
            while middle < right:
                summ = nums[i]+nums[middle]+nums[right] 
                if summ == target:
                    return summ
                closests.append(summ)
                if summ < target:
                    middle+=1
                else:
                    right-=1
        closests.append(target)
        closests.sort()
        index = closests.index(target)
        if index == 0:
            return closests[1]
        elif index == len(closests)-1:
            return closests[index-1]
        else:
            l_side = abs(closests[index]-closests[index-1])
            r_side = abs(closests[index]-closests[index+1])
            if l_side < r_side :
                return closests[index-1]
            return closests[index+1]



        
