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
                    #ToDo: create the new dictionary with NAME, INGREDIENTS AND HOW MUCH YOU NEED, FOR HOW MANY PEOPLE WILL THIS DISH BE.
                    new_key = input('Please, enter the name of the new recipe\n')
                    recipes[f'{new_key}_ing'] = input('Now, enter the needed ingredients\n')
                    recipes[f'{new_key}_ppl'] = input('For how many people will this dish be?(include the words "adults, children, people")\n')
                    print(f'You have added a new recipe: {new_key}. Ingredients: {recipes[f'{new_key}_ing']}. It will be made for: {recipes[f'{new_key}_ppl']}')
            elif option == "2":
                print("You have selected a tab:[MY RECIPES]")
                print("To continue - type (c)ontinue, to go back - type (b)ack")
                answer = input()
                if answer == "b" or answer == "back":
                    break
                elif answer == "c" or answer == "continue":
                    #ToDo: print the list of accessible recipes
                    #      then ask for a name of necessary recipe and check by this name the recipe
                    print('workinprogress')
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