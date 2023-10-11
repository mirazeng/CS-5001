def main():
    grades = []  # this is a nested list

    my_grade = float(input("enter a grade, negative to stop: "))
    while my_grade >= 0:
        # asking for the metadata
        # Metadata: data about data, prepare for
        # what is coming / what is going on.
        semester = input("Which semester (FA20, SP23, etc.)")
        # a flag we will use to track the state of finding lists? tracker
        # take action or not, give it an initial value
        found = False
        for each in grades:
            # why each not grades? cuz nested list?
            if semester.upper() in each:  # list exists in our grades
                each.append(my_grade)
                found = True
                # optimization: stop when we found what we want
                break
        # either way stop or create a new list with new entry metadata
        if not found:  # aka if found == False
            # adding a list with input metadata plus the grades we want to keep on record
            grades.append([semester.upper(), my_grade])

        my_grade = float(input("enter a grade, neg to stop: "))

    print(grades)


if __name__ == "__main__":
    main()
