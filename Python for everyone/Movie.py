
Favouritemovie = False
while Favouritemovie == False:
    print("What movie do you want to watch?")
    answer = input()
    if answer =="WALL-E":
        Favouritemovie = True
        break
    else:
        print("That was fun. Let's watch another one.")
        continue
print("That was my favourite movie of all time.")
print("I think I'll power down now.")