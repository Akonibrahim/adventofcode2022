import re

with open("input.txt", "r") as file:
    all_data = [a.replace("    "," ") for a in file.read().splitlines()]

separator = all_data.index("")
stacks_inverse,instructions = all_data[0:separator-1], all_data[separator+1:]

def get_stacks(num_of_stacks):
    global stacks_inverse
    stacks = [[] for _ in range(num_of_stacks)]
    for stack_info in stacks_inverse:
        for index, element in enumerate(stack_info.split(" ")):
            if element:
                stacks[index].insert(0, element.replace("]","").replace("[",""))
    return stacks


def shuffle_stack(stacks, part):
    global instructions
    for instruction in instructions:
        num_of_times, from_stack, to_stack = map(int,re.findall(r'\d+', instruction))
        for n in range(num_of_times):
            if part == "part_1":
                stacks[to_stack-1].append(stacks[from_stack-1].pop())
            else:
                stacks[to_stack-1].append(stacks[from_stack-1].pop(-(num_of_times-n)))
    return "".join([a[-1] for a in stacks])

stacks = get_stacks(9)
print(shuffle_stack(stacks,"part_1"))
stacks = get_stacks(9)
print(shuffle_stack(stacks,"part_2"))