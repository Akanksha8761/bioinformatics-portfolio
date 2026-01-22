"""
Day 8: The "Config Builder" Challenge
======================================

The Scenario:
You are writing a setup function for a web server. You have some default settings, 
but you want to allow users to override them with their own custom settings.

The Task:
Write a function called build_config:
    1. It should define a dictionary of defaults (port: 8080, host: "localhost", debug: False)
    2. It should accept any number of keyword arguments (**kwargs)
    3. It should return a dictionary that combines the defaults with the kwargs
    4. Important: User values should overwrite defaults; new keys should be added
"""

import os
import json

print("=" * 70)
print("Day 8: Config Builder Challenge")
print("=" * 70)


# ============================================================================
# Understanding **kwargs
# ============================================================================
print("\n" + "=" * 70)
print("Understanding **kwargs")
print("=" * 70)

def demo_kwargs(**kwargs):
    """Demonstrate how **kwargs works."""
    print(f"Type: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print(f"\nIndividual items:")
    for key, value in kwargs.items():
        print(f"  {key} = {value} (type: {type(value).__name__})")

print("\n--- Calling with keyword arguments ---")
demo_kwargs(port=9000, host='0.0.0.0', debug=True)

print("\n--- Calling with no arguments ---")
demo_kwargs()

print("\n--- Calling with mixed types ---")
demo_kwargs(timeout=30, ssl=True, max_connections=100, name="MyServer")


# ============================================================================
# Your Original Approach (Before **kwargs)
# ============================================================================
print("\n" + "=" * 70)
print("Your Original Approach (Single Key-Value)")
print("=" * 70)

def build_config_v1(key, value):
    """Original approach - handles one key-value pair at a time."""
    defaults = {'port': 8080, 'host': "localhost", 'debug': False}
    
    if key in defaults.keys():
        print(f"The Key '{key}' is present with value {defaults[key]}")
        defaults.update({key: value})
        print(f"Updated: {defaults}")
    else:
        print(f"Key '{key}' not present in defaults")
        defaults[key] = value
        print(f"Added: {defaults}")
    
    return defaults  # Added return for clarity

print("\nTesting original approach:")
result1 = build_config_v1('timeout', 452)
print(f"Result 1: {result1}\n")

result2 = build_config_v1('port', 78)
print(f"Result 2: {result2}")

print("\n⚠️  Issues with this approach:")
print("  1. Can only set ONE key-value pair at a time")
print("  2. Need multiple calls for multiple settings")
print("  3. Each call creates a new defaults dict")


# ============================================================================
# Your Improved Solution - Perfect! ✅
# ============================================================================
print("\n" + "=" * 70)
print("Your Improved Solution (Using **kwargs) ✅")
print("=" * 70)

def build_config(**kwargs):
    """Build configuration by merging defaults with custom settings."""
    defaults = {'port': 8080, 'host': "localhost", 'debug': False}
    defaults.update(kwargs)  # This automatically overwrites existing and adds new
    return defaults

print("\nTesting improved solution:")
config = build_config(port=9000, timeout=30)
print(f"build_config(port=9000, timeout=30)")
print(f"Result: {config}")

print(f"\nbuild_config(host='0.0.0.0', ssl=True)")
config2 = build_config(host='0.0.0.0', ssl=True)
print(f"Result: {config2}")

print(f"\nbuild_config() # No arguments")
config3 = build_config()
print(f"Result: {config3}")

print("\n✅ Perfect! This solution:")
print("  ✓ Accepts multiple keyword arguments")
print("  ✓ Merges them in one call")
print("  ✓ Returns the result")
print("  ✓ Handles overwrites and new keys automatically")


# ============================================================================
# Understanding .update() Method
# ============================================================================
print("\n" + "=" * 70)
print("Understanding .update() Method")
print("=" * 70)

print("\nHow .update() works:")
config = {'a': 1, 'b': 2}
print(f"Original: {config}")

config.update({'b': 3, 'c': 4})
print(f"After update({'b': 3, 'c': 4}): {config}")
print("  → 'b' was overwritten (2 → 3)")
print("  → 'c' was added")

print("\n.update() can also use keyword arguments:")
config.update(d=5, e=6)
print(f"After update(d=5, e=6): {config}")


# ============================================================================
# Solution 2: Dictionary Unpacking (Python 3.5+)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 2: Dictionary Unpacking")
print("=" * 70)

def build_config_unpack(**kwargs):
    """Build configuration using dictionary unpacking."""
    defaults = {'port': 8080, 'host': "localhost", 'debug': False}
    return {**defaults, **kwargs}  # kwargs overwrites defaults

print("\nHow unpacking works:")
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
result = {**d1, **d2}
print(f"d1 = {d1}")
print(f"d2 = {d2}")
print(f"{{**d1, **d2}} = {result}")
print("  → Later values overwrite earlier ones")

print("\nTesting unpacking version:")
config = build_config_unpack(port=9000, timeout=30)
print(f"Result: {config}")


# ============================================================================
# Solution 3: Dictionary Union Operator (Python 3.9+)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 3: Dictionary Union Operator | (Python 3.9+)")
print("=" * 70)

def build_config_union(**kwargs):
    """Build configuration using | operator."""
    defaults = {'port': 8080, 'host': "localhost", 'debug': False}
    return defaults | kwargs  # kwargs overwrites defaults

print("\nHow | operator works:")
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
result = d1 | d2
print(f"d1 = {d1}")
print(f"d2 = {d2}")
print(f"d1 | d2 = {result}")

print("\nTesting union operator version:")
try:
    config = build_config_union(port=9000, timeout=30)
    print(f"Result: {config}")
except TypeError as e:
    print(f"⚠️  Your Python version doesn't support | operator")
    print(f"   (Requires Python 3.9+)")


# ============================================================================
# Solution 4: Manual Loop
# ============================================================================
print("\n" + "=" * 70)
print("Solution 4: Manual Loop (Explicit Control)")
print("=" * 70)

def build_config_loop(**kwargs):
    """Build configuration with explicit merging."""
    config = {'port': 8080, 'host': "localhost", 'debug': False}
    
    print("  Processing kwargs:")
    for key, value in kwargs.items():
        if key in config:
            print(f"    Overwriting '{key}': {config[key]} → {value}")
        else:
            print(f"    Adding '{key}': {value}")
        config[key] = value
    
    return config

print("\nTesting manual loop version:")
config = build_config_loop(port=9000, timeout=30)
print(f"\nResult: {config}")


# ============================================================================
# Bonus: Advanced Variations
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Advanced Variations")
print("=" * 70)

# Variation 1: With Validation
print("\n--- With Type Validation ---")

def build_config_validated(**kwargs):
    """Build config with type validation."""
    defaults = {'port': 8080, 'host': "localhost", 'debug': False}
    config = {**defaults, **kwargs}
    
    # Validate types
    if not isinstance(config['port'], int):
        raise TypeError(f"port must be int, got {type(config['port']).__name__}")
    if not isinstance(config['host'], str):
        raise TypeError(f"host must be str, got {type(config['host']).__name__}")
    if not isinstance(config['debug'], bool):
        raise TypeError(f"debug must be bool, got {type(config['debug']).__name__}")
    
    return config

try:
    config = build_config_validated(port=9000, timeout=30)
    print(f"Valid config: {config}")
    
    # This will raise an error
    bad_config = build_config_validated(port="9000")
except TypeError as e:
    print(f"✗ Validation error: {e}")


# Variation 2: With Required Keys
print("\n--- With Required Keys ---")

def build_config_required(required=None, **kwargs):
    """Build config with required key validation."""
    defaults = {'port': 8080, 'host': "localhost", 'debug': False}
    config = {**defaults, **kwargs}
    
    # Check required keys
    if required:
        missing = [key for key in required if key not in config]
        if missing:
            raise ValueError(f"Missing required keys: {missing}")
    
    return config

try:
    # This will fail - missing 'database_url'
    config = build_config_required(required=['database_url'], port=9000)
except ValueError as e:
    print(f"✗ Error: {e}")

# This will succeed
config = build_config_required(
    required=['database_url'], 
    port=9000, 
    database_url='postgresql://localhost'
)
print(f"✓ Valid: {config}")


# Variation 3: Nested Config Merge
print("\n--- Nested Config Merge ---")

def build_config_nested(**kwargs):
    """Build config with nested dictionary support."""
    defaults = {
        'port': 8080,
        'host': "localhost",
        'debug': False,
        'database': {
            'host': 'localhost',
            'port': 5432,
            'name': 'mydb'
        }
    }
    
    def merge_dicts(base, override):
        """Recursively merge dictionaries."""
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value)
            else:
                result[key] = value
        return result
    
    return merge_dicts(defaults, kwargs)

config = build_config_nested(
    port=9000,
    database={'port': 3306}  # Only overrides database.port
)
print(f"\nNested config:")
print(f"  port: {config['port']}")
print(f"  database: {config['database']}")
print("  → database.host and database.name kept from defaults")


# Variation 4: With Environment Variables
print("\n--- With Environment Variable Support ---")

def build_config_env(**kwargs):
    """Build config with environment variable support."""
    defaults = {'port': 8080, 'host': "localhost", 'debug': False}
    
    # Environment variables override defaults
    env_config = {}
    if 'PORT' in os.environ:
        env_config['port'] = int(os.environ['PORT'])
    if 'HOST' in os.environ:
        env_config['host'] = os.environ['HOST']
    if 'DEBUG' in os.environ:
        env_config['debug'] = os.environ['DEBUG'].lower() == 'true'
    
    # Priority: defaults < env vars < kwargs
    return {**defaults, **env_config, **kwargs}

# Set an environment variable (for demo)
os.environ['PORT'] = '3000'

config = build_config_env(debug=True)
print(f"\nWith PORT=3000 in environment:")
print(f"  Result: {config}")
print("  → port from env (3000), debug from kwargs (True)")

# Cleanup
del os.environ['PORT']


# Variation 5: Config Class
print("\n--- Config Class Implementation ---")

class Config:
    """Configuration class with validation and defaults."""
    
    DEFAULTS = {
        'port': 8080,
        'host': 'localhost',
        'debug': False
    }
    
    def __init__(self, **kwargs):
        self.config = {**self.DEFAULTS, **kwargs}
        self._validate()
    
    def _validate(self):
        """Validate configuration."""
        if not 1024 <= self.config['port'] <= 65535:
            raise ValueError(f"Port must be between 1024-65535, got {self.config['port']}")
    
    def get(self, key, default=None):
        """Get configuration value."""
        return self.config.get(key, default)
    
    def update(self, **kwargs):
        """Update configuration."""
        self.config.update(kwargs)
        self._validate()
    
    def __repr__(self):
        return f"Config({self.config})"
    
    def __getitem__(self, key):
        """Allow dict-like access."""
        return self.config[key]

config = Config(port=9000, timeout=30)
print(f"\nConfig object: {config}")
print(f"  config.get('port'): {config.get('port')}")
print(f"  config['timeout']: {config['timeout']}")

config.update(debug=True)
print(f"  After update(debug=True): {config}")


# ============================================================================
# Common Mistakes Demonstration
# ============================================================================
print("\n" + "=" * 70)
print("Common Mistakes to Avoid")
print("=" * 70)

print("\n--- Mistake 1: Wrong merge order ---")

def bad_order(**kwargs):
    defaults = {'port': 8080}
    return {**kwargs, **defaults}  # Wrong! defaults overwrite kwargs

result = bad_order(port=9000)
print(f"bad_order(port=9000) = {result}")
print("⚠️  Expected port=9000, got port=8080 (defaults overwrote kwargs)")

print("\n--- Mistake 2: Modifying global defaults ---")

GLOBAL_DEFAULTS = {'port': 8080}

def bad_global(**kwargs):
    GLOBAL_DEFAULTS.update(kwargs)  # Mutates global!
    return GLOBAL_DEFAULTS

result1 = bad_global(port=9000)
result2 = bad_global()
print(f"First call (port=9000): {result1}")
print(f"Second call (no args): {result2}")
print("⚠️  Global defaults were permanently changed!")

print("\n--- Mistake 3: Not returning the config ---")

def no_return(**kwargs):
    defaults = {'port': 8080}
    defaults.update(kwargs)
    # Missing return!

result = no_return(port=9000)
print(f"no_return(port=9000) = {result}")
print("⚠️  Function returns None (forgot return statement)")


# ============================================================================
# Comprehensive Testing
# ============================================================================
print("\n" + "=" * 70)
print("Comprehensive Testing")
print("=" * 70)

def test_build_config():
    """Test all scenarios."""
    tests = [
        ({}, {'port': 8080, 'host': 'localhost', 'debug': False}, "No arguments"),
        ({'port': 9000}, {'port': 9000, 'host': 'localhost', 'debug': False}, "Override port"),
        ({'port': 9000, 'debug': True}, {'port': 9000, 'host': 'localhost', 'debug': True}, "Override multiple"),
        ({'timeout': 30}, {'port': 8080, 'host': 'localhost', 'debug': False, 'timeout': 30}, "Add new key"),
        ({'port': 9000, 'timeout': 30, 'ssl': True}, {'port': 9000, 'host': 'localhost', 'debug': False, 'timeout': 30, 'ssl': True}, "Mix override and new"),
    ]
    
    passed = 0
    failed = 0
    
    for kwargs, expected, description in tests:
        result = build_config(**kwargs)
        if result == expected:
            print(f"✅ {description}")
            passed += 1
        else:
            print(f"❌ {description}")
            print(f"   Expected: {expected}")
            print(f"   Got: {result}")
            failed += 1
    
    print(f"\n{'='*70}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("🎉 All tests passed!")
    
    return failed == 0

test_build_config()


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)

print("""
Challenge Requirements:
✓ Accept **kwargs for custom settings
✓ Define default configuration
✓ Merge defaults with kwargs
✓ User values overwrite defaults
✓ New keys are added

Your Perfect Solution:
def build_config(**kwargs):
    defaults = {'port': 8080, 'host': "localhost", 'debug': False}
    defaults.update(kwargs)
    return defaults

Alternative Methods:
1. .update() - Mutates dict in-place
2. {**d1, **d2} - Creates new dict (immutable)
3. d1 | d2 - Dictionary union (Python 3.9+)
4. Manual loop - Explicit control

Key Concepts Learned:
✓ **kwargs for keyword arguments
✓ Dictionary merging techniques
✓ .update() method
✓ Dictionary unpacking
✓ Configuration patterns
✓ Avoiding mutable defaults
""")

print("=" * 70)
print("✅ Day 8 completed!")
print("=" * 70)
