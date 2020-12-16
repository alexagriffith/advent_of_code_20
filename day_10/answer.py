from itertools import permutations, combinations

class ArrayAdapter(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def execute(self):
        inputs = self.read_input()
        nums, dist = self.find_distribution(inputs)
        return self.find_permutations(inputs, dist, inputs[-1])

    def read_input(self):
        inputs = []
        f = open(self.input_file, "r")
        for line in f:
            inputs.append(int(line.strip()))
        return sorted(inputs)

    def find_distribution(self, inputs):
        last_voltage = 0
        distribution = {1: 0, 2: 0, 3: 1}
        for input in inputs:
            difference = input - last_voltage
            distribution[difference] += 1
            last_voltage = input
        print(distribution)
        return distribution[1] * distribution[3], distribution

    def find_permutations(self, inputs, distribution, adapter):
        pass

result = ArrayAdapter(input_file='input_small_test.txt').execute()
print(result)
