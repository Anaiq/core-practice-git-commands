import pytest


def always_returns_true():
    print("digital car crash")
    return True


def test_always_returns_true():
    assert always_returns_true()