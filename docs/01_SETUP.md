### Installare Poetry

To install poetry, follow the proper instructions for your system from the [Poetry website](https://python-poetry.org/docs/#installation).

## On the first clone run from terminal

```terminal
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
poetry install
```

to create a new virtual environment inside the root folder of the repository (`.venv` folder). To activate it, simply run:

```terminal
source .venv/bin/activate
```

and deactivate it with:

```terminal
source deactivate
```

Note that poetry will try to install the environment with the local python version ratherthan the one specified in the `.toml` file. Tip: install the specified python version with `pyenv` and then run

```terminal
pyenv local my_python_version
```
to set it as a local version for the repository.

### Add/remove a dependency

To add a new dependency run:
````terminal
poetry add dependency_name
````

To remove a dependency from inside the `pyproject.toml` file, cancel the row and run:
````terminal
poetry update
````