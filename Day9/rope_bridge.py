import numpy as np
with open("input.txt", "r") as file:
    positions = file.read().splitlines()

def solve(positions):
    grid = np.zeros((14,14))
    tail = [5,5]
    visited = set()
    grid[tail[0]][tail[1]] = 6
    # visited.add(tuple(tail))
    for position in positions:
        direction, distance = position.split(" ")
        distance = int(distance)
        if distance > 1:
            # print("sd")
            if direction == "R":
                for i in range(1, distance):
                    tail[1] += 1
                    grid[tail[0]][tail[1]] = 1
                    visited.add(tuple(tail))
            elif direction == "L":
                for i in range(1, distance):
                    tail[1] -= 1
                    grid[tail[0]][tail[1]] = 2
                    visited.add(tuple(tail))
            elif direction == "U":
                print(tail)

                for i in range(1, distance):
                    if i == 1:
                        
                    tail[0] -= 1
                    grid[tail[0]][tail[1]] = 3
                    visited.add(tuple(tail))
                    print(tail)
            elif direction == "D":
                for i in range(1, distance):
                    tail[0] += 1
                    grid[tail[0]][tail[1]] = 4
                    visited.add(tuple(tail))

    print('========|"grid"|========')
    print(grid)
    print('=================')
    
solve(positions)