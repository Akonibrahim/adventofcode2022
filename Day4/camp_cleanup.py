with open("input.txt", "r") as file:
    elfs_sections = file.read().splitlines()

boundings, overlaps = 0, 0
for sections in elfs_sections:
    elf1 , elf2 = sections.split(",")
    elf1_start, elf1_end = map(int,elf1.split("-"))
    elf2_start, elf2_end = map(int,elf2.split("-"))
    
    # Part 1 :  Find bounding pairs
    if elf1_start <= elf2_start and elf1_end >= elf2_end:
        boundings += 1
    elif elf1_start >= elf2_start and elf1_end <= elf2_end:
        boundings += 1
    
    # Part 2 : Find overlapping pairs
    if elf1_start <= elf2_end and elf1_end >= elf2_start:
        overlaps += 1 

print(boundings, overlaps)
    
        

