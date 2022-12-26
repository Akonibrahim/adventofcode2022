with open("input.txt", "r") as file:
    positions = file.read().splitlines()

def part1(positions):
    x, cycle, total = 1, 0, 0
    for line in positions:
        n = 1 if line.startswith("n") else 2
        for _ in range(n):
            cycle += 1
            if cycle in range(20,221,40):
                total += cycle * x
        if n == 2: x += int(line.split(" ")[-1])
    return total

print(f"PART 1 : {part1(positions)}")

def display_screen(pixels):
    for i in pixels:
        print("".join(i))
    return None

def get_row(c):
    return 0 if c <= 40 else 1 if c <= 80 else 2 if c <= 120 else 3 if c <= 160 else 4 if c <= 200 else 5

def part2(positions):
    pixels = [[" "] * 40 for a in range(40,241,40)]
    x, cycle = 1, 0
    for line in positions:
        n = 1 if line.startswith("n") else 2
        for _ in range(n):
            row = get_row(cycle)
            if cycle % 40 in range(x-1,x+2):
                pixels[row][cycle % 40] = "#"
            cycle += 1
        if n == 2: x += int(line.split(" ")[-1])
    return display_screen(pixels)

print("PART 2")
part2(positions)