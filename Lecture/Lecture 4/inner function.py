# in global scope
# talking about the local and global scope
# inner function variable: local and global
PI = 3.1415


def test():
    print("hello, world!")
    x = 1

    # is still a function but inside a local scope not global
    def inner_test():
        print("Let's go to dinner, Inner!")
        print("Outer's x value is: ", x)

        # call function
        # mind the indentation

    inner_test()  # the () make a call to the function


def main():
    test()

    # you cant directly call inner function here

if __name__ == "__main__":
    main()
