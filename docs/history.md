# History and migration

The package was extracted from COMPAS commit `6fb509e1f1a831b9f0832aa3d67309b39cdefc62`, immediately before
removal commit `7e009ac0dd6b48a120041864308e10b499779ae3`. The source is unchanged, including non-Python assets.

The `compas-extraction` tag identifies the filtered historical snapshot before
standalone boilerplate was added. Original commit authors, dates, and relevant
merge history survive; hashes change because unrelated files and commits are
removed. The repository includes a commit map and an original source blob
inventory under `provenance`.

See HISTORY.md in the repository for reproduction instructions, AUTHORS.md for
contributors, and TODO.md for the COMPAS 3.x migration checklist. In particular,
plugin discovery, removed core helpers, geometry APIs, scene objects, and the
host/Python support matrix require validation before declaring COMPAS 3.x support.
