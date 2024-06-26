import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns(self):
        bun = Bun("whole grain bun", 120)
        burger = Burger()
        burger.set_buns(bun)
        assert "whole grain bun" in burger.get_receipt()

    def test_add_ingredient(self):
        bun = Bun("whole grain bun", 120)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "spicy sauce", 90)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert "spicy sauce" in burger.get_receipt()

    def test_remove_ingredient(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "whole grain bun"
        mock_bun.get_price.return_value = 120
        mock_ing_sauce = Mock()
        mock_ing_sauce.get_name.return_value = "spicy sauce"
        mock_ing_sauce.get_price.return_value = 90
        mock_ing_filling = Mock()
        mock_ing_filling.get_name.return_value = "bacon"
        mock_ing_filling.get_price.return_value = 150
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_sauce)
        burger.add_ingredient(mock_ing_filling)
        burger.remove_ingredient(0)
        assert mock_ing_sauce not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "whole grain bun"
        mock_bun.get_price.return_value = 120
        mock_ing_filling = Mock()
        mock_ing_filling.get_name.return_value = "bacon"
        mock_ing_filling.get_price.return_value = 150
        mock_ing_sauce_first = Mock()
        mock_ing_sauce_first.get_name.return_value = "spicy sauce"
        mock_ing_sauce_first.get_price.return_value = 90
        mock_ing_sauce_second = Mock()
        mock_ing_sauce_second.get_name.return_value = "mustard"
        mock_ing_sauce_second.get_price.return_value = 60
        burger.set_buns(mock_bun)
        # Добавляем два ингредиента
        burger.add_ingredient(mock_ing_filling)
        burger.add_ingredient(mock_ing_sauce_first)
        burger.add_ingredient(mock_ing_sauce_second)
        # Перемещаем ингредиенты
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == mock_ing_sauce_second

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 120
        mock_ing_sauce = Mock()
        mock_ing_sauce.get_price.return_value = 90
        mock_ing_filling = Mock()
        mock_ing_filling.get_price.return_value = 150
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_sauce)
        burger.add_ingredient(mock_ing_filling)
        assert burger.get_price() == 480

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "whole grain bun"
        mock_bun.get_price.return_value = 120
        mock_ing_sauce = Mock()
        mock_ing_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ing_sauce.get_name.return_value = "spicy sauce"
        mock_ing_sauce.get_price.return_value = 90
        mock_ing_filling = Mock()
        mock_ing_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ing_filling.get_name.return_value = "bacon"
        mock_ing_filling.get_price.return_value = 150
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_sauce)
        burger.add_ingredient(mock_ing_filling)
        assert burger.get_receipt() == ('(==== whole grain bun ====)\n'
                                        '= sauce spicy sauce =\n'
                                        '= filling bacon =\n'
                                        '(==== whole grain bun ====)\n'
                                        '\n'
                                        'Price: 480')

