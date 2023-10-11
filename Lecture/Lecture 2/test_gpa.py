from gpa import calculate_gpa

def test_calculate_gpa(current_gpa, num_class, new_grade, expected):

    print(f"Testing inputs {current_gpa}, {num_class}, {new_grade}")
    actual = calculate_gpa(current_gpa, num_class, new_grade)
    print(f"Expected Result: {expected}, Actucal result: {actual}")

def main():
    test_calculate_gpa(0, 0, 3.5, 3.5)
    test_calculate_gpa(4.0, 1, 4.0, 4.0)

if __name__ == "__main__":
    main()


#this is my testing code, if i run my testing code first

#why does the result showed there?
