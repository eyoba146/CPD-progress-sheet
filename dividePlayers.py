class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teams = []
        chemistry = -1
        left = 0
        is_first = True
        not_equal = False
        equal = 0
        right = len(skill)-1
        while left < right:
            teams.append([skill[left],skill[right]])
            if is_first:
                equal = skill[left]+skill[right]
                is_first = False
            else:
                if skill[left]+skill[right] != equal:
                    not_equal = True
                    break
            left+=1
            right-=1
        if not_equal:
            return chemistry
        chemistry = 0
        for i in range(len(teams)):
            chemistry+=(teams[i][0]*teams[i][1])
        return chemistry
