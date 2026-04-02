# --- TASK 1: Data Parsing & Profile Cleaning ---

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

for student in raw_students:
    # 1. Cleaning
    clean_name = student["name"].strip().title()
    
    # 2. Conversion of roll Numbers in the form of int
    clean_roll = int(student["roll"])
    
    # 3. Conversion of marks string to a list of integers
    clean_marks = [int(m.strip()) for m in student["marks_str"].split(",")]
    
    # Store the cleaned data in a new dictionary
    student_data = {
        "name": clean_name,
        "roll": clean_roll,
        "marks": clean_marks
    }
    cleaned_students.append(student_data)

    # Check if words are alphabetic
    is_valid = all(word.isalpha() for word in clean_name.split())
    status = "✓ Valid name" if is_valid else "✕ Invalid name"
    print(f"{clean_name}: {status}")

    # Printing of Profile Cards
    print("-" * 30)
    print(f"Student : {clean_name}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("-" * 30)

# ALL CAPS and lowercase for roll number 103
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"Roll 103 (Upper): {s['name'].upper()}")
        print(f"Roll 103 (Lower): {s['name'].lower()}")

print("\n" + "="*40 + "\n")


# --- TASK 2: Marks Analysis (Individual) ---

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"Analysis for {student_name}:")
for i in range(len(subjects)):
    m = marks[i]
    if m >= 90: grade = "A+"
    elif m >= 80: grade = "A"
    elif m >= 70: grade = "B"
    elif m >= 60: grade = "C"
    else: grade = "F"
    print(f"{subjects[i]}: {m} ({grade})")

# Calculations
total = sum(marks)
avg = total / len(marks)
max_idx = marks.index(max(marks))
min_idx = marks.index(min(marks))

print(f"\nTotal marks: {total}")
print(f"Average marks: {avg:.2f}")
print(f"Highest scoring subject: {subjects[max_idx]} ({marks[max_idx]})")
print(f"Lowest scoring subject: {subjects[min_idx]} ({marks[min_idx]})")

# While loop for new entries
print("\n--- Add New Subjects ---")
while True:
    new_sub = input("Enter subject name (or type 'done'): ").strip()
    if new_sub.lower() == 'done':
        break
    
    mark_input = input(f"Enter marks for {new_sub}: ")
    if mark_input.isdigit():
        m_val = int(mark_input)
        if 0 <= m_val <= 100:
            subjects.append(new_sub)
            marks.append(m_val)
        else:
            print("Warning: Please enter a score between 0 and 100.")
    else:
        print("Warning: Invalid input. Please enter a number.")

new_avg = sum(marks) / len(marks)
print(f"Updated Average: {new_avg:.2f} across {len(subjects)} subjects.")

print("\n" + "="*40 + "\n")


# --- TASK 3: Class Performance Summary ---

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85])
]

print(f"{'Name':<15} | {'Average':<8} | {'Status'}")
print("-" * 35)

pass_count = 0
fail_count = 0
topper_name = ""
topper_avg = 0
total_class_marks = 0

for name, marks_list in class_data:
    student_avg = round(sum(marks_list) / len(marks_list), 2)
    status = "Pass" if student_avg >= 60 else "Fail"
    
    if status == "Pass": pass_count += 1
    else: fail_count += 1
    
    if student_avg > topper_avg:
        topper_avg = student_avg
        topper_name = name
        
    total_class_marks += student_avg
    print(f"{name:<15} | {student_avg:<8} | {status}")

print(f"\nStudents Passed: {pass_count}, Failed: {fail_count}")
print(f"Class Topper: {topper_name} with {topper_avg}")
print(f"Class Average: {total_class_marks / len(class_data):.2f}")

print("\n" + "="*40 + "\n")


# --- TASK 4: String Manipulation Utility ---

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# 1. Strip
clean_essay = essay.strip()

# 2. Convert to Title Case
print(f"Title Case: {clean_essay.title()}")

# 3. Count 'python'
py_count = clean_essay.lower().count("python")
print(f"Occurrences of 'python': {py_count}")

# 4. Replace python with emoji
modified_essay = clean_essay.replace("python", "Python 🐍")
print(f"Modified Essay: {modified_essay}")

# 5. Split using a period, followed by a space
sentences = clean_essay.split(". ")
print("\nNumbered Sentences:")
for i, sentence in enumerate(sentences, 1):
    sentence = sentence.strip()
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")
