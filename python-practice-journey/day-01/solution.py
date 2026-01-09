"""
Day 1: The "Clean & Filter" Challenge
======================================

The Scenario:
You are given a list of messy user-submitted tags for a blog. 
Some have extra spaces, some are in different cases, and some are just empty strings.

The Task:
Given the following list:
raw_tags = [" python", "programming ", " ", "JS", " REACt ", "python", " php ", ""]

Write a single line of code (a List Comprehension) that transforms this list into 
a new list called clean_tags which:
    1. Removes all leading/trailing whitespace.
    2. Converts everything to lowercase.
    3. Removes any strings that are empty after stripping.
    4. Ensures every tag is unique (no duplicates like "python").
"""

# Input data
raw_tags = [" python", "programming ", " ", "JS", " REACt ", "python", " php ", ""]

print("=" * 60)
print("Day 1: Clean & Filter Challenge")
print("=" * 60)
print(f"\nOriginal tags: {raw_tags}")
print(f"Number of raw tags: {len(raw_tags)}")


# Solution 1: Using for loop (Traditional Approach)
print("\n" + "=" * 60)
print("Solution 1: Using For Loop")
print("=" * 60)

clean_tags_loop = []
for i in raw_tags:
    if i.strip():  # Check if string is not empty after stripping
        clean_tags_loop.append(i.lower().strip())

# Convert to set to remove duplicates
clean_tags_loop_set = set(clean_tags_loop)

print(f"\nCleaned tags (for loop): {clean_tags_loop_set}")
print(f"Number of unique tags: {len(clean_tags_loop_set)}")


# Solution 2: Using Set Comprehension (Pythonic Approach)
print("\n" + "=" * 60)
print("Solution 2: Using Set Comprehension")
print("=" * 60)

clean_tags = {i.lower().strip() for i in raw_tags if i.strip()}

print(f"\nCleaned tags (set comprehension): {clean_tags}")
print(f"Number of unique tags: {len(clean_tags)}")


# Solution 3: Bonus - As a sorted list
print("\n" + "=" * 60)
print("Bonus: Sorted Clean Tags")
print("=" * 60)

sorted_clean_tags = sorted({i.lower().strip() for i in raw_tags if i.strip()})

print(f"\nSorted clean tags: {sorted_clean_tags}")


# Solution 4: Bonus - As a reusable function
def clean_tag_list(tags, min_length=1, return_sorted=False):
    """
    Clean and filter a list of tags.
    
    Args:
        tags (list): List of raw tags to clean
        min_length (int): Minimum length for tags (default: 1)
        return_sorted (bool): Whether to return sorted list (default: False)
    
    Returns:
        set or list: Cleaned tags as set or sorted list
    """
    cleaned = {tag.lower().strip() for tag in tags 
               if tag.strip() and len(tag.strip()) >= min_length}
    
    return sorted(cleaned) if return_sorted else cleaned


print("\n" + "=" * 60)
print("Bonus: Using Reusable Function")
print("=" * 60)

# Test the function with different parameters
result1 = clean_tag_list(raw_tags)
result2 = clean_tag_list(raw_tags, min_length=2)
result3 = clean_tag_list(raw_tags, return_sorted=True)

print(f"\nDefault function call: {result1}")
print(f"With min_length=2: {result2}")
print(f"Sorted output: {result3}")


# Summary
print("\n" + "=" * 60)
print("Summary")
print("=" * 60)
print(f"""
Raw tags count: {len(raw_tags)}
Unique clean tags: {len(clean_tags)}
Tags removed: {len(raw_tags) - len(clean_tags)}
Removed tags: {[tag for tag in raw_tags if not tag.strip() or tag.lower().strip() in [t for t in raw_tags[:raw_tags.index(tag)] if t.strip()]]}
""")

print("✅ Challenge completed!")
print("=" * 60)
