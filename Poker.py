import random


class Deck:
    def __init__(self):
        self.card_list = []

    def create_deck(self):
        for suit in range(1, 4):
            if suit == 1:
                suit_value = "C"
            elif suit == 2:
                suit_value = "S"
            elif suit == 3:
                suit_value = "D"
            elif suit == 4:
                suit_value = "H"

            for value in range(2, 15):
                if value < 11:
                    self.card_list.append(suit_value + ":" + str(value))
                else:
                    if value == 11:
                        self.card_list.append(suit_value + ":J")
                    elif value == 12:
                        self.card_list.append(suit_value + ":Q")
                    elif value == 13:
                        self.card_list.append(suit_value + ":K")
                    elif value == 14:
                        self.card_list.append(suit_value + ":A")

    def shuffle_cards(self):
        random.shuffle(self.card_list)

    def get_card_deck(self):
        return self.card_list


class Player:

    def __init__(self, hand):
        self.hand = hand


def deal_hand():
    hand = []
    for i in range(5):
        card = card_deck.pop(-1)
        hand.append(card)
    print(hand)


card_deck = Deck()
card_deck.create_deck()
card_deck.shuffle_cards()
print(card_deck.get_card_deck())
deal_hand()

