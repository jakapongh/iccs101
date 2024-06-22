class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    # Special methods that enable use of sorted()
    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __repr__(self):
        return f"Student(name={self.name}, score={self.score})"


class Classroom:
    def __init__(self, students: list[Student]):
        self.students = students

    def find_average(self):
        total_score = 0
        for student in self.students:
            total_score += student.score

        return total_score / len(self.students)

    def median_students(self):
        sorted_students = sorted(self.students)

        # Get midpoint
        midpoint_idx = (len(sorted_students) - 1) // 2
        if (len(sorted_students) - 1) % 2 != 0:
            # No "real" midpoint, return two students
            return [sorted_students[midpoint_idx], sorted_students[midpoint_idx + 1]]
        else:
            # One real midpoint
            return [sorted_students[midpoint_idx]]

    def find_median(self):
        student_names =[]
        median_score = 0

        for median_student in self.median_students():
            student_names.append(median_student.name)
            median_score += median_student.score

        if len(self.median_students()) > 1:
            median_score /= 2

        return median_score, student_names


def main():
    students_list = [
        Student("4", 10),
        Student("6", 32),
        Student("2", 50),
        Student("3", 90),
        Student("5", 92),
        Student("1", 100),
    ]
    classroom = Classroom(students_list)
    print("No. students:", len(classroom.students))
    print("Average:", classroom.find_average())
    print("Median:", classroom.find_median())


if __name__ == "__main__":
    main()
