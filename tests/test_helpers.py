import pytest

import compas_blender


def test_default_and_explicit_blender_versions():
    assert compas_blender._check_blender_version(None) == "4.2"
    assert compas_blender._check_blender_version("3.6") == "3.6"


def test_unsupported_blender_version():
    with pytest.raises(Exception, match="Unsupported Blender version"):
        compas_blender._check_blender_version("unsupported")


def test_missing_bootstrapper(tmp_path):
    assert compas_blender._get_bootstrapper_data(str(tmp_path / "missing.py")) == {}


def test_read_bootstrapper(tmp_path):
    bootstrapper = tmp_path / "compas_bootstrapper.py"
    bootstrapper.write_text('ENVIRONMENT_NAME = "example"\n')
    assert compas_blender._get_bootstrapper_data(str(bootstrapper))["ENVIRONMENT_NAME"] == "example"
