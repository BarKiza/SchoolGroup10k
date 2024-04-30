import random

""" card game
- inv
- effects(multible turns)
- multible players (local coop)
- progression
- special abilities
- pre determined deck(you can see the deck and in what order you will draw the cards)exec() for variable creaation
"""
"""TO DO LIST
-draw cards for 2 players
-have 2 fields for the 2 players

"""
class card:
    def __init__(self,atk,hp,special,name):
        self.atk = int(atk)
        self.hp = int(hp)
        self.special = special
        self.name = str(name)

class field:
    def __init__(self,f1,f2,f3,f4):
        self.f1 =f1
        self.f2 =f2
        self.f3 =f3
        self.f4 =f4


soldier = card(1,2,None,"Soldier")
mercenary = card(2,5,None,"Mercenary")
cards = [soldier, mercenary]
temp2=[1,2]
deck = [soldier,mercenary]
temp = random.choices(temp2,weights= [7,1],k=20)

class Player:
    def __init__(self,hp,inv):
        self.hp = hp
        self.inv = inv
Player1 = Player(inv=[],hp=30)
Player2 = Player(inv=[],hp=30)
"""field1 = field()
field2 = field() not finished"""



for i in temp:

    a = 1
    b = 1
    if i == 1:
        exec(f"soldier{a} =  card(1,2,None,\"Soldier\")")
        exec(f"deck.append(soldier{a})")
        exec("a += 1")
    elif i==2:
        exec(f"mercenary{b} =  card(2,5,None,\"Mercenary\")")
        exec(f"deck.append(mercenary{b})")
        exec("b += 1")



def draw(user, amount):
    for i in range(amount):
        user.inv.append(deck[0])
        deck.pop(0)

def viewhand(user):
    for i in user.inv:
        print(i.name)
    print("\n")

draw(Player1,5)
draw(Player2,5)
viewhand(Player1)
viewhand(Player2)





