cards = 99
#  While loop will run until the number of cards is equal to zero
while cards != 0:
    print("{0} duel monsters cards on the wall, {0} duel monsters cards!".format(cards))
    cards -= 1
    if cards != 0:
        print("Take one down, trade it around {} duel monsters cards on the wall!".format(cards))
    else:
        print("So take it down, trade it around, no more duel monsters cards on the wall!")

