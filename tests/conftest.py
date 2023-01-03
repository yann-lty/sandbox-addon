import pytest

import bpy


@pytest.fixture()
def addon():
    """Fixture loading/enabling the addon."""
    import addon_utils

    return addon_utils.enable("sandbox", persistent=True, default_set=True)


@pytest.fixture()
def new_file():
    """Fixture loading the default template file."""
    bpy.ops.wm.read_homefile(app_template="")


@pytest.fixture(autouse=True)
def setup_test(new_file, addon):
    """
    Default setup for unit test functions that orchestrate fixtures to:
      - open default scene from empty app template
      - load the addon
    """
    assert addon is not None
    yield
