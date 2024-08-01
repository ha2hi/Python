def solution(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    
    if len(s) < 2 and s == s[::-1]:
        return len(s)
    
    res = ''
    for i in range(len(s)-1):
        res = max(res, expand(i, i+1), expand(i, i+2), key = len)
    return len(res)


s = "a"
solution(s)
