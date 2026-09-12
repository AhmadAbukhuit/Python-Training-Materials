# Professional Project Structure

When you transition from writing single-file scripts to building full applications, organization becomes just as important as the code itself. If another developer (or you, six months from now) opens your project, they should instantly understand where everything is located.

A professional project separates source code, dependencies, documentation, and testing into a predictable, standardized layout.

## The Standard Directory Tree

While Python does not force a strict directory structure on you like some other languages do, the industry has settled on a highly standard convention. A professional Python project usually looks like this:

```text
my_awesome_project/
│
├── venv/                   # The isolated Python environment (NEVER touch the files inside)
├── src/                    # Your actual Python source code goes here (sometimes named 'app/')
│   ├── main.py             
│   └── utils.py            
│
├── tests/                  # All automated testing scripts go here
│   ├── test_main.py        
│   └── test_utils.py       
│
├── .gitignore              # Tells Git which files to ignore (crucial!)
├── requirements.txt        # The blueprint of your environment dependencies
└── README.md               # The manual explaining what the project is and how to run it
```

## Separation of Concerns

Notice how everything has a dedicated place:

* **The Code:** Lives exclusively in the `src/` (source) folder.
* **The Environment:** Lives exclusively in `venv/`. You never write your own code inside `venv/`.
* **The Tests:** Live in a `tests/` folder, completely separate from the production code. This prevents test code from accidentally being shipped to end-users.

## The Golden Rule: The `.gitignore` File

If you are using Git (which is standard for version control), there are certain files and folders you **must never commit** to your repository.

* `venv/`: Virtual environments contain thousands of files and are tied to your specific operating system (a Windows `venv` will break a Mac). Because you have a `requirements.txt` file, anyone can recreate the environment, so there is no need to upload the `venv` folder itself.
* `__pycache__/`: When Python runs, it creates compiled bytecode files (ending in `.pyc`) to make your program load faster next time. These are generated automatically and should not be shared.
* `.env` **/ Secrets**: Files containing API keys, database passwords, or secret tokens should never be pushed to a repository.

To prevent Git from tracking these files, you create a plain text file named exactly `.gitignore` at the root of your project.

Here is a standard `.gitignore` template for a Python project:

```text
# Environments
venv/
env/

# Python Cache
__pycache__/
*.pyc

# Secrets and Configs
.env
```

By setting this up before you make your first commit, you ensure your repository remains clean, secure, and professional.
