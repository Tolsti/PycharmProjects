import Deck2


def poker_combinations(five_cards):
    card = [(five_cards[0].dignity, five_cards[0].suit),
            (five_cards[1].dignity, five_cards[1].suit),
            (five_cards[2].dignity, five_cards[2].suit),
            (five_cards[3].dignity, five_cards[3].suit),
            (five_cards[4].dignity, five_cards[4].suit)]
    print(*card)
    
    # if card[0][0]in card[]
    # elif card[0][0] == 'Ace' and\
    #         card[1][0] == '2' and\
    #         card[2][0] == '3' and\
    #         card[3][0] == '4' and\
    #         card[4][0] == '5':
    #     return 'Туз'
    # else:
    #     return 'Нет комбинации'


if __name__ == '__main__':
    deck = Deck2.Deck()
    hand_of_five_cards = [deck.remove_card() for _ in range(5)]
    # for i in hand_of_five_cards:
    #     print(i)
    # deck.show_deck()
    print(poker_combinations(hand_of_five_cards))
