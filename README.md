# PyCon Workshop 2025

Welcome to the PyCon Workshop 2025! This repository contains the materials for the workshop.
The workshop is designed to help you learn and practice Python programming in a fun and interactive way.

The main target is to give you a simple taste of what you can easily build with tools as streamlit.

First of all you need to install the dependencies. To do so, you can use `poetry` or `pip`.

My personal preference relies on poetry.

## On the first clone run from terminal

```
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
poetry install
```
to create a new virtual environment inside the root folder of the repository (`.venv` folder). To activate it, simply run:
```
source .venv/bin/activate
```
and deactivate it with:
```
source deactivate
```
Note that poetry will try to install the environment with the local python version ratherthan the one specified in the `.toml` file. Tip: install the specified python version with `pyenv` and then run
```
pyenv local my_python_version
```
to set it as a local version for the repository.

### Add/remove a dependency

To add a new dependency run:
````
poetry add dependency_name
````

To remove a dependency from inside the `pyproject.toml` file, cancel the row and run:
````
poetry update
````