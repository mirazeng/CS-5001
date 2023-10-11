def foo(x):
    if x < 0:
        return "1"
    print("-1")
    return "0"


def main():
    print(foo(-1))
    print(foo(0))


if __name__ == '__main__':
    main()
