class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        boat_count = 0
        while left <= right:
            if left == right:
                boat_count+=1
                break
            if people[left]+people[right] > limit:
                if limit-people[right] <= people[left]:
                    boat_count+=1
                    right-=1
                else:
                    boat_count+=2
                    left+=1
                    right-=1
            if people[left]+people[right] <= limit:
                boat_count+=1
                left+=1
                right-=1
        return boat_count
