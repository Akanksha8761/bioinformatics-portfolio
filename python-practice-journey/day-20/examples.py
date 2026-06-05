######################### Example 1: Basic Module Review #########################

# This is from Day 16 - module1.py
# Demonstrates basic module structure

# File: module1.py
"""
def greet(name):
    '''Prints a greeting message'''
    return f"Hello, {name}! Welcome to Palampur!"

def calculate(num1, num2):
    '''Returns multiple calculations'''
    sum_result = num1 + num2
    sub = num1 - num2
    multi = num1 * num2
    divide = num1 / num2
    return sum_result, sub, multi, divide

if __name__ == "__main__":
    print("Testing module1.py")
    print(greet("Test"))
    results = calculate(30, 10)
    print(f"Results: {results}")
"""

# File: main_program.py
"""
import module1

print("Using module1")
print(module1.greet('Akanksha'))

sum_result, sub, multi, divide = module1.calculate(10, 2)
print(f"Sum: {sum_result}")
print(f"Difference: {sub}")
print(f"Product: {multi}")
print(f"Quotient: {divide}")
"""

######################### Example 2: Package Structure #########################

print("=" * 60)
print("EXAMPLE 2: Creating a Package")
print("=" * 60)

# Demonstrating package structure
print("""
Package Structure Example:

bioinformatics/
├── __init__.py          # Makes it a package
├── sequence.py          # Module for sequence operations
├── stats.py             # Module for statistics
└── utils.py             # Utility functions

# bioinformatics/__init__.py
'''Bioinformatics analysis package'''

from .sequence import gc_content, reverse_complement
from .stats import calculate_mean

__version__ = "1.0.0"
__all__ = ["gc_content", "reverse_complement", "calculate_mean"]

# bioinformatics/sequence.py
def gc_content(sequence):
    '''Calculate GC percentage'''
    sequence = sequence.upper()
    g = sequence.count('G')
    c = sequence.count('C')
    return ((g + c) / len(sequence)) * 100

def reverse_complement(sequence):
    '''Return reverse complement'''
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement[base] for base in reversed(sequence.upper()))

# bioinformatics/stats.py
def calculate_mean(values):
    '''Calculate mean of values'''
    return sum(values) / len(values)

# Usage:
import bioinformatics

# Thanks to __init__.py, these work directly:
gc = bioinformatics.gc_content("ATGCGCAT")
rev_comp = bioinformatics.reverse_complement("ATGC")
""")

######################### Example 3: Sub-Packages #########################

print("\n" + "=" * 60)
print("EXAMPLE 3: Sub-Packages")
print("=" * 60)

print("""
Complex Project with Sub-Packages:

gene_analyzer/
├── __init__.py
├── io/
│   ├── __init__.py
│   ├── fasta.py
│   └── csv_handler.py
├── analysis/
│   ├── __init__.py
│   ├── gc_analysis.py
│   └── motif_finder.py
└── utils/
    ├── __init__.py
    └── validators.py

# gene_analyzer/__init__.py
from .io import read_fasta, write_csv
from .analysis import analyze_gc_content, find_motifs

__version__ = "2.0.0"

# gene_analyzer/io/__init__.py
from .fasta import read_fasta
from .csv_handler import write_csv

# gene_analyzer/io/fasta.py
def read_fasta(filename):
    '''Read FASTA file'''
    sequences = {}
    with open(filename, 'r') as f:
        current_id = None
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:]
                sequences[current_id] = ""
            else:
                sequences[current_id] += line
    return sequences

# gene_analyzer/analysis/__init__.py
from .gc_analysis import analyze_gc_content
from .motif_finder import find_motifs

# gene_analyzer/analysis/gc_analysis.py
def analyze_gc_content(sequence):
    '''Analyze GC content'''
    # Using relative import from parent package
    from ..utils.validators import validate_dna_sequence
    
    if not validate_dna_sequence(sequence):
        raise ValueError("Invalid DNA sequence")
    
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return ((g_count + c_count) / len(sequence)) * 100

# Usage with absolute imports:
from gene_analyzer.io import read_fasta
from gene_analyzer.analysis import analyze_gc_content

sequences = read_fasta('data.fasta')
for seq_id, seq in sequences.items():
    gc = analyze_gc_content(seq)
    print(f"{seq_id}: {gc:.2f}% GC")
""")

######################### Example 4: Absolute vs Relative Imports #########################

print("\n" + "=" * 60)
print("EXAMPLE 4: Absolute vs Relative Imports")
print("=" * 60)

print("""
Project Structure:
myproject/
├── package1/
│   ├── __init__.py
│   ├── module_a.py
│   └── module_b.py
└── package2/
    ├── __init__.py
    └── module_c.py

# ABSOLUTE IMPORTS (Recommended)
# In myproject/package1/module_a.py:

from myproject.package1.module_b import function_b
from myproject.package2.module_c import function_c

# Clear and works from anywhere!

# RELATIVE IMPORTS
# In myproject/package1/module_a.py:

from .module_b import function_b      # Same directory
from ..package2.module_c import function_c  # Parent's sibling

# Dots meaning:
# .         = current package
# ..        = parent package
# ...       = grandparent package
# .module   = module in current package
# ..sibling = sibling package

# When to use relative imports:
# - Inside packages only
# - When package will be moved/renamed
# - For internal package structure

# Best Practice: Use absolute imports for clarity!
""")

######################### Example 5: Virtual Environment Workflow #########################

print("\n" + "=" * 60)
print("EXAMPLE 5: Virtual Environment Workflow")
print("=" * 60)

print("""
Complete Virtual Environment Workflow:

# Step 1: Create project directory
mkdir my_project
cd my_project

# Step 2: Create virtual environment
python -m venv venv

# Step 3: Activate virtual environment
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\\Scripts\\activate

# You'll see (venv) in your prompt now!

# Step 4: Install packages
pip install numpy pandas matplotlib

# Step 5: Save dependencies
pip freeze > requirements.txt

# Step 6: Work on project
python main.py

# Step 7: Deactivate when done
deactivate

# ==========================================
# Later, on a different machine:
# ==========================================

# Step 1: Clone project
git clone <repo>
cd my_project

# Step 2: Create virtual environment
python -m venv venv

# Step 3: Activate
source venv/bin/activate  # or venv\\Scripts\\activate on Windows

# Step 4: Install dependencies
pip install -r requirements.txt

# Ready to go! Same environment!
""")

######################### Example 6: requirements.txt Examples #########################

print("\n" + "=" * 60)
print("EXAMPLE 6: requirements.txt Formats")
print("=" * 60)

print("""
# Basic requirements.txt
numpy
pandas
matplotlib

# Pinned versions (exact)
numpy==1.24.0
pandas==2.0.0
matplotlib==3.7.0

# Minimum version
numpy>=1.20.0
pandas>=1.5.0

# Version range
matplotlib>=3.5.0,<4.0.0

# From Git repository
git+https://github.com/user/repo.git

# Comments and organization
# Data processing
numpy>=1.20.0
pandas>=1.5.0

# Visualization
matplotlib>=3.5.0
seaborn>=0.12.0

# Scientific computing
scipy>=1.9.0
scikit-learn>=1.2.0

# Bioinformatics
biopython>=1.79

# Development dependencies (requirements-dev.txt)
pytest>=7.0.0
black>=22.0.0
flake8>=5.0.0
mypy>=0.990
""")

######################### Example 7: Complete Project Example #########################

print("\n" + "=" * 60)
print("EXAMPLE 7: Complete Bioinformatics Project")
print("=" * 60)

print("""
gene_toolkit/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
│
├── src/
│   └── gene_toolkit/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── sequence.py
│       │   └── analysis.py
│       ├── io/
│       │   ├── __init__.py
│       │   ├── readers.py
│       │   └── writers.py
│       └── utils/
│           ├── __init__.py
│           └── validators.py
│
├── tests/
│   ├── __init__.py
│   ├── test_sequence.py
│   └── test_analysis.py
│
└── data/
    └── sample.fasta

# src/gene_toolkit/__init__.py
'''Gene Toolkit - Bioinformatics analysis package'''

from .core.sequence import reverse_complement, translate
from .core.analysis import gc_content, calculate_tm
from .io.readers import read_fasta
from .io.writers import write_fasta

__version__ = "1.0.0"
__all__ = [
    "reverse_complement",
    "translate", 
    "gc_content",
    "calculate_tm",
    "read_fasta",
    "write_fasta"
]

# src/gene_toolkit/core/sequence.py
'''Core sequence operations'''

from ..utils.validators import validate_dna

def reverse_complement(sequence):
    '''Return reverse complement of DNA sequence'''
    if not validate_dna(sequence):
        raise ValueError("Invalid DNA sequence")
    
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement[base] for base in reversed(sequence.upper()))

def translate(sequence):
    '''Translate DNA to protein'''
    # Implementation here
    pass

# src/gene_toolkit/core/analysis.py
'''Analysis functions'''

def gc_content(sequence):
    '''Calculate GC percentage'''
    sequence = sequence.upper()
    g = sequence.count('G')
    c = sequence.count('C')
    return ((g + c) / len(sequence)) * 100

def calculate_tm(sequence):
    '''Calculate melting temperature'''
    # Implementation here
    pass

# src/gene_toolkit/utils/validators.py
'''Validation utilities'''

def validate_dna(sequence):
    '''Check if sequence contains only valid DNA bases'''
    valid_bases = set('ATGC')
    return all(base.upper() in valid_bases for base in sequence)

# requirements.txt
biopython>=1.79
numpy>=1.20.0
pandas>=1.5.0

# setup.py
from setuptools import setup, find_packages

setup(
    name="gene-toolkit",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "biopython>=1.79",
        "numpy>=1.20.0",
        "pandas>=1.5.0",
    ],
    python_requires=">=3.8",
)

# Usage:
from gene_toolkit import gc_content, reverse_complement, read_fasta

# Read sequences
sequences = read_fasta('data/sample.fasta')

# Analyze
for seq_id, seq in sequences.items():
    gc = gc_content(seq)
    rev_comp = reverse_complement(seq)
    print(f"{seq_id}:")
    print(f"  GC Content: {gc:.2f}%")
    print(f"  Reverse Complement: {rev_comp[:50]}...")
""")

print("\n" + "=" * 60)
print("Day 20 Complete - Professional Project Structure!")
print("=" * 60)
