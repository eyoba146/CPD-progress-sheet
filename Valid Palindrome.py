class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        letters = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                letters.append(s[i].lower())
        if len(letters) == 0:
            return True   
        r = len(letters) -1
        while r > l:
            if letters[l] != letters[r]:
                return False
            r-=1
            l+=1
        return True
