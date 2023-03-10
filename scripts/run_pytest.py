import sys

import pytest


TESTS_FOLDER = "tests"


def main(args):
    """Run tests and return pytest's exit code."""
    return pytest.main([TESTS_FOLDER] + args)


if __name__ == "__main__":
    script_args = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    sys.exit(main(script_args))
