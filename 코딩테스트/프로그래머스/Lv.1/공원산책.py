# https://school.programmers.co.kr/learn/courses/30/lessons/172928

"""
def solution(park, routes):
    park_len = len(park)
    grid = []
    for i in range(park_len):
        grid.append([])
        for idx, x in enumerate(park[i]):
            if x == "S":
                H = i
                W = idx
            grid[i].append(x)

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    grid_row = len(grid)
    grid_col = len(grid[0])
    for route in routes:
        op, n = route.split()
        n = int(n)
        next_H = H
        next_W = W
        check = 0
        if op == 'N':
            for _ in range(n):
                next_H += dx[0] 
                next_W += dy[0] 
                if not 0<=next_H<grid_row or not 0<=next_W<grid_col or grid[next_H][next_W] == "X":
                    check = 1
            if check == 0:
                H = next_H
                W = next_W
                
        elif op == 'E':
            for _ in range(n):
                next_H += dx[1] 
                next_W += dy[1] 
                if not 0<=next_H<grid_row or not 0<=next_W<grid_col or grid[next_H][next_W] == "X":
                    check = 1
            if check == 0:
                H = next_H
                W = next_W
        elif op == 'S':
            for _ in range(n):
                next_H += dx[2] 
                next_W += dy[2] 
                if not 0<=next_H<grid_row or not 0<=next_W<grid_col or grid[next_H][next_W] == "X":
                    check = 1
            if check == 0:
                H = next_H
                W = next_W
        elif op == 'W':
            for _ in range(n):
                next_H += dx[3] 
                next_W += dy[3] 
                if not 0<=next_H<grid_row or not 0<=next_W<grid_col or grid[next_H][next_W] == "X":
                    check = 1
            if check == 0:
                H = next_H
                W = next_W
    return [H,W]
"""

class Dog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

    @classmethod
    def InitDistinct(self, park):
        for row, value1 in enumerate(park):
            for col, value2 in enumerate(value1):
                if value2 == "S":
                    return row, col
    
    def move(self, park, direct, distance):
        x, y = self.x + self.d[direct][0] * distance, self.y + self.d[direct][1] * distance
        if x < 0 or x >= len(park) or y < 0 or y >= len(park[0]):
            return park
        
        if "X" in park[x][min(y, self.y) : max(y, self.y)+1] or "X" in [row[y] for row in park[min(x, self.x) : max(x, self.x)+1]]:
            return park

        park[self.x][self.y] = 0
        park[x][y] = "S"
        self.x = x
        self.y = y
        return park


def solution(park, routes):
    park = [list(row) for row in park]
    x, y = Dog.InitDistinct(park)

    dog = Dog(x,y)
    
    for route in routes:
        direct, distance = route.split()

        park = dog.move(park, direct, int(distance))
    
    return [dog.x, dog.y]