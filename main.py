import pytest


def always_returns_true():
    print("digital car crash")


def test_always_returns_true():
    assert always_returns_true()