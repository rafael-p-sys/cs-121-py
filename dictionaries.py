students = {
    "001": {"name": "Alice", "age": 20, "major": "Computer Science"},
    "002": {"name": "Bob", "age": 22, "major": "Mathematics"},
    "003": {"name": "Charlie", "age": 21, "major": "Physics"}
}

def get_new_id():
    highest_id = max(int(sid) for sid in students.keys())
    return str(highest_id + 1).zfill(3)

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    major = input("Enter student major: ")

    new_id = get_new_id()

    students[new_id] = {
        "name": name,
        "age": age,
        "major": major
    }

    print(f"\nStudent added! Assigned ID: {new_id}")

def display_students():
    print("\n--- STUDENT LIST ---")
    for student_id, info in students.items():
        print(f"ID: {student_id}, Name: {info['name']}, Age: {info['age']}, Major: {info['major']}")

print("Current Students:")
display_students()

print("\nAdd a new student:")
add_student()

print("\nUpdated Student List:")
display_students()