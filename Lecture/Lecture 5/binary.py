def binary(digits):
    # reverse the string by using slicing
    digits = digits[::-1]

    # we iterate
    # it is a tracker (should be outside of loop)
    value = 0
    # starts at a 0 and ending in len(digits)
    for i in range(len(digits)):
        # the formula
        value = value + int(digits[i]) * (2 ** i)
    # watch for the indentation
    return value


def main():
    print("001", binary("001"))  # 1
    print("100", binary("100"))  # 4
    print("101", binary("101"))  # 5
    print("111", binary("111"))  # 7

    print(["1", "1", "1"], binary(["1", "1", "1"]))


if __name__ == "__main__":
    main()
