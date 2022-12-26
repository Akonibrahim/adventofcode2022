import re

with open("input.txt") as f:
    monkey_set = f.read().split("\n\n")

class Monkey():
    
    def __init__(self, instructions=None):
        self.name = None
        self.instructions = instructions.split("\n")
        self.items = []
        self.activity = 0
        self.divisor = 1
        self.super_modulo = 1
        if instructions:
            self.parse_instructions()
    
    def parse_instructions(self):
        items = list(map(int,re.findall(r"\d+", self.instructions[1])))
        for item in items:
            self.add_item(item)
        self.name = self.instructions[0]
        self.divisor = int((re.findall(r"\d+", self.instructions[3]))[0])
        
    def add_item(self, item):
        self.items.append(item)
        self.activity += 1
    
    def new_item(self, modulo):
        item = self.items.pop(0)
        operation = self.instructions[2].split("Operation: new = old ")[-1]
        
        if operation == "* old":
            new =  item * item
        elif len(operation.split("* ")) > 1:
            new = item * int(operation.split("* ")[-1])
        elif len(operation.split("+ ")) > 1:
            new = item + int(operation.split("+ ")[-1])
        
        if modulo == 3:
            return new // modulo
        else: 
            return new % modulo

    def pass_to(self, new):
        if new % self.divisor == 0:
            return int((re.findall(r"\d+", self.instructions[4]))[0])
        else:
            return int((re.findall(r"\d+", self.instructions[5]))[0])

    def get_activity(self):
        return self.activity - len(self.items)

    def __repr__(self):
        return self.name


def monkey_in_the_middle(monkey_set, times=20, modulo=3):
    monkeys = []
    super_modulo = 1
    for monkey in monkey_set:
        m = Monkey(monkey)
        monkeys.append(m)
        super_modulo *= m.divisor

    for i in range(times):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                if modulo == 3:
                    item = monkey.new_item(modulo)
                else:
                    item = monkey.new_item(super_modulo)
                pass_to = monkey.pass_to(item)
                next_monkey = monkeys[pass_to]
                next_monkey.add_item(item)

    activities = sorted([m.get_activity() for m in monkeys])
    return activities[-1] * activities[-2]
        

print(f" Part 1 : {monkey_in_the_middle(monkey_set, 20, 3)}")
print(f" Part 2 : {monkey_in_the_middle(monkey_set, 10000, 4)}")

            

