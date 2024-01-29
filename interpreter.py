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
        self.loop_start = 0

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

    def start_loop(self, pc):
        self.loop_start = pc
    
    def reset_loop(self, pc):
        if self.memory[self.mem_pointer] == 0:
            return pc
        else:
            return self.loop_start

    def print_ascii(self):
        print(chr(self.memory[self.mem_pointer]))

memblock = MemoryBlock(24)

pc = 0
for line in lines:
    if line == '':
        continue
    
    pc = 0
    while(pc < len(line)):
        if line[pc] == '>':
            memblock.mov_right()
        elif line[pc] == '<':
            memblock.mov_left()
        elif line[pc] == '+':
            memblock.increment()
        elif line[pc] == '-':
            memblock.decrement()
        elif line[pc] == '.':
            memblock.print_ascii()
        elif line[pc] == '[':
            memblock.start_loop(pc)
        elif line[pc] == ']':
            pc = memblock.reset_loop(pc)
            
        pc += 1