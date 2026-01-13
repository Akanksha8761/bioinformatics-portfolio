"""
Day 3: The "Student Ranking System" Challenge
==============================================

The Scenario:
You have a list of students, where each student is represented as a dictionary 
with their name and their exam score.

The Task:
    1. Filter: Create a new list containing only students who scored above 80.
    2. Sort: Sort that filtered list by their score in descending order (highest first).
    3. Tie-breaker: If two students have the same score (like Alice and David), 
       sort them alphabetically by name.

The Constraint:
Try to use the sorted() function
"""

from collections import defaultdict
from operator import itemgetter

# Input data
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 88},
    {"name": "Eve", "score": 79}
]

print("=" * 70)
print("Day 3: Student Ranking System Challenge")
print("=" * 70)
print(f"\nOriginal students list:")
for student in students:
    print(f"  {student['name']:10} - Score: {student['score']}")


# ============================================================================
# Your Original Approach: Using defaultdict
# ============================================================================
print("\n" + "=" * 70)
print("Your Original Approach: Using defaultdict")
print("=" * 70)

merged_dict = defaultdict(list)
for d in students:
    for key, value in d.items():
        if d['score'] > 80:
            merged_dict[key].append(value)

new = dict(merged_dict)
print(f"\nMerged dictionary: {new}")

for key in new:
    new[key].sort()
print(f"After sorting: {new}")

print("\nNote: This approach creates a different data structure.")
print("Let's see alternative approaches that maintain the list of dictionaries format.")


# ============================================================================
# Solution 1: Using sorted() with Lambda (Recommended)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 1: Using sorted() with Lambda (Recommended)")
print("=" * 70)

# Filter students with score > 80
filtered_students = [s for s in students if s['score'] > 80]
print(f"\nFiltered students (score > 80): {len(filtered_students)} students")
for student in filtered_students:
    print(f"  {student['name']:10} - Score: {student['score']}")

# Sort by score (descending) then by name (ascending)
sorted_students = sorted(filtered_students, key=lambda x: (-x['score'], x['name']))

print(f"\nSorted students (by score desc, then name asc):")
for i, student in enumerate(sorted_students, 1):
    print(f"  {i}. {student['name']:10} - Score: {student['score']}")


# ============================================================================
# Solution 2: One-Liner (Pythonic)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 2: One-Liner Solution")
print("=" * 70)

result = sorted([s for s in students if s['score'] > 80], 
                key=lambda x: (-x['score'], x['name']))

print(f"\nOne-liner result:")
for i, student in enumerate(result, 1):
    print(f"  {i}. {student['name']:10} - Score: {student['score']}")


# ============================================================================
# Solution 3: Using filter() Function
# ============================================================================
print("\n" + "=" * 70)
print("Solution 3: Using filter() Function")
print("=" * 70)

# Filter using filter() function
filtered_students_func = list(filter(lambda s: s['score'] > 80, students))

# Sort
sorted_students_func = sorted(filtered_students_func, 
                               key=lambda x: (-x['score'], x['name']))

print(f"\nUsing filter() function:")
for i, student in enumerate(sorted_students_func, 1):
    print(f"  {i}. {student['name']:10} - Score: {student['score']}")


# ============================================================================
# Solution 4: Using operator.itemgetter
# ============================================================================
print("\n" + "=" * 70)
print("Solution 4: Using operator.itemgetter")
print("=" * 70)

# Filter students
filtered_students_op = [s for s in students if s['score'] > 80]

# Sort by name first (for stable sorting)
sorted_by_name = sorted(filtered_students_op, key=itemgetter('name'))

# Then sort by score (descending) - stable sort maintains name order for ties
sorted_students_op = sorted(sorted_by_name, key=itemgetter('score'), reverse=True)

print(f"\nUsing itemgetter with stable sort:")
for i, student in enumerate(sorted_students_op, 1):
    print(f"  {i}. {student['name']:10} - Score: {student['score']}")


# ============================================================================
# Solution 5: Custom Sorting Function
# ============================================================================
print("\n" + "=" * 70)
print("Solution 5: Custom Sorting Function")
print("=" * 70)

def sort_key(student):
    """
    Custom sorting function for students.
    Returns tuple: (negative score, name) for proper sorting.
    """
    return (-student['score'], student['name'])

filtered_students_custom = [s for s in students if s['score'] > 80]
sorted_students_custom = sorted(filtered_students_custom, key=sort_key)

print(f"\nUsing custom sort function:")
for i, student in enumerate(sorted_students_custom, 1):
    print(f"  {i}. {student['name']:10} - Score: {student['score']}")


# ============================================================================
# Understanding Lambda and Tuple Sorting
# ============================================================================
print("\n" + "=" * 70)
print("Understanding Lambda and Tuple Sorting")
print("=" * 70)

print("\nHow tuple sorting works:")
print("When sorting by (-score, name), Python compares tuples element by element:")
for student in sorted_students:
    print(f"  ({-student['score']:3}, '{student['name']:8}') -> {student}")


# ============================================================================
# Bonus: Enhanced Ranking System
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Enhanced Ranking System")
print("=" * 70)

def get_grade(score):
    """Assign letter grade based on score."""
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

def rank_students(students, min_score=0, max_results=None):
    """
    Rank students by score with optional filtering.
    
    Args:
        students (list): List of student dictionaries
        min_score (int): Minimum score threshold (default: 0)
        max_results (int): Maximum number of results (default: None)
    
    Returns:
        list: Sorted and filtered list of students with ranks and grades
    """
    # Filter
    filtered = [s for s in students if s['score'] > min_score]
    
    # Sort
    sorted_students = sorted(filtered, key=lambda x: (-x['score'], x['name']))
    
    # Add rank and grade
    ranked = []
    for i, student in enumerate(sorted_students, 1):
        ranked_student = {
            'rank': i,
            'name': student['name'],
            'score': student['score'],
            'grade': get_grade(student['score'])
        }
        ranked.append(ranked_student)
    
    # Limit results if specified
    return ranked[:max_results] if max_results else ranked

# Test the enhanced function
ranked_students = rank_students(students, min_score=80)

print(f"\nEnhanced ranking (with rank and grade):")
print(f"{'Rank':<6} {'Name':<12} {'Score':<8} {'Grade':<6}")
print("-" * 35)
for student in ranked_students:
    print(f"{student['rank']:<6} {student['name']:<12} "
          f"{student['score']:<8} {student['grade']:<6}")


# ============================================================================
# Bonus: Class Statistics
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Class Statistics")
print("=" * 70)

def calculate_stats(students):
    """Calculate comprehensive statistics for the class."""
    if not students:
        return {}
    
    scores = [s['score'] for s in students]
    sorted_scores = sorted(scores)
    
    return {
        'total_students': len(students),
        'average': round(sum(scores) / len(scores), 2),
        'highest': max(scores),
        'lowest': min(scores),
        'median': sorted_scores[len(scores) // 2],
        'passing_count': len([s for s in students if s['score'] > 80]),
        'passing_rate': round(len([s for s in students if s['score'] > 80]) / len(students) * 100, 1)
    }

stats = calculate_stats(students)
print(f"\nClass Statistics:")
for key, value in stats.items():
    label = key.replace('_', ' ').title()
    if key == 'passing_rate':
        print(f"  {label}: {value}%")
    else:
        print(f"  {label}: {value}")


# ============================================================================
# Bonus: Top N Students
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Top N Students")
print("=" * 70)

def get_top_students(students, n=3, min_score=0):
    """Get top N students above a minimum score."""
    ranked = rank_students(students, min_score=min_score, max_results=n)
    return ranked

top_3 = get_top_students(students, n=3, min_score=0)
print(f"\nTop 3 Students (all scores):")
for student in top_3:
    print(f"  {student['rank']}. {student['name']:10} - "
          f"Score: {student['score']} (Grade: {student['grade']})")

top_2_above_80 = get_top_students(students, n=2, min_score=80)
print(f"\nTop 2 Students (score > 80):")
for student in top_2_above_80:
    print(f"  {student['rank']}. {student['name']:10} - "
          f"Score: {student['score']} (Grade: {student['grade']})")


# ============================================================================
# Bonus: Group by Score Range
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Group by Score Range")
print("=" * 70)

def group_by_score_range(students, range_size=10):
    """Group students by score ranges."""
    groups = defaultdict(list)
    for student in students:
        range_key = (student['score'] // range_size) * range_size
        groups[range_key].append(student)
    
    # Sort each group
    for key in groups:
        groups[key] = sorted(groups[key], key=lambda x: (-x['score'], x['name']))
    
    return dict(sorted(groups.items(), reverse=True))

grouped = group_by_score_range(students)
print(f"\nStudents grouped by score range:")
for score_range, group in grouped.items():
    print(f"\n  {score_range}-{score_range+9} range ({len(group)} students):")
    for student in group:
        print(f"    - {student['name']:10} (Score: {student['score']})")


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)

print(f"""
Challenge Requirements:
✓ Filter students with score > 80
✓ Sort by score (descending)
✓ Tie-breaker: alphabetical by name
✓ Use sorted() function

Results:
--------
Total students: {len(students)}
Students above 80: {len([s for s in students if s['score'] > 80])}

Final Ranking (Score > 80):
""")

for i, student in enumerate(sorted_students, 1):
    print(f"{i}. {student['name']:10} - Score: {student['score']}")

print(f"""
Methods demonstrated:
✓ Lambda functions with tuple sorting
✓ List comprehensions for filtering
✓ operator.itemgetter for cleaner sorting
✓ filter() function for functional approach
✓ Custom sort functions
✓ Enhanced ranking with grades
✓ Statistical analysis
✓ Grouping and aggregation
""")

print("=" * 70)
print("✅ Challenge completed!")
print("=" * 70)
