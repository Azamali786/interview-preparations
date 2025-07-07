# This file will contain learning resources, notes and other stack realted informations #

################ Intermediate pythn  #####################

1. Functions (Deep Dive)
    - Default parameters
        Default parameters allow you to specify default values for function arguments:

        def greet(name, greeting="Hello"):
            print(f"{greeting}, {name}!")

        greet("Alice")  # Output: Hello, Alice!
        greet("Bob", "Hi")  # Output: Hi, Bob!

        Key points:
            Default parameters must come after non-default parameters
            Default values are evaluated when the function is defined, not when it's called
            Mutable default values (like lists/dicts) can lead to unexpected behavior

        

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

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    1. Core OOP Concepts
        Class
        Blueprint for creating objects
        Example: class Car: pass

        Object (Instance)
        Instantiation of a class
        Example: my_car = Car()

        Attributes
        Data stored in objects (variables)
        Types:
        Class attributes (shared)
        Instance attributes (object-specific)

        Methods
        Functions defined in a class
        Types:
        Instance methods (self parameter)
        Class methods (@classmethod, cls parameter)
        Static methods (@staticmethod, no self/cls)

        Constructor (__init__)
        Initializes object state
        Example: def __init__(self, name): self.name = name

        Destructor (__del__)
        Cleans up resources before object deletion

    2. Pillars of OOP
        Encapsulation
        Bundling data + methods within a class
        Access control:
        Public (self.name)
        Protected (self._name convention)
        Private (self.__name, name mangling)

        Inheritance
        Creating child classes from parent classes
        Types:
        Single inheritance
        Multiple inheritance
        Multilevel inheritance
        Example: class ElectricCar(Car): pass

        Polymorphism
        Same interface, different implementations
        Forms:
        Method overriding (child class redefines parent method)
        Method overloading (not natively in Python, simulated via *args)
        Duck typing (object suitability by methods, not type)

        Abstraction
        Hiding complex logic, exposing only essentials
        Tools:
        Abstract classes (from abc import ABC, abstractmethod)
        Interfaces (Python uses ABCs)

    3. Advanced OOP Topics
        Magic/Dunder Methods
        Special methods like __str__, __add__, __len__
        Example: def __str__(self): return f"Car: {self.name}"

        Property Decorators
        @property, @attribute.setter, @attribute.deleter
        Example:
        python
        @property
        def speed(self):
            return self._speed

        Descriptors
        Custom attribute access (__get__, __set__, __delete__)

        Metaclasses
        Classes that create classes (type or custom metaclasses)
        Example: class Meta(type): pass

        Method Resolution Order (MRO)
        Determines method search path in inheritance (C3 linearization)
        Viewed via ClassName.__mro__

        Class Decorators
        Modify class behavior (e.g., @dataclass, @singleton)
        Slots (__slots__)
        Optimizes memory by restricting attributes

        Example: __slots__ = ['name', 'speed']

        Monkey Patching

        Dynamically modifying classes/methods at runtime

        Object Serialization

        Pickling (pickle module) for object persistence

        Design Patterns

        Common solutions (e.g., Singleton, Factory, Observer)

        4. Python-Specific OOP Features
        Duck Typing

        Focus on behavior over type

        Example:

        python
        def quack(obj):
            obj.quack()  # Works if obj has quack(), regardless of type
        Data Classes (Python 3.7+)

        Auto-generates __init__, __repr__

        Example:

        python
        from dataclasses import dataclass
        @dataclass
        class Point:
            x: float
            y: float
        Protocols (Structural Subtyping)

        Formalized duck typing (typing.Protocol)

        Abstract Base Classes (ABCs)

        Enforce method implementation

        Example:

        python
        from abc import ABC, abstractmethod
        class Shape(ABC):
            @abstractmethod
            def area(self): pass
        Operator Overloading

        Customize operators via dunder methods (e.g., __add__, __eq__)

        Context Managers (__enter__, __exit__)

        Used in with blocks

        Iterator Protocol (__iter__, __next__)

        Enables iteration

        Generator Classes

        Stateful iterators using yield

        Dynamic Attribute Access

        __getattr__, __setattr__, __getattribute__

        Decorators in OOP

        Combining @property with other decorators

        5. OOP Best Practices
        Composition Over Inheritance

        Favor object composition ("has-a") over deep inheritance ("is-a")

        SOLID Principles

        Single Responsibility

        Open/Closed Principle

        Liskov Substitution

        Interface Segregation

        Dependency Inversion

        Law of Demeter

        "Only talk to immediate friends" (loose coupling)

        Factory Pattern

        Centralize object creation

        Dependency Injection

        Pass dependencies externally

        6. Common OOP Pitfalls in Python
        Mutable default arguments

        Accidental class variable sharing

        Overusing inheritance (god objects)

        Misunderstanding super() in multiple inheritance

        Confusing is (identity) with == (equality)

    - difference between class methods, static methods and instance methods
        1. Instance Methods
            Purpose: Operate on instance-level data.
            First Parameter: self (reference to the instance).
            Access: Can modify both instance attributes and class attributes.
            When to Use: For logic that needs access to or modifies instance-specific data.

            class Pizza:
                def __init__(self, toppings):
                    self.toppings = toppings  # Instance attribute
                
                # Instance method
                def description(self):
                    return f"Pizza with {', '.join(self.toppings)}"

            pizza = Pizza(["cheese", "pepperoni"])
            print(pizza.description())  # "Pizza with cheese, pepperoni"

        2. Class Methods (@classmethod)
            Purpose: Operate on class-level data (shared across all instances).
            First Parameter: cls (reference to the class).
            Access: Can modify class attributes but not instance attributes directly.
            When to Use: For factory methods, alternative constructors, or modifying class-wide state.

            class Pizza:
                total_pizzas = 0  # Class attribute
                
                def __init__(self, toppings):
                    self.toppings = toppings
                    Pizza.total_pizzas += 1
                
                # Class method (alternative constructor)
                @classmethod
                def margherita(cls):
                    return cls(["cheese", "tomatoes"])  # Returns new instance
                
                @classmethod
                def get_total_pizzas(cls):
                    return cls.total_pizzas

            # Usage
            margherita = Pizza.margherita()  # Creates Pizza instance
            print(Pizza.get_total_pizzas())   # 1 (class-level counter)

        3. Static Methods (@staticmethod)
            Purpose: Utility functions independent of class/instance state.
            Parameters: No self or cls (just regular function parameters).
            Access: Cannot modify class or instance attributes (no access to cls/self).
            When to Use: For helper functions logically grouped with the class.

            class Pizza:
                @staticmethod
                def cooking_time():
                    return "12-15 minutes"  # No dependency on class/instance

            # Usage
            print(Pizza.cooking_time())  # "12-15 minutes" (called on class)
            pizza = Pizza(["cheese"])
            print(pizza.cooking_time())  # Also works (but avoid this)

            # Note:
            - when you need to play with instance attributes define instance methods
            - when you need to play with class attributes define class methods
            - when you need to show some information (Utility), define static methods 
                class Temperature:
                    unit = "Celsius"  # Class attribute
                    
                    def __init__(self, value):
                        self.value = value  # Instance attribute
                    
                    # Instance method (uses self)
                    def describe(self):
                        return f"{self.value}° {self.unit}"
                    
                    # Class method (uses cls)
                    @classmethod
                    def change_unit(cls, new_unit):
                        cls.unit = new_unit
                    
                    # Static method (no self/cls)
                    @staticmethod
                    def is_valid(value):
                        return -100 <= value <= 100

                # Usage
                temp = Temperature(25)
                print(temp.describe())          # "25° Celsius" (instance method)
                Temperature.change_unit("Fahrenheit")  # Class method
                print(temp.describe())          # "25° Fahrenheit" (class state changed)
                print(Temperature.is_valid(150)) # False (static method)

            1. Use Instance Methods When:
                Scenario:
                You need to access or modify instance-specific data (attributes).
                The method’s behavior depends on the state of a particular object.
                Examples:
                Getters/setters for instance attributes.
                Methods that process object-specific data.

                class BankAccount:
                    def __init__(self, balance):
                        self.balance = balance  # Instance-specific data
                    
                    # Instance method (operates on self)
                    def deposit(self, amount):
                        self.balance += amount

                account = BankAccount(100)
                account.deposit(50)  # Modifies THIS account's balance

            2. Use Class Methods (@classmethod) When:
                Scenario:
                You need to work with class-level state (shared across all instances).
                You want to create alternative constructors (factory methods).
                Examples:
                Tracking global counters (e.g., number of instances).
                Parsing different input formats to create objects.
                class Pizza:
                    total_pizzas = 0  # Class-level counter
                    
                    def __init__(self, toppings):
                        self.toppings = toppings
                        Pizza.total_pizzas += 1
                    
                    # Class method (factory for common pizza types)
                    @classmethod
                    def margherita(cls):
                        return cls(["cheese", "tomatoes"])  # Returns new instance
                    
                    @classmethod
                    def get_total_pizzas(cls):
                        return cls.total_pizzas

                # Usage
                margherita = Pizza.margherita()  # Alternative constructor
                print(Pizza.get_total_pizzas())   # Access class state

            3. Use Static Methods (@staticmethod) When:
                Scenario:
                The method is a utility function logically related to the class.
                It doesn’t need access to instance or class state (self/cls).
                Examples:
                Validation helpers.
                Unit conversions or pure calculations.
                class TemperatureConverter:
                    @staticmethod
                    def celsius_to_fahrenheit(c):
                        return (c * 9/5) + 32  # No self/cls needed
                    
                    @staticmethod
                    def is_valid_temp(c):
                        return -273.15 <= c <= 1000

                # Usage
                print(TemperatureConverter.celsius_to_fahrenheit(25))  # 77.0
                print(TemperatureConverter.is_valid_temp(-300))       # False

            
3. Modules and Packages
    A module is a Python file containing reusable code (functions, classes, variables). Modules help organize code logically and enable code reuse.
    Importing a Module
        import mymodule
    Import Specific Items
        from mymodule import greet, PI
    Import with Alias
        import mymodule as mm
    Import All (Generally Discouraged)
        from mymodule import *  # Imports all names (can cause naming conflicts)

    NOTE ==  random.choice(list1), random.choices(list1, k=2)

    Understanding if __name__ == "__main__"


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




##############################################################################################
Mutable vs. Immutable Concepts

Why does modifying a list inside a function affect the original list, but modifying an integer doesn’t? (Mutable vs. Immutable behavior)
Ans: Mutability and non mutability

What happens when you assign a = b where b is a list? Does changing a affect b? (Shallow copy behavior)
Ans: if all elements are immutable then new list b wi

Why does x += 1 behave differently for integers vs. lists? (+= mutates lists but rebinds integers)

Lists (list)

Why does list1 = list2 not create an independent copy? How can you make a true copy? (Shallow vs. Deep copy)

Why does [1, 2, 3] == [1, 2, 3] return True, but [1, 2, 3] is [1, 2, 3] return False? (Identity vs. Equality)

Why does list.append() return None instead of the modified list? (In-place mutation vs. returning new objects)

Why does list.sort() sort in-place, while sorted(list) returns a new list? (Design choices in Python)

Dictionaries (dict)

Why can’t a list or dict be used as a dictionary key, but a tuple can? (Hashability requirement)

Why does dictionary order insertion matter in Python 3.7+? (Dicts are now ordered by default)

What happens if you modify a dictionary while iterating over it? (RuntimeError due to changing size)

Strings (str)
Why are strings immutable in Python? What are the advantages? (Safety, hashability, optimization)

Why does "hello" + "world" work, but "hello" - "world" raise an error? (Operator overloading rules)

Why does "a" * 3 return "aaa", but "a" / 3 raise an error? (String multiplication vs. division)

Tuples (tuple)
Why can a tuple contain mutable objects (e.g., ([1, 2], 3)), but still be considered immutable? (Immutability of references, not contents)

Why does (1) evaluate to 1 (an integer), but (1,) evaluate to a tuple? (Single-element tuple syntax quirk)

Sets (set)
Why does {1, 2, 3} == {3, 2, 1} return True, but [1, 2, 3] == [3, 2, 1] return False? (Sets are unordered, lists are ordered)

Why does set.add() return None instead of the modified set? (Consistency with list.append())

Floats (float)
Why does 0.1 + 0.2 == 0.3 return False in Python? (Floating-point precision issues)

Why does float("inf") exist, and how is it used? (Representing infinity in calculations)

General Python Quirks
Why does is return True for small integers (e.g., 5 is 5) but False for larger ones (e.g., 500 is 500)? (Integer interning optimization)

########################################################################################################################

# Builtin Methods #
## Strings
Method	                    Description	                    Example
str.capitalize()	Capitalizes first character	        "hello".capitalize() → returns "Hello"
str.lower()	        Converts to lowercase	            "HELLO".lower() → returns  "hello"
str.upper()	        Converts to uppercase	            "hello".upper() → returns "HELLO"
str.strip()	        Removes leading/trailing whitespace	" hello ".strip() → returns "hello"
str.split()	        Splits into list by delimiter	    "a,b,c".split(",") → returns ["a","b","c"], default is name.split() split at spaces
str.join()	        Joins iterable with string	        ",".join(["a","b"]) → returns "a,b"
str.replace()	    Replaces substring	                "hello".replace("l","x") →returns "hexxo"
str.startswith()	Checks prefix	                    "hello".startswith("he") → True
str.endswith()	    Checks suffix	                    "hello".endswith("lo") → True
str.find()	        Returns first index of substring	"hello".find("l") → 2
str.isdigit()	    Checks if all chars are digits	    "123".isdigit() → True

isalpha, isalnum, isnumeric, isdecimal

## List
Method	                            Description	                    Example
list.append(x)	                Adds x to end	                [1,2].append(3) → inplace [1,2,3]
list.extend(iter)	            Adds all elements from iterable	[1,2].extend([3,4]) → inplace [1,2,3,4]
list.insert(i, x)	            Inserts x at index i	        [1,3].insert(1,2) → inplace [1,2,3]
list.remove(x)	                Removes first occurrence of x	[1,2,2].remove(2) → inplace [1,2]
list.pop(i)	                    Removes & returns item at i	    [1,2,3].pop(1) → inplace update and returns poped 2 (list becomes [1,3])
list.clear()	                Removes all items	            [1,2].clear() → inplace []
list.index(x)	                Returns index of x	            [1,2,3].index(2) → returns 1
list.count(x)	                Counts occurrences of x	        [1,2,2].count(2) → returns 2
list.sort()	                    Sorts in-place	                [3,1,2].sort() → inplace [1,2,3]
list.reverse()	                Reverses in-place	            [1,2,3].reverse() → inplace [3,2,1]
list.copy()	                    Returns shallow copy	        [1,2].copy() → [1,2]

## Dictionary
Method                              Description                                     example
dict.get(key)	                Returns value for key (safe)	                {"a":1}.get("a") →  1
dict.keys()	                    Returns view of keys	                        {"a":1}.keys() → dict_keys(["a"])
dict.values()	                Returns view of values	                        {"a":1}.values() → dict_values([1])
dict.items()	                Returns view of (key, value) pairs	            {"a":1}.items() → dict_items([("a", 1)])
dict.update(dict2)	            Merges dict2 into dict	                        {"a":1}.update({"b":2}) → inplace {"a":1, "b":2}
dict.pop(key)	                Removes key and returns value	                {"a":1}.pop("a") → 1
dict.clear()	                Removes all items	                            {"a":1}.clear() → {}
dict.copy()	                    Returns shallow copy	                        {"a":1}.copy() → {"a":1}
dict.setdefault(key, default)	Returns key's value, sets default if missing	{}.setdefault("a", 1) → 1

## Tuples
Method	                Description	                            Example
tuple.count(x)	    Counts occurrences of x	            (1,2,2).count(2) → 2
tuple.index(x)	    Returns index of x	                (1,2,3).index(2) → 1


## Sets
Method	                    Description	                            Example
set.add(x)	            Adds x to set	                        {1,2}.add(3) → {1,2,3}
set.remove(x)	        Removes x (raises KeyError if missing)	{1,2}.remove(2) → {1}
set.discard(x)	        Removes x (no error if missing)	        {1,2}.discard(3) → {1,2}
set.pop()	            Removes & returns arbitrary element	    {1,2}.pop() → 1
set.clear()	            Removes all elements	                {1,2}.clear() → set()
set.union(s2)	        Returns union of sets	                {1,2}.union({2,3}) → {1,2,3}
set.intersection(s2)	Returns intersection	                {1,2}.intersection({2,3}) → {2}
set.difference(s2)	    Returns elements in s1 not in s2	    {1,2}.difference({2,3}) → {1}
