# compas_blender

Blender integration for the COMPAS framework.

This standalone repository preserves the package from COMPAS immediately before
its removal in `7e009ac0dd6`. The complete recovered source and binary assets
are unchanged. See [HISTORY.md](HISTORY.md) for provenance and history mapping.

## Status and compatibility

This is an extraction baseline for the move toward COMPAS 3.x, retaining the
original package version `2.15.0`. It is **not yet ported to COMPAS 3.x**.
The dependency is deliberately constrained to `compas>=2.15,<3` until the API
migration and host tests are complete. See [TODO.md](TODO.md).

The standalone project targets Python 3.12+. Host integration requires Blender
and its own Python/.NET APIs; a regular CPython installation cannot run those
features. The recovered installers, supported-host constants, and IronPython
components are historical code, not a claim of support for those environments
with Python 3.12 or COMPAS 3.x.

## Development installation

```bash
python -m pip install -e ".[dev,docs]"
invoke test
invoke lint
invoke build
invoke docs
```

Use a clean, disposable environment. COMPAS 2.x also bundles these integration
modules; install the standalone integrations after COMPAS and recreate the
environment when switching versions rather than uninstalling overlapping packages. For development against a local COMPAS checkout, install
that checkout editable first, provided its API matches the dependency constraint.
The COMPAS 3.x development branch requires the migration work listed in TODO.md.

Host modules such as `Rhino`, `Grasshopper`, `System`, `rhinoscriptsyntax`,
`scriptcontext`, `bpy`, and `mathutils` come from the host application. Do not
install unrelated packages with these names as substitutes.

## Repository layout

- `src/compas_blender`: original integration code and assets.
- `tests`: host-independent behavior checks and optional host smoke tests.
- `docs`: standalone MkDocs documentation.
- `archive/compas-docs`: host-specific documentation recovered from COMPAS.
- `provenance`: original blob inventory and original-to-filtered commit maps.

See [CONTRIBUTING.md](CONTRIBUTING.md) for checks and release setup.

## License

MIT. The original COMPAS Association copyright notice is preserved in [LICENSE](LICENSE).
