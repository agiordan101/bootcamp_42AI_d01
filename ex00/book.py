import datetime
from recipe import Recipe


class Book:

    def __init__(self, name="Empty book's name", recipe_list={
                                                        "starter": [],
                                                        "lunch": [],
                                                        "dessert": []
                                                       }):
        error = False
        if not isinstance(name, str):
            print("Name <{}> is not an Integer !".format(name))
            error = True
        if not isinstance(recipe_list, dict):
            print("Recipe_list <{}> is not an Integer !".format(recipe_list))
            error = True
        if error is True:
            quit()
        self.name = name
        self.recipe_list = recipe_list
        self.creation_date = datetime.datetime
        self.last_update = datetime.datetime

    def get_recipe_by_name(self, name):
        if isinstance(name, str):
            find = False
            for recipes in self.recipe_list.values():
                for recipe in recipes:
                    if name == recipe.name:
                        print(recipe)
                        find = True
            if not find:
                print("Recipe <{}> is not in this Book".format(name))
        else:
            print("Recipe type <{}> is not a String".format(name))

    def get_recipe_by_types(self, r_type):
        if isinstance(r_type, str):
            if r_type in self.recipe_list:
                print("All recipes of type {} : | ".format(r_type), end="")
                for recipe_name in self.recipe_list[r_type]:
                    print(recipe_name.name, end=" ")
                print("|")
            else:
                print("Recipe type <{}> is not in this Book".format(r_type))
        else:
            print("Recipe type <{}> is not a String".format(r_type))

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("Param <{}> is not a Recipe" % recipe)
            quit()
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime
