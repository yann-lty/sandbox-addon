def test_load_addon():
    """Ensure addon loads correctly."""
    import addon_utils

    assert addon_utils.check("sandbox")[1]
