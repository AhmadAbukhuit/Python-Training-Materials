# Data Classes & Modern Python OOP

In modern software development, a large percentage of classes exist solely to store and pass around structured data (e.g., API payloads, database records, network configuration models).

Before Python 3.7, writing a data container class required writing dozens of lines of repetitive boilerplate: an `__init__` constructor, a `__repr__` for readable printing, and an `__eq__` method for comparison.

Python 3.7 introduced **Data Classes** (via the `dataclasses` standard library module) to eliminate this boilerplate entirely.

---

## 1. The Problem: Boilerplate Overload

Consider modeling a `HostRecord` the traditional way vs. the modern `@dataclass` way:

### The Traditional Way (Boilerplate Heavy)

```python
class HostRecord:
    def __init__(self, hostname: str, ip_address: str, port: int = 80):
        self.hostname = hostname
        self.ip_address = ip_address
        self.port = port

    def __repr__(self):
        return f"HostRecord(hostname={self.hostname!r}, ip_address={self.ip_address!r}, port={self.port!r})"

    def __eq__(self, other):
        if not isinstance(other, HostRecord):
            return NotImplemented
        return (self.hostname, self.ip_address, self.port) == (other.hostname, other.ip_address, other.port)
```

### The Modern Way: `@dataclass`

```python
from dataclasses import dataclass

@dataclass
class HostRecord:
    hostname: str
    ip_address: str
    port: int = 80
```

With just **5 lines of code**, `@dataclass` automatically writes:

* An `__init__()` method that initializes all attributes.
* A formatted `__repr__()` for easy debugging.
* An `__eq__()` method that compares instances by value, not memory address!

```python
h1 = HostRecord("web-01", "10.0.0.1")
h2 = HostRecord("web-01", "10.0.0.1")

print(h1)          # Outputs: HostRecord(hostname='web-01', ip_address='10.0.0.1', port=80)
print(h1 == h2)    # Outputs: True (Automatically compares values!)
```

---

## 2. Advanced Defaults with `field(default_factory=...)`

Just like standard classes, **never use a mutable object (like a list or dictionary) directly as a default value**. In dataclasses, Python protects you from this by raising a `ValueError`.

To supply a default list, dictionary, or set, use `field(default_factory=...)`:

```python
from dataclasses import dataclass, field

@dataclass
class ServerProfile:
    hostname: str
    ip_address: str
    # ❌ tags: list[str] = []  <-- Raises ValueError: mutable default not allowed!
    # ✅ Use default_factory:
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)

s1 = ServerProfile("app-01", "10.0.0.5")
s2 = ServerProfile("app-02", "10.0.0.6")

s1.tags.append("production")
print(s1.tags)  # ['production']
print(s2.tags)  # [] (Completely isolated!)
```

---

## 3. Immutable Data Structures: `frozen=True`

If you are passing records across threads, storing configurations, or using your objects as keys in a dictionary or elements in a `set`, you can freeze your dataclass to make it immutable:

```python
@dataclass(frozen=True)
class Subnet:
    network_address: str
    cidr_prefix: int

lan = Subnet("192.168.1.0", 24)

# Attempting to modify any field raises FrozenInstanceError!
# lan.cidr_prefix = 16  <-- dataclasses.FrozenInstanceError: cannot assign to field 'cidr_prefix'

# Because it is frozen and immutable, it is automatically hashable!
subnet_lookup = {lan: "Main Office"}
print(subnet_lookup[lan])  # Main Office
```

---

## 4. Post-Initialization Validation: `__post_init__`

What if you need validation or derived attribute calculation upon instantiation?

`@dataclass` automatically invokes `__post_init__` right after the generated `__init__` finishes:

```python
@dataclass
class NetworkEndpoint:
    host: str
    port: int
    protocol: str = "https"
    url: str = field(init=False)  # Derived attribute, not passed to __init__

    def __post_init__(self):
        # 1. Validation
        if not (1 <= self.port <= 65535):
            raise ValueError(f"Invalid network port: {self.port}")
        
        # 2. Derived state calculation
        self.url = f"{self.protocol}://{self.host}:{self.port}"

endpoint = NetworkEndpoint("api.service.io", 443)
print(endpoint.url)  # https://api.service.io:443
```

---

## 5. Architectural Comparison

When should you choose a dataclass versus other Python structures?

| Tool | Mutability | Typing Support | Methods Support | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Dictionary (`dict`)** | Mutable | Weak | No | Parsing dynamic JSON payloads without known schemas |
| **`namedtuple`** | Immutable | Optional | Lightweight | Quick, memory-optimized tuples with named fields |
| **Standard `class`** | Configurable | Manual | Full | Complex behavior, inheritance hierarchies, custom state logic |
| **`@dataclass`** | Configurable (`frozen`) | Strong | Full | Clean, typed data-centric objects with built-in comparisons |

---

## 6. Common Gotchas to Avoid

* **Type Hints are Mandatory:**  
`@dataclass` only inspects attributes with explicit type hints. If you write `hostname = "localhost"` without a type annotation (like `str`), dataclass treats it as a static class attribute rather than an instance field!

* **Inheritance Ordering:**  
In dataclass inheritance, fields without default values cannot follow fields with default values in the inheritance chain (adhering to standard Python argument ordering rules).
