# Module 05: Object-Oriented Programming (OOP)

Welcome to Module 05. Up to this point, we have treated data and behavior as two separate things: we built data structures (like dictionaries or lists) and then wrote standalone functions to manipulate them.

As applications grow—especially when building large web applications, distributed systems, games, or complex data pipelines—keeping track of which functions modify which dictionaries becomes unmanageable. **Object-Oriented Programming (OOP)** solves this by bundling data and the functions that operate on that data into a single, cohesive unit called an **Object**.

In this module, you will master how to design robust, modular, and reusable software by mapping real-world concepts into code using classes, encapsulation, inheritance, magic methods, composition, and modern data classes.

---

## Topics Covered

* **[1. Classes & Objects: The Blueprint](./01_Classes_and_Objects/)**  
  Understanding the difference between a class (blueprint) and an object (instance), initializing state with `__init__`, mastering `self`, distinguishing class attributes from instance attributes, avoiding the mutable default trap, and working with `@classmethod` and `@staticmethod`.

* **[2. Encapsulation & Properties](./02_Encapsulation_and_Properties/)**  
  Protecting your object's internal state using access conventions (public, protected `_`, and private name-mangling `__`), avoiding invalid states with `@property` getters, setters, and deleters, and implementing computed read-only properties.

* **[3. Inheritance & Polymorphism](./03_Inheritance_and_Polymorphism/)**  
  Keeping your code DRY (Don't Repeat Yourself) with "IS-A" relationships, leveraging `super()` for parent initialization, overriding methods dynamically, checking types with `isinstance()` and `issubclass()`, enforcing contracts with Abstract Base Classes (`abc.ABC`), and understanding Multiple Inheritance and MRO.

* **[4. Magic (Dunder) Methods](./04_Magic_Methods/)**  
  Unlocking Python's native power by customizing object behavior: developer vs. user string representations (`__repr__` vs. `__str__`), value equality (`__eq__`), container emulation (`__len__`, `__getitem__`, `__contains__`), mathematical operators (`+`, `-`), and context managers (`__enter__`, `__exit__`).

* **[5. Composition vs. Inheritance](./05_Composition_vs_Inheritance/)**  
  Moving from basic OOP to professional software architecture: adhering to the Gang of Four principle (*"Favor object composition over class inheritance"*), distinguishing "IS-A" from "HAS-A", using Dependency Injection, and building flexible, modular composite systems.

* **[6. Data Classes & Modern Python OOP](./06_Dataclasses_and_Modern_OOP/)**  
Eliminating repetitive boilerplate in modern Python (3.7+) with `@dataclass`, typed fields, safe defaults with `field(default_factory=...)`, immutable records with `frozen=True`, and post-init validation with `__post_init__`.
