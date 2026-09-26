# Encapsulation & Properties

Once you begin bundling data into objects, protecting that data becomes critical. In production systems, you cannot allow arbitrary code to put your objects into invalid, broken states (e.g., setting a network port to `-99` or assigning a string to an MTU limit).

**Encapsulation** is the practice of bundling data with the methods that operate on it and restricting direct access to internal components to ensure data integrity.

---

## 1. Access Levels in Python: Convention vs. Enforcement

Unlike languages such as Java or C++ which enforce strict access modifiers (`public`, `protected`, `private`), Python takes a pragmatic approach often summarized as:

> *"We are all consenting adults here."*

Python communicates intent through naming conventions rather than strict compiler-enforced restrictions.

```python
class NetworkInterface:
    def __init__(self, name: str, ip_address: str, auth_token: str):
        self.name = name              # Public: Intended for unrestricted access
        self._ip_address = ip_address # Protected: Internal convention; do not access externally
        self.__auth_token = auth_token # Private (Name Mangled): Hidden to avoid name collisions
```

### Access Modifiers at a Glance

| Style | Syntax | Meaning | Behavior |
| :--- | :--- | :--- | :--- |
| **Public** | `self.name` | Free access | Accessible and mutable from anywhere inside or outside the class. |
| **Protected** | `self._ip_address` | Internal use | Python convention signaling: *"Treat this as private internal state."* Still technically accessible if forced. |
| **Private (Name Mangling)** | `self.__auth_token` | Strict internal | Python automatically renames the attribute to `_NetworkInterface__auth_token` behind the scenes to prevent accidental overriding in child classes. |

```python
nic = NetworkInterface("eth0", "192.168.1.1", "secret-key-xyz")

# Public attribute: Direct access
print(nic.name)          # eth0

# Protected attribute: Convention says do not touch, but Python permits it:
print(nic._ip_address)   # 192.168.1.1 (discouraged)

# Private attribute: Direct access raises AttributeError
# print(nic.__auth_token)  <-- AttributeError: 'NetworkInterface' object has no attribute '__auth_token'

# Under the hood: Python "mangled" the attribute name
print(nic._NetworkInterface__auth_token)  # secret-key-xyz
```

---

## 2. Using `@property` for Safe Getters & Setters

Instead of writing clunky Java-style `get_mtu()` and `set_mtu()` methods, Python provides the `@property` decorator. This lets you attach validation logic to an attribute while allowing callers to interact with it using clean, natural attribute access syntax (`interface.mtu = 1500`).

```python
class NetworkInterface:
    def __init__(self, interface_name: str, initial_mtu: int = 1500):
        self.interface_name = interface_name
        self._mtu = 1500
        
        # Route through the setter so validation runs at initialization
        self.mtu = initial_mtu

    # 1. The Getter (Read access)
    @property
    def mtu(self) -> int:
        """The Maximum Transmission Unit in bytes."""
        return self._mtu

    # 2. The Setter (Write access & validation gatekeeper)
    @mtu.setter
    def mtu(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"MTU must be an integer, got {type(value).__name__}")
        if not (576 <= value <= 9000):
            raise ValueError(f"Invalid MTU: {value}. Standard range is between 576 and 9000.")
        self._mtu = value

    # 3. The Deleter (Cleanup logic when `del obj.attr` is executed)
    @mtu.deleter
    def mtu(self):
        print("Resetting MTU back to standard default (1500)...")
        self._mtu = 1500


# Interacting with properties cleanly
eth0 = NetworkInterface("eth0", 1500)

# Calls the @property getter
print(f"Current MTU: {eth0.mtu}")  # 1500

# Calls the @mtu.setter behind the scenes
eth0.mtu = 9000
print(f"Updated MTU: {eth0.mtu}")  # 9000

# Raises ValueError immediately, protecting object state!
try:
    eth0.mtu = 99999
except ValueError as e:
    print(f"Caught error: {e}")

# Calls the @mtu.deleter
del eth0.mtu
print(f"MTU after reset: {eth0.mtu}")  # 1500
```

---

## 3. Computed / Read-Only Properties

Properties can also calculate values on the fly without storing duplicate data in memory:

```python
class NetworkInterface:
    def __init__(self, name: str, mtu: int):
        self.name = name
        self.mtu = mtu

    # Read-only computed property (no setter defined)
    @property
    def is_jumbo_frame_enabled(self) -> bool:
        """Returns True if the interface MTU exceeds standard 1500 bytes."""
        return self.mtu > 1500

nic = NetworkInterface("eth0", 9000)
print(nic.is_jumbo_frame_enabled)  # True

# Attempting to assign to a read-only property fails:
# nic.is_jumbo_frame_enabled = False  <-- AttributeError: can't set attribute
```

---

## 4. The Pythonic Philosophy on Encapsulation

In many other languages, best practice dictates wrapping *every single field* with a getter and setter upfront.

In Python, this is considered an **anti-pattern**:

1. **Start Simple:** Use plain public attributes (`self.port = 80`).
2. **Refactor Only When Needed:** If validation or transformation is required later, wrap the attribute with `@property` and `@setter`.
3. **Zero Breaking Changes:** Because callers already use `obj.port`, converting an attribute into a `@property` never breaks external client code!

---

## 5. Common Gotchas to Avoid

[!WARNING] **The Infinite Recursion Setter Trap**

Inside `@property.setter`, you must assign to the internal variable (`self._mtu = value`), **not** the property itself (`self.mtu = value`).

```python
# ❌ WRONG: Infinite Recursion -> RecursionError: maximum recursion depth exceeded
@mtu.setter
def mtu(self, value):
    self.mtu = value  # Calls the setter again, and again, and again...

# ✅ CORRECT: Mutate the internal storage variable
@mtu.setter
def mtu(self, value):
    self._mtu = value
```
