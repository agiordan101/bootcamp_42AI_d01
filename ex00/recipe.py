class Recipe:

    def __str__(self):
        text = "Recipe {} : {}\nPreparation time : {}\n\
        Ingredients needed : {}\nCooking lvl : {}\nCooking for : {}".format(
            self.name, self.description, self.cooking_time,
            self.ingredients, self.cooking_lvl, self.recipe_type)
        return text

    def __init__(self, name="Empty Recipe's name", cooking_lvl=1,
                 cooking_time=0, ingredients=["Ingredients are empty"],
                 description="Empty description", recipe_type="lunch"):
        error = False
        if not isinstance(name, str):
            print("Name <{}> is not a String !".format(name))
            error = True
        if (not isinstance(cooking_lvl, int) or
           cooking_lvl < 1 or cooking_lvl > 5):
            print("Cooking_lvl <{}> is not an Integer\
            between 1 and 5!".format(cooking_lvl))
            error = True
        if not isinstance(cooking_time, int):
            print("Cooking_time <{}> is not an Integer !".format(cooking_time))
            error = True
        if not isinstance(ingredients, list):
            print("Ingredients <{}> is not a List !".format(ingredients))
            error = True
        if not isinstance(description, str):
            print("Description <{}> is not an String !".format(description))
            error = True
        if (not isinstance(recipe_type, str) or
           (recipe_type != "starter" and
                recipe_type != "lunch" and
                recipe_type != "dessert")):
            print("Recipe_type <{}> is not an String !".format(recipe_type))
            error = True
        if error is True:
            quit()
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
