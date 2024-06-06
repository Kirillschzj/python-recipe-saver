while True:
    recipes = {}
    print("Choose option:")
    print("1 = [NEW RECIPE]")
    print("2 = [MY RECIPES]")
    print("3 = [ABOUT]")
    print("q = quit")
    option = input("Input a number: ")
    while True:
        if option == "q":
            print("Thanks for using our module!")
            exit()
        else:
            if option == "1":
                print("You have selected a tab:[NEW RECIPE]")
                print("To continue - type (c)ontinue, to go back - type (b)ack")
                answer = input()
                if answer == "b" or answer == "back":
                    break
                elif answer == "c" or answer == "continue":
                    response = input("Type a name for the new recipe: \n")
                    recipes[response] = {}
                    recipes[response]["name"] = response
                    recipes[response]["ingredients"] = input("Input ingredients using comma, like this (soap, fireworks, dinamyte): \n")
                    recipes[response]["people"] = input("Input for how many people will this dish be(indicate the age of consumer): \n")
            elif option == "2":
                print("You have selected a tab:[MY RECIPES]")
                print("To continue - type (c)ontinue, to go back - type (b)ack")
                answer = input()
                if answer == "b" or answer == "back":
                    break
                elif answer == "c" or answer == "continue":
                    for recipe_name in recipes:
                        print(recipe_name)

                    response_name = input("Type the reciepe you are searching for: ")

                    if recipes[response_name] == None:
                        print("This recipe is not available: ")
                    else:
                        print(f"Name = '{recipes[response_name]["name"]}'")
                        print(f"Ingredients = '{recipes[response_name]["ingredients"]}'")
                        print(f"People = '{recipes[response_name]["people"]}'")
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