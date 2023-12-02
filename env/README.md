# Getting started

## Initial installation

```bash
pip install -r env/dev.txt
```

## Adding requirements

```bash
pip-compile -o env/dev.txt env/requirements.in env/dev.in;
pip-compile -o env/requirements.txt env/requirements.in;
```

## Updating requirements

```bash
pip-compile --upgrade -o env/dev.txt env/requirements.in env/dev.in;
pip-compile --upgrade -o env/requirements.txt env/requirements.in;
```