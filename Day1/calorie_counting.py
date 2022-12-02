with open("input.txt", "r") as file:
    calories = file.read().splitlines()

# Part 1 : Find the most calories carried by elf
largest_calorie, current_elf_calorie, all_calories = 0, 0, []
for elf, calorie in enumerate(calories):
    if calorie == "":
        all_calories.append(current_elf_calorie)
        if current_elf_calorie > largest_calorie:
            largest_calorie = current_elf_calorie
        current_elf_calorie = 0
    else:
        current_elf_calorie += int(calorie)
print(largest_calorie)

# Part 2 : Find top three elfs carrying most calories
print(sum(sorted(all_calories)[::-1][0:3]))