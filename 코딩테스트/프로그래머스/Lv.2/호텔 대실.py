# https://school.programmers.co.kr/learn/courses/30/lessons/155651
def solution(book_time):
    book_time.sort(key=lambda x: x[0]) 
    time = list(map(int, book_time[0][1].split(':')))
    room = [time[0] * 60 + time[1] + 10]

    for i in range(1, len(book_time)):
        tmp_s = list(map(int, book_time[i][0].split(':')))
        tmp_e = list(map(int, book_time[i][1].split(':')))
        tmp_time = (tmp_s[0] * 60) + tmp_s[1]
        ch = False
        for idx, x in enumerate(room):
            if tmp_time >= x:
                room[idx] = (tmp_e[0] * 60) + (tmp_e[1] + 10)
                ch = True
                break
        if not ch:
            room.append((tmp_e[0] * 60) + (tmp_e[1] + 10))

    return len(room)
