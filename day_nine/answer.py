import time

class ErrorEncoder(object):
    def __init__(self, input_file='input.txt', preamble=25):
        self.input_file = input_file
        self.preamble = preamble

    def execute(self):
        start = time.time()
        nums = self.read_input()
        answer = self.compare_sums(nums)
        end = time.time()
        return answer, end - start

    def read_input(self):
        f = open(self.input_file, "r")
        nums = []
        for line in f:
            nums.append(int(line))
        f.close()
        return nums

    def compare_sums(self, nums):
        idx1 = 0
        idx2 = self.preamble - 1
        num_idx = self.preamble
        not_sum_number = None

        while not_sum_number is None:
            prev_nums = sorted(nums[idx1:idx2 + 1])
            num = nums[num_idx]

            # if the num is lower than or above the possible range.
            if True in [self.is_sum(prev_nums, num) is False, num - prev_nums[-1] > prev_nums[-1],
                        num - prev_nums[0] < prev_nums[0]]:
                not_sum_number = num
            else:
                idx1 += 1
                idx2 += 1
                num_idx += 1

        return not_sum_number

    def is_sum(self, prev_nums, num):
        for n in prev_nums:
            if num - n in prev_nums:
                return True
        return False


# result = ErrorEncoder(input_file='input_test.txt', preamble=5).execute()
result, time = ErrorEncoder().execute()
print(result, time)
