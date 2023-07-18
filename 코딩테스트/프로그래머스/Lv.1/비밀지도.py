# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n,arr1,arr2):
    answer = []
    for i in range(n):
        arr1[i] = format(arr1[i],'b')
        arr2[i] = format(arr2[i],'b')
        
        k = ""
        a = str(int(arr1[i]) + int(arr2[i]))
        if len(a) < n:
            a = '0' * (n-len(a)) + a
        for j in a:
            if j=='0':
                k += ' '
            else:
                k += '#'
        answer.append(k)
    return answer