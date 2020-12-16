class YesCounter(object):
    def __init__(self, input_file='input.txt'):
        self.input_file = input_file

    def execute(self):
        sum_anyone_yes = self.run_part_one()
        sum_everyone_yes = self.run_part_two()
        return sum_anyone_yes, sum_everyone_yes

    def run_part_one(self):
        group_answers = self.read_anyone_yes()
        return self.sum_counts(group_answers)

    def read_anyone_yes(self):
        group_answers = []
        group = []
        f = open(self.input_file, "r")
        for line in f:
            answer = list(line.strip())
            if answer:
                group += answer
            else:
                group_answers.append(set(group))
                group = []
        if group:
            group_answers.append(set(group))
        f.close()
        return group_answers

    def sum_counts(self, group_answers):
        sum = 0
        for answer in group_answers:
            sum += len(answer)
        return sum

    def run_part_two(self):
        group_answers = self.read_everyone_yes()
        return self.sum_counts(group_answers)

    def read_everyone_yes(self):
        group_answers = []
        group = []
        f = open(self.input_file, "r")
        for line in f:
            answer = set(line.strip())
            if answer:
                group.append(answer)
            else:
                if len(group) > 1:
                    group_answers.append(set.intersection(*group))
                else:
                    group_answers.append(group[0])
                group = []

        if group:
            if len(group) > 1:
                group_answers.append(set.intersection(*group))
            else:
                group_answers.append(group[0])
        f.close()
        return group_answers


# result = YesCounter(input_file='input_test.txt').execute()
result = YesCounter().execute()

print(result)
