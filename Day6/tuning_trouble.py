with open("input.txt", "r") as file:
    lines = file.read()

# Part 1 : Find index when there are non repeting 4 digit characters appears first
# Part 2 : Find index when there are non repeting 14 digit characters appears first
def find_patters(lines, step):
    for i in range(len(lines)):
        if(len(set(lines[i:i+step]))) == step:
            return step + i

print(find_patters(lines, 4))
print(find_patters(lines, 14))