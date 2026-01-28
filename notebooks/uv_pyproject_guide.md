# Learning Report: pyproject.toml and uv

## 1. What is `pyproject.toml`?

`pyproject.toml` is the modern, standardized configuration file for Python projects, defined in [PEP 518](https://peps.python.org/pep-0518/). It replaces multiple older configuration files like `setup.py`, `setup.cfg`, `requirements.txt`, and `MANIFEST.in`, consolidating them into a single, declarative source of truth.

### Key Sections
- **`[project]`**: Defines standard metadata like name, version, description, and dependencies.
  ```toml
  [project]
  name = "my-project"
  version = "0.1.0"
  dependencies = ["numpy", "torch"]
  ```
- **`[build-system]`**: Specifies the build backend (e.g., setuptools, hatchling).
- **Tool Configuration**: Centralizes config for tools like `black`, `ruff`, `pytest`, and `uv` (under `[tool.uv]`).

## 2. What is `uv`?

`uv` is an extremely fast Python package installer and project manager written in Rust. It functions as a replacement for `pip`, `pip-tools`, and `virtualenv`.

### Key Features
- **Performance**: 10-100x faster than pip.
- **Unified Workflow**: Manages Python versions, virtual environments, and dependencies.
- **Cross-Platform Locking**: Generates a `uv.lock` file that works across Linux, macOS, and Windows.

## 3. The Relationship: `pyproject.toml` + `uv`

In our project, `uv` uses `pyproject.toml` as the input to generate a reproducible environment.

### Workflow
1.  **Declaration**: You list abstract requirements (e.g., "I need torch") in `pyproject.toml`.
2.  **Resolution**: `uv lock` resolves these to exact versions (e.g., "torch==2.1.0 specific-hash") in `uv.lock`.
3.  **Sync**: `uv sync` installs exactly what is in the lockfile into your `.venv`.

### Advanced Configuration (Our Use Case)
We used `[tool.uv.sources]` to handle the complex requirement of supporting **CUDA 13.0 on Linux** and **MPS on macOS** simultaneously.

```toml
[tool.uv.sources]
torch = [
  { index = "pytorch-cu130", marker = "sys_platform == 'linux' or sys_platform == 'win32'" }, # Use Custom Index
  { index = "pypi", marker = "sys_platform == 'darwin'" },                                     # Use Standard PyPI
]
```

This tells `uv`: "If on Linux or Windows, get Torch from the CUDA 13 repository. If on Mac, get it from PyPI."
