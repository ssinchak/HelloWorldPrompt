"""
Unit and regression test for the helloworld package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import helloworld


def test_helloworld_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "helloworld" in sys.modules
