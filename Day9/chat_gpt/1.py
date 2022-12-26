#parse the input
with open("../input.txt", "r") as file:
    lines = file.read().splitlines()
#initialize the position of the head and tail to (0,0)
hx, hy, tx, ty = 0, 0, 0, 0

#initialize a set to store the positions the tail visited
visited = set()

#add the starting position of the tail to the set
visited.add((tx, ty))

#iterate through each motion
for line in lines:
  #get the direction and distance of the motion
  direction, distance = line[0], int(line[1:])

  #move the head in the specified direction
  if direction == "R":
    hx += distance
  elif direction == "L":
    hx -= distance
  elif direction == "U":
    hy += distance
  elif direction == "D":
    hy -= distance

  #if the head and tail are not in the same row or column
  if hx != tx and hy != ty:
    #move the tail one step diagonally in the direction that minimizes its taxicab distance to the head
    if abs(hx - tx) < abs(hy - ty):
      if hx > tx:
        tx += 1
      else:
        tx -= 1
    else:
      if hy > ty:
        ty += 1
      else:
        ty -= 1

  #if the head and tail are in the same row or column
  elif hx == tx or hy == ty:
    #if the head is two steps directly up, down, left, or right from the tail, move the tail one step in the same direction as the head
    if direction == "R" and hx - tx == 2:
      tx += 1
    elif direction == "L" and tx - hx == 2:
      tx -= 1
    elif direction == "U" and hy - ty == 2:
      ty += 1
    elif direction == "D" and ty - hy == 2:
      ty -= 1

  #add the new position of the tail to the set of visited positions
  visited.add((tx, ty))

#output the number of positions the tail visited at least once
print(len(visited))
