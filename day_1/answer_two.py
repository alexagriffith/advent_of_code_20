def read_input():
    nums = []
    f = open("input.txt", "r")
    for line in f:
        num = int(line.strip())
        nums.append(num)
    f.close()
    return sorted(nums)


def compare_nums(nums):
    large_cnt = 1
    small_cnt = 0
    while large_cnt < len(nums) - 1:
        larger_num = nums[large_cnt]
        smaller_num = nums[small_cnt]
        remaining = 2020 - larger_num - smaller_num
        if remaining > 0:
            if remaining in nums:
                return remaining * larger_num * smaller_num
            else:
                large_cnt += 1
        else:
            small_cnt += 1
            large_cnt = small_cnt + 1


if __name__ == '__main__':
    nums = read_input()
    print(compare_nums(nums))