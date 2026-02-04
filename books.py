def solve():
    n,t = map(int,input().split())
    book_time = list(map(int,input().split()))
    left = 0
    right = 1
    ans = 0
    pref_sum = [0]
    sum = 0
    for i in range(n):
        sum+=book_time[i]
        pref_sum.append(sum)
    for i in range(n):
        if pref_sum[right]-pref_sum[left] <= t:
            ans = max(ans,right-left)
        else:
            left+=1
        right+=1
    return ans

print(solve())
