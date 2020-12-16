def read_input():
    """
    split the numbers into two categories:
    >= 2020 and < 2020
    """
    greater_than_or_1010 = []
    less_than_1010 = []
    f = open("input.txt", "r")
    for line in f:
        num = int(line.strip())
        if num >= 1010:
            greater_than_or_1010.append(num)
        if num < 1010:
            less_than_1010.append(num)
    f.close()
    return greater_than_or_1010, less_than_1010


def compare_nums(greater_than_or_1010, less_than_1010):
    """
    the remainder of one list should be present in
    the other list
    """
    if greater_than_or_1010.count(1010) == 2:
        return 1010 * 1010
    for num in greater_than_or_1010:
        remaining = 2020 - num
        if remaining in less_than_1010:
            return num * remaining


if __name__ == '__main__':
    greater_than_or_1010, less_than_1010 = read_input()
    print(compare_nums(greater_than_or_1010, less_than_1010))
