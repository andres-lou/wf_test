with open("cake") as f:
    cake = f.read().strip()
    print(cake)
    if cake  == "THE CAKE IS A LIE!":
        print(True)
    else:
        print(False)

