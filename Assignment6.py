import numpy as np


def analyze_student_performance(grades: np.ndarray, passing_threshold: float = 60.0) -> dict:
    """
    Analyze student grades across multiple exams.

    Parameters:
    -----------
    grades : np.ndarray
        2D array of shape (num_students, num_exams) containing grades
    passing_threshold : float
        Minimum grade to pass (default 60.0)

    Returns:
    --------
    dict with keys:
        - 'student_averages': np.ndarray - Average grade per student
        - 'exam_averages': np.ndarray - Average grade per exam
        - 'overall_average': float - Average of all grades
        - 'passing_students': np.ndarray - Indices of students with ALL exams passing
        - 'at_risk_students': np.ndarray - Indices of students with ANY exam failing
        - 'top_performer_index': int - Index of student with highest average
        - 'hardest_exam_index': int - Index of exam with lowest average
    """
    student_averages = np.mean(grades, axis=1)
    exam_averages = np.mean(grades, axis=0)
    overall_average = np.mean(grades)
    passing_students = np.where(np.all(grades >= passing_threshold, axis=1))[0]
    at_risk_students = np.where(np.any(grades < passing_threshold, axis=1))[0]
    top_performer_index = np.argmax(student_averages)
    hardest_exam_index = np.argmin(exam_averages)
    output = {
        "student_averages": student_averages,
        "exam_averages": exam_averages,
        "overall_average": overall_average,
        "passing_students": passing_students,
        "at_risk_students": at_risk_students,
        "top_performer_index": top_performer_index,
        "hardest_exam_index": hardest_exam_index,
    }
    return output


def main():
    grades = np.array([
        [85, 72, 90, 68],  # Student 0
        [55, 60, 58, 62],  # Student 1
        [92, 88, 95, 91],  # Student 2
        [70, 45, 75, 80],  # Student 3
        [78, 82, 79, 85]  # Student 4
    ])

    result = analyze_student_performance(grades, passing_threshold=60)

    print("Student Averages:", result['student_averages'])
    # [78.75, 58.75, 91.5, 67.5, 81.0]

    print("Exam Averages:", result['exam_averages'])
    # [76.0, 69.4, 79.4, 77.2]

    print("Overall Average:", result['overall_average'])
    # 75.5

    print("Passing Students (all exams >= 60):", result['passing_students'])
    # [0, 2, 4]

    print("At-Risk Students (any exam < 60):", result['at_risk_students'])
    # [1, 3]

    print("Top Performer Index:", result['top_performer_index'])
    # 2

    print("Hardest Exam Index:", result['hardest_exam_index'])
    # 1


if __name__ == '__main__':
    main()
