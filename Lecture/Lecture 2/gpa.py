def calculate_gpa(current_gpa, num_class, new_grade):
    overall = current_gpa * num_class
    new_overall = overall + new_grade
    new_gpa = new_overall / (num_class +1)
    return new_gpa


#this my code under testing
