
"""Student academic grading management module."""

import hashlib
import json
import os
import secrets
from pathlib import Path

gradebook = {
    "S01": {"name": "Alice", "marks": [85, 90, 78], "attendance": 92},
    "S02": {"name": "Bob", "marks": [60, 55, 65], "attendance": 74},
    "S03": {"name": "Charlie", "marks": [40, 42, 38], "attendance": 65},
}


def add_grade(student_id, mark, grade_list=None):
    """Record a student's mark and optionally append an audit message."""
    if student_id not in gradebook or not 0 <= mark <= 100:
        return False

    gradebook[student_id]["marks"].append(mark)

    if grade_list is not None:
        grade_list.append(f"Recorded score {mark} for student id {student_id}")

    return True


def record_attendance(student_id, present_days):
    """Add attendance days for an existing student."""
    if student_id not in gradebook:
        return False

    if not isinstance(present_days, int) or present_days < 0:
        return False

    gradebook[student_id]["attendance"] += present_days
    return True


def check_passing_status(student_id, pass_threshold=50.0):
    """Return whether a student's average meets the passing threshold."""
    student = gradebook.get(student_id)

    if student is None or not student["marks"]:
        return False

    average = sum(student["marks"]) / len(student["marks"])
    return average >= pass_threshold


def compute_weighted_gpa(student_id):
    """Calculate GPA on a 4.0 scale using the average mark."""
    student = gradebook.get(student_id)

    if student is None or not student["marks"]:
        raise ValueError("Student does not exist or has no recorded marks.")

    average = sum(student["marks"]) / len(student["marks"])
    return average / 25.0


def generate_student_hash(student_id):
    """Return a SHA-256 digest for a student identifier."""
    return hashlib.sha256(student_id.encode("utf-8")).hexdigest()


def generate_registration_pin():
    """Generate a four-digit registration PIN."""
    return secrets.randbelow(9000) + 1000


def export_grade_sheet(filename="grade_sheet.txt"):
    """Export the gradebook as JSON."""
    output_path = Path(filename)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(gradebook, file, indent=4)

    print(f"Grade sheet exported to: {output_path}")


def main():
    """Run a sample grading workflow."""
    portal_token = os.getenv("GRADE_PORTAL_TOKEN")

    add_grade("S01", 95)
    record_attendance("S02", 2)

    print("Is S01 passing:", check_passing_status("S01"))
    print("Calculated GPA:", compute_weighted_gpa("S01"))
    print("Student Hash:", generate_student_hash("S01"))
    print("Registration PIN:", generate_registration_pin())
    export_grade_sheet()

    print("Portal token configured:", bool(portal_token))


if __name__ == "__main__":
    main()
