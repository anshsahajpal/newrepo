import pytest

from ..security import get_password_hash, verify_password



def test_get_passwrod_hash():
    pass_hash = get_password_hash("testpass")
    assert pass_hash


def test_verify_password():
    pass_hash = get_password_hash("testpass")
    assert verify_password("testpass",pass_hash)
