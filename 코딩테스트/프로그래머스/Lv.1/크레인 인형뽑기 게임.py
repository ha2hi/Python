# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(boards, moves):
    moves = map(lambda x : x-1, moves)
    k = [0]
    cnt = 0
    for i in moves:
        for board in boards:
            if board[i] != 0:
                k.append(board[i])
                board[i] = 0
                
                if k[-1] == k[-2]:
                    k.pop()
                    k.pop()
                    cnt += 2
                break
    
    return cnt