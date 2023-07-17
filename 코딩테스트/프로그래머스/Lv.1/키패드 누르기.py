# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    left = [1,4,7]
    right = [3,6,9]
    position = {
        1 : (0,0), 2 : (0,1), 3 : (0,2),
        4 : (1,0), 5 : (1,1), 6 : (2,2),
        7 : (2,0), 8 : (2,1), 9 : (0,2),
        "*" : (3,0), 0 : (3,1), "#" : (3,2),
    }
    hand_position = ["*", "#"]
    result = ""
    
    for number in numbers:
        if number in left:
            hand_position[0] = position[number]
            result += "L"
            
            
        elif number in right:
            hand_position[1] = position[number]
            result += "R"
            
            
        else:
            left_right_number = left_right(hand_position[0],hand_position[1], position, number,hand)
            if left_right_number == 'left':
                hand_position[0] = position[number]
                result += "L"
                
            else:
                hand_position[1] = position[number]
                result += "R"
                
    return result

def left_right(l,r, position, number,hand):
    left_distance = abs(position[l][0] - position[number][0]) + abs(position[l][1] - position[number][1])
    right_distance = abs(position[r][0] - position[number][0]) + abs(position[r][1] - position[number][1])
    
    if left_distance == right_distance:
        left_right_number = 'left' if hand == 'left' else 'right'
    else:
        left_right_number = 'left' if left_distance < right_distance else 'right'
    return left_right_number