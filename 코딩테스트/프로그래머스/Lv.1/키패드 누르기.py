# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    res = ''
    left = (3,0)
    right = (3,2)
    direct = {1: (0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}
    for number in numbers:
        if number in {1,4,7}:
            res += 'L'
            left = direct[number]

        elif number in {3,6,9}:
            res += 'R'
            right = direct[number]

        else:
            left_diff = abs(left[0] - direct[number][0]) + abs(left[1] - direct[number][1])
            right_diff = abs(right[0] - direct[number][0]) + abs(right[1] - direct[number][1])

            if left_diff > right_diff:
                res += 'R'
                right = direct[number]

            elif left_diff < right_diff:
                res += 'L'
                left = direct[number]

            else:
                if hand == 'right':
                    res += 'R'
                    right = direct[number]
                else:
                    res += 'L'
                    left = direct[number]
    return res