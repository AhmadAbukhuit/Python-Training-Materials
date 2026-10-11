# 06. Application Structuring, APIRouter & CORS

As your backend grows from a simple script into a production enterprise application, keeping all your endpoints inside a single `main.py` file quickly becomes unmaintainable.

In this lesson, you will learn how to structure large codebases using **`APIRouter`**, configure **CORS** so web frontends (like React or Vue) can communicate with your API, and write custom **Middlewares**.

---

## 1. Modularizing Routes with `APIRouter`

`APIRouter` functions like a "mini FastAPI app". It allows you to organize related endpoints into separate Python files and include them into your central application.

### Recommended Production Directory Structure

```text
my_project/
├── app/
│   ├── __init__.py
│   ├── main.py             # App initialization, middleware, router inclusions
│   ├── config.py           # Environment variables and settings
│   ├── schemas/            # Pydantic data schemas
│   │   ├── user.py
│   │   └── device.py
│   └── routers/            # Modular endpoint files
│       ├── users.py
│       └── devices.py
└── requirements.txt
```

---

## 2. Writing a Modular Router

Inside `app/routers/devices.py`:

```python
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# 1. Initialize an APIRouter with a path prefix and OpenAPI documentation tag
router = APIRouter(
    prefix="/devices",
    tags=["Devices"]  # Groups all these routes cleanly in Swagger UI
)

class Device(BaseModel):
    id: int
    name: str

@router.get("/", response_model=list[Device])
def list_devices():
    return [{"id": 1, "name": "Edge Router"}]

@router.get("/{device_id}", response_model=Device)
def get_device(device_id: int):
    return {"id": device_id, "name": f"Device {device_id}"}
```

---

## 3. Assembling Routers in `main.py`

In your central `main.py`, simply import each router and include it using `app.include_router()`:

```python
from fastapi import FastAPI
# Assuming routers are inside a 'routers' package
from routers import devices

app = FastAPI(title="Enterprise API Platform")

# Register the modular router
app.include_router(devices.router)

@app.get("/")
def root():
    return {"message": "API Gateway is active"}
```

In Swagger UI (`/docs`), all routes under `devices.router` will now be logically grouped under the **"Devices"** header with URL paths prefixed by `/devices`!

---

## 4. Cross-Origin Resource Sharing (CORS)

By default, web browsers enforce security policies that prevent JavaScript running on one domain (e.g., `http://localhost:3000` running React) from making requests to an API on another domain or port (e.g., `http://localhost:8000`).

When this happens, the browser blocks the request with the dreaded error:

```text
Access to XMLHttpRequest has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present...
```

To enable frontend web applications to interact with your FastAPI backend, register the built-in `CORSMiddleware`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Specify the frontend origins permitted to make cross-origin requests
origins = [
    "http://localhost:3000",       # Local React / Next.js development
    "http://localhost:5173",       # Local Vite / Vue development
    "https://mycompany-portal.com" # Production web application
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # Allowed origins list
    allow_credentials=True,        # Allow cookies and authentication headers
    allow_methods=["*"],           # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],           # Allow all request headers
)
```

> [!CAUTION]
> In production environments, never set `allow_origins=["*"]` with `allow_credentials=True`, as this allows arbitrary websites to execute authenticated requests on behalf of your users!

---

## 5. Custom HTTP Middleware

A **Middleware** is a function that intercepts every HTTP request before it reaches a route handler, and intercepts every response before it is returned to the client.

A classic real-world use case is profiling request execution times and appending an `X-Process-Time` diagnostic header:

```python
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # 1. Code here runs BEFORE the request reaches the endpoint
    start_time = time.perf_counter()

    # 2. Process the request through the application
    response = await call_next(request)

    # 3. Code here runs AFTER the endpoint finishes
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}s"

    return response
```
