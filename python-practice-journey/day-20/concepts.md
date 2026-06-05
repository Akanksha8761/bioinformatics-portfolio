# Day 20: Python Project Structure & Package Management - Concepts

## 📌 Core Concepts Covered

Today we learn how to organize Python projects professionally, understand packages vs modules, manage dependencies, use virtual environments, and structure real-world applications. This is essential knowledge for building production software!

---

## 1. Modules vs Packages

### **Module:**
A **module** is a single Python file (`.py`) containing code.

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"
```

**Usage:**
```python
import my_module
my_module.greet("Alice")
```

### **Package:**
A **package** is a directory containing Python modules and a special `__init__.py` file.

```
my_package/
├── __init__.py      # Makes it a package!
├── module1.py
└── module2.py
```

**Key Difference:**
- **Module** = Single file
- **Package** = Directory with modules + `__init__.py`

---

## 2. The `__init__.py` File

### **Purpose:**
- Marks a directory as a Python package
- Executes when package is imported
- Can define what gets imported with `from package import *`
- Can expose convenient imports

### **Example:**

**Package structure:**
```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

**`__init__.py` (empty):**
```python
# Empty file - just marks directory as package
```

**`__init__.py` (with code):**
```python
# Makes imports easier
from .module1 import function1
from .module2 import function2

__version__ = "1.0.0"
```

**Usage:**
```python
# Without __init__.py imports
import mypackage.module1
mypackage.module1.function1()

# With __init__.py imports
import mypackage
mypackage.function1()  # Easier!
```

---

## 3. Sub-Packages

Packages can contain other packages (nested structure).

### **Structure:**
```
project/
├── main_package/
│   ├── __init__.py
│   ├── module1.py
│   ├── sub_package/
│   │   ├── __init__.py
│   │   └── module2.py
│   └── another_sub/
│       ├── __init__.py
│       └── module3.py
```

### **Importing from Sub-Packages:**
```python
from main_package.sub_package import module2
from main_package.another_sub.module3 import function
```

---

## 4. Absolute vs Relative Imports

### **Absolute Imports:**
Full path from project root.

```python
# From any file in project
from myproject.package.module import function
from myproject.utils import helper
```

**Pros:**
- Clear and explicit
- Works from anywhere
- Recommended for most cases

### **Relative Imports:**
Path relative to current file location.

```python
# Inside myproject/package/module1.py

from . import module2           # Same directory
from .. import utils            # Parent directory
from ..other import helper      # Parent's sibling
from .sub import submodule      # Sub-directory
```

**Syntax:**
- `.` = current directory
- `..` = parent directory
- `...` = grandparent directory

**Pros:**
- Package can be renamed/moved easily
- Shorter

**Cons:**
- Less clear
- Only works within packages
- Can't use in scripts run directly

**Best Practice:** Use absolute imports for clarity!

---

## 5. Professional Project Structure

### **Small Project:**
```
my_project/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
└── tests/
    ├── __init__.py
    └── test_utils.py
```

### **Medium Project:**
```
bioinformatics_tool/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── parser.py
│   │   └── cleaner.py
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── statistics.py
│   │   └── visualization.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_parser.py
│   └── test_statistics.py
├── data/
│   └── sample_data.txt
└── docs/
    └── usage.md
```

### **Large Project:**
```
ml_framework/
├── README.md
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── .gitignore
├── .env.example
├── src/
│   └── ml_framework/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── model.py
│       │   └── trainer.py
│       ├── data/
│       │   ├── __init__.py
│       │   ├── loader.py
│       │   └── preprocessor.py
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── logger.py
│       │   └── config.py
│       └── api/
│           ├── __init__.py
│           └── endpoints.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── docs/
├── scripts/
├── config/
└── data/
    ├── raw/
    ├── processed/
    └── models/
```

---

## 6. Virtual Environments

### **What is a Virtual Environment?**
An isolated Python environment with its own packages, separate from system Python.

### **Why Use Virtual Environments?**
1. **Isolation** - Each project has its own dependencies
2. **No conflicts** - Different projects can use different package versions
3. **Reproducibility** - Easy to recreate exact environment
4. **Clean system** - Don't pollute system Python

### **Creating Virtual Environments:**

**Using venv (built-in):**
```bash
# Create virtual environment
python -m venv myenv

# Activate (Linux/Mac)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Deactivate
deactivate
```

**Using virtualenv:**
```bash
# Install
pip install virtualenv

# Create
virtualenv myenv

# Activate
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate      # Windows
```

---

## 7. Managing Dependencies

### **requirements.txt:**
Lists all project dependencies.

```
# requirements.txt
numpy==1.24.0
pandas>=2.0.0
matplotlib>=3.5.0,<4.0.0
requests
```

**Creating requirements.txt:**
```bash
# Save current environment
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

### **requirements-dev.txt:**
Development dependencies (testing, linting, etc.)

```
# requirements-dev.txt
pytest>=7.0.0
black
flake8
mypy
```

### **setup.py:**
For distributable packages.

```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
    ],
    python_requires=">=3.8",
)
```

---

## 8. venv vs Conda

### **venv:**
- Built into Python (3.3+)
- Lightweight
- Python packages only
- Fast
- Simple

### **Conda:**
- Separate installation
- Heavier
- Python + non-Python packages (C libraries, R, etc.)
- Environment and package manager
- Cross-language

### **When to Use Each:**

**Use venv when:**
- Pure Python project
- Want lightweight solution
- Don't need system libraries
- Standard Python development

**Use Conda when:**
- Need non-Python dependencies (C libraries, CUDA)
- Data science (NumPy with MKL, TensorFlow, PyTorch)
- Need specific Python version not on system
- Complex scientific computing

**For most projects: venv is sufficient!**

---

## 9. Complete Project Example

### **Bioinformatics Tool Structure:**

```
gene_analyzer/
├── README.md                 # Project description
├── requirements.txt          # Dependencies
├── .gitignore               # Git ignore file
├── setup.py                 # Package setup
├── LICENSE                  # License file
│
├── src/
│   └── gene_analyzer/       # Main package
│       ├── __init__.py
│       ├── cli.py           # Command-line interface
│       │
│       ├── io/              # Input/Output
│       │   ├── __init__.py
│       │   ├── fasta_reader.py
│       │   └── csv_writer.py
│       │
│       ├── processing/      # Data processing
│       │   ├── __init__.py
│       │   ├── sequence.py
│       │   └── quality.py
│       │
│       ├── analysis/        # Analysis algorithms
│       │   ├── __init__.py
│       │   ├── gc_content.py
│       │   └── motif_finder.py
│       │
│       └── utils/           # Utilities
│           ├── __init__.py
│           ├── validators.py
│           └── logger.py
│
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_io.py
│   ├── test_processing.py
│   └── test_analysis.py
│
├── data/                    # Sample data
│   ├── sample.fasta
│   └── expected_output.csv
│
├── docs/                    # Documentation
│   ├── usage.md
│   └── api.md
│
└── scripts/                 # Utility scripts
    └── analyze.py
```

### **Example Files:**

**`src/gene_analyzer/__init__.py`:**
```python
"""Gene Analyzer - A bioinformatics tool"""

from .analysis.gc_content import calculate_gc_content
from .io.fasta_reader import read_fasta

__version__ = "1.0.0"
__all__ = ["calculate_gc_content", "read_fasta"]
```

**`src/gene_analyzer/analysis/gc_content.py`:**
```python
"""GC content calculation"""

def calculate_gc_content(sequence):
    """Calculate GC percentage in DNA sequence"""
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    
    if total == 0:
        return 0.0
    
    return ((g_count + c_count) / total) * 100
```

**`requirements.txt`:**
```
biopython>=1.79
pandas>=1.3.0
numpy>=1.20.0
```

**`setup.py`:**
```python
from setuptools import setup, find_packages

setup(
    name="gene-analyzer",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "biopython>=1.79",
        "pandas>=1.3.0",
        "numpy>=1.20.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "gene-analyzer=gene_analyzer.cli:main",
        ],
    },
)
```

---

## 10. Best Practices

### **Project Structure:**
1. **Use src/ layout** - Keeps source separate from tests/docs
2. **One package, one purpose** - Single responsibility
3. **Flat is better than nested** - Don't over-nest packages
4. **Consistent naming** - Use snake_case for packages/modules
5. **Include tests/** - Test from day one

### **Package Design:**
1. **Clear __init__.py** - Define public API
2. **Absolute imports** - Clear and explicit
3. **Avoid circular imports** - Design dependencies carefully
4. **Document everything** - Docstrings in all modules

### **Dependency Management:**
1. **Pin versions** - For reproducibility
2. **Separate dev dependencies** - requirements-dev.txt
3. **Use virtual environments** - Always!
4. **Update regularly** - Security patches

### **Version Control:**
1. **Use .gitignore** - Exclude venv, __pycache__, etc.
2. **Commit requirements.txt** - Track dependencies
3. **Don't commit virtual environments** - Too large
4. **Tag releases** - v1.0.0, v1.1.0, etc.

---

## 11. Common Files Explained

### **README.md:**
Project description, installation, usage.

### **requirements.txt:**
Python package dependencies.

### **.gitignore:**
```
__pycache__/
*.pyc
.env
venv/
*.egg-info/
dist/
build/
```

### **setup.py:**
Makes package installable with pip.

### **LICENSE:**
Legal terms for using the code.

### **MANIFEST.in:**
Include non-Python files in package.

### **.env:**
Environment variables (API keys, secrets).
**Never commit this file!**

---

## 💡 Key Takeaways

1. **Module = file, Package = directory with __init__.py**
2. **__init__.py makes a directory a package**
3. **Sub-packages = nested packages**
4. **Absolute imports** are clearer (recommended)
5. **Relative imports** use dots (., .., ...)
6. **Virtual environments isolate dependencies**
7. **venv for Python-only**, Conda for system libraries
8. **requirements.txt lists dependencies**
9. **setup.py makes packages installable**
10. **Professional structure = src/, tests/, docs/**

---

## 📚 Quick Reference

| Concept | Description |
|---------|-------------|
| Module | Single .py file |
| Package | Directory with __init__.py |
| __init__.py | Marks directory as package |
| Sub-package | Package inside package |
| Absolute import | `from package.module import x` |
| Relative import | `from . import x` |
| venv | Built-in virtual environment |
| requirements.txt | Dependency list |
| setup.py | Package installer |

---

*Professional project structure is the foundation of maintainable, scalable software. Master it to build real applications!*
