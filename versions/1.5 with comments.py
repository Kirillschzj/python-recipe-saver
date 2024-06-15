import json
from pathlib import Path

# recipes = [] # Dictionary to store recipes

my_recipes = Path("recipes.json")

def read_recipes():
    if my_recipes.exists():
        with my_recipes.open('r') as my_file:
            d = json.load(my_file)
        return d
    else:
        return []


def save_on_file(content):
    my_list = read_recipes()
    print(f"Content:\n{content}")
    my_list.append(content)
    with my_recipes.open("w") as my_file:
        json.dump(my_list, my_file, ensure_ascii=False, indent=4)
     

def add_recipe(name, ingredients, people): # Method to add a new recipe
    content =  {
              "name": name,
              "ingredients": ingredients,
              "people": people
         }
    save_on_file(content)

def show_recipes(): # Method to show all available recipes
    print("Available recipes:")
    for name in read_recipes():
        print(f"{name["name"]}")

def show_recipe(name): # Method to show a specific recipe
    for i in read_recipes():
        if name in i["name"]:
            print(f"Recipe of {i["name"]}: ")
            print(f"Ingridients are {i["ingredients"]}")
            print(f"People {i["people"]}")
        else:
             continue






while True: # Main loop
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
            while True: # New recipe loop
                print("You have selected a tab:[NEW RECIPE]")
                print("To continue - type (c)ontinue, to go back - type (b)ack")
                answer = input()
                if answer == "b" or answer == "back":
                    break
                elif answer == "c" or answer == "continue":
                        response = input("Type a name for the new recipe: \n") # request recipe's name
                        ing = input("Input ingredients and quantities, like this (soap - 1kg, fireworks - 250000 tonns, dinamyte - 1mg): \n") # request ingredients and quantities
                        ppl = input("Input for how many people will this dish be(indicate the age of consumer): \n") # request number of people
                        add_recipe(response, ing, ppl) # using the method from begginig we add a recipe
                        break # return to the main loop
    elif option == "2":
            while True: # Loop that shows all recipes
                print("You have selected a tab:[MY RECIPES]")
                print("To continue - type (c)ontinue, to go back - type (b)ack")
                answer = input()
                if answer == "b" or answer == "back":
                    break
                elif answer == "c" or answer == "continue":
                        show_recipes() # using method the we show all available recipes
                        response_name = input("Type the reciepe you are searching for: ")
                        show_recipe(response_name) # using the method we show a recipe
                        response2 = input("Type (b)ack to go back ")
                        if response2 == "b":
                            break
    elif option == "3": 
            while True: # About project loop
                print("You have selected a tab:[ABOUT]")
                print('\tThis project is dedicated to help you store your liked recipes.\nHere, you can put a recipe in our program in order to easily find it when you want to cook it.\nDaily, many people find themselves struggling to find a recipe they have heard about in the past, but not being able to find it.\nThis program is the solution.')
                print("To go back - type (b)ack")
                answer = input()
                if answer == "b" or answer == "back":
                    break
