import sys

from invoke import task


def run_python(ctx, arguments):
    ctx.run(f'"{sys.executable}" {arguments}')


@task
def test(ctx):
    """Run behavior tests."""
    run_python(ctx, "-m pytest")


@task
def lint(ctx):
    """Check maintained tooling and tests."""
    run_python(ctx, "-m ruff check .")
    run_python(ctx, "-m ruff format --check .")
    run_python(ctx, "-m compileall -q src")


@task(name="format")
def format_code(ctx):
    """Format maintained tooling and tests."""
    run_python(ctx, "-m ruff check --fix .")
    run_python(ctx, "-m ruff format .")


@task
def build(ctx):
    """Build and verify both distribution formats."""
    run_python(ctx, "-m build")
    run_python(ctx, "scripts/verify_distribution.py")
    run_python(ctx, "-m twine check dist/*")


@task
def docs(ctx):
    """Build standalone documentation."""
    run_python(ctx, "-m mkdocs build --strict")
