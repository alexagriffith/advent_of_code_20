class BootCodeReader(object):
    def __init__(self, input_file='input.txt'):
        self.input_file = input_file

    def execute(self):
        instructions = self.read_instructions()
        acc_value, prev_instructions = self.get_acc_value(instructions)
        return self.get_acc_val_two(instructions, prev_instructions)

    def read_instructions(self):
        insructions = []
        f = open(self.input_file, "r")
        for line in f:
            # 0 means not been used.
            insructions.append(line.split() + [0])
        f.close()
        return insructions

    def get_acc_value(self, instructions):
        acc = 0
        instruction = 0
        prev_instructions = []
        while instructions[instruction][2] != 1:
            operation = instructions[instruction][0]
            argument = instructions[instruction][1]

            # go ahead and marked as seen
            instructions[instruction][2] = 1
            prev_instructions.append(instruction)

            if operation == 'nop':
                instruction += 1
            elif operation == 'jmp':
                instruction = self.inc_var(instruction, argument)
            elif operation == 'acc':
                acc = self.inc_var(acc, argument)
                instruction += 1

            if len(instructions) == instruction:
                prev_instructions.append(instruction)
                break

        return acc, prev_instructions


    def get_acc_val_two(self, instructions, prev_instructions_idxs):
        instructions = [[i[0], i[1], 0] for i in instructions]
        new_instructions, prev_instructions_idxs = self.find_jmp_or_nop_in_prev(instructions, prev_instructions_idxs)
        acc, prev_instructions = self.get_acc_value(new_instructions)
        if prev_instructions[-1] == len(instructions):
            return acc
        else:
            return self.get_acc_val_two(instructions, prev_instructions_idxs)

    def find_jmp_or_nop_in_prev(self, instructions, prev_instructions_idxs):
        prev_instruction_idx = prev_instructions_idxs.pop(-1)
        prev_instruction = instructions[prev_instruction_idx]
        operation = prev_instruction[0]
        if operation == 'jmp':
            instructions[prev_instruction_idx][0] = 'nop'
        elif operation == 'nop':
            instructions[prev_instruction_idx][0] = 'jmp'
        else:
            self.find_jmp_or_nop_in_prev(instructions, prev_instructions_idxs)

        return instructions, prev_instructions_idxs

    def inc_var(self, inc_var, argument):
        if '+' in argument:
            inc_var += int(argument[1:])
        if '-' in argument:
            inc_var -= int(argument[1:])
        return inc_var


# result = BootCodeReader(input_file='input_test.txt').execute()
result = BootCodeReader().execute()
print(result)