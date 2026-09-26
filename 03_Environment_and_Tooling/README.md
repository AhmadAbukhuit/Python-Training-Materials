# Module 03: Environment & Tooling

Welcome to Module 03. Writing Python code is only half the battle; managing where and how that code runs is what separates beginners from professionals. In this module, we transition from writing standalone scripts to managing full-scale project environments.

You will learn how to isolate your projects using Virtual Environments, install third-party libraries using `pip`, and make your code reproducible so it runs perfectly on any machine.

## Topics Covered

* **[1. Virtual Environments (venv):](./01_Virtual_Environments/)**  
    Understanding environment isolation, and learning how to create, activate, and deactivate virtual environments to prevent version conflicts.
* **[2. Package Management (pip):](./02_Package_Management/)**  
    Harnessing the Python Package Index (PyPI) to install, upgrade, and remove external libraries using Python's default package manager.
* **[3. Dependency Management:](./03_Dependency_Management/)**  
    Creating reproducible builds by "freezing" environments and generating/installing from requirements.txt files.
* **[4. Professional Project Structure:](./04_Professional_Project_Structure/)**  
    Organizing your workspace, separating source code from environment files, and configuring .gitignore to keep your version control clean.

---

## Hands-On Practice Tasks

### Task 3.1: The Project Skeleton

**Objective:** Organize a workspace professionally by separating source code, tests, and environment configurations.

* **Where to work:** Navigate to the **[task_3_1_skeleton](./Tasks/task_3_1_skeleton/)** directory.
* **Requirements:**
    * Using your terminal or file explorer, create two new folders inside this directory: `src` and `tests`.
    * Create a new file named exactly `.gitignore` in the root of this directory.
    * Open the `.gitignore` file and add the rules to ignore virtual environments (`venv/`) and Python cache files (`__pycache__/`).
* **Execution:** Once the folders and files are in place, run the automated test script.

**How to test your workspace:**

```bash
cd task_3_1_skeleton
python test_skeleton.py
```

---

### Task 3.2: The Blueprint Reader

**Objective:** Practice reading a `requirements.txt` file to recreate a project's exact environment.

* **Where to work:** Navigate to the **[task_3_2_blueprint](./Tasks//task_3_2_blueprint/)** directory.
* **Requirements:**
    * Create a new `requirements.txt` file in this folder and add these two lines exactly:
        * `requests==2.31.0`
        * `colorama==0.4.6`
    * Using your terminal, create a virtual environment named `venv`.
    * **Activate** your virtual environment.
    * Use `pip` to install the packages directly from your `requirements.txt` file.
* **Execution:** Run the test script. **Important:** Your virtual environment must be activated when you run the test, otherwise it will fail!

**How to test your environment:**

```bash
cd task_3_2_blueprint
python test_blueprint.py
```

---

### Task 3.3: The Blueprint Writer

**Objective:** Practice installing third-party libraries and "freezing" an environment to create a reproducible blueprint.

* **Where to work:** Navigate to the **[task_3_3_freeze](./Tasks/task_3_3_freeze/)** directory.
* **Requirements:**
    * Create and activate a new virtual environment in this folder.
    * Use `pip` to install the `cowsay` package (a fun terminal graphics library).
    * Use the `pip freeze` command to generate a `requirements.txt` file.
* **Execution:** Run the test script to verify that your blueprint was generated correctly.

**How to test your blueprint:**

```bash
cd task_3_3_freeze
python test_freeze.py
```

---

### Task 3.4: The API Consumer

**Objective:** Write a Python script that successfully utilizes a third-party library installed in an isolated environment.

* **Where to work:** Navigate to the **[task_3_4_api](./Tasks/task_3_4_api/)** directory.
* **Requirements:**
    * Create a virtual environment, activate it, and `pip install requests`.
    * Create a file named `fetch_data.py`.
    * Inside `fetch_data.py`, import the `requests` library.
    * Use the library to send a GET request to `[https://api.github.com](https://api.github.com)`.
    * Print the `status_code` of the response (it should be 200).
* **Execution:** Run the test script (with your environment activated) to verify your code fetches the data successfully.

**How to test your code:**

```bash
cd task_3_4_api
python test_api.py
```
