with open("input.txt", "r") as file:
    grid = [list(a) for a in file.read().splitlines()]


def count_visible_trees(grid):
    # Traverse a 2d grid
    cols = len(grid)
    rows = len(grid[0])
    visible = 0
    scenic_score = 0
    for row in range(rows):
        for col in range(cols):
            # The outer trees are all visible
            if row == 0 or col == 0 or row+1 == rows or col+1 == cols:
                visible += 1
            else:
                curr = grid[row][col]
                point_status = {"left": False, "right": False, "top": False, "bottom": False}
                
                # Check left in the grid
                l = 0
                for i in range(col-1, -1, -1):
                    l += 1
                    if grid[row][i] >= curr:
                        point_status["left"] = True
                        break
                # Check right in the grid
                r = 0
                for i in range(col+1, rows):
                    r += 1
                    if grid[row][i] >= curr:
                        point_status["right"] = True
                        break
                # Check top in the grid
                t = 0
                for i in range(row-1, -1, -1):
                    t += 1
                    if grid[i][col] >= curr:
                        point_status["top"] = True
                        break

                # Check bottom in the grid
                b = 0
                for i in range(row+1, cols):
                    b += 1
                    if grid[i][col] >= curr:
                        point_status["bottom"] = True
                        break

                if t * l * r * b > scenic_score:
                    scenic_score = t * l * r * b


                if not all(point_status.values()):
                    visible += 1
    return visible, scenic_score

print(f"Part 1 & Part 2: {count_visible_trees(grid)}")
