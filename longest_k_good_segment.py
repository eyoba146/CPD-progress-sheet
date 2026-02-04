def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    freq = {}
    left = 0
    l = 0
    lenn = 0
    for right in range(n):
        freq[a[right]] = freq.get(a[right], 0) + 1
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        if right - left + 1 > lenn:
            lenn = right - left + 1
            l = left
    print(l + 1, l + lenn)

solve()
