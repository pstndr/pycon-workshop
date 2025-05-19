# PyCon Workshop 2025


Per convertire il file pyproject.toml di Poetry in un classico requirements.txt, puoi utilizzare il comando integrato di Poetry per esportare le dipendenze.
```terminal
poetry export -f requirements.txt --output requirements.txt --without-hashes
```