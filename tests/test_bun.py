import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("white bun", 200),
    ("black bun", 150),
    ("red bun", 180)
])
def test_bun_attributes(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price

