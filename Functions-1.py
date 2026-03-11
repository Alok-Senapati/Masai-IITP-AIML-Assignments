def calculate_average(marks):
    return sum(marks) / len(marks)

def count_pass_fail(marks, pass_mark=50):
    passed = len([m for m in marks if m >= pass_mark])
    failed = len([m for m in marks if m < pass_mark])
    return passed, failed

def display_summary(marks):
    total_students = len(marks)
    avg_marks = calculate_average(marks)
    passed, failed = count_pass_fail(marks)
    print(f"Total Students: {total_students}")
    print(f"Average Marks: {avg_marks}")
    print(f"Students Passed: {passed}")
    print(f"Students Failed: {failed}")

## Demonstrate Local/Global Variable
global_val = 100

def local_variable():
    global_val = 10
    print(f"Local Variable global_val = {global_val}") ## Here global_val is a local variable local to this function

if __name__ == '__main__':
    marks = [75, 60, 85, 90, 45, 67, 80, 92]
    display_summary(marks)

    print(f"Global Variable glabal_val = {global_val}") ## Prints global variable value
    local_variable()
    print(f"Global Variable glabal_val = {global_val}") ## Prints global variable value
