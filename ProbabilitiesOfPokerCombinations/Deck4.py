import random
import time

suit = '♥ ♣ ♦ ♠'.split()
rank = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
deck = [str(r) + '' + str(i) for i in suit for r in rank]


def face_combination(hand):
    all_face = sorted([i for h in hand for i, s in enumerate('234567891JQKA', start = 2) if h[0] == s])
    repeat_face = [f for f in all_face if all_face.count(f) in range(2, 5)]
    
    if len(repeat_face) == 2:
        return 'ONE PAIR'
    if len(repeat_face) == 4 and repeat_face[0] != repeat_face[-1]:
        return 'TWO PAIRS'
    if len(repeat_face) == 3:
        return 'THREE OF KIND'
    if len(repeat_face) == 5:
        return 'FULL HOUSE'
    if len(repeat_face) == 4 and repeat_face[0] == repeat_face[-1]:
        return 'FOUR OF KIND'
    
    all_suit = [h[-1] for h in hand]
    straight = (all_face[-1] - all_face[0] == 4 or all_face == [2, 3, 4, 5, 14]) and len(repeat_face) == 0
    flush = len([s for s in all_suit if all_suit.count(s) == 5]) == 5
    
    if all_face == [10, 11, 12, 13, 14] and flush:
        return 'ROYAL FLUSH'
    if straight and flush:
        return 'STRAIGHT FLUSH'
    if flush:
        return 'FLUSH'
    if straight:
        return 'STRAIGHT'
    if 13 in all_face and 14 in all_face:
        return 'ACE KING'
    return 'NOTHING'


def show_statistics(combination):
    dict_statistics = {'count_nothing': 0,
                       'count_ace_king': 0,
                       'count_one_pair': 0,
                       'count_two_pairs': 0,
                       'count_three_of_kind': 0,
                       'count_straight': 0,
                       'count_flush': 0,
                       'count_full_house': 0,
                       'count_four_of_kind': 0,
                       'count_straight_flush': 0,
                       'count_royal_flush': 0}


def take_five_random_cards(t_deck, count_cards=5):
    tmp_deck = t_deck.copy()
    five_cards = list()
    
    for _ in range(count_cards):
        i_card = random.randrange(len(tmp_deck))
        five_cards.append(tmp_deck[i_card])
        tmp_deck.pop(i_card)
    
    return five_cards


if __name__ == '__main__':
    t_start = time.perf_counter()
    
    count_nothing = 0
    count_ace_king = 0
    count_one_pair = 0
    count_two_pairs = 0
    count_three_of_kind = 0
    count_straight = 0
    count_flush = 0
    count_full_house = 0
    count_four_of_kind = 0
    count_straight_flush = 0
    count_royal_flush = 0
    
    number_of_hands = 100000
    
    for n in range(number_of_hands):
        hand = take_five_random_cards(deck)
        handy = face_combination(hand)
        
        if handy == 'NOTHING':
            count_nothing += 1
        elif handy == 'ACE KING':
            count_ace_king += 1
        elif handy == 'ONE PAIR':
            count_one_pair += 1
        elif handy == 'TWO PAIRS':
            count_two_pairs += 1
        elif handy == 'THREE OF KIND':
            count_three_of_kind += 1
        elif handy == 'STRAIGHT':
            count_straight += 1
        elif handy == 'FLUSH':
            count_flush += 1
        elif handy == 'FULL HOUSE':
            count_full_house += 1
        elif handy == 'FOUR OF KIND':
            count_four_of_kind += 1
        elif handy == 'STRAIGHT FLUSH':
            # print(hand)
            count_straight_flush += 1
        elif handy == 'ROYAL FLUSH':
            print(hand)
            count_royal_flush += 1
    
    print('NOTHING:', count_nothing / number_of_hands * 100)
    print('ACE KING:', count_ace_king / number_of_hands * 100)
    print('ONE PAIR:', count_one_pair / number_of_hands * 100)
    print('TWO PAIRS:', count_two_pairs / number_of_hands * 100)
    print('THREE OF KIND:', count_three_of_kind / number_of_hands * 100)
    print('STRAIGHT:', count_straight / number_of_hands * 100)
    print('FLUSH:', count_flush / number_of_hands * 100)
    print('FULL HOUSE:', count_full_house / number_of_hands * 100)
    print('FOUR OF KIND:', count_four_of_kind / number_of_hands * 100)
    print('STRAIGHT FLUSH:', count_straight_flush / number_of_hands * 100)
    print('ROYAL FLUSH:', count_royal_flush / number_of_hands * 100)
    
    print(time.perf_counter() - t_start)
