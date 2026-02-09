# Student Management System - OOP Practice

A comprehensive Python project demonstrating object-oriented programming (OOP) concepts and common Python data types.

## 📋 Project Overview

This project implements a student management system that showcases:

- **Classes and Objects** - Student class with attributes and methods
- **Lists** - Grade management with list operations (append, pop, indexing)
- **Tuples** - Immutable grade tuples with exception handling
- **Sets** - Collection of unique grades across all students
- **Dictionaries** - Email-to-Student object mapping
- **Regular Expressions** - Email validation
- **Type Hints** - Python type annotations for better code clarity
- **Exception Handling** - Try/except blocks for error handling
- **List Comprehensions** - Filtering and transforming data

## 🎯 Parts Overview

### Part 1: Class Definition

- Implemented `Student` class with:
  - **Attributes**: name, email, grades
  - **Methods**:
    - `add_grade(grade)` - Add a grade to the student's list
    - `average_grade()` - Calculate average grade
    - `display_info()` - Display student information
    - `grades_tuple()` - Return grades as immutable tuple

### Part 2: Working with Objects

- Created 3 student objects with different names and emails
- Added 2 new grades to each student
- Displayed complete information for each student

### Part 3: Dictionary & Set Integration

- Created `student_dict` mapping emails to Student objects
- Implemented `get_student_by_email()` function with safe `.get()` access
- Created a set of all unique grades across all students

### Part 4: Tuple Practice

- Demonstrated tuple immutability
- Caught `TypeError` when attempting to modify tuple elements
- Included try/except exception handling

### Part 5: List Operations

- Removed last grade from each student using `.pop()`
- Accessed and printed first/last grades using indexing
- Printed grade counts using `len()`

### Part 6: Bonus Features

- **Email Validation**: Used regex pattern `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
- **Grade Analysis**: Counted grades above 90 across all students
- **Breakdown**: Showed high grades per student

## 📦 File Structure

```
Object-Oriented Python Practice/
├── student_management.py    # Main script with all functionality
└── README.md                # This file
```

## 🚀 Running the Script

```bash
python3 student_management.py
```

## 💡 Key Concepts Demonstrated

| Concept                 | Implementation                                       | Location               |
| ----------------------- | ---------------------------------------------------- | ---------------------- |
| **Classes**             | Student class with **init**                          | Lines 13-43            |
| **Methods**             | add_grade, average_grade, display_info, grades_tuple | Lines 45-104           |
| **Type Hints**          | Function signatures with type annotations            | Throughout             |
| **Lists**               | grades list with append, pop, indexing               | Lines 45-57, 238-244   |
| **Tuples**              | grades_tuple() method and immutability demo          | Lines 98-104, 251-264  |
| **Sets**                | all_grades collection                                | Lines 224-228          |
| **Dictionaries**        | student_dict email mapping                           | Lines 215-220          |
| **Regex**               | Email validation pattern                             | Lines 106-118          |
| **Exception Handling**  | TypeError catch for tuple modification               | Lines 251-264          |
| **List Comprehensions** | Filtering grades above 90                            | Lines 144-148, 285-290 |

## 📊 Sample Output

The script produces organized output showing:

- Student information display
- Grade averages
- Dictionary operations
- Tuple immutability demonstrations
- List operations with first/last/count
- Email validation results
- High grade statistics

## 🔍 Code Quality Features

- ✅ Comprehensive docstrings for all classes and methods
- ✅ Type hints for better IDE support and code clarity
- ✅ Input validation for grades
- ✅ Safe dictionary access with `.get()`
- ✅ Error handling with try/except blocks
- ✅ Clear comments explaining OOP concepts
- ✅ Organized code structure with logical sections

## 👤 Student Information

This project was created as part of object-oriented programming practice and demonstrates professional Python development practices.

## 📝 License

This project is provided for educational purposes.
