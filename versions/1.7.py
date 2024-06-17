import json
from pathlib import Path

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

def add_recipe(name, ingredients, people): 
    content = {
        "name": name,
        "ingredients": ingredients,
        "people": people
    }
    save_on_file(content)

def show_recipes(): 
    print("Available recipes:")
    for recipe in read_recipes():  
        print(f"{recipe['name']}")  

def show_recipe(name): 
    for recipe in read_recipes():  
        if name.lower() in recipe["name"].lower():  
            print(f"Recipe of {recipe['name']}: ")  
            print(f"Ingridients are {recipe['ingredients']}")  
            print(f"People {recipe['people']}")  
        else:
            continue

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
            print("To go back - type (b)ack")
            answer = input("[Press Enter to continue], type (b)ack to go back ")
            if answer == "b" or answer == "back":
                break
            response = input("Type a name for the new recipe: \n") 
            ing = input("Input ingredients and quantities, like this (soap - 1kg, fireworks - 250000 tons, dynamite - 1mg): \n") 
            ppl = input("Input for how many people will this dish be (indicate the age of consumer): \n") 
            add_recipe(response, ing, ppl) 
            break 
    elif option == "2":
        while True: 
            print("You have selected a tab:[MY RECIPES]")
            print("To go back - type (b)ack")
            answer = input("[Press Enter to continue], type (b)ack to go back  ")
            if answer == "b" or answer == "back":
                break
            show_recipes() 
            response_name = input("Type the recipe you are searching for: ")  
            show_recipe(response_name) 
            response2 = input("Type (b)ack to go back ")
            if response2 == "b":
                break
    elif option == "3": 
        while True: 
            print("You have selected a tab:[ABOUT]")
            print('\tThis project is dedicated to help you store your liked recipes.\nHere, you can put a recipe in our program in order to easily find it when you want to cook it.\nDaily, many people find themselves struggling to find a recipe they have heard about in the past, but not being able to find it.\nThis program is the solution.')
            print("To go back - type (b)ack")
            answer = input()
            if answer == "b" or answer == "back":
                break
