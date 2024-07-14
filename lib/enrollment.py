class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []  # List to hold enrollments
        self._grades = {}  # {enrollment: grade}

    def course_count(self):
        """Counts the number of courses a student is enrolled in."""
        return len(self._enrollments)

    def aggregate_average_grade(self):
        """Calculates the average grade across all courses."""
        if not self._grades:
            return 0
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses


class Enrollment:
    all = []  # Class variable to hold all enrollments

    def __init__(self, student, course, enrollment_date):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date
        Enrollment.all.append(self)  # Add to the class-level list
        student._enrollments.append(self)  # Add to the student's enrollments

    def get_enrollment_date(self):
        return self.enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        """Counts enrollments per day."""
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count


class TestCodegrade:
    """Codegrade placeholder"""

    def test_codegrade_placeholder(self):
        assert True

    def test_course_count(self):
        """Test the course count for a student."""
        student = Student("Alice")
        Enrollment(student, "Math", "2023-01-01")
        Enrollment(student, "Science", "2023-01-02")
        assert student.course_count() == 2

    def test_aggregate_average_grade(self):
        """Test the average grade calculation for a student."""
        student = Student("Bob")
        enrollment1 = Enrollment(student, "Math", "2023-01-01")
        enrollment2 = Enrollment(student, "Science", "2023-01-02")
        student._grades[enrollment1] = 90
        student._grades[enrollment2] = 80
        assert student.aggregate_average_grade() == 85

    def test_aggregate_enrollments_per_day(self):
        """Test counting enrollments per day."""
        student1 = Student("Alice")
        student2 = Student("Bob")
        Enrollment(student1, "Math", "2023-01-01")
        Enrollment(student2, "Science", "2023-01-01")
        Enrollment(student1, "History", "2023-01-02")
        result = Enrollment.aggregate_enrollments_per_day()
        assert result == {"2023-01-01": 2, "2023-01-02": 1}
