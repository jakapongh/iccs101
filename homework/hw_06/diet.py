# Assignment 06, Task 05
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: an hour

NUTRIENT_CALORIES_PER_GRAM = {
    "carbs": 4,
    "protein": 4,
    "fats": 9
}


def get_recipe(recipe_name_to_find: str, recipes: list):
    found_recipe = None
    for recipe in recipes:
        recipe_name = recipe.split(":")[0]
        if recipe_name_to_find == recipe_name:
            found_recipe = recipe
            break
    return found_recipe


def get_nutrition_from_ingredient(ingredient_name: str, db: list):
    nutrition = None
    for item in db:
        name = item.split(":")[0]
        if name == ingredient_name:
            nutrition = item.split(":")[1].split(',')

    labeled_nutrition = {
        'carbs': int(nutrition[0]),
        'protein': int(nutrition[1]),
        'fats': int(nutrition[2]),
    }
    return labeled_nutrition


def get_calories_from_recipe(recipe: str, db: list):
    ingredient = recipe.split(":")[1]
    total_calories = 0

    for unparsed_ingredient in ingredient.split(","):
        # Ingredients: Cabbage, Carrot, Fatty Pork
        ingredient = unparsed_ingredient.split("*")[0]
        ingredient_units = int(unparsed_ingredient.split("*")[1])
        nutritional_contents = get_nutrition_from_ingredient(ingredient, db)

        for nutrient_name in nutritional_contents:
            nutrient_grams = nutritional_contents[nutrient_name]
            nutrient_calories_per_gram = int(NUTRIENT_CALORIES_PER_GRAM[nutrient_name])
            calories_of_nutrient = nutrient_calories_per_gram * nutrient_grams * ingredient_units
            total_calories += calories_of_nutrient

    return total_calories


def mealCal(meal: list[str], recipes: list[str], db: list[str]) -> float:
    total_calories = 0
    for meal_item in meal:
        recipe = get_recipe(meal_item, recipes)
        total_calories += get_calories_from_recipe(recipe, db)

    return total_calories


def test_mealCal():
    meal = ["T-Bone", "T-Bone", "Green Salad1"]

    # Name:Ingredient*Units,Ingredient*Units...
    recipes = [
        "Pork Stew:Cabbage*5,Carrot*1,Fatty Pork*10",
        "Green Salad1:Cabbage*10,Carrot*2,Pineapple*5",
        "T-Bone:Carrot*2,Steak Meat*1"
    ]

    # Name:carbs, protein, fat in grams
    db = [
        "Cabbage:4,2,0",
        "Carrot:9,1,5",
        "Fatty Pork:431,1,5",
        "Pineapple:7,1,0",
        "Steak Meat:5,20,10",
        "Rabbit Meat:7,2,20"
    ]

    assert mealCal(meal=meal, recipes=recipes, db=db) == 1290


test_mealCal()
