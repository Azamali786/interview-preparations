# This file will contain learning resources, notes and other stack realted informations #

################ Intermediate pythn  #####################

1. Functions (Deep Dive)
    - Default parameters
    - Variable-length arguments (*args, **kwargs)
    - Keyword-only arguments
    - Returning multiple values
    - Anonymous functions (lambda)
    - Scope: local, nonlocal, global
    - Closures

2. OOP Basics
    - Classes and Objects
    - __init__ method
    - Instance methods, class methods, static methods
    - Class variables vs instance variables
    - Dunder (magic) methods (__str__, __repr__, etc.)

3. Modules and Packages
    - Creating and importing modules
    - Using built-in modules (math, datetime, os, etc.)
    - Understanding __name__ == "__main__"

4. Exception Handling
    - try, except, finally
    - else clause in exception handling
    - Raising exceptions manually
    - Multiple except blocks
    - try-except-else-finally flow

5. Comprehensions
    - List comprehension
    - Dictionary comprehension
    - Set comprehension
    - Nested comprehensions

6. File Handling
    - Opening files (read, write, append modes)
    - Context manager with with statement
    - Working with text and binary files
    - Reading and writing JSON

7. Working with Standard Libraries
    - collections
    - datetime
    - random
    - os and sys
    - shutil
    - math

8. String Manipulation
    - Advanced string formatting (f-strings, format())
    - Regular expressions (re module)
    - Encoding and decoding strings (UTF-8, etc.)

9. Decorators (Introduction)
    - What is a decorator?
    - Simple function decorators
    - Using @decorator syntax

10. Iterators and Generators (Basics)
    - Iterable vs Iterator
    - Creating custom iterators
    - Simple generators (yield)
    - Generator expressions

11. Functional Programming Basics
    - map(), filter(), reduce()
    - lambda functions
    - zip()
    - enumerate()
    - any(), all()

12. Working with External Libraries
    - Installing libraries with pip
    - Using libraries like requests, beautifulsoup4, pandas (basic intro)

13. Intro to Testing
    - Basic unit tests with unittest
    - Assertions
    - Writing simple test cases

14. Basic Data Persistence
    - Reading/writing JSON
    - Using pickle
    - Intro to sqlite3 database operations

15. Intro to Virtual Environments
    - Creating virtual environments (venv)
    - Activating/deactivating environments
    - Installing packages within environments

16. Command Line Arguments
    - Using sys.argv
    - Simple command-line utilities

17. Basic Multi-threading and Multi-processing
 - Intro to threading module
 - Intro to multiprocessing module

18. Comprehension and Slicing
    - Advanced list slicing
    - Slicing strings, tuples
    - Slice notation [start:stop:step]

19. Understanding Mutable vs Immutable Types
    - Lists, Dictionaries (Mutable)
    - Tuples, Strings (Immutable)
    - Effects of mutability on function arguments

20. Data Structures (Pythonic)
    - Stacks, Queues, Linked Lists (basic implementations)
    - Use of deque
    - Intro to heapq




############## Advance Python #########################

1. Advanced Data Structures
    - Collections module (namedtuple, deque, Counter, defaultdict, OrderedDict)
    - Heap queue (heapq)
    - Priority Queue
    - Set and frozenset advanced use

2. OOP (Object-Oriented Programming) Advanced
    - Inheritance (Single, Multiple, Multilevel)
    - Polymorphism
    - Encapsulation and Abstraction
    - MRO (Method Resolution Order)
    - super() and its advanced usage
    - Abstract Base Classes (abc module)
    - Mixins

3. Decorators
    - Function decorators
    - Class decorators
    - Chaining multiple decorators
    - Parameterized decorators
    - functools.wraps

4. Generators and Iterators
    - Generator functions
    - Generator expressions
    - yield, yield from
    - Custom iterator classes
    - itertools module

5. Context Managers
    - with statement
    - Creating custom context managers (__enter__, __exit__)
    - contextlib module

6. Metaprogramming
    - Metaclasses
    - type() for dynamic class creation
    - __new__ vs __init__
    - Reflection (using getattr, setattr, hasattr, delattr)
    - Dynamic attributes and methods

7. Concurrency and Parallelism
    - Multithreading (threading module)
    - Multiprocessing (multiprocessing module)
    - Asyncio (async/await, event loop, tasks)
    - GIL (Global Interpreter Lock) and its effects

8. Memory Management and Performance
    - Memory profiling
    - Garbage Collection (gc module)
    - sys.getsizeof()
    - Weak references (weakref module)

9. Functional Programming
    - map(), filter(), reduce()
    - lambda functions
    - functools (partial, lru_cache, reduce, etc.)
    - Currying
    - Higher-order functions
    - Comprehensions (List, Dict, Set, Generator)

10. Type Hints and Annotations
    - Basic Type Annotations
    - Advanced Typing (Union, Optional, Any, Tuple, Callable, TypeVar, Protocols)
    - Static type checking with mypy

11. Exception Handling (Advanced)
    - Custom Exception Classes
    - Exception Chaining (raise from)
    - Context-specific exception handling
    - Suppressing exceptions (contextlib.suppress)

12. Modules and Packaging
    - __init__.py, __main__.py
    - Import system (absolute vs relative imports)
    - Creating installable packages (setup.py, setuptools, pyproject.toml)
    - Virtual environments (venv, pipenv, poetry)

13. Design Patterns
    - Singleton
    - Factory
    - Builder
    - Observer
    - Strategy
    - Proxy
    - Adapter
    - Command pattern

14. Descriptors
    - __get__, __set__, __delete__
    - Property decorators vs descriptors

15. Memory-efficient Programming
    - slots
    - Lazy evaluation
    - Generator-based pipelines

16. Dynamic Code Execution
    - exec()
    - eval()
    - compile()
    - ast module (Abstract Syntax Trees)

17. Advanced File Handling
    - Context managers with files
    - Binary files (rb, wb)
    - Working with pickle, shelve, csv, json, xml, yaml

18. Networking
    - socket programming
    - Working with HTTP libraries (requests, http.client, aiohttp)
    - REST API consumption and WebSocket communication

19. Logging and Debugging
    - Advanced logging configuration
    - Custom loggers
    - Logging to files, emails, external systems
    - Debugging with pdb, ipdb

20. Testing
    - Unit testing (unittest, pytest)
    - Mocking and patching
    - Test-driven development (TDD)
    - Benchmarking and profiling tests

21. Database Interaction
    - ORM libraries (SQLAlchemy, Django ORM)
    - Direct database connection using sqlite3, psycopg2, mysql-connector-python
    - Connection pooling

22. Security Best Practices
    - Input validation and sanitation
    - Preventing code injection (e.g., SQL Injection)
    - Safe serialization/deserialization 
    - Secure password handling


####################### python advance topics ######################
1- higher order function

2- lambda functions

3- type hinting

Type hinting in Python helps make your code more maintainable, readable, and less prone to runtime errors. 
1. Basic Type Hints

Variable Annotations

name: str = "Alice"
age: int = 30
is_active: bool = True
pi: float = 3.14159

functional annotations

def greet(name: str) -> str:
    return f"Hello, {name}"

def calculate_area(length: float, width: float) -> float:
    return length * width

2. Common Type Annotations

Collections: 

from typing import List, Dict, Set, Tuple

names: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
unique_ids: Set[int] = {101, 102, 103}
coordinates: Tuple[float, float] = (10.5, 20.3)

Optional Values:
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Returns str or None


Union Types:
from typing import Union

def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2

3. Advanced Type Hints
Type Aliases:
from typing import Dict, List

UserId = int
UserName = str
UserData = Dict[UserId, UserName]

def process_users(users: UserData) -> List[UserName]:
    return list(users.values())



4- decorators

5- generator functions

6- magic methods (Dunder Methods)

7- *args and **kwargs

8- comprehensions (list, dict)

9- context manager

10- Async Programming (used for I/O bound tasks)

11- Error Handling 
    BaseException
    ├── SystemExit
    ├── KeyboardInterrupt
    ├── GeneratorExit
    └── Exception
        ├── StopIteration
        ├── ArithmeticError
        │    ├── FloatingPointError
        │    ├── OverflowError
        │    └── ZeroDivisionError
        ├── AssertionError
        ├── AttributeError
        ├── BufferError
        ├── EOFError
        ├── ImportError
        ├── LookupError
        │    ├── IndexError
        │    └── KeyError
        ├── MemoryError
        ├── NameError
        ├── OSError
        │    ├── FileNotFoundError
        │    ├── PermissionError
        │    └── ...
        ├── RuntimeError
        ├── SyntaxError
        ├── TypeError
        ├── ValueError
        └── ...

12- file handling in python (normal and binary files both)

####################################################################################

"At the same time": Two trains arriving at a station at the exact same moment.
"Overlapping time": A meeting starting at 9:00 AM and ending at 10:00 AM overlaps with another meeting starting at 9:30 AM and ending at 10:30 AM

