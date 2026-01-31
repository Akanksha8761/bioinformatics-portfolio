# 🐍 Python Journey: From Basics to AI/ML

Welcome to my Python learning journey! This repository documents my progress from Python fundamentals to advanced AI/ML concepts.

## 📚 About This Repository

This is a personal learning log where I track my daily progress, code exercises, and projects as I advance from Python basics to artificial intelligence and machine learning.

**Started:** January 2026  
**Goal:** Master Python and become proficient in AI/ML

## 🗺️ Learning Roadmap

### Phase 1: Python Fundamentals ✅ (In Progress)
- [x] Day 1: Data Types, Variables, and Type Conversion
- [x] Day 2: Strings and String Manipulation
- [x] Day 3: Arithmetic Operators and Mathematical Operations
- [x] Day 4: Week 1 Revision & Bioinformatics Applications
- [x] Day 5: Conditional Statements (if/else)
- [x] Day 6: Loops (while and for) & Loop Control
- [x] Day 7: Advanced Loop Patterns & Practice
- [x] Day 8: Practice & Consolidation (elif)
- [x] Day 9: Lists - Python's Fundamental Data Structure
- [ ] List Comprehensions and Advanced List Operations
- [ ] Functions and Modules
- [ ] Dictionaries and Sets
- [ ] Tuples and String Methods
- [ ] File Handling
- [ ] Exception Handling
- [ ] Object-Oriented Programming (OOP)

### Phase 2: Intermediate Python
- [ ] Decorators and Generators
- [ ] List Comprehensions
- [ ] Lambda Functions
- [ ] Regular Expressions
- [ ] Working with APIs
- [ ] Virtual Environments

### Phase 3: Data Analysis & Visualization
- [ ] NumPy
- [ ] Pandas
- [ ] Matplotlib & Seaborn
- [ ] Data Cleaning & Preprocessing

### Phase 4: Machine Learning Basics
- [ ] Scikit-learn
- [ ] Supervised Learning (Regression, Classification)
- [ ] Unsupervised Learning (Clustering, Dimensionality Reduction)
- [ ] Model Evaluation & Validation

### Phase 5: Deep Learning & AI
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
│   ├── notes.md
│   ├── exercises.py
│   └── concepts.md
├── Day-10-.../
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

*Last Updated: January 22, 2026*
