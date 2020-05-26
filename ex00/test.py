from book import Book
from recipe import Recipe

salad = Recipe("Salad", 1, 15, ["Salad", "Tomate", "Mais"],
               "A mix of vegetables", "starter")
sandwich = Recipe("Sandwich", 2, 10,
                  ["Salad", "Tomate", "pain", "steak", "fromage"],
                  "A mix of great things", "starter")
recipes = {
            "starter": [salad, sandwich],
            "lunch": [],
            "dessert": []
          }

print(str(salad))
print()

cookbook = Book("My cookbook")
cookbook.get_recipe_by_name("Salad")
cookbook.get_recipe_by_types("starter")
print()

cookbook.get_recipe_by_name("efgztgz")
cookbook.get_recipe_by_types("rzgzrhzrs")
print()

cookbook.add_recipe(sandwich)
cookbook.add_recipe(salad)
cookbook.get_recipe_by_name("Salad")
cookbook.get_recipe_by_types("starter")
print()

cookbook = Book("My cookbook", recipes)
cookbook.get_recipe_by_name("Salad")
cookbook.get_recipe_by_types("starter")
