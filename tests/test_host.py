import importlib

import pytest


def test_host_integration_imports():
    pytest.importorskip("bpy")
    importlib.import_module("compas_blender.conversions")
