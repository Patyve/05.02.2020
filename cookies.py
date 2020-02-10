# endlosschleife
# input --> give me some cookies----> yes or no in klein
# answer yes --> print danke --> abbruch
# print ok --> abbruch
# answer in klein umwandeln (case sensitive)
# lower ( )


monster = "\n\nGIVE ME SOME COOKIES\n\nYES OR NO?!"
user_input = input (monster.lower())

var = 1

while var == 1:
    if (user_input == "yes" ):
        print ("thanks")
        quit ()
    elif (user_input == "no"):
        print ("okay")
        quit()
    else:
        print ("yes or no")


