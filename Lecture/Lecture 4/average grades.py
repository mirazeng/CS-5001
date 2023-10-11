'''
grades cal
'''


def main():
    grades = []
    my_grade = float(input("Enter a grade, negative to stop: "))
    while my_grade >= 0:
        grades.append(my_grade)
        my_grade = float(input("Enter a grade, negative to stop: "))
    average = sum(grades) / len(grades)

    # 分母不能为0
    if len(grades) > 0:
        average = sum(grades) / len(grades)
    else:
        average = "Unknown - no grades available"
    print(f"Your average is {average}")


if __name__ == '__main__':
    main()
