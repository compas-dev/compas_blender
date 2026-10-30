# Contributing

Use Python 3.12 or newer, preferably the `compas3` Conda environment. Install the
project with `python -m pip install -e ".[dev,docs]"`.

```bash
invoke test
invoke lint
invoke format
invoke build
invoke docs
git diff --check
```

`invoke lint` and `invoke format` cover newly maintained tooling and tests. The
recovered package source is excluded until its migration, preserving the exact
extraction. `invoke test` runs host-independent behavior checks; the host smoke
test skips when Blender is unavailable. These checks do not certify host integration.
`invoke build` builds both sdist and wheel and verifies every recovered source
file and asset is present in both. `invoke docs` builds MkDocs with strict mode.

Keep migration changes separate from extraction provenance. Preserve the license,
original authorship, extraction tag, and commit maps. Add focused behavior tests
for changes and run affected host integration tests inside the application.

## Release setup

The release workflow runs on published GitHub releases and builds distributions
from that release's checkout. Before publishing a release, complete TODO.md,
update `pyproject.toml` and the package's `__version__` together, and update the
changelog. The workflow checks the tag against the project version.

Configure PyPI trusted publishing for the eventual owner/repository and
`.github/workflows/release.yml`, using a protected GitHub environment named
`pypi`. No credentials or remote configuration are included in this bootstrap.
The `docs.yml` workflow validates and uploads the rendered documentation as an
artifact; documentation hosting can be configured after choosing the repository.
