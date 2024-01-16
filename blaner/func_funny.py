def inputnum(prompt):
    while True:
        u = input(prompt)
        try:
            u = int(u)
            return u
        except:
            print("Number Please!")



def fileopen(name):
    try:
        f = open(f"{name}.txt","a")
        return f
    except:
        f = open(f"{name}.txt", "x")
        return f