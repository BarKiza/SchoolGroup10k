import random, func_funny, datetime as date

x = random.randint(1,1000)
print(x)

f = func_funny.fileopen("numbguesslog")

username = input("Who is playing?: ")

guesses = 0
def log():
    f.write(f"{username},{guesses},{x}")


def top10():
    a=0
    f = open("numbguesslog.txt", "r")
    while True:
        temp = f.readline()
        temp = temp.split(",")
        exec(f"f\"l{a} = {temp[0]} in {temp[1]} with {x} to guess\"")
        exec(f'print(f"l{a}")')
top10()

while True:
    u = func_funny.inputnum("Take a guess between 1-1000")
    if u > x:
        print("Too High")
        guesses += 1
    elif u < x:
        print("Too Low")
        guesses += 1
    elif u == x:
        print(f"The number was {x}!")
        guesses += 1
        log()
        break