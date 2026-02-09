"""
Student Management System - OOP Practice
This script demonstrates object-oriented programming concepts in Python,
including classes, objects, dictionaries, sets, tuples, and list operations.
"""

import re
from typing import Dict, Set, Tuple, List


class Student:
    """
    A class to represent a student with grades and contact information.
    
    Attributes:
        name (str): Student's name
        email (str): Student's email address
        grades (list): List of integer grades
    """
    
    def __init__(self, name: str, email: str, grades: List[int]):
        """
        Initialize a Student object.
        
        Args:
            name: Student's name
            email: Student's email address
            grades: Initial list of grades
        """
        self.name = name
        self.email = email
        self.grades = grades
    
    def add_grade(self, grade: int) -> None:
        """
        Add a grade to the student's grades list.
        
        Args:
            grade: The grade to add (integer)
        """
        if isinstance(grade, int) and 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Added grade {grade} to {self.name}")
        else:
            print(f"Invalid grade: {grade}. Grade must be an integer between 0 and 100.")
    
    def average_grade(self) -> float:
        """
        Calculate and return the average of all grades.
        
        Returns:
            float: The average grade, or 0 if no grades exist
        """
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self) -> None:
        """
        Display the student's information including name, email, and grades.
        """
        print(f"\n{'='*50}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")
        print(f"{'='*50}")
    
    def grades_tuple(self) -> Tuple[int, ...]:
        """
        Convert grades list to a tuple.
        
        Returns:
            tuple: The grades as an immutable tuple
        """
        return tuple(self.grades)


def validate_email(email: str) -> bool:
    """
    Validate that an email follows the format: name@domain.com
    
    Args:
        email: The email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
    """
    # Simple regex pattern for email validation: name@domain.com
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def get_student_by_email(email: str, student_dict: Dict[str, Student]) -> Student:
    """
    Safely retrieve a student object from the dictionary by email.
    
    Args:
        email: The email to search for
        student_dict: Dictionary mapping emails to Student objects
        
    Returns:
        Student object if found, None otherwise
    """
    student = student_dict.get(email)
    if student is None:
        print(f"No student found with email: {email}")
    return student


def count_grades_above_90(students: List[Student]) -> int:
    """
    Count how many grades are above 90 across all students.
    
    Args:
        students: List of Student objects
        
    Returns:
        int: Total count of grades above 90
    """
    count = 0
    for student in students:
        count += sum(1 for grade in student.grades if grade > 90)
    return count


def main():
    """
    Main function to demonstrate all OOP concepts and features.
    """
    print("\n" + "="*50)
    print("STUDENT MANAGEMENT SYSTEM - OOP PRACTICE")
    print("="*50)
    
    # ==================== PART 1: Class Definition ====================
    print("\n--- PART 1: Class Definition ---")
    print("Student class created with attributes: name, email, grades")
    print("Methods: add_grade(), average_grade(), display_info(), grades_tuple()")
    
    # ==================== PART 2: Working with Objects ====================
    print("\n--- PART 2: Creating Student Objects ---")
    
    # Create 3 student objects with initial grades
    student1 = Student("Alice Johnson", "alice@example.com", [85, 90, 92])
    student2 = Student("Bob Smith", "bob@example.com", [78, 88, 95])
    student3 = Student("Charlie Davis", "charlie@example.com", [92, 95, 88])
    
    students = [student1, student2, student3]
    
    # Add 2 new grades to each student
    print("\nAdding 2 new grades to each student:")
    student1.add_grade(87)
    student1.add_grade(91)
    
    student2.add_grade(93)
    student2.add_grade(89)
    
    student3.add_grade(96)
    student3.add_grade(94)
    
    # Display information and average grade for each student
    print("\nDisplaying information for all students:")
    for student in students:
        student.display_info()
    
    # ==================== PART 3: Dictionary & Set Integration ====================
    print("\n--- PART 3: Dictionary & Set Integration ---")
    
    # Create dictionary mapping email to Student object
    student_dict: Dict[str, Student] = {
        student1.email: student1,
        student2.email: student2,
        student3.email: student3
    }
    
    print("\nStudent Dictionary created:")
    for email, student in student_dict.items():
        print(f"  {email}: {student.name}")
    
    # Test get_student_by_email function
    print("\nTesting get_student_by_email():")
    retrieved_student = get_student_by_email("alice@example.com", student_dict)
    if retrieved_student:
        print(f"Found student: {retrieved_student.name}")
    
    retrieved_student = get_student_by_email("nonexistent@example.com", student_dict)
    
    # Create set of all unique grades across all students
    all_grades: Set[int] = set()
    for student in students:
        all_grades.update(student.grades)
    
    print(f"\nAll unique grades across all students: {sorted(all_grades)}")
    print(f"Set representation: {all_grades}")
    
    # ==================== PART 4: Tuple Practice ====================
    print("\n--- PART 4: Tuple Practice (Immutability) ---")
    
    # Get grades as tuple and demonstrate immutability
    for student in students:
        grades_tuple = student.grades_tuple()
        print(f"\n{student.name}'s grades as tuple: {grades_tuple}")
        print(f"Tuple type: {type(grades_tuple)}")
        
        # Try to modify tuple (should raise an error)
        try:
            grades_tuple[0] = 100
            print("ERROR: Tuple was modified (this shouldn't happen!)")
        except TypeError as e:
            print(f"✓ Correctly caught TypeError: {e}")
            print(f"  Tuples are immutable and cannot be modified!")
    
    # ==================== PART 5: List Operations ====================
    print("\n--- PART 5: List Operations ---")
    
    print("\nRemoving the last grade from each student:")
    for student in students:
        removed_grade = student.grades.pop()
        print(f"{student.name}: Removed grade {removed_grade}")
    
    print("\nAccessing first and last grades:")
    for student in students:
        if student.grades:  # Check if grades list is not empty
            first_grade = student.grades[0]
            last_grade = student.grades[-1]
            num_grades = len(student.grades)
            print(f"{student.name}: First={first_grade}, Last={last_grade}, Total={num_grades}")
        else:
            print(f"{student.name}: No grades available")
    
    # ==================== PART 6: Bonus Features ====================
    print("\n--- PART 6: Bonus Features ---")
    
    # Email validation
    print("\nEmail Validation using Regex:")
    all_students_data = [
        ("alice@example.com", student1.name),
        ("bob@example.com", student2.name),
        ("charlie@example.com", student3.name),
    ]
    
    for email, name in all_students_data:
        is_valid = validate_email(email)
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"  {email} ({name}): {status}")
    
    # Count grades above 90
    high_grade_count = count_grades_above_90(students)
    print(f"\nGrades above 90 across all students: {high_grade_count}")
    
    # Show breakdown by student
    print("Breakdown by student:")
    for student in students:
        high_grades = [g for g in student.grades if g > 90]
        print(f"  {student.name}: {len(high_grades)} grades above 90 -> {high_grades}")
    
    # ==================== Summary ====================
    print("\n" + "="*50)
    print("SUMMARY OF DEMONSTRATED CONCEPTS:")
    print("="*50)
    print("✓ Classes and Objects (Student class)")
    print("✓ Methods and Attributes")
    print("✓ Type Hints (typing module)")
    print("✓ Lists (grades list, pop, indexing)")
    print("✓ Tuples (grades_tuple, immutability)")
    print("✓ Sets (unique grades collection)")
    print("✓ Dictionaries (student_dict with email keys)")
    print("✓ Regular Expressions (email validation)")
    print("✓ Exception Handling (try/except for tuple immutability)")
    print("✓ List Comprehensions (filtering grades > 90)")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
