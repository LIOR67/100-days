
print("welcome to the treasure hunt")
choice1 = input("left or right?")
if choice1 == "left":
    print("game over")
elif choice1 == "right":
    choice2 = input("you found a boat, should you use it or swim on your own?")
    if choice2 == "swim":
        print("game over")
    elif choice2 == "boat":
        choice3 = input("you passed safely and you found 3 doors, each with a different color. the first door is blue, "
                        "the second is green and the thirs is yellow. which do you choose?")
        if choice3 == "blue":
            print("you win")
        else:
            print("game over")
    else:
        print("game over")

else:
    print("game over")
