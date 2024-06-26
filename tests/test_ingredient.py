import pytest
from praktikum.ingredient import Ingredient

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "Соус традиционный галактический", 50),
    ("FILLING", "Хрустящие минеральные кольца", 80)
])
def test_ingredient_attributes(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price

