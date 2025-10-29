class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        index1 = 0
        index2 = 0
        while nums1[index1] != nums2[index2] or nums1[index1] == nums2[index2]:
            if index1 >= len(nums1) or index2 >= len(nums2):
                return -1
            else:
                if nums1[index1] < nums2[index2]:
                    if index1 < len(nums1):
                        index1+=1
                    else:
                        return -1
            if index1 >= len(nums1) or index2 >= len(nums2):
                return -1
            else:
                if nums2[index2] < nums1[index1]:
                    if index2 < len(nums2):
                        index2+=1
                    else:
                        return -1
            if index1 >= len(nums1) or index2 >= len(nums2):
                return -1
            else:
                if nums1[index1] == nums2[index2]:
                    return nums1[index1]
        return -1     
