from api.models import Recipe
import pytest


def test_create_recipe():

    recipe = Recipe('Spaghetti Bolognese', 'Spaghetti, Tomato Sauce, Meat, Salt, Spices',
                    'Boil spaghetti, Mix Sauce with meat, Add salt and spices, Serve', 5, True)
    assert recipe.name == 'Spaghetti Bolognese'
    assert recipe.ingredients == 'Spaghetti, Tomato Sauce, Meat, Salt, Spices'
    assert recipe.steps == 'Boil spaghetti, Mix Sauce with meat, Add salt and spices, Serve'
    assert recipe.rating == 5
    assert recipe.favorite == True
