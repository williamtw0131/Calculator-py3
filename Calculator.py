
# messages:
nuberr = "Insert only numbers"
ask1 = "First number: "
ask2 = "Second number: "


while True:
    # simple explain
    print("This is a simple Calculator")
    print("===========================")
    print("Enter < + > to add two numbers")
    print("Enter < - > to substract two numbers")
    print("Enter < * > to multiply two numbers")
    print("Enter < / > to divide two numbers")
    print("Enter < quit > to quit program")
    print("===========================")

    # ask for next move
    userinput = input("Your request: ")


    if userinput == "quit":
        break

    elif userinput == "+":

        # prompt user for a number
        try:
            nub1 = float(input (ask1))
        # if that input can't be transform to a float
        # it must be a string and will show a ValueError
        # we catch it here and tell the user
        # then return to top
        except ValueError:
            print(nuberr)
            continue
        try:
            nub2 = float(input (ask2))
        except ValueError:
            print(nuberr)
            continue
        else:
            ans = float(nub1) + float(nub2)
            print(f"the answer is {ans}")

    elif userinput == "-":
        try:
            nub1 = float(input (ask1))
        except ValueError:
            print(nuberr)
            continue
        try:
            nub2 = float(input (ask2))
        except ValueError:
            print(nuberr)
            continue
        else:
            ans = nub1 - nub2
            print(f"the answer is {ans}")

    elif userinput == "*":
        try:
            nub1 = float(input (ask1))
        except ValueError:
            print(nuberr)
            continue
        try:
            nub2 = float(input (ask2))
        except ValueError:
            print(nuberr)
            continue
        else:
            ans = nub1 * nub2
            print(f"the answer is {ans}")

    elif userinput == "/":
        try:
            nub1 = float(input (ask1))
        except ValueError:
            print(nuberr)
            continue
        try:
            nub2 = float(input (ask2))
        except ValueError:
            print(nuberr)
            continue
        else:
            # check for dividing by zero
            # can use try-except-else here
            if nub2 == 0:
                print("Cannot  be devided by zero")
            else:
                ans = nub1 / nub2
                print(f"the answer is {ans}")
    else:
        print("unknown request")
