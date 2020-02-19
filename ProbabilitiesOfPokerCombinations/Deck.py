import random

# Достоинства карт
Ace = 'Ace'
King = 'King'
Queen = 'Queen'
Jack = 'Jack'
# Масть карт
Heart = 'Heart'
Club = 'Club'
Diamond = 'Diamond'
Spade = 'Spade'
# Колода
Deck = ((Ace, Heart), (2, Heart), (3, Heart), (4, Heart), (5, Heart), (6, Heart),
        (7, Heart), (8, Heart), (9, Heart), (10, Heart), (Jack, Heart), (Queen, Heart), (King, Heart),
        (Ace, Club), (2, Club), (3, Club), (4, Club), (5, Club), (6, Club),
        (7, Club), (8, Club), (9, Club), (10, Club), (Jack, Club), (Queen, Club), (King, Club),
        (Ace, Diamond), (2, Diamond), (3, Diamond), (4, Diamond), (5, Diamond), (6, Diamond),
        (7, Diamond), (8, Diamond), (9, Diamond), (10, Diamond), (Jack, Diamond), (Queen, Diamond), (King, Diamond),
        (Ace, Spade), (2, Spade), (3, Spade), (4, Spade), (5, Spade), (6, Spade),
        (7, Spade), (8, Spade), (9, Spade), (10, Spade), (Jack, Spade), (Queen, Spade), (King, Spade))


def deal_carts(player=1):
    deck = list(Deck)
    random.shuffle(deck)
    # print(deck)
    players = list()
    player1 = list()
    player2 = list()
    player3 = list()
    player4 = list()
    player5 = list()
    player6 = list()
    player7 = list()
    player8 = list()
    player9 = list()
    player10 = list()

    flag = 0
    while flag < 5:
        if 1 <= player <= 10:
            player1.append(deck[0])
            deck.pop(0)
            if player >= 2:
                player2.append(deck[0])
                deck.pop(0)
                if player >= 3:
                    player3.append(deck[0])
                    deck.pop(0)
                    if player >= 4:
                        player4.append(deck[0])
                        deck.pop(0)
                        if player >= 5:
                            player5.append(deck[0])
                            deck.pop(0)
                            if player >= 6:
                                player6.append(deck[0])
                                deck.pop(0)
                                if player >= 7:
                                    player7.append(deck[0])
                                    deck.pop(0)
                                    if player >= 8:
                                        player8.append(deck[0])
                                        deck.pop(0)
                                        if player >= 9:
                                            player9.append(deck[0])
                                            deck.pop(0)
                                            if player == 10:
                                                player10.append(deck[0])
                                                deck.pop(0)
        else:
            players = False
            break
        flag += 1
    if 10 >= player >= 1:
        players.append(player1)
        if player >= 2:
            players.append(player2)
            if player >= 3:
                players.append(player3)
                if player >= 4:
                    players.append(player4)
                    if player >= 5:
                        players.append(player5)
                        if player >= 6:
                            players.append(player6)
                            if player >= 7:
                                players.append(player7)
                                if player >= 8:
                                    players.append(player8)
                                    if player >= 9:
                                        players.append(player9)
                                        if player == 10:
                                            players.append(player10)
    return players  # сделать players что бы возвращала список плэеров


def get_combination(carts_of_player):  # принимает руку игрока только через for
    # carts_of_player = [('Ace', 'Spade'), ('Queen', 'Spade'), ('Jack', 'Spade'), ('King', 'Spade'), (10, 'Spade')]
    kind_carts = [carts_of_player[0][0], carts_of_player[1][0], carts_of_player[2][0], carts_of_player[3][0],
                  carts_of_player[4][0]]
    suit_carts = [carts_of_player[0][1], carts_of_player[1][1], carts_of_player[2][1], carts_of_player[3][1],
                  carts_of_player[4][1]]

    # print(kind_carts)
    # print(suit_carts)
    # straight = [carts_of_player[0][0], carts_of_player[1][0], carts_of_player[2][0], carts_of_player[3][0],
    #             carts_of_player[4][0]]

    if ((kind_carts[0] in [10, 'Jack', 'Queen', 'King', 'Ace'] and \
         kind_carts[1] in [10, 'Jack', 'Queen', 'King', 'Ace'] and \
         kind_carts[2] in [10, 'Jack', 'Queen', 'King', 'Ace'] and \
         kind_carts[3] in [10, 'Jack', 'Queen', 'King', 'Ace'] and \
         kind_carts[4] in [10, 'Jack', 'Queen', 'King', 'Ace']) and \
            suit_carts[0] == suit_carts[1] == suit_carts[2] == suit_carts[3] == suit_carts[4]):
        return 'ROYAL FLUSH'
    elif kind_carts[0] == kind_carts[1] == kind_carts[2] == kind_carts[3] or \
            kind_carts[0] == kind_carts[1] == kind_carts[2] == kind_carts[4] or \
            kind_carts[0] == kind_carts[1] == kind_carts[3] == kind_carts[4] or \
            kind_carts[0] == kind_carts[2] == kind_carts[3] == kind_carts[4] or \
            kind_carts[1] == kind_carts[2] == kind_carts[3] == kind_carts[4]:
        return 'FOUR OF A KIND'
    elif (kind_carts[0] == kind_carts[1] and kind_carts[2] == kind_carts[3] == kind_carts[4]) or \
            (kind_carts[1] == kind_carts[2] and kind_carts[0] == kind_carts[3] == kind_carts[4]) or \
            (kind_carts[2] == kind_carts[3] and kind_carts[0] == kind_carts[1] == kind_carts[4]) or \
            (kind_carts[3] == kind_carts[4] and kind_carts[0] == kind_carts[1] == kind_carts[2]) or \
            (kind_carts[0] == kind_carts[2] and kind_carts[1] == kind_carts[3] == kind_carts[4]) or \
            (kind_carts[0] == kind_carts[3] and kind_carts[1] == kind_carts[2] == kind_carts[4]) or \
            (kind_carts[0] == kind_carts[4] and kind_carts[1] == kind_carts[2] == kind_carts[3]) or \
            (kind_carts[1] == kind_carts[3] and kind_carts[0] == kind_carts[2] == kind_carts[4]) or \
            (kind_carts[1] == kind_carts[4] and kind_carts[0] == kind_carts[2] == kind_carts[3]) or \
            (kind_carts[2] == kind_carts[4] and kind_carts[0] == kind_carts[1] == kind_carts[3]):
        return 'FULL HOUSE'
    elif ('Ace' in kind_carts and 2 in kind_carts and 3 in kind_carts and 4 in kind_carts and 5 in kind_carts) or \
            (2 in kind_carts and 3 in kind_carts and 4 in kind_carts and 5 in kind_carts and 6 in kind_carts) or \
            (3 in kind_carts and 4 in kind_carts and 5 in kind_carts and 6 in kind_carts and 7 in kind_carts) or \
            (4 in kind_carts and 5 in kind_carts and 6 in kind_carts and 7 in kind_carts and 8 in kind_carts) or \
            (5 in kind_carts and 6 in kind_carts and 7 in kind_carts and 8 in kind_carts and 9 in kind_carts) or \
            (6 in kind_carts and 7 in kind_carts and 8 in kind_carts and 9 in kind_carts and 10 in kind_carts) or \
            (7 in kind_carts and 8 in kind_carts and 9 in kind_carts and 10 in kind_carts and 'Jack' in kind_carts) or \
            (8 in kind_carts and 9 in kind_carts and 10 in kind_carts and
             'Jack' in kind_carts and 'Queen' in kind_carts) or \
            (9 in kind_carts and 10 in kind_carts and 'Jack' in kind_carts and
             'Queen' in kind_carts and 'King' in kind_carts) or \
            (10 in kind_carts and 'Jack' in kind_carts and 'Queen' in kind_carts and
             'King' in kind_carts and 'Ace' in kind_carts):
        if suit_carts[0] == suit_carts[1] == suit_carts[2] == suit_carts[3] == suit_carts[4]:
            return 'STRAIGHT FLUSH'
        return 'STRAIGHT'
    elif suit_carts[0] == suit_carts[1] == suit_carts[2] == suit_carts[3] == suit_carts[4]:
        return 'FLUSH'
    elif kind_carts[0] == kind_carts[1] == kind_carts[2] or \
            kind_carts[0] == kind_carts[1] == kind_carts[3] or \
            kind_carts[0] == kind_carts[1] == kind_carts[4] or \
            kind_carts[1] == kind_carts[2] == kind_carts[3] or \
            kind_carts[1] == kind_carts[2] == kind_carts[4] or \
            kind_carts[2] == kind_carts[3] == kind_carts[4] or \
            kind_carts[2] == kind_carts[3] == kind_carts[0] or \
            kind_carts[3] == kind_carts[4] == kind_carts[0] or \
            kind_carts[3] == kind_carts[4] == kind_carts[1]:
        return 'THREE OF A KIND'
    elif (kind_carts[0] == kind_carts[1] and kind_carts[2] == kind_carts[3]) or \
            (kind_carts[0] == kind_carts[1] and kind_carts[2] == kind_carts[4]) or \
            (kind_carts[0] == kind_carts[1] and kind_carts[3] == kind_carts[4]) or \
            (kind_carts[1] == kind_carts[2] and kind_carts[0] == kind_carts[3]) or \
            (kind_carts[1] == kind_carts[2] and kind_carts[0] == kind_carts[4]) or \
            (kind_carts[1] == kind_carts[2] and kind_carts[3] == kind_carts[4]) or \
            (kind_carts[2] == kind_carts[3] and kind_carts[0] == kind_carts[4]) or \
            (kind_carts[2] == kind_carts[3] and kind_carts[1] == kind_carts[4]) or \
            (kind_carts[3] == kind_carts[4] and kind_carts[0] == kind_carts[2]) or \
            (kind_carts[0] == kind_carts[2] and kind_carts[1] == kind_carts[4]) or \
            (kind_carts[0] == kind_carts[2] and kind_carts[1] == kind_carts[3]) or \
            (kind_carts[0] == kind_carts[3] and kind_carts[1] == kind_carts[4]) or \
            (kind_carts[0] == kind_carts[3] and kind_carts[2] == kind_carts[4]) or \
            (kind_carts[0] == kind_carts[4] and kind_carts[1] == kind_carts[3]) or \
            (kind_carts[1] == kind_carts[3] and kind_carts[2] == kind_carts[4]) or \
            (kind_carts[2] == kind_carts[4] and kind_carts[0] == kind_carts[1]):
        return 'TWO PAIRS'
    elif (kind_carts[0] in [kind_carts[1], kind_carts[2], kind_carts[3], kind_carts[4]] or \
          kind_carts[1] in [kind_carts[2], kind_carts[3], kind_carts[4]] or \
          kind_carts[2] in [kind_carts[3], kind_carts[4]] or \
          kind_carts[3] in [kind_carts[4]]):
        return 'ONE PAIR'
    elif 'Ace' in kind_carts and 'King' in kind_carts:
        return 'ACE KING'
    else:
        return 'NO COMBINATION'
    # if cart1[0] == cart2[0] or \
    #         cart1[0] == cart3[0] or \
    #         cart1[0] == cart4[0] or \
    #         cart1[0] == cart5[0] or \
    #         cart2[0] == cart3[0] or \
    #         cart2[0] == cart4[0] or \
    #         cart2[0] == cart5[0] or \
    #         cart3[0] == cart4[0] or \
    #         cart3[0] == cart5[0] or \
    #         cart4[0] == cart5[0]:
    #     if ((cart1[0] == cart2[0]) and (cart3[0] == cart4[0])) or \
    #             ((cart1[0] == cart2[0]) and (cart3[0] == cart5[0])) or \
    #             ((cart1[0] == cart2[0]) and (cart4[0] == cart5[0])) or \
    #             ((cart2[0] == cart3[0]) and (cart1[0] == cart4[0])) or \
    #             ((cart2[0] == cart3[0]) and (cart1[0] == cart5[0])) or \
    #             ((cart2[0] == cart3[0]) and (cart4[0] == cart5[0])) or \
    #             ((cart3[0] == cart4[0]) and (cart1[0] == cart5[0])) or \
    #             ((cart3[0] == cart4[0]) and (cart2[0] == cart5[0])) or \
    #             ((cart4[0] == cart5[0]) and (cart1[0] == cart3[0])) or \
    #             ((cart4[0] == cart5[0]) and (cart1[0] == cart3[0])) or \
    #             ((cart1[0] == cart3[0]) and (cart2[0] == cart5[0])) or \
    #             ((cart1[0] == cart3[0]) and (cart2[0] == cart4[0])) or \
    #             ((cart1[0] == cart4[0]) and (cart2[0] == cart5[0])) or \
    #             ((cart1[0] == cart4[0]) and (cart3[0] == cart5[0])) or \
    #             ((cart1[0] == cart5[0]) and (cart2[0] == cart4[0])) or \
    #             ((cart2[0] == cart4[0]) and (cart3[0] == cart5[0])) or \
    #             ((cart3[0] == cart5[0]) and (cart1[0] == cart2[0])):
    #         return 'TWO PAIRS'
    #     if (cart1[0] == cart2[0] == cart3[0]) or \
    #             (cart1[0] == cart2[0] == cart4[0]) or \
    #             (cart1[0] == cart2[0] == cart5[0]) or \
    #             (cart2[0] == cart3[0] == cart4[0]) or \
    #             (cart2[0] == cart3[0] == cart5[0]) or \
    #             (cart3[0] == cart4[0] == cart5[0]) or \
    #             (cart3[0] == cart4[0] == cart1[0]) or \
    #             (cart4[0] == cart5[0] == cart1[0]) or \
    #             (cart4[0] == cart5[0] == cart2[0]):
    #         return 'THREE OF A KIND'
    #     return 'ONE PAIR'
    # if ((straight[0] == 'Ace' or straight[0] == 2 or straight[0] == 3 or straight[0] == 4 or straight[0] == 5) and \
    #     (straight[1] == 'Ace' or straight[1] == 2 or straight[1] == 3 or straight[1] == 4 or straight[1] == 5) and \
    #     (straight[2] == 'Ace' or straight[2] == 2 or straight[2] == 3 or straight[2] == 4 or straight[2] == 5) and \
    #     (straight[3] == 'Ace' or straight[3] == 2 or straight[3] == 3 or straight[3] == 4 or straight[3] == 5) and \
    #     (straight[4] == 'Ace' or straight[4] == 2 or straight[4] == 3 or straight[4] == 4 or straight[4] == 5)) or \
    #         ((straight[0] == 2 or straight[0] == 3 or straight[0] == 4 or straight[0] == 5 or straight[0] == 6) and \
    #          (straight[1] == 2 or straight[1] == 3 or straight[1] == 4 or straight[1] == 5 or straight[1] == 6) and \
    #          (straight[2] == 2 or straight[2] == 3 or straight[2] == 4 or straight[2] == 5 or straight[2] == 6) and \
    #          (straight[3] == 2 or straight[3] == 3 or straight[3] == 4 or straight[3] == 5 or straight[3] == 6) and \
    #          (straight[4] == 2 or straight[4] == 3 or straight[4] == 4 or straight[4] == 5 or straight[4] == 6)) or \
    #         ((straight[0] == 3 or straight[0] == 4 or straight[0] == 5 or straight[0] == 6 or straight[0] == 7) and \
    #          (straight[1] == 3 or straight[1] == 4 or straight[1] == 5 or straight[1] == 6 or straight[1] == 7) and \
    #          (straight[2] == 3 or straight[2] == 4 or straight[2] == 5 or straight[2] == 6 or straight[2] == 7) and \
    #          (straight[3] == 3 or straight[3] == 4 or straight[3] == 5 or straight[3] == 6 or straight[3] == 7) and \
    #          (straight[4] == 3 or straight[4] == 4 or straight[4] == 5 or straight[4] == 6 or straight[4] == 7)) or \
    #         ((straight[0] == 4 or straight[0] == 5 or straight[0] == 6 or straight[0] == 7 or straight[0] == 8) and \
    #          (straight[1] == 4 or straight[1] == 5 or straight[1] == 6 or straight[1] == 7 or straight[1] == 8) and \
    #          (straight[2] == 4 or straight[2] == 5 or straight[2] == 6 or straight[2] == 7 or straight[2] == 8) and \
    #          (straight[3] == 4 or straight[3] == 5 or straight[3] == 6 or straight[3] == 7 or straight[3] == 8) and \
    #          (straight[4] == 4 or straight[4] == 5 or straight[4] == 6 or straight[4] == 7 or straight[4] == 8)) or \
    #         ((straight[0] == 5 or straight[0] == 6 or straight[0] == 7 or straight[0] == 8 or straight[0] == 9) and \
    #          (straight[1] == 5 or straight[1] == 6 or straight[1] == 7 or straight[1] == 8 or straight[1] == 9) and \
    #          (straight[2] == 5 or straight[2] == 6 or straight[2] == 7 or straight[2] == 8 or straight[2] == 9) and \
    #          (straight[3] == 5 or straight[3] == 6 or straight[3] == 7 or straight[3] == 8 or straight[3] == 9) and \
    #          (straight[4] == 5 or straight[4] == 6 or straight[4] == 7 or straight[4] == 8 or straight[4] == 9)) or \
    #         ((straight[0] == 6 or straight[0] == 7 or straight[0] == 8 or straight[0] == 9 or straight[0] == 10) and \
    #          (straight[1] == 6 or straight[1] == 7 or straight[1] == 8 or straight[1] == 9 or straight[1] == 10) and \
    #          (straight[2] == 6 or straight[2] == 7 or straight[2] == 8 or straight[2] == 9 or straight[2] == 10) and \
    #          (straight[3] == 6 or straight[3] == 7 or straight[3] == 8 or straight[3] == 9 or straight[3] == 10) and \
    #          (straight[4] == 6 or straight[4] == 7 or straight[4] == 8 or straight[4] == 9 or straight[4] == 10)) or \
    #         ((straight[0] == 7 or straight[0] == 8 or straight[0] == 9 or straight[0] == 10 or straight[
    #             0] == 'Jack') and \
    #          (straight[1] == 7 or straight[1] == 8 or straight[1] == 9 or straight[1] == 10 or straight[
    #              1] == 'Jack') and \
    #          (straight[2] == 7 or straight[2] == 8 or straight[2] == 9 or straight[2] == 10 or straight[
    #              2] == 'Jack') and \
    #          (straight[3] == 7 or straight[3] == 8 or straight[3] == 9 or straight[3] == 10 or straight[
    #              3] == 'Jack') and \
    #          (straight[4] == 7 or straight[4] == 8 or straight[4] == 9 or straight[4] == 10 or straight[
    #              4] == 'Jack')) or \
    #         ((straight[0] == 8 or straight[0] == 9 or straight[0] == 10 or straight[0] == 'Jack' or straight[
    #             0] == 'Queen') and \
    #          (straight[1] == 8 or straight[1] == 9 or straight[1] == 10 or straight[1] == 'Jack' or straight[
    #              1] == 'Queen') and \
    #          (straight[2] == 8 or straight[2] == 9 or straight[2] == 10 or straight[2] == 'Jack' or straight[
    #              2] == 'Queen') and \
    #          (straight[3] == 8 or straight[3] == 9 or straight[3] == 10 or straight[3] == 'Jack' or straight[
    #              3] == 'Queen') and \
    #          (straight[4] == 8 or straight[4] == 9 or straight[4] == 10 or straight[4] == 'Jack' or straight[
    #              4] == 'Queen')) or \
    #         ((straight[0] == 9 or straight[0] == 10 or straight[0] == 'Jack' or straight[0] == 'Queen' or straight[
    #             0] == 'King') and \
    #          (straight[1] == 9 or straight[1] == 10 or straight[1] == 'Jack' or straight[1] == 'Queen' or straight[
    #              1] == 'King') and \
    #          (straight[2] == 9 or straight[2] == 10 or straight[2] == 'Jack' or straight[2] == 'Queen' or straight[
    #              2] == 'King') and \
    #          (straight[3] == 9 or straight[3] == 10 or straight[3] == 'Jack' or straight[3] == 'Queen' or straight[
    #              3] == 'King') and \
    #          (straight[4] == 9 or straight[4] == 10 or straight[4] == 'Jack' or straight[4] == 'Queen' or straight[
    #              4] == 'King')) or \
    #         ((straight[0] == 10 or straight[0] == 'Jack' or straight[0] == 'Queen' or straight[0] == 'King' or straight[
    #             0] == 'Ace') and \
    #          (straight[1] == 10 or straight[1] == 'Jack' or straight[1] == 'Queen' or straight[1] == 'King' or straight[
    #              1] == 'Ace') and \
    #          (straight[2] == 10 or straight[2] == 'Jack' or straight[2] == 'Queen' or straight[2] == 'King' or straight[
    #              2] == 'Ace') and \
    #          (straight[3] == 10 or straight[3] == 'Jack' or straight[3] == 'Queen' or straight[3] == 'King' or straight[
    #              3] == 'Ace') and \
    #          (straight[4] == 10 or straight[4] == 'Jack' or straight[4] == 'Queen' or straight[4] == 'King' or straight[
    #              4] == 'Ace')):
    #     if cart1[1] == cart2[1] == cart3[1] == cart4[1] == cart5[1]:
    #         if cart1[0] == (10 or 'Jack' or 'Queen' or 'King' or 'Ace') and \
    #                 cart2[0] == (10 or 'Jack' or 'Queen' or 'King' or 'Ace') and \
    #                 cart3[0] == (10 or 'Jack' or 'Queen' or 'King' or 'Ace') and \
    #                 cart4[0] == (10 or 'Jack' or 'Queen' or 'King' or 'Ace') and \
    #                 cart5[0] == (10 or 'Jack' or 'Queen' or 'King' or 'Ace'):
    #             print(carts_of_player)
    #             return 'ROYAL FLUSH'
    #         return 'STRAIGHT FLUSH'
    #     return 'STRAIGHT'
    # else:
    #     return 'NO COMBINATION'


no_combination = 0
ace_king = 0
one_pair = 0
two_pairs = 0
three_of_a_kind = 0
straight = 0
flush = 0
full_house = 0
four_of_a_kind = 0
straight_flush = 0
royal_flush = 0

i = 1000000
while i > 0:
    for hand in deal_carts():
        if get_combination(hand) == 'NO COMBINATION':
            no_combination += 1
        elif get_combination(hand) == 'ACE KING':
            # print('AK: {}\t{}\t{}\t{}\t{}'.format(hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]))
            ace_king += 1
        elif get_combination(hand) == 'ONE PAIR':
            # print('OP: {}\t{}\t{}\t{}\t{}'.format(hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]))
            one_pair += 1
        elif get_combination(hand) == 'TWO PAIRS':
            two_pairs += 1
        elif get_combination(hand) == 'THREE OF A KIND':
            three_of_a_kind += 1
        elif get_combination(hand) == 'STRAIGHT':
            # print('ST: {}\t{}\t{}\t{}\t{}'.format(hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]))
            straight += 1
        elif get_combination(hand) == 'FLUSH':
            flush += 1
        elif get_combination(hand) == 'FULL HOUSE':
            # print('FH: {}\t{}\t{}\t{}\t{}'.format(hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]))
            full_house += 1
        elif get_combination(hand) == 'FOUR OF A KIND':
            # print('FK: {}\t{}\t{}\t{}\t{}'.format(hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]))
            four_of_a_kind += 1
        elif get_combination(hand) == 'STRAIGHT FLUSH':
            print(hand)
            straight_flush += 1
        elif get_combination(hand) == 'ROYAL FLUSH':
            print(hand)
            royal_flush += 1
    i -= 1
# print(deal_carts())
print('Нет комбинации: {}\n'
      'Туз король: {}\n'
      'Одна пара: {}\n'
      'Две пары: {}\n'
      'Три одинаковые: {}\n'
      'Стрит: {}\n'
      'Флеш: {}\n'
      'Фул хаус: {}\n'
      'Каре: {}\n'
      'Стрит флеш: {}\n'
      'Роял флеш: {}'.format(no_combination, ace_king, one_pair, two_pairs, three_of_a_kind, straight, flush,
                             full_house, four_of_a_kind, straight_flush, royal_flush))
# for i in deal_carts():
#     print(i)
#     print(get_combination(i))
# print('Пробная')
# print(get_combination([(6, 'Club'), (5, 'Club'), (3, 'Heart'), (4, 'Heart'), (7, 'Club')]))
# print(get_combination()
# for i in deal_carts(8):
#     print(get_combination(i))
