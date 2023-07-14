# https://school.programmers.co.kr/learn/courses/30/lessons/161990#qna
class File:
    @classmethod
    def process(self, wallpaper):
        lux = luy = 51
        rux = ruy = 0
        for x, row in enumerate(wallpaper):
            for y, value in enumerate(row):
                if value == "#":
                    print(x,y)
                    lux = min(lux, x)
                    luy = min(luy, y)
                    rux = max(rux, x + 1)
                    ruy = max(ruy, y + 1)
        return lux, luy, rux, ruy

def solution(wallpaper):
    wallpaper = [list(row) for row in wallpaper]
    lux, luy, rux, ruy = File.process(wallpaper)

    return lux, luy, rux, ruy