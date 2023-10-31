# greet = lambda name: print("Hello " + name + "!")

def language_input():
    """
    asks user to choose language
    """
    language = input("Please choose a langauge: English, Spanish, Chinese\n")
    return language

def name_input():
    """
    asks user to input name in chosen language and returns input as string
    """
    name = input("Please enter your name in the chosen language: ")
    return name

def greet():
    language = input("Please choose a language: English, Spanish, Chinese\n")
    name = ""
    if language == "English":
        name = input("Please enter your name: ")
        print ("Hello " + name + "!")
    elif language == "Spanish":
        name = input("Por favor, escriba su nombre: ")
        print ("Hola " + name + "!")
    elif language == "Chinese":
        name = input("请输入你的名字: ")
        print (u"你好 " + name + u"！")

greet()
