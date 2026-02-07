class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        right = 1
        max_size = 1
        summ = 1
        comparisions = []
        if len(arr) == 1:
            return 1
        while right < len(arr):
            if arr[left] < arr[right]:
                comparisions.append('<')
            elif arr[left] > arr[right]:
                comparisions.append('>')
            else:
                comparisions.append('=')
            left+=1
            right+=1
        for i in range(len(comparisions)):
            if comparisions[i] == '=':
                summ = 1
            elif i == 0 or comparisions[i] != comparisions[i-1]:
                summ += 1
            else: 
                summ = 2
            max_size = max(max_size, summ)
        return max_size
