recipes = {}

def add_recipe(name, ingredients, people):
    recipes[name] = {}
    recipes[name]["name"] = name
    recipes[name]["ingredients"] = ingredients
    recipes[name]["people"] = people

def show_recipes():
    print("Available recipes:")
    for recipe_name in recipes:
        print(recipe_name)

def show_recipe(name):
    if name in recipes:
        print(f"Recipe of {name}:")
        print(f"Ingredients = '{recipes[name]["ingredients"]}'")
        print(f"People = '{recipes[name]["people"]}'")
    else:
        print(f"Recipe '{name}' not found.")






while True:
    print("Choose option:")
    print("1 = [NEW RECIPE]")
    print("2 = [MY RECIPES]")
    print("3 = [ABOUT]")
    print("q = quit")
    option = input("Input a number: ")
    if option == "q":
        print("Thanks for using our module!")
        exit()
    elif option == "1":
            while True:
                print("You have selected a tab:[NEW RECIPE]")
                print("To continue - type (c)ontinue, to go back - type (b)ack")
                answer = input()
                if answer == "b" or answer == "back":
                    break
                elif answer == "c" or answer == "continue":
                        response = input("Type a name for the new recipe: \n")
                        ing = input("Input ingredients and quantities, like this (soap - 1kg, fireworks - 250000 tonns, dinamyte - 1mg): \n")
                        ppl = input("Input for how many people will this dish be(indicate the age of consumer): \n")
                        add_recipe(response, ing, ppl)
                        break
    elif option == "2":
            while True:
                print("You have selected a tab:[MY RECIPES]")
                print("To continue - type (c)ontinue, to go back - type (b)ack")
                answer = input()
                if answer == "b" or answer == "back":
                    break
                elif answer == "c" or answer == "continue":
                        show_recipes()
                        response_name = input("Type the reciepe you are searching for: ")
                        show_recipe(response_name)
                        response2 = input("Type (b)ack to go back ")
                        if response2 == "b":
                            break
    elif option == "3":
                print("You have selected a tab:[ABOUT]")
                print("To continue - type (c)ontinue, to go back - type (b)ack")
                answer = input()
                if answer == "b" or answer == "back":
                    break
                elif answer == "c" or answer == "continue":
                    #ToDo: print something about our project)
                    print('\tThis project is dedicated to help you store your liked recipes.\nHere, you can put a recipe in our program in order to easily find it when you want to cook it.\nDaily, many people find themselves struggling to find a recipe they have heard about in the past, but not being able to find it.\nThis program is the solution.')
                    print("To go back - type (b)ack")
                    answer = input()
                    if answer == "b" or answer == "back":
                        break
