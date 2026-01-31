"""
Day 9: The "Log File Parser" Challenge
=======================================

Extract error messages from log data and write to file.
"""

# Sample log data
log_data = """
INFO: User logged in
ERROR: Database connection failed
INFO: Search performed
ERROR: File not found
DEBUG: Cache cleared
"""

print("=" * 70)
print("Day 9: Log File Parser Challenge")
print("=" * 70)

# ============================================================================
# Recommended Solution
# ============================================================================
def get_errors(log_data):
    """Extract error messages from log data."""
    try:
        if not isinstance(log_data, str):
            return []
        
        errors = [
            line.split(": ", 1)[1]
            for line in log_data.splitlines()
            if line.strip().startswith("ERROR:")
        ]
        
        return errors
    except (IndexError, AttributeError):
        return []

# Test the function
print("\nTesting get_errors():")
errors = get_errors(log_data)
print(f"Errors found: {errors}")

# Write to file
print("\nWriting to file...")
with open('errors.txt', 'w') as f:
    for error in errors:
        f.write(error + '\n')
print("✓ Written to errors.txt")

# ============================================================================
# Your Original Approach (with analysis)
# ============================================================================
print("\n" + "=" * 70)
print("Your Original Approach Analysis")
print("=" * 70)

# Create test file
with open('error.txt', 'w') as f:
    f.write("INFO: User logged in\nERROR: Database connection failed\nINFO: Search performed\nERROR: File not found\nDEBUG: Cache cleared")

def get_error_original(data):
    """Your original function (with issues noted)."""
    error = []
    with open('error.txt', 'r') as f:
        if isinstance(data, str):
            print(f"The input '{data}' is a string")
            # Issue: doesn't process when IS a string
        elif not isinstance(data, str):
            try:
                error = [i.strip().split(": ", 1)[1] for i in f if i.startswith('ERROR')]
                print(f"Found errors: {error}")
                return error
            except (TypeError, ValueError, AttributeError):
                print("Error occurred")
                return []
    return error

print("\nIssues with original approach:")
print("1. Reads from file instead of using 'data' parameter")
print("2. Logic backwards: processes when NOT a string")
print("3. get_error(12) works but get_error('hey') doesn't\n")

print("Testing original:")
result = get_error_original(12)
print(f"get_error(12) = {result}\n")

result = get_error_original('hey')
print(f"get_error('hey') = {result}")

print("\n✅ All tests completed!")
print("=" * 70)
