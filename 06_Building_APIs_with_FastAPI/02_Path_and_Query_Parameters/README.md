# 02. Path and Query Parameters

Clients frequently need to request specific resources (such as retrieving server `#42`) or customize the results of a search (such as filtering, sorting, or pagination).

FastAPI handles these inputs elegantly using **Path Parameters** and **Query Parameters**, pairing Python type hints with automatic validation.

---

## 1. Path Parameters: Dynamic URL Segments

A **Path Parameter** is a variable segment embedded directly inside the URL path using curly braces `{}`:

```python
from fastapi import FastAPI

app = FastAPI()

# 1. Declaring a Path Parameter with a Type Hint
@app.get("/servers/{server_id}")
def get_server_by_id(server_id: int):
    """Retrieve details for a specific server using its numeric ID."""
    return {
        "server_id": server_id,
        "hostname": f"srv-node-{server_id}",
        "status": "online"
    }
```

### Automatic Type Conversion and Validation

FastAPI inspects the type annotation (`server_id: int`):

* If a client visits `GET /servers/42`, FastAPI automatically converts the string `"42"` into the integer `42` before passing it to your function.
* If a client visits `GET /servers/supercomputer`, FastAPI automatically catches the type mismatch and returns an **HTTP 422 Unprocessable Entity** error with an exact JSON error description:

```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["path", "server_id"],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "supercomputer"
    }
  ]
}
```

---

## 2. Route Precedence: Order Matters

When defining routes that share a URL prefix, **fixed paths must always be declared before dynamic path parameters**. Python executes route handlers in the order they are defined:

```python
# ✅ CORRECT: Specific fixed path comes FIRST
@app.get("/servers/summary")
def get_servers_summary():
    return {"total_count": 128, "active": 124, "degraded": 4}

# Dynamic parameter comes AFTER
@app.get("/servers/{server_id}")
def get_server_detail(server_id: int):
    return {"server_id": server_id}
```

*(If `/servers/{server_id}` were declared first, requests to `/servers/summary` would match `{server_id}`, causing an integer parsing validation error!).*

---

## 3. Predefined Values Using Python `Enum`

To restrict a path parameter to a fixed set of permissible choices, use Python's standard `enum.Enum`:

```python
from enum import Enum
from fastapi import FastAPI

class DeviceType(str, Enum):
    ROUTER = "router"
    SWITCH = "switch"
    FIREWALL = "firewall"

app = FastAPI()

@app.get("/devices/type/{device_type}")
def get_devices_by_type(device_type: DeviceType):
    """Returns devices matching a specific hardware category."""
    return {
        "selected_type": device_type.value,
        "message": f"Listing all active {device_type.name} units."
    }
```

In Swagger UI (`/docs`), FastAPI automatically renders a **dropdown select box** populated with your enum values!

---

## 4. Query Parameters: Filtering, Sorting & Pagination

Any function parameter that is **not** present in the path decorator string is automatically interpreted as a **Query Parameter** (the key-value pairs following `?` in a URL):

```python
from fastapi import FastAPI

app = FastAPI()

# URL Example: /servers?limit=25&active_only=true&region=us-east
@app.get("/servers")
def list_servers(
    limit: int = 10,                 # Default value 10
    active_only: bool = False,       # Default False (smart boolean parsing)
    region: str | None = None        # Optional parameter (defaults to None)
):
    results = {"limit": limit, "active_only": active_only}
    if region:
        results["region_filter"] = region
    return results
```

### Smart Boolean Parsing

FastAPI is intelligent with boolean types. A client can supply `?active_only=1`, `?active_only=true`, `?active_only=True`, `?active_only=yes`, or `?active_only=on`, and FastAPI will parse all of them to Python `True`!

---

## 5. Advanced Parameter Validation (`Path` & `Query`)

To enforce strict validation rules (such as string lengths or numeric ranges), use `Path` and `Query` from `fastapi`:

```python
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/inventory/{warehouse_id}/search")
def search_inventory(
    # Path parameter validation
    warehouse_id: int = Path(
        ..., # '...' means this field is strictly required
        title="Warehouse Identifier",
        description="The unique numerical ID of the warehouse facility.",
        ge=1,   # Greater than or equal to 1
        le=500  # Less than or equal to 500
    ),
    # Query parameter validation
    search_term: str = Query(
        ...,
        min_length=3,
        max_length=30,
        description="Search keyword for filtering parts"
    ),
    page: int = Query(default=1, ge=1)
):
    return {
        "warehouse_id": warehouse_id,
        "search_term": search_term,
        "page": page
    }
```

### Common Validation Constraints

| Constraint | Meaning | Applicable Types |
| :--- | :--- | :--- |
| `ge=N` | Greater than or equal to $N$ | `int`, `float` |
| `gt=N` | Strictly greater than $N$ | `int`, `float` |
| `le=N` | Less than or equal to $N$ | `int`, `float` |
| `lt=N` | Strictly less than $N$ | `int`, `float` |
| `min_length=N` | Minimum string character length | `str` |
| `max_length=N` | Maximum string character length | `str` |
| `pattern=r"..."` | Regex expression matching | `str` |

---

## 6. Summary Checklist

* **Path Parameters:** Part of the URL route itself (`/items/{id}`); best for identifying a specific resource.
* **Query Parameters:** Key-value pairs after `?` (`/items?page=1`); best for filtering, sorting, and pagination.
* **Validation:** Combine Python type hints with `Path()` and `Query()` to reject bad client inputs before your function code ever runs.
