# greet = lambda name: print("Hello " + name + "!")

def language_input():
    """
    asks user to choose language
    """
    language = input("Please choose a langauge: English, Spanish, Chinese\n")
    return language

def greet(language):
    if language == "English":
        name = input("Please enter your name: ")
        print ("Hello " + name + "!")
    elif language == "Spanish":
        name = input("Por favor, escriba su nombre: ")
        print ("Hola " + name + "!")
    elif language == "Chinese":
        name = input("请输入你的名字: ")
        print (u"你好 " + name + u"！")

greet(language_input())
