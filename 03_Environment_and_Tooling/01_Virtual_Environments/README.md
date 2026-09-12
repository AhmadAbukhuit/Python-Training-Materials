# Virtual Environments (venv)

Imagine you are building two different Python projects on the same computer. Project A is an older application that requires version 1.0 of a specific library, while Project B is a brand-new application that strictly requires version 2.0 of that exact same library.

If you install your packages directly into your main computer's global Python installation, you will overwrite one version with the other. One of your projects will inevitably break. This is known as **Dependency Hell**.

The professional solution to this problem is **Environment Isolation** using Virtual Environments.

## What is a Virtual Environment?

A virtual environment is a self-contained directory that houses its own isolated Python installation and its own independent set of installed libraries.

When you use a virtual environment for a project, any library you install, update, or delete only affects that specific project. It leaves your global system, and all your other projects completely untouched.

## Creating a Virtual Environment

Python comes with a built-in module called `venv` specifically for this purpose.

To create a virtual environment, open your terminal, navigate to your project directory, and run the following command:

```bash
# Windows
python -m venv venv

# macOS / Linux
python3 -m venv venv
```

* `python -m venv`: Tells Python to run the built-in `venv` module.
* `venv` **(the second word)**: This is the name of the folder that will be created. Naming it `venv` or `env` is the industry standard.

If you look at your project folder after running this command, you will see a new folder named `venv`. **Never write your own code inside this folder!** It is strictly for Python to manage its isolated system.

## Activating the Virtual Environment

Creating the environment doesn't automatically turn it on. You must *activate* it. The command differs depending on your operating system:

**For Windows (Command Prompt):**

```bash
venv\Scripts\activate.bat
```

**For Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

**For macOS / Linux:**

```bash
source venv/bin/activate
```

**How do you know it worked?**
When activated successfully, your terminal prompt will change to show the name of the environment in parentheses, like this:

`(venv) C:\Users\YourName\YourProject>`

Once activated, your terminal is temporarily "hijacked." Any Python code you run or any packages you install will now exclusively use this isolated environment.

## Deactivating the Environment

When you are done working on your project and want to return to your computer's normal, global Python environment, simply run:

```bash
deactivate
```

The `(venv)` prefix will disappear from your terminal prompt, indicating you have safely exited the isolated environment.
