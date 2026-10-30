# compas_blender Agent Guide

- Keep this repository focused on the Blender integration. COMPAS core belongs in COMPAS.
- Support Python 3.12+, preserve unrelated changes, and prefer simple standard Python protocols.
- Keep recovered source unchanged until explicitly undertaking its migration; record deferred design in TODO.md.
- Use modern typing and NumPy-style Markdown docstrings when modernizing code.
- Keep host imports out of build metadata and host-independent tooling.
- Preserve LICENSE, provenance files, and the compas-extraction tag.
- Use the compas3 Conda environment when available. Run focused tests, invoke lint, invoke build, invoke docs, and git diff --check.
- Test host behavior in the actual application; do not treat skipped host tests as integration validation.
