# greet = lambda name: print("Hello " + name + "!")

def language_input():
    """
    asks user to choose language
    """
    language = input("Please choose a langauge: English, Spanish, Chinese")
    return language

def name_input():
    """
    asks user to input name in chosen language and returns input as string
    """
    name = input("Please enter your name in the chosen language: ")
    return name

def greet(name):
    """
    takes a name parameter and prints greeting with name
    """
    print("Hello " + name + "!")

"""greet(name_input())"""