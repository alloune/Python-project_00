import pytest
from schemas.user import User
from router.auth import register

users = [
    User(
        email="allan.lelay@gmail.com",
        full_name="Allan Le Lay",
        hashed_password="toto12345"
    ),
    User(
        email="charlotte.dechoudens@laposte.net",
        full_name="Charlotte de Choudens",
        hashed_password="toto12345"
    )
]

new_user = User(email="test@test.fr", full_name="test test", hashed_password="toto1234")

async def test_register_new():
    user = await register(new_user)
    assert user == new_user
