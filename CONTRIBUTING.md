# Contributing to **Spot_Vinyl**

## How to Contribute

1. Fork the repository and clone your fork
2. Create a branch from `main` using `git checkout -b fix/name` (replace name with a descriptive name)
3. Make your changes and test using `python ui/Spot_Vinyl.py`
4. Commit your changes with a clear message
5. Push and open a pull request against `main` branch

---

## Development Setup

### Creating a virtual environment and installing dependencies:

#### If using **uv**:
```
uv venv venv
```

#### If using **Python**:
```
python -m venv venv
```


### Activating the virtual environment:

#### If using cmd:
```
.venv\Scripts\activate
```

#### If using Powershell:
```
.venv\Scripts\Activate.ps1
```

#### If using GitBash:
```
source .venv/Scripts/activate
```

### Installing dependencies:

#### If using uv:
```
uv pip install -r requirements.txt
```

#### If using pip:
```
pip install -r requirements.txt
```

---

## Committing

- Be specific with your commit messages, don't put "fix bugs", "update code" or something similar
- Make sure that the commit is in imperative mood: `Fix theme selector not working`

---

## Branch naming

- Feature: `feat/short-description`
- Bug fix: `fix/short-description`
- Refactor: `refactor/short-description`
