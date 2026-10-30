# Installation

The standalone package requires Python 3.12+ and COMPAS `>=2.15,<3`.
Blender features must run with the host application's Python/.NET APIs available.
The historical installers and host version constants have not been revalidated
for this Python baseline. See the repository's TODO.md before attempting a deployment.

For local development, clone this repository and run:

```bash
python -m pip install -e ".[dev,docs]"
invoke test
invoke lint
invoke build
invoke docs
```



Do not install similarly named PyPI packages to substitute for application APIs.
Host smoke tests skip when the application is unavailable; full integration
validation must run inside the selected host and Python version.
