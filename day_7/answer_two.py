import re

class BagProcessor(object):
    def __init__(self, input_file='input.txt'):
        self.input_file = input_file
        self.num = 0

    def execute(self):
        all_bags = self.read_rules()
        return self.get_num_bags(all_bags, 'shiny gold') - 1


    def read_rules(self):
        parent_exp = re.compile('''^(.+) bags contain''')
        child_exp = re.compile('''(?:contain|,)? ([0-9]+) ([a-z ]+) bag(?:s?)''')
        f = open(self.input_file, "r")
        all_bags = {}
        for line in f:
            parent = parent_exp.findall(line)[0]
            children = child_exp.findall(line)
            all_bags[parent] = {}
            for child in children:
                if not child:
                    continue
                all_bags[parent][child[1]] = int(child[0])

        f.close()
        return all_bags

    def get_num_bags(self, all_bags, bag_color):
        count = 1
        for bag in all_bags[bag_color]:
            num_bag = all_bags[bag_color][bag]
            count += num_bag * self.get_num_bags(all_bags, bag)
            print(count)
        return count

# result = BagProcessor(input_file='input_test_two.txt').execute()
result = BagProcessor().execute()
print(result)