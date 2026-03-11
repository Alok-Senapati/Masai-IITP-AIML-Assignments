def main():
    score = int(input("Enter you score (0-100): "))
    print(f"Score: {score}")
    grade = ""
    if score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80 and score <= 89:
        grade = "B"
    elif score >= 70 and score <= 79:
        grade = "C"
    elif score >= 60 and score <= 69:
        grade = "D"
    elif score < 60 and score >= 0:
        grade = "F"
    else:
        print("Invalid Score!!")
        return
    print(f"Grade: {grade}")
    status = "Failed" if grade == "F" else "Passed"
    print(f"Status: {status}")


if __name__ == '__main__':
    main()