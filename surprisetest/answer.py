foodtype = input(str("Enter the type for foods: "))

if foodtype == "fastfood" or foodtype == "desert" or  foodtype == "appt" or  foodtype == "drinks" or  foodtype == "maincourse":
    # Code block for fastfood
    if foodtype == "fastfood":
        fast_food = input(str("Type the fast food name: "))
        # burger, sausage, sandwhich, hotdog, frechfry
        if fast_food == "burger":
            print("Burger is delicious")

        elif fast_food == "sausage":
            print("Sausage is tasty")

        elif fast_food == "sandwhich":
            print("sandwhich is tasty")

        elif fast_food == "hotdog":
            print("hotdog is tasty")

        elif fast_food == "frechfry":
            print("frechfry is tasty")

        else:
            print("It's not fastfood")

    if foodtype == "desert":
        fast_food = input(str("Type the desert name: "))
        # sondesh, cake, faluda, finni, jorda
        if fast_food == "sondesh":
            print("sondesh is delicious")

        elif fast_food == "cake":
            print("cake is tasty")

        elif fast_food == "faluda":
            print("faluda is tasty")

        elif fast_food == "finni":
            print("finni is tasty")

        elif fast_food == "jorda":
            print("jorda is tasty")
        else:
            print("It's not desert")

    if foodtype == "appt":
        fast_food = input(str("Type the appt name: "))
        # burger, appt2, appt3, appt4, appt5
        if fast_food == "soup":
            print("soup is delicious")

        elif fast_food == "appt2":
            print("appt2 is tasty")

        elif fast_food == "appt3":
            print("appt3 is tasty")

        elif fast_food == "appt4":
            print("appt4 is tasty")

        elif fast_food == "appt5":
            print("appt5 is tasty")
        else:
            print("It's not appt")
else:
    print("I don't know what this is :/ ")

