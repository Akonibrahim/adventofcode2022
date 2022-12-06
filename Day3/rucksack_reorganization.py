import string

with open("input.txt", "r") as file:
    sacks = file.read().splitlines()

def get_value_for_letter(intersection):
    if intersection.islower():
        return string.ascii_lowercase.index(intersection) + 1
    else:
        return string.ascii_uppercase.index(intersection) + 27

# Part 1 : What is the sum of the priorities of those item types?
def part_1(sacks):
    score = 0
    for item in sacks:
        # score += get_value_for_letter(next(iter(set(item[0:len(item) // 2]) & set(item[len(item) // 2:]))))
        half_point = len(item) // 2
        first, second = set(item[0:half_point]) , set(item[half_point:])
        intersection = first & second
        intersection = next(iter(intersection))
        score += get_value_for_letter(intersection)
    return score

# print(part_1(sacks))

# Part 2 : Find the common letter in first three line and calculate total.
def part_2(sacks):
    group = []
    score = 0
    for item in sacks:
        group.append(item)
        if len(group) == 3:
            first, second, third = set(group[0]) , set(group[1]), set(group[2])
            intersection = first & second & third
            intersection = next(iter(intersection))
            score += get_value_for_letter(intersection)
            group = []

    return score

print(part_2(sacks))






