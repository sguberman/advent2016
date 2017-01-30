class AssemBunny:

    def __init__(self, instructions, registers, start=0):
        self.instructions = instructions
        self.registers = registers
        self.step = start
        self.instruction_set = {'inc': self.inc,
                                'dec': self.dec,
                                'jnz': self.jnz,
                                'cpy': self.cpy,
                                }

    def inc(self, register):
        self.registers[register] += 1
        self.step += 1

    def dec(self, register):
        self.registers[register] -= 1
        self.step += 1

    def jnz(self, x, steps):
        if x in self.registers:
            if self.registers[x] != 0:
                self.step += int(steps)
            else:
                self.step += 1
        elif int(x) != 0:
            self.step += int(steps)
        else:
            self.step += 1

    def cpy(self, x, register):
        if x in self.registers:
            self.registers[register] = self.registers[x]
        else:
            self.registers[register] = int(x)
        self.step += 1

    def execute(self):
        while self.step < len(self.instructions):
            self.evaluate(self.instructions[self.step])
        return self.registers

    def evaluate(self, instruction):
        name, *args = instruction.split()
        print(self.step, self.registers, name, args)
        self.instruction_set[name](*args)


if __name__ == '__main__':
    instructions = open('input.txt').readlines()
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    asm = AssemBunny(instructions, registers)
    results = asm.execute()
    print(results)
