# 🐍 Python Journey: From Basics to AI/ML

Welcome to my Python learning journey! This repository documents my progress from Python fundamentals to advanced AI/ML concepts.

## 📚 About This Repository

This is a personal learning log where I track my daily progress, code exercises, and projects as I advance from Python basics to artificial intelligence and machine learning.

**Started:** January 2026  
**Goal:** Master Python and become proficient in AI/ML

## 🗺️ Learning Roadmap

### Phase 1: Python Fundamentals ✅ COMPLETE!
- [x] Day 1: Data Types, Variables, and Type Conversion
- [x] Day 2: Strings and String Manipulation
- [x] Day 3: Arithmetic Operators and Mathematical Operations
- [x] Day 4: Week 1 Revision & Bioinformatics Applications
- [x] Day 5: Conditional Statements (if/else)
- [x] Day 6: Loops (while and for) & Loop Control
- [x] Day 7: Advanced Loop Patterns & Practice
- [x] Day 8: Practice & Consolidation (elif)
- [x] Day 9: Lists - Python's Fundamental Data Structure
- [x] Day 10: Dictionaries - Key-Value Data Structures
- [x] Day 11: Tuples - Immutable Sequences
- [x] Day 12: Sets - Unique Elements & Mathematical Operations
- [x] Day 13: List Comprehensions - Elegant List Creation
- [x] Day 14: Week 3 Revision & Consolidation
- [x] Day 15: Functions - Part 1 (Basics, Parameters, Return Values, Scope)
- [x] Day 16: Modules - Code Organization & Reusability
- [x] Day 17: File Handling (Reading and Writing Files)
- [x] Day 18: Exception Handling & Debugging
- [x] Day 19: Advanced Functions (*args, **kwargs, Lambda)
- [x] Day 20: Python Project Structure & Package Management

### Phase 2: Scientific Computing & Data Analysis 🔄 (In Progress)
- [x] Day 21: NumPy Introduction - Arrays, Indexing, Arithmetic, Broadcasting
- [x] Day 22: NumPy Advanced - Reshape, Masking, Stacking, File I/O, Linear Algebra
- [x] Day 23: Pandas Introduction - Series, DataFrames, Indexing, CSV Loading
- [ ] Pandas Data Manipulation - Cleaning, Grouping, Merging
- [ ] Matplotlib & Seaborn
- [ ] Data Cleaning & Preprocessing

### Phase 3: Machine Learning Basics
- [ ] Scikit-learn
- [ ] Supervised Learning (Regression, Classification)
- [ ] Unsupervised Learning (Clustering, Dimensionality Reduction)
- [ ] Model Evaluation & Validation

### Phase 4: Deep Learning & AI
- [ ] Neural Networks Fundamentals
- [ ] TensorFlow/Keras or PyTorch
- [ ] Computer Vision
- [ ] Natural Language Processing (NLP)
- [ ] Advanced AI Techniques

## 📂 Repository Structure

```
python-journey-to-ai-ml/
├── README.md
├── Day-01-Data-Types-and-Variables/
├── Day-02-Strings-and-Manipulation/
├── Day-03-Arithmetic-Operators/
├── Day-04-Week-1-Revision/
├── Day-05-Conditional-Statements/
├── Day-06-Loops/
├── Day-07-Advanced-Loops/
├── Day-08-Practice-Consolidation/
├── Day-09-Lists/
├── Day-10-Dictionaries/
├── Day-11-Tuples/
├── Day-12-Sets/
├── Day-13-List-Comprehensions/
├── Day-14-Week-3-Revision/
├── Day-15-Functions-Part-1/
├── Day-16-Modules/
├── Day-18-Exception-Handling/
├── Day-19-Advanced-Functions/
├── Day-20-Project-Structure-Packages/
├── Day-21-NumPy-Introduction/
├── Day-22-NumPy-Advanced/
├── Day-23-Pandas-Introduction/
│   ├── exercises.py
│   ├── concepts.md
│   ├── notes.md
│   └── sample.csv
├── Day-24-.../
└── projects/
```

## 🚀 Daily Progress

### Day 1: Data Types, Variables, and Type Conversion
**Date:** January 13, 2026

**Topics Covered:**
- Python data types (int, float, string, boolean, None)
- Print function and f-strings
- Type checking with `type()`
- Dynamic typing
- Type conversion/casting
- User input with `input()`

**Key Takeaways:**
- Python is dynamically typed - variables can change types
- F-strings are the modern way to format strings in Python
- `input()` always returns a string, requiring conversion for numbers
- Type conversion is explicit using `int()`, `float()`, `str()`, `bool()`

**Exercises Completed:** 8 tasks covering personal details, product info, temperature conversion, string manipulation, user input, boolean flags, and type reassignment.

[View Day 1 Details →](./day-01/concepts.md)

---

### Day 2: Strings and String Manipulation
**Date:** January 14, 2026

**Topics Covered:**
- String concatenation with `+` and f-strings
- String multiplication with `*`
- String indexing (positive and negative)
- String slicing with `[start:stop:step]`
- String length with `len()`
- Escape sequences (`\n`, `\t`, `\'`, `\"`)
- Raw strings with `r` prefix

**Key Takeaways:**
- String slicing is powerful: `text[::-1]` reverses a string
- Negative indexing counts from the end: `-1` is the last character
- F-strings handle type conversion automatically
- Escape sequences allow special characters in strings
- Raw strings treat backslashes literally (useful for file paths)
- Strings are immutable - cannot change individual characters

**Exercises Completed:** 7 tasks covering concatenation, decorative separators, character extraction, substring creation, user input with length, escape sequences, and palindrome checking.

[View Day 2 Details →](./day-02/concepts.md)

---

### Day 3: Arithmetic Operators and Mathematical Operations
**Date:** January 15, 2026

**Topics Covered:**
- Basic operators: Addition, Subtraction, Multiplication, Division
- Advanced operators: Floor Division, Modulus, Exponentiation
- Operator precedence (BODMAS/PEMDAS)
- Division types: `/` vs `//`
- Type conversion in arithmetic operations
- Practical calculator implementations

**Key Takeaways:**
- Division (`/`) always returns a float, even for whole numbers
- Floor division (`//`) returns an integer, rounding down
- Modulus (`%`) is perfect for even/odd checks and remainders
- Exponentiation (`**`) can calculate roots: `9 ** 0.5 = 3.0`
- Operator precedence follows BODMAS/PEMDAS rules
- Exponentiation associates right-to-left
- Use parentheses to make complex expressions clear

**Exercises Completed:** 8 tasks including operator practice, division comparisons, even/odd checker, power calculator, rectangle calculator, order of operations, simple interest calculator, and tip calculator.

**Practical Applications:** Built 5 functional calculators demonstrating real-world use of arithmetic operators.

[View Day 3 Details →](./day-03/concepts.md)

---

### Day 4: Week 1 Revision & Bioinformatics Applications
**Date:** January 16, 2026

**Topics Covered:**
- Comprehensive revision of Days 1-3 concepts
- Integration of variables, strings, and arithmetic
- Introduction to bioinformatics applications
- DNA sequence analysis and GC content calculation
- Protein sequence composition analysis
- Molecular weight calculations

**Key Takeaways:**
- All Week 1 concepts work together in real applications
- String methods like `.count()` are powerful for biological data
- Python is used in real scientific research (genomics, proteomics)
- Breaking complex problems into simple steps is essential
- Type conversion and f-strings are fundamental to interactive programs
- Bioinformatics is accessible with basic Python skills

**Exercises Completed:** 8 comprehensive tasks including personal info display, geometry calculations, average calculator, welcome message, integrated mini-challenge, DNA sequence analysis, amino acid composition, and molecular weight calculation.

**Practical Applications:** Analyzed DNA sequences for GC content, examined protein compositions, and calculated molecular weights - real tasks used in research labs!

[View Day 4 Details →](./day-04/concepts.md)

---

### Day 5: Conditional Statements (if/else)
**Date:** January 17, 2026

**Topics Covered:**
- Comparison operators (==, !=, >, <, >=, <=)
- Boolean values and logic
- if statements for conditional execution
- else statements for alternatives
- Python indentation and code blocks
- Type conversion with conditionals
- Decision-making in programs

**Key Takeaways:**
- Programs can now make decisions based on conditions
- Comparison operators return True or False (booleans)
- Indentation defines code blocks in Python (4 spaces)
- Use == for comparison, not = (which is assignment)
- Always convert input() before using in comparisons
- if/else creates two possible execution paths
- Modulus (%) with conditionals is perfect for even/odd checks

**Exercises Completed:** 7 programs including comparison operator practice, positive/negative checker, password validator, gene expression analyzer, adult/minor classifier, even/odd checker, and pass/fail grading system.

**Practical Applications:** Built password validator, gene expression analyzer, grading system - programs that respond intelligently to different inputs!

[View Day 5 Details →](./day-05/concepts.md)

---

### Day 6: Loops (while and for) & Loop Control
**Date:** January 19, 2026

**Topics Covered:**
- while loops for condition-based repetition
- for loops for iterating over sequences
- Loop control with break (exit loop) and continue (skip iteration)
- range() function for number sequences
- try/except for error handling
- Increment/decrement operators (+=, -=)
- Practical loop patterns and applications

**Key Takeaways:**
- Loops enable automation - process unlimited data with few lines
- while loops run while condition is True (unknown iterations)
- for loops iterate over known sequences (lists, ranges)
- break exits loop immediately, continue skips current iteration
- while True with break creates controlled infinite loops (perfect for menus)
- try/except prevents crashes from invalid input
- range() creates number sequences (stop value is exclusive)
- Loops + conditionals = powerful data processing

**Exercises Completed:** 5 programs including countdown timer, input validator with try/except, gene list search with break, patient status processor with continue, and fully functional ATM simulator.

**Practical Applications:** Built ATM simulator, gene search engine, patient data processor - real automation and interactive applications!

[View Day 6 Details →](./day-06/concepts.md)

---

### Day 7: Advanced Loop Patterns & Practice
**Date:** January 20, 2026

**Topics Covered:**
- Advanced range() usage (start, stop, step variations)
- Negative step for backward counting
- String iteration (character-by-character processing)
- Combining loops with conditionals for filtering
- Logical operators in loops (AND, OR, NOT)
- Common loop patterns (repetition, filtering, searching, accumulation)
- Practical password systems and validation loops
- Bioinformatics applications (genome scanning)

**Key Takeaways:**
- range() is incredibly versatile - can create any number sequence
- Negative step enables countdown: range(10, 0, -1)
- Strings are iterable - can loop through each character
- Loops + conditionals = powerful data filtering and processing
- Logical operators (and/or) enable complex filtering conditions
- Pattern recognition is key - most problems fit common patterns
- Practice reveals patterns and builds muscle memory
- for with range() is cleaner than while for counting

**Exercises Completed:** 8 comprehensive tasks including squares calculator, balance decrementer, divisibility filter, number validator, multiples finder, 3-attempt password system, skip multiples with continue, and genome scanner.

**Practical Applications:** Built password authentication system with limited attempts, created genome scanner simulating chromosome processing, implemented sophisticated filters with logical operators!

[View Day 7 Details →](./day-07/concepts.md)

---

### Day 8: Practice & Consolidation (elif)
**Date:** January 21, 2026

**Topics Covered:**
- elif statement for efficient multi-way decisions
- Comparison: if/elif/else vs multiple if statements
- Decision tree patterns and category classification
- Simplifying conditional logic in elif chains
- Integration of all concepts from Days 1-8
- Code optimization and efficiency
- Multiple solution approaches to same problem

**Key Takeaways:**
- elif is more efficient than multiple ifs - stops at first True condition
- Only ONE block executes in if/elif/else chain
- Order matters - check most specific conditions first
- Later elifs can be simplified - they know previous conditions were False
- Use if/elif/else for mutually exclusive categories
- Use multiple ifs for independent conditions that can all be true
- Consolidation strengthens understanding better than rushing to new topics
- Every problem often has multiple valid solutions

**Exercises Completed:** 3 focused tasks including grade classifier with if/elif/else, even number filter (showing 3 different methods), and bottles countdown with while loop.

**Practical Applications:** Built efficient grade classification system, demonstrated multiple solution approaches to filtering, integrated all 8 days of concepts seamlessly!

[View Day 8 Details →](./day-08/concepts.md)

---

### Day 9: Lists - Python's Fundamental Data Structure
**Date:** January 22, 2026

**Topics Covered:**
- List creation (integers, strings, mixed types, empty lists)
- Indexing (positive and negative) to access elements
- Slicing with [start:stop:step] notation
- List mutability - modifying lists after creation
- Adding elements (append, insert, extend methods)
- Removing elements (pop, remove, del, clear methods)
- List methods (sort, reverse, count, index)
- Membership testing with 'in' operator
- Iterating through lists with for loops
- List operations (concatenation, repetition)
- Bioinformatics applications (gene lists, methylation data)

**Key Takeaways:**
- Lists are mutable - can be changed after creation (unlike strings!)
- Indexing starts at 0, negative indices count from end (-1 is last)
- Slicing stop value is exclusive, [::-1] reverses a list
- append() adds to end, insert() adds at specific position
- pop() removes and returns item, remove() removes by value
- sort() modifies list in place, sorted() returns sorted copy
- Lists + loops = powerful data processing capability
- Lists are fundamental to working with real datasets
- in operator checks membership efficiently
- Lists open the door to data science and analysis

**Exercises Completed:** Comprehensive exploration of list operations including creation, indexing, slicing, modification, adding/removing elements, sorting, iteration, and practical bioinformatics applications with gene lists and methylation data.

**Practical Applications:** Managed gene lists, processed methylation values with threshold filtering, tracked experiment workflows - real research data processing patterns!

[View Day 9 Details →](./day-09/concepts.md)

---

### Day 10: Dictionaries - Key-Value Data Structures
**Date:** January 23, 2026 🌼 *Vasant Panchami - Festival of Knowledge*

**Topics Covered:**
- Dictionary creation (empty, with data, dict() constructor)
- Accessing values with [] and .get() methods
- Adding and modifying items (same syntax!)
- Removing items (del, pop(), popitem(), clear())
- Dictionary views (keys(), values(), items())
- Membership testing with 'in' operator
- Iterating through dictionaries (three methods)
- Valid keys and values (immutability requirement)
- Common dictionary patterns (counting, filtering, building)
- Bioinformatics applications (gene expression mapping, patient records)

**Key Takeaways:**
- Dictionaries map keys to values for fast lookups (O(1) time)
- Use [] when certain key exists, .get() when it might not exist
- Same syntax for adding and modifying: dict[key] = value
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be any type (including lists and other dictionaries)
- .items() iteration is most Pythonic: for key, value in dict.items()
- Dictionary views are dynamic - automatically reflect changes
- pop() removes and returns value, del just deletes
- Perfect for structured data: patient info, gene expression, configs
- Dictionaries are everywhere: JSON, APIs, databases, configs

**Exercises Completed:** Comprehensive dictionary operations including creation, access ([] vs .get()), adding/modifying, removing (all methods), views, membership testing, iteration patterns, and methylation analysis mini-project filtering hypermethylated sites.

**Practical Applications:** Built gene expression mapper, patient metadata storage, methylation site analyzer - real-world key-value data organization matching database and API patterns!

[View Day 10 Details →](./day-10/concepts.md)

---

### Day 11: Tuples - Immutable Sequences
**Date:** January 26, 2026

**Topics Covered:**
- Tuple creation (parentheses, tuple packing, single-element tuples)
- Tuple immutability - cannot change after creation
- Indexing and slicing (same as lists and strings)
- Tuple unpacking - extracting elements into variables
- Tuple methods (count and index - only 2 methods!)
- Converting between tuples, lists, and strings
- When to use tuples vs lists vs dictionaries
- Tuples as dictionary keys
- Common tuple patterns (multiple returns, coordinate pairs)
- Bioinformatics applications (genomic coordinates, patient IDs)

**Key Takeaways:**
- Tuples are IMMUTABLE - cannot be changed after creation (data integrity!)
- Single element tuple requires trailing comma: (1,) not (1)
- Parentheses are optional for tuple packing: 1, 2, 3 is a tuple
- Same indexing and slicing as lists: my_tuple[0], my_tuple[1:3], my_tuple[::-1]
- Only 2 methods: count() and index() (no modification methods!)
- Unpacking extracts elements: x, y = (10, 20)
- Tuples can be dictionary keys (lists cannot - they're mutable!)
- Faster and use less memory than lists
- Perfect for data that shouldn't change (coordinates, IDs, config)
- Variable swapping uses tuples: a, b = b, a
- Functions naturally return tuples for multiple values
- Immutability is a feature, not a limitation - ensures data integrity

**Exercises Completed:** Comprehensive tuple operations including creation (all methods), single-element tuples with trailing comma, indexing/slicing, immutability testing, concatenation, unpacking (basic and with different types), count() and index() methods with try/except, and bioinformatics applications with genomic coordinates and patient samples.

**Practical Applications:** Created genomic coordinate tuples, defined immutable DNA base constants, stored patient IDs that shouldn't change, built coordinate systems for chromosome positions - real data integrity patterns!

[View Day 11 Details →](./day-011/concepts.md)

---

### Day 12: Sets - Unique Elements & Mathematical Operations
**Date:** January 27, 2026

**Topics Covered:**
- Set creation (curly braces, from lists/tuples, set() constructor)
- Automatic duplicate removal (uniqueness property)
- Unordered nature (no indexing or slicing allowed)
- Elements must be immutable (hashable types only)
- Adding elements (add for single, update for multiple)
- Removing elements (remove, discard, pop, clear methods)
- Fast membership testing with 'in' operator (O(1) time)
- Set operations: union (|), intersection (&), difference (-), symmetric difference (^)
- Subset and superset relationships (<=, >=, <, >)
- Bioinformatics applications (gene comparison, sample analysis)

**Key Takeaways:**
- Sets automatically remove duplicates - no manual deduplication needed!
- {} creates empty dict, NOT empty set - use set() instead
- Sets are unordered - cannot use indexing or slicing
- Elements must be immutable (strings, numbers, tuples OK; lists, dicts NOT OK)
- add() adds single element, update() adds multiple elements
- remove() raises KeyError if not found, discard() doesn't (safer!)
- pop() removes arbitrary element (sets are unordered)
- O(1) membership testing vs O(n) for lists - huge performance gain
- Mathematical operators: | (union/OR), & (intersection/AND), - (difference/MINUS), ^ (XOR)
- Perfect for removing duplicates and comparing collections
- Subset (<=) checks if all elements of A in B, superset (>=) checks if A contains all of B
- Set operations enable powerful data comparisons in one line

**Exercises Completed:** Comprehensive set operations including creation (from lists, tuples, direct), duplicate removal, adding/removing elements (all methods), membership testing, mathematical operations (union, intersection, difference, symmetric difference), subset/superset checks, and bioinformatics mini-project comparing hypermethylated genes across samples.

**Practical Applications:** Built gene comparison analyzer finding common genes, sample-specific genes, and all unique genes across samples - real genomics research patterns using set theory!

[View Day 12 Details →](./day-12/concepts.md)

---

### Day 13: List Comprehensions - Elegant List Creation
**Date:** January 28, 2026

**Topics Covered:**
- Basic list comprehensions (simple transformations)
- List comprehensions with filtering
- Conditional expressions in list comprehensions
- Combining transformation and filtering
- Nested list comprehensions
- Flattening lists of lists
- Bioinformatics applications (gene processing, methylation filtering)

**Key Takeaways:**
- List comprehensions are more concise than traditional for loops
- Basic syntax: `[expression for item in iterable]`
- With filter: `[expression for item in iterable if condition]`
- With if/else: `[expr1 if condition else expr2 for item in iterable]`
- Nested syntax: `[expr for i in outer for j in inner]`
- More readable and Pythonic than equivalent loop code
- Generally faster than traditional loops (optimized in Python)
- Filter comes BEFORE transformation in syntax
- Conditional expression (if/else) comes BEFORE the for clause
- Perfect for transforming and filtering lists in one elegant line
- Can become hard to read if too complex - keep it simple!
- Works with any iterable (lists, tuples, sets, strings, ranges)

**Exercises Completed:** Comprehensive practice with basic transformations (squares, uppercase, suffixes), filtering (even numbers, threshold values, gene names by prefix), conditional expressions (Even/Odd labels, High/Low categorization), combined operations (transform + filter), nested comprehensions (coordinate pairs, list flattening), and bioinformatics applications with gene name processing and methylation analysis.

**Practical Applications:** Built elegant one-line solutions for gene name preprocessing (uppercase conversion, suffix addition), methylation value filtering (above threshold), gene filtering by starting letter, and expression level categorization - demonstrating the power and elegance of Pythonic code!

[View Day 13 Details →](./day-13/concepts.md)

---

### Day 14: Week 3 Revision & Consolidation
**Date:** January 29, 2026

**Topics Covered:**
- Complete revision of Lists (create, access, modify, extend, remove, check)
- Complete revision of Tuples (immutability, unpacking, membership testing)
- Complete revision of Dictionaries (access patterns, modification, iteration)
- Complete revision of Sets (operations, uniqueness, filtering)
- Complete revision of List Comprehensions (all patterns)
- Integrated tasks combining multiple data structures
- Dictionary comprehensions (advanced introduction)
- zip() function for pairing iterables

**Key Takeaways:**
- Completed 20+ comprehensive revision tasks covering all Week 3 content
- Reinforced understanding of all 4 core data structures
- Practiced side-by-side comparisons of traditional loops vs comprehensions
- Mastered integration of multiple structures in real-world scenarios
- Lists excel at ordered sequences that need modification
- Tuples provide immutability and data integrity for fixed data
- Dictionaries enable fast O(1) lookups with meaningful keys
- Sets automatically handle uniqueness and support mathematical operations
- List comprehensions make code more Pythonic and readable
- Dictionary comprehension syntax: {key: value for item in iterable}
- zip() pairs elements from multiple iterables for parallel processing
- Choosing the right data structure is crucial for efficient code

**Exercises Completed:** 6 comprehensive sections with 20+ individual tasks - Lists (3 tasks), Tuples (3 tasks), Dictionaries (3 tasks), Sets (3 tasks), List Comprehensions (4 tasks), Integrated Tasks (4 tasks) - all comparing traditional approaches with modern Pythonic solutions, demonstrating mastery of all Week 3 concepts.

**Practical Applications:** Gene expression value management, genomic coordinate handling, patient metadata processing, mutation type analysis with automatic deduplication, gene pathway comparison using set operations, QC sample filtering, and advanced dictionary comprehensions for gene-expression mapping - complete data structure integration!

[View Day 14 Details →](./day-14/concepts.md)

---

### Day 15: Functions - Part 1
**Date:** January 30, 2026

**Topics Covered:**
- Function definition using def keyword
- Basic functions (no parameters, no return)
- Functions with parameters (single and multiple)
- Return values (single and multiple via tuples)
- Positional vs keyword arguments
- Default parameter values
- Variable scope (local vs global)
- The global keyword and why to avoid it
- Docstrings for documentation
- Best practices for writing functions

**Key Takeaways:**
- Functions enable code reuse - write once, use many times (DRY principle)
- Use def keyword followed by function name and parentheses
- Parameters make functions flexible and reusable with different inputs
- return sends data back to the caller - can return any type
- Multiple values returned as tuples and can be unpacked
- Keyword arguments allow calling in any order
- Default parameters create optional arguments
- Parameters must be: non-defaults first, then defaults
- Local variables only exist inside functions (local scope)
- Global variables can be read but avoid modifying with global keyword
- Better practice: pass as parameter, return new value
- Variable shadowing - local variable can have same name as global
- Docstrings ("""text""") document what functions do
- Functions should focus on ONE clear task
- Descriptive names make code self-documenting
- Return early for error cases
- Functions can call other functions (composition)

**Exercises Completed:** Comprehensive practice with basic functions (say_hello, show_analysis_result), parameterized functions (greet, area_triangle), return values (add_numbers, get_list_stats), keyword arguments (gene_description), default parameters (set_analysis_parameter, configure_plot), scope examples (global vs local), and built a complete calculator function.

**Practical Applications:** Created gene description formatter, triangle area calculator, list statistics analyzer, methylation analysis parameter configurator, plot configuration function with defaults, and interactive calculator - demonstrating real-world function usage for bioinformatics and data analysis!

[View Day 15 Details →](./day-15/concepts.md)

---

### Day 16: Modules - Code Organization & Reusability
**Date:** January 31, 2026

**Topics Covered:**
- What are modules (Python files as reusable libraries)
- Creating custom modules (module1.py)
- Importing modules (import statement)
- Using imported functions (module.function() syntax)
- The `if __name__ == "__main__":` pattern
- The `__name__` magic variable
- Different import styles (standard, specific, alias, wildcard)
- Module search path and Python path
- Module best practices and naming conventions
- Module structure and organization
- Testing modules directly vs importing

**Key Takeaways:**
- Modules are simply Python files (.py) that can be imported
- Any Python file can be a module - no special syntax required
- Use `import module_name` to make functions available
- Access functions with `module_name.function_name()` syntax
- The `__name__` variable is set to "__main__" when file run directly
- The `__name__` variable equals module name when file is imported
- `if __name__ == "__main__":` allows dual-purpose files (module + script)
- This pattern enables testing within the module file
- Standard import (`import module`) is clearest and most professional
- Specific imports (`from module import function`) are shorter but less clear
- Alias imports (`import module as m`) balance brevity and clarity
- Avoid wildcard imports (`from module import *`) - causes namespace pollution
- Modules enable code organization and reusability (DRY principle)
- Keep related functions together in one module
- Use lowercase names with underscores for modules
- Include docstrings in modules and functions
- Test modules by running them directly
- Professional code is organized into multiple modules

**Exercises Completed:** Created module1.py with greet() and calculate() functions, created main_program.py that imports and uses module1, implemented `if __name__ == "__main__":` pattern for testing, demonstrated both direct execution and import usage, practiced different import styles.

**Practical Applications:** Built reusable calculator module with multiple operations (sum, difference, product, quotient), created greeting function for Palampur welcome message, demonstrated professional code organization, showed how to test modules independently, illustrated real-world module usage pattern!

[View Day 16 Details →](./day-16/concepts.md)

---

### Day 17: File Handling - Reading and Writing Data
**Date:** February 2, 2026

**Topics Covered:**
- File handling basics (open, read/write, close)
- File modes (r, w, a, r+, w+, a+)
- Writing text to files (write() method)
- Reading text from files (read(), readline(), readlines())
- Reading files line by line (iteration)
- Appending data to existing files
- The `with` statement (context manager)
- Automatic file closing with `with`
- String methods for file processing (strip(), split())
- File paths (relative vs absolute)
- Processing data pipelines (read → process → write)
- Creating and processing gene lists
- Filtering and transforming file data

**Key Takeaways:**
- Files enable data persistence - data survives program execution
- Three-step pattern: Open → Read/Write → Close
- Always use `with` statement - ensures automatic file closing
- `with` prevents resource leaks even when errors occur
- File mode 'r' reads (file must exist)
- File mode 'w' writes (OVERWRITES existing content - dangerous!)
- File mode 'a' appends (safely adds to end)
- write() method does NOT add newlines automatically - must include \n
- read() returns entire file as single string
- readline() returns one line at a time
- readlines() returns list of all lines
- Iterating with `for line in file` is best for large files
- Always use strip() to remove whitespace from read lines
- `with open(file, mode) as f:` is the professional pattern
- Nested `with` statements enable read-process-write workflows
- File handling is ESSENTIAL for real-world data processing

**Exercises Completed:** Wrote text to first_file.txt with multiple lines and gene data, read entire file with read() method, read line-by-line with iteration, appended new content safely, used `with` statement for automatic closing, created gene_list.txt with gene names, processed genes (read, uppercase, filter by starting letter), wrote selected genes to selected_genes.txt - complete data pipeline!

**Practical Applications:** Built real bioinformatics data pipeline - read gene list from file, converted to uppercase, filtered genes starting with 'T' or 'A', wrote results to new file. Created experiment logging system with append mode. Demonstrated read-process-write workflow for data transformation. This is REAL data processing!

[View Day 17 Details →](./day-17/concepts.md)

---

### Day 18: Exception Handling & Debugging
**Date:** February 3, 2026

**Topics Covered:**
- What are exceptions (runtime errors)
- The try-except block (basic error handling)
- Catching specific exceptions (ZeroDivisionError, ValueError, IndexError, etc.)
- Handling multiple exception types
- The else block (runs if no exception occurred)
- The finally block (always runs for cleanup)
- Complete try-except-else-finally pattern
- Accessing exception information with 'as'
- Raising custom exceptions with 'raise'
- Re-raising caught exceptions
- Common exception types and their causes
- Exception handling best practices
- Debugging technique 1: Reading tracebacks
- Debugging technique 2: print() debugging ("caveman debugging")
- Debugging technique 3: IDE debugger (breakpoints, stepping)
- Defensive programming (input validation)

**Key Takeaways:**
- Exceptions are errors that occur during program execution
- Without exception handling, programs crash when errors occur
- try-except allows programs to handle errors gracefully and continue running
- Always catch SPECIFIC exceptions, not generic Exception class
- try block contains code that might cause an error
- except block handles the error if it occurs
- Multiple except blocks can handle different error types
- else block runs ONLY if no exception occurred in try block
- finally block ALWAYS runs, whether error occurred or not
- finally is perfect for cleanup code (closing files, releasing resources)
- Use 'except ExceptionType as e' to capture exception object
- Use 'raise' to trigger exceptions manually for validation
- raise ValueError("message") creates custom error with message
- Common exceptions: ZeroDivisionError, ValueError, IndexError, KeyError, FileNotFoundError, TypeError
- Read tracebacks bottom-up: shows error type, location, and call stack
- print() debugging: add debug prints to trace execution flow
- Test edge cases: empty lists, None values, zero, invalid inputs
- Defensive programming: validate inputs before processing
- Don't silence exceptions - handle them meaningfully
- Exceptions are for exceptional cases, not normal control flow

**Exercises Completed:** Basic try-except with ZeroDivisionError, multiple exception handling (ValueError and IndexError), else block usage for success code, finally block for guaranteed cleanup, raising custom exceptions in methylation validation function, reading and understanding tracebacks, print() debugging with calculate_average function showing execution flow, complete exception handling pattern with file operations.

**Practical Applications:** Safe division operations, safe file reading with error handling, methylation value validation (must be 0-1), gene expression data processing with error recovery, complete data pipeline with try-except-else-finally pattern. Built production-quality code that handles all error cases gracefully!

[View Day 18 Details →](./day-18/concepts.md)

---

### Day 19: Advanced Functions - *args, **kwargs, Lambda
**Date:** February 4, 2026

**Topics Covered:**
- Variable positional arguments (*args)
- Variable keyword arguments (**kwargs)
- Understanding *args as tuple
- Understanding **kwargs as dictionary
- Combining *args and **kwargs in functions
- Parameter order rules (positional, defaults, *args, keyword-only, **kwargs)
- Lambda functions (anonymous functions)
- Lambda syntax: lambda parameters: expression
- Single expression limitation in lambdas
- Higher-order functions with lambdas
- map() function for transformations
- filter() function for selections
- sorted() function with custom key
- Functional programming patterns

**Key Takeaways:**
- *args collects extra positional arguments into a tuple
- **kwargs collects keyword arguments into a dictionary
- *args enables functions to accept any number of positional arguments
- **kwargs enables functions to accept any number of keyword arguments
- Can combine *args and **kwargs for maximum flexibility
- Parameter order is strict: regular positional, defaults, *args, keyword-only, keyword defaults, **kwargs
- Lambda creates anonymous one-line functions
- Lambda syntax: lambda params: expression (single expression only)
- Lambda automatically returns the expression result
- Lambda perfect for short, simple operations
- map(function, iterable) applies function to each element
- filter(function, iterable) keeps elements where function returns True
- sorted(iterable, key=function) sorts using custom key function
- Lambda commonly used with map(), filter(), and sorted()
- *args type is tuple - iterate with for loop
- **kwargs type is dict - use .items(), .get(), .keys()
- Functional programming enables elegant data pipelines
- Higher-order functions accept functions as parameters
- Use lambda for quick operations, regular functions for complex logic

**Exercises Completed:** Created greet() with *args accepting any number of arguments, sum_of_numbers() summing variable arguments, greeting() combining required and *args parameters, print_all_keywords() demonstrating **kwargs, configure_hyperparameters() with defaults from **kwargs, combined_function() using both *args and **kwargs, multiple lambda examples (add, square, max, conditionals), map() with lambda to transform data, filter() with lambda to select data, sorted() with lambda key for custom sorting, gene expression filtering and sorting pipeline.

**Practical Applications:** Built flexible logging function accepting any messages with metadata, created ML hyperparameter configuration accepting any settings, filtered high gene expression using lambda and filter(), sorted genes by expression level using lambda key, built data transformation pipeline combining map() and filter(), demonstrated functional programming patterns for data processing!

[View Day 19 Details →](./day-19/concepts.md)

---

### Day 20: Python Project Structure & Package Management
**Date:** February 5, 2026

**Topics Covered:**
- Modules vs Packages (key differences)
- Creating Python packages (directory + __init__.py)
- The __init__.py file (purpose, usage, public API)
- Sub-packages (nested package structure)
- Absolute imports (full path from project root)
- Relative imports (dot notation: ., .., ...)
- Virtual environments with venv (built-in)
- Creating and activating virtual environments
- Managing dependencies with requirements.txt
- pip freeze for capturing dependencies
- Installing from requirements.txt
- setup.py for distributable packages
- Professional project structure (src/ layout)
- venv vs Conda (when to use each)
- .gitignore for version control

**Key Takeaways:**
- Module = single .py file; Package = directory with __init__.py
- __init__.py is what makes a directory a Python package
- __init__.py executes when package is imported
- __init__.py defines the public API of the package
- Sub-packages are packages inside packages (nested directories)
- Absolute imports use full path: from myproject.package.module import x
- Relative imports use dots: from . import x (same dir), from .. import x (parent)
- Absolute imports are recommended for clarity
- Virtual environments isolate project dependencies completely
- venv is built into Python 3 - no installation needed
- Create venv: python -m venv venv
- Activate on Linux/Mac: source venv/bin/activate
- Activate on Windows: venv\Scripts\activate
- pip freeze > requirements.txt saves exact versions
- pip install -r requirements.txt recreates environment
- requirements.txt enables reproducible environments
- setup.py makes package installable with pip
- Professional structure: src/, tests/, docs/, README.md, requirements.txt
- Use venv for pure Python projects (lightweight)
- Use Conda for scientific computing needing system libraries (CUDA, MKL)
- Never commit virtual environment to git (.gitignore)
- Always use virtual environments for projects

**Exercises Completed:** Module vs package review (module1.py, main_program.py), created bioinformatics package structure with __init__.py, demonstrated sub-packages (io/, analysis/, utils/), showed absolute vs relative import patterns, complete virtual environment workflow, requirements.txt formats (pinned, minimum, range), complete gene_toolkit project structure with src/ layout.

**Practical Applications:** Built complete gene_toolkit bioinformatics package structure with sub-packages for I/O, analysis, and utilities. Demonstrated professional __init__.py with version and public API. Created requirements.txt for bioinformatics dependencies. Showed complete project lifecycle: create, activate venv, install, freeze, commit, reproduce!

[View Day 20 Details →](./day-20/concepts.md)

---

## 🔢 Phase 2: Scientific Computing & Data Analysis

### Day 21: NumPy Introduction - Arrays, Indexing, Arithmetic, Broadcasting
**Date:** February 6, 2026 | **Week 5, Day 1** 🎉

**Topics Covered:**
- Why NumPy (speed, memory, vectorization vs Python lists)
- Creating 1D and 2D arrays from Python lists
- Specifying dtype (float, int16, complex)
- Built-in creation functions: zeros, ones, full, eye, arange, linspace
- Random arrays: rand, randn, randint
- arange vs linspace (step vs count)
- Array attributes: ndim, shape, size, dtype, itemsize, nbytes
- 1D indexing (positive and negative)
- 2D indexing (row, col syntax)
- 1D and 2D slicing (all patterns)
- Slices are VIEWS not copies (.copy() for independence)
- Element-wise arithmetic (+, -, *, /, **)
- Scalar broadcasting in arithmetic
- Comparison operators (return boolean arrays)
- Universal functions: sin, cos, exp, log, log10, sqrt
- Aggregation: sum, min, max, mean, std, var, median
- np.median() vs arr.median() (no array method!)
- axis parameter: axis=0 (down columns), axis=1 (across rows)
- Broadcasting rules and examples
- Incompatible shapes → ValueError (handled with try-except)

**Key Takeaways:**
- NumPy is 10-100x faster than Python lists (C backend, vectorized)
- Arrays are homogeneous - all elements same dtype
- Vectorized operations eliminate for loops
- np.array() creates array from list; shape attribute shows dimensions
- arange(start, stop, step) like Python range; linspace(start, stop, count) for n points
- ndim=dimensions, shape=(rows,cols), size=total elements, dtype=element type
- Slices are VIEWS - modifying slice modifies original! Use .copy()
- All arithmetic is element-wise by default
- np.median(arr) ONLY - there is no arr.median() method!
- axis=0 operates down columns (collapses rows); axis=1 operates across rows (collapses columns)
- Broadcasting: dimensions compatible if equal or one is 1
- NumPy is the foundation of pandas, scikit-learn, TensorFlow, PyTorch

**Exercises Completed:** Created 1D/2D arrays, all creation functions, attribute inspection, 1D/2D indexing and modification, all slicing patterns, observed view behavior, element-wise arithmetic, ufuncs, all aggregation functions with and without axis, 2D axis operations, broadcasting examples (scalar, row vector, column vector), incompatible shape error handling.

**Practical Applications:** Gene expression matrix (mean per gene/sample, high-expression filtering), methylation data statistics (hypermethylated/hypomethylated sites), vectorized normalization (no loops!), boolean indexing for data filtering. **This is the foundation of MethylGraph-AI!**

[View Day 21 Details →](./day-21/concepts.md)

---

### Day 22: NumPy Advanced - Reshape, Masking, Stacking, File I/O, Linear Algebra
**Date:** February 7, 2026 | **Week 5, Day 2**

**Topics Covered:**
- Reshaping arrays (2D, 3D, the -1 inference trick)
- Compatible reshape rules (total elements must match)
- Flattening: ravel() returns VIEW, flatten() returns COPY
- Flatten ordering: row-major ('C') vs column-major ('F')
- Boolean array masking (condition-based filtering)
- Compound conditions using & (AND), | (OR), ~ (NOT)
- Modifying arrays in-place with boolean indexing
- Boolean indexing on 2D arrays
- vstack / row_stack (adds rows)
- hstack (concatenates flat for 1D, adds columns for 2D)
- column_stack (treats 1D arrays as columns of a 2D matrix)
- concatenate with axis parameter (most general)
- hsplit, vsplit, split (with count and index-based splitting)
- File I/O: np.save / np.load (.npy binary, single array)
- File I/O: np.savez / np.load (.npz archive, multiple arrays)
- File I/O: np.savetxt / np.loadtxt (CSV/text files)
- Handling missing data: genfromtxt and nan_to_num
- Linear algebra: dot product, matrix multiplication (@)
- Transpose (.T), inverse (linalg.inv), determinant (linalg.det)
- Eigenvalues and eigenvectors (linalg.eig)
- Matrix rank (linalg.matrix_rank)
- Trace (np.trace - sum of diagonal)

**Key Takeaways:**
- reshape total elements must match: 3×5=15 ≠ 20 → ValueError
- Use -1 in reshape to let NumPy infer that dimension automatically
- reshape returns a VIEW - modifying it changes the original!
- ravel() returns a VIEW (fast, memory efficient, modifies original)
- flatten() always returns a COPY (safe, independent)
- Boolean masking: use & | ~ NOT Python's and/or/not
- Parentheses required: (arr > 3) & (arr < 7)
- vstack adds rows, hstack for 2D adds columns
- column_stack turns 1D arrays into columns (not flat concatenation!)
- .npy = fast binary for single arrays
- .npz = dictionary-like archive for multiple named arrays
- Always close .npz files with loaded.close()
- genfromtxt handles missing values (NaN) gracefully
- nan_to_num replaces NaN with specified value
- @ operator for matrix multiplication, * for element-wise
- Matrix rank reveals linear dependence of rows/columns
- Eigenvalues/eigenvectors critical for PCA and dimensionality reduction

**Exercises Completed:** All reshape patterns including -1, ravel vs flatten comparison, boolean masking with simple and compound conditions, 2D masking and in-place modification, vstack/hstack/column_stack/concatenate for 1D and 2D, hsplit/vsplit/split with count and index arrays, save/load .npy single array, save/load .npz multiple named arrays, savetxt/loadtxt CSV, genfromtxt with missing values, nan_to_num, complete linear algebra suite.

**Practical Applications:** Gene expression filtering with boolean masks (no loops!), dataset save/load with .npz for complete experiments, neural network weight operations with @, PCA foundation with eigenvalue decomposition, reshape for ML pipelines (images to feature vectors), bioinformatics data persistence.

[View Day 22 Details →](./day-22/concepts.md)

---

### Day 23: Pandas Introduction - Series, DataFrames, Indexing, CSV
**Date:** February 8, 2026 | **Week 5, Day 3**

**Topics Covered:**
- What is Pandas (tabular data on top of NumPy)
- Pandas Series (1D labelled array)
- Creating Series (from list, NumPy, dict, with custom index and name)
- Missing keys in dict Series → NaN automatically
- Series attributes (values, index, dtype, shape, ndim, size, name, hasnans)
- Series indexing: .loc[] for labels, .iloc[] for positions
- Label slicing is INCLUSIVE at both ends (unique to pandas!)
- Position slicing is EXCLUSIVE at end (like Python/NumPy)
- Vectorized operations on Series (arithmetic, NumPy ufuncs)
- Boolean filtering on Series
- .get() for safe label access (avoids KeyError)
- Pandas DataFrame (2D labelled table)
- Creating DataFrames (dict of lists, list of dicts, 2D NumPy, dict of Series)
- Missing keys in list-of-dicts → NaN per cell
- DataFrame attributes (shape, index, columns, dtypes, values, ndim, size)
- DataFrame inspection (head, tail, info, describe)
- describe(include='all') for mixed data types
- Selecting single column → Series, multiple columns → DataFrame
- Attribute access for column selection (df.ColName)
- .loc[] for label-based row and column selection
- .iloc[] for integer position-based row and column selection
- Boolean indexing on DataFrames (filter rows)
- pd.read_csv() with common parameters

**Key Takeaways:**
- Series = 1D labelled array (NumPy array + named index)
- DataFrame = 2D labelled table (dict of Series sharing index)
- Always use .iloc for position, .loc for labels (never mix!)
- Label slicing s['a':'c'] includes 'c' - INCLUSIVE end
- Position slicing s[:3] excludes index 3 - EXCLUSIVE end
- s[1] with string index raises KeyError - use s.iloc[1]
- Single bracket df['Age'] returns Series
- Double brackets df[['Age']] returns DataFrame
- df[condition] filters rows, df['col'] selects column
- .loc[rows, cols] allows simultaneous row and column selection
- Missing keys in creation → NaN (Pandas handles messy real data)
- pd.read_csv() loads any tabular data in one line
- index_col parameter turns a column into the row index
- info() shows structure, describe() shows statistics

**Exercises Completed:** All Series creation methods, Series attributes inspection, .loc/.iloc indexing, inclusive vs exclusive slicing, vectorized operations, boolean filtering, .get() safe access, all DataFrame creation methods, DataFrame attributes, head/tail/info/describe, single and multiple column selection, .loc and .iloc row/column selection, boolean indexing with .loc, pd.read_csv() with index_col.

**Practical Applications:** Gene expression Series with named index, patient metadata DataFrame with custom row labels, clinical filtering (age, metastasis), gene expression CSV loading and analysis, chromosome filtering, tumor suppressor identification.

[View Day 23 Details →](./day-23/concepts.md)

## 💡 Resources

- [Python Official Documentation](https://docs.python.org/)
- [Real Python](https://realpython.com/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Kaggle](https://www.kaggle.com/learn)

## 🎯 Goals

- **Short-term:** Complete Python fundamentals within 2 months
- **Medium-term:** Build 3-5 data analysis projects
- **Long-term:** Develop and deploy an AI/ML application

## 📝 Notes

This is a learning journey, and mistakes are part of the process. Each day builds upon the previous one, and I'm committed to consistent practice and improvement.

---

**Happy Coding! 🚀**

**🔢 WEEK 5 IN PROGRESS! NumPy Mastered, Pandas Started! 🐼**

*Last Updated: February 8, 2026*
