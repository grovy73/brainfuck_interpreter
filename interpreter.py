import sys

program_file = sys.argv[1]
lines = []

with open(program_file, "r") as bf_file:
    for line in bf_file.readlines():
        lines.append(line if line[-1] != '\n' else line[:-1])


'''
    > - move right
    < - move left
    + - increment
    - - decrement
    [] - loop until 0
    . - print out ascii value
'''

class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.memory = [0]*self.size
        self.mem_pointer = 0

    def mov_right(self):
        self.mem_pointer += 1
        if self.mem_pointer > self.size:
            sys.exit("Memory Pointer is greater than size of memory block!")
    
    def mov_left(self):
        self.mem_pointer -= 1
        if self.mem_pointer < 0:
            sys.exit("Memory pointer == -1")

    def increment(self):
        self.memory[self.mem_pointer] += 1

    def decrement(self):
        self.memory[self.mem_pointer] -= 1

    def loop(self):
        # TODO!
        if self.memory[self.mem_pointer] <= 0:
            pass
        else:
            pass
    
    def print_ascii(self):
        print(chr(self.memory[self.mem_pointer]))

memblock = MemoryBlock(24)

for line in lines:
    if line == '':
        continue

    for command in line:
        if command == '>':
            memblock.mov_right()
        elif command == '<':
            memblock.mov_left()
        elif command == '+':
            memblock.increment()
        elif command == '-':
            memblock.decrement()
        elif command == '.':
            memblock.print_ascii()