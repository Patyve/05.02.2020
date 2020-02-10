# 2x input fuer zahl1 und zahl2
# 1x input fuer die rechenoperation
# umwandlung in fließkommazahl
# -> keine rechenoperation --> print error



while True:
    try:
        zahl1 = float (input("geben sie die 1. zahl ein:\n"))
        break
    except ValueError:
        print("das war keine zahl.geben sie eine zahl ein")

operation = input("geben sie +,-,/,* ein:\n")

while True:
    try:
        zahl2 = float (input("geben sie die 2. zahl ein:\n"))
        break
    except ValueError:
        print("das war keine zahl.geben sie eine zahl ein")


if(operation == "+"):
    print(float(zahl1)+float(zahl2))
elif(operation == "-"):
    print(float(zahl1) - float(zahl2))
elif(operation == "*"):
    print(float(zahl1) * float(zahl2))
elif(operation == "/"):
    if(float(zahl2)!=0):
        print(float(zahl1) - float(zahl2))
    else:
        print("2. zahl darf nicht 0 sein")
else:
    print("keine rechenoperation")

