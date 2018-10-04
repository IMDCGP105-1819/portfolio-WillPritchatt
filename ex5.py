cards = 99
while cards != 0:
    print("{0} duel monsters cards on the wall, {0} duel monsters cards!".format(cards))
    cards -= 1
    if cards != 0:
        print("Take one down, trade it around {} duel monsters cards on the wall!".format(cards))
    else:
        print("So take it down, pass it around, no more duel monsters cards on the wall!")
