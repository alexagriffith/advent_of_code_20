import re


def read_input():
    # group the min, max, letter, and password
    r = re.compile("([0-9]+)\\-([0-9]+)\\s([a-z])\\:\\s([a-z]+)")
    f = open("input.txt", "r")
    policies_passwords = []
    for line in f:
        grouped = r.findall(line)[0]
        # this isn't efficient but whatever
        policy_password = dict(min=int(grouped[0]), max=int(grouped[1]), letter=grouped[2], pwd=grouped[3])
        policies_passwords.append(policy_password)
    f.close()
    return policies_passwords


def validate_num_occurences(policies_passwords):
    num_valid = 0
    for policy_password in policies_passwords:
        # this feels inefficient too
        count = policy_password['pwd'].count(policy_password['letter'])
        if policy_password['min'] <= count <= policy_password['max']:
            num_valid += 1
    return num_valid

def validate_position_occurnces(policies_passwords):
    num_valid = 0
    #data bc im lazy
    for data in policies_passwords:
        in_min = data['pwd'][data['min'] - 1] == data['letter']
        in_max = data['pwd'][data['max'] - 1] == data['letter']
        if in_min + in_max == 1:
            num_valid += 1
    return num_valid


if __name__ == '__main__':
    policies_passwords = read_input()
    print(validate_num_occurences(policies_passwords))
    print(validate_position_occurnces(policies_passwords))
