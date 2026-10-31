class Student:

    def __init__(self, roll_no: str, name: str, course: str, marks: float):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.marks = marks
    
class StudentManagementSystem:

    def __init__(self):
        self.students = {}

    def add_student(self, roll_no: str, name: str, course: str, marks: float) -> bool:
        if roll_no in self.students:
            print(f"\n[Error] Student with Roll Number '{roll_no}' already exists.")
            return False

        self.students[roll_no] = Student(roll_no, name, course, marks)
        print(f"\n[Success] Student '{name}' added successfully.")
        return True

    def display_all(self) -> None:
        if not self.students:
            print("\n[Info] No student records available.")
            return

        #print("\n" + "=" * 65)
        print(f"{'Roll No':<12} | {'Name':<22} | {'Course':<15} | {'Marks':<6}")
       # print("-" * 65)
        for roll_no, s in sorted(self.students.items(), key=lambda item: item[0]):
            print(f"{roll_no:<12} | {s.name:<22} | {s.course:<15} | {s.marks:<6.2f}")
        #print("=" * 65)
        print(f"Total Students: {len(self.students)}")

    def search_student(self, query: str) -> None:
        query_clean = query.strip().lower()
        matches = [
            s for s in self.students.values()
            if query_clean == s.roll_no.lower() or query_clean in s.name.lower()
        ]

        if not matches:
            print(f"\n[Info] No records found matching '{query}'.")
            return

        print("\n--- Search Results ---")
        print(f"{'Roll No':<12} | {'Name':<22} | {'Course':<15} | {'Marks':<6}")
       # print("-" * 65)
        for s in matches:
            print(f"{s.roll_no:<12} | {s.name:<22} | {s.course:<15} | {s.marks:<6.2f}")
       # print("-" * 65)

    def update_student(self, roll_no: str) -> bool:
        student = self.students.get(roll_no)
        if not student:
            print(f"\n[Error] No record found for Roll Number '{roll_no}'.")
            return False

        print(f"\nUpdating Record for: {student.name} ({student.roll_no})")
        print("(Press Enter without typing to keep the current value)")

        new_name = input(f"New Name [{student.name}]: ").strip()
        if new_name:
            student.name = new_name

        new_course = input(f"New Course [{student.course}]: ").strip()
        if new_course:
            student.course = new_course

        new_marks_raw = input(f"New Marks [{student.marks}]: ").strip()
        if new_marks_raw:
            try:
                new_marks = float(new_marks_raw)
                if 0 <= new_marks <= 100:
                    student.marks = new_marks
                else:
                    print("[Warning] Marks must be between 0 and 100. Retaining old marks.")
            except ValueError:
                print("[Warning] Invalid number format. Retaining old marks.")

        print("\n[Success] Record updated successfully.")
        return True

    def delete_student(self, roll_no: str) -> bool:
        student = self.students.get(roll_no)
        if not student:
            print(f"\n[Error] No record found for Roll Number '{roll_no}'.")
            return False

        confirm = input(
            f"Are you sure you want to delete {student.name} ({roll_no})? (y/n): "
        ).strip().lower()

        if confirm == "y":
            del self.students[roll_no]
            print(f"\n[Success] Student record {roll_no} deleted.")
            return True
        else:
            print("\n[Action Cancelled] Record was not deleted.")
            return False

    def display_statistics(self) -> None:
        if not self.students:
            print("\n[Info] Not enough data to generate statistics.")
            return

        all_marks = [s.marks for s in self.students.values()]
        avg_marks = sum(all_marks) / len(all_marks)
        topper = max(self.students.values(), key=lambda s: s.marks)

        #print("\n" + "=" * 35)
        print("       PERFORMANCE METRICS       ")
       # print("=" * 35)
        print(f"Total Registered : {len(self.students)}")
        print(f"Class Average    : {avg_marks:.2f}")
        print(f"Highest Score    : {topper.marks:.2f} ({topper.name})")
       # print("=" * 35)

def prompt_non_empty(message: str) -> str:
    while True:
        value = input(message).strip()
        if value:
            return value
        print("[Error] This field cannot be left blank.")


def prompt_marks(message: str) -> float:
    while True:
        raw_val = input(message).strip()
        try:
            marks = float(raw_val)
            if 0.0 <= marks <= 100.0:
                return marks
            print("[Error] Marks must be between 0 and 100.")
        except ValueError:
            print("[Error] Invalid input. Please enter a valid number.")

def main():
    sms = StudentManagementSystem()
    sms.add_student("101", "Amit Shukla", "B.s.c", 84.5)
    sms.add_student("102", "Kaushal Dubey", "BCA", 80.0)
    sms.add_student("103", "Mayank Mishra", "B.Tech", 92.0)

    while True:
        print("\n" + "#" * 35)
        print("    STUDENT MANAGEMENT SYSTEM    ")
        print("#" * 35)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student (Roll No / Name)")
        print("4. Update Student Details")
        print("5. Delete Student Record")
        print("6. View Performance Statistics")
        print("7. Exit")
        #print("-" * 35)

        choice = input("Enter your selection (1-7): ").strip()

        if choice == "1":
            print("\n--- Add New Student ---")
            roll_no = prompt_non_empty("Enter Roll Number: ")
            name = prompt_non_empty("Enter Full Name: ")
            course = prompt_non_empty("Enter Course: ")
            marks = prompt_marks("Enter Marks (0-100): ")
            sms.add_student(roll_no, name, course, marks)

        elif choice == "2":
            sms.display_all()

        elif choice == "3":
            query = prompt_non_empty("Enter Roll Number or Name to search: ")
            sms.search_student(query)

        elif choice == "4":
            roll_no = prompt_non_empty("Enter Roll Number to update: ")
            sms.update_student(roll_no)

        elif choice == "5":
            roll_no = prompt_non_empty("Enter Roll Number to delete: ")
            sms.delete_student(roll_no)

        elif choice == "6":
            sms.display_statistics()

        elif choice == "7":
            print("\nExiting system. Have a great day!")
            break

        else:
            print("\n[Invalid Selection] Please choose a valid number between 1 and 7.")


if __name__ == "__main__":
    main()
