import time

class ErrorEncoder(object):
    def __init__(self, input_file='input.txt', preamble=25):
        self.input_file = input_file
        self.preamble = preamble

    def execute(self):
        start = time.time()
        nums = self.read_input()
        answer = self.compare_sums(nums)
        end1 = time.time()
        contiguous_nums_sum = self.find_contiguous_nums(nums, answer)
        end2 = time.time()
        return contiguous_nums_sum, end1 - start, end2 - start
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

    def find_contiguous_nums(self, nums, answer):
        contig_nums = []
        sum = 0
        idx = 0

        while sum != answer:
            if sum > answer:
                sum -= contig_nums.pop(0)
            if sum < answer:
                idx += 1
                sum += nums[idx]
                contig_nums.append(nums[idx])

        contig_nums = sorted(contig_nums)
        print(contig_nums,sum)
        return contig_nums[0] + contig_nums[-1]




# result, time1, time2 = ErrorEncoder(input_file='input_test.txt', preamble=5).execute()
result, time1, time2 = ErrorEncoder().execute()
print(result, time1, time2)
