# I THINK THIS IS ALREADY THE OPTIMAL SOLUTION
def count_substring(string, sub_string):
    # count how many times sub_string in string
    count = 0
    for i in range(len(string)):
        for j in range(len(string) + 1):
            subset = string[i:j]
            if subset == sub_string:
                count += 1

    return count


if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"

    count = count_substring(string, sub_string)
    print(count)
