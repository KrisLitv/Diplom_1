from praktikum.database import Database

def test_available_buns():
    database = Database()
    buns = database.available_buns()
    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_name() == "white bun"
    assert buns[2].get_name() == "red bun"

def test_available_ingredients():
    database = Database()
    ingredients = database.available_ingredients()
    assert len(ingredients) == 6
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[3].get_name() == "cutlet"

