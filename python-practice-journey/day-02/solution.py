"""
Day 2: The "Word Frequency Counter" Challenge
==============================================

The Scenario:
You are building a basic search engine. You have a string of text, and you need 
to count how many times each word appears to determine its "weight."

The Task:
Given this string:
text = "Python is amazing. Python is fast. Is python easy? YES!"

Create a dictionary called word_counts where:
    1. The keys are the words (lowercase).
    2. The values are the number of times that word appears.
    3. Punctuation must be ignored (e.g., "amazing." and "amazing" should be treated as the same).

The Constraint:
Try to solve this using the .get() method for dictionaries OR the collections.Counter 
class from Python's standard library.
"""

from collections import Counter, defaultdict
import string
import re

# Input data
text = "Python is amazing. Python is fast. Is python easy? YES!"

print("=" * 70)
print("Day 2: Word Frequency Counter Challenge")
print("=" * 70)
print(f"\nOriginal text: {text}")


# ============================================================================
# Solution 1: Using Counter (Most Pythonic) - Your Approach
# ============================================================================
print("\n" + "=" * 70)
print("Solution 1: Using Counter (Your Approach)")
print("=" * 70)

# Remove punctuation
clean_text = text.translate(str.maketrans('', '', string.punctuation))
print(f"\nAfter removing punctuation: {clean_text}")

# Convert to lowercase
text_lower = clean_text.lower()
print(f"After converting to lowercase: {text_lower}")

# Split into words
words = text_lower.split()
print(f"Word list: {words}")

# Count using Counter
word_counts = Counter(words)
print(f"\nWord counts (Counter): {word_counts}")
print(f"Type: {type(word_counts)}")


# ============================================================================
# Solution 2: Using Dictionary .get() Method
# ============================================================================
print("\n" + "=" * 70)
print("Solution 2: Using Dictionary .get() Method")
print("=" * 70)

clean_text = text.translate(str.maketrans('', '', string.punctuation))
words = clean_text.lower().split()

word_counts_dict = {}
for word in words:
    # .get() returns 0 if word doesn't exist, otherwise returns current count
    word_counts_dict[word] = word_counts_dict.get(word, 0) + 1

print(f"\nWord counts (dict with .get()): {word_counts_dict}")


# ============================================================================
# Solution 3: Using defaultdict
# ============================================================================
print("\n" + "=" * 70)
print("Solution 3: Using defaultdict")
print("=" * 70)

clean_text = text.translate(str.maketrans('', '', string.punctuation))
words = clean_text.lower().split()

word_counts_defaultdict = defaultdict(int)
for word in words:
    word_counts_defaultdict[word] += 1

print(f"\nWord counts (defaultdict): {dict(word_counts_defaultdict)}")


# ============================================================================
# Solution 4: Using Regular Expressions (Advanced)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 4: Using Regular Expressions")
print("=" * 70)

# \b = word boundary, \w+ = one or more word characters
words_regex = re.findall(r'\b\w+\b', text.lower())
word_counts_regex = Counter(words_regex)

print(f"\nWords extracted with regex: {words_regex}")
print(f"Word counts (regex + Counter): {word_counts_regex}")


# ============================================================================
# Solution 5: One-Liner (For the Brave)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 5: One-Liner Solution")
print("=" * 70)

word_counts_oneliner = Counter(text.translate(str.maketrans('', '', string.punctuation)).lower().split())
print(f"\nWord counts (one-liner): {word_counts_oneliner}")


# ============================================================================
# Advanced Features with Counter
# ============================================================================
print("\n" + "=" * 70)
print("Advanced: Counter Features")
print("=" * 70)

# Most common words
print(f"\nMost common word: {word_counts.most_common(1)}")
print(f"Top 3 most common: {word_counts.most_common(3)}")

# Total word count
print(f"Total words: {sum(word_counts.values())}")

# Unique words
print(f"Unique words: {len(word_counts)}")


# ============================================================================
# Bonus: Reusable Function
# ============================================================================
def count_words(text, min_length=1, ignore_case=True, remove_stopwords=False):
    """
    Count word frequencies in text with various options.
    
    Args:
        text (str): Text to analyze
        min_length (int): Minimum word length to count (default: 1)
        ignore_case (bool): Whether to ignore case (default: True)
        remove_stopwords (bool): Whether to remove common stop words (default: False)
    
    Returns:
        Counter: Word frequency counter
    """
    # Common English stop words
    stop_words = {'is', 'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 
                  'of', 'and', 'or', 'but', 'with', 'from', 'as'}
    
    # Remove punctuation
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Handle case
    if ignore_case:
        clean_text = clean_text.lower()
    
    # Split into words
    words = clean_text.split()
    
    # Filter by length and stop words
    filtered_words = [
        word for word in words 
        if len(word) >= min_length and (not remove_stopwords or word not in stop_words)
    ]
    
    return Counter(filtered_words)


print("\n" + "=" * 70)
print("Bonus: Using Reusable Function")
print("=" * 70)

# Test with different parameters
result1 = count_words(text)
result2 = count_words(text, min_length=4)
result3 = count_words(text, remove_stopwords=True)

print(f"\nDefault: {result1}")
print(f"Min length 4: {result2}")
print(f"Without stop words: {result3}")


# ============================================================================
# Advanced Analysis
# ============================================================================
print("\n" + "=" * 70)
print("Advanced: Text Analysis")
print("=" * 70)

def analyze_text(text):
    """Perform comprehensive text analysis."""
    word_counts = count_words(text)
    
    total_words = sum(word_counts.values())
    unique_words = len(word_counts)
    avg_word_length = sum(len(word) * count for word, count in word_counts.items()) / total_words
    most_common = word_counts.most_common(1)[0] if word_counts else None
    
    return {
        'total_words': total_words,
        'unique_words': unique_words,
        'avg_word_length': round(avg_word_length, 2),
        'most_common_word': most_common[0] if most_common else None,
        'most_common_count': most_common[1] if most_common else None,
        'vocabulary_richness': round(unique_words / total_words * 100, 2)
    }

analysis = analyze_text(text)
print(f"\nText Analysis:")
for key, value in analysis.items():
    print(f"  {key.replace('_', ' ').title()}: {value}")


# ============================================================================
# Visualization Helper
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Visual Representation")
print("=" * 70)

def display_word_chart(word_counts, top_n=5):
    """Display a simple text-based bar chart of word frequencies."""
    most_common = word_counts.most_common(top_n)
    
    if not most_common:
        print("No words to display")
        return
    
    # Find the maximum count for scaling
    max_count = most_common[0][1]
    
    print(f"\nTop {top_n} Words:")
    print("-" * 50)
    
    for word, count in most_common:
        # Create a bar using '█' characters
        bar_length = int((count / max_count) * 30)
        bar = '█' * bar_length
        print(f"{word:12} | {bar} {count}")

display_word_chart(word_counts)


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)

print(f"""
Original text: "{text}"
Cleaned text: "{clean_text.lower()}"

Results:
--------
Word frequency: {dict(word_counts)}
Total words: {sum(word_counts.values())}
Unique words: {len(word_counts)}
Most common: "{word_counts.most_common(1)[0][0]}" ({word_counts.most_common(1)[0][1]} times)

Methods used:
✓ Counter (from collections)
✓ Dictionary .get() method
✓ defaultdict
✓ Regular expressions
✓ String manipulation (translate, lower, split)
""")

print("=" * 70)
print("✅ Challenge completed!")
print("=" * 70)
