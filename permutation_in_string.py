class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        need = {}
        window = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
        for i in range(n):
            window[s2[i]] = window.get(s2[i], 0) + 1
        if window == need:
            return True
        for i in range(n, m):
            window[s2[i]] = window.get(s2[i], 0) + 1
            left_char = s2[i - n]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if window == need:
                return True
        return False
