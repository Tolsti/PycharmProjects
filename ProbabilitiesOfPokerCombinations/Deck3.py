import random

suit = '♥ ♣ ♦ ♠'.split()
rank = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
deck = [str(r) + ' ' + str(i) for i in suit for r in rank]


def one_pair(hand):
    all_face = [h[0] for h in hand]
    combination = [f for f in all_face if all_face.count(f) == 2 or all_face.count(f) == 3]
    if len(combination) == 2:
        return True
    else:
        return False


def two_pairs(hand):
    all_face = [h[0] for h in hand]
    combination = [f for f in all_face if all_face.count(f) == 2]
    if len(combination) == 4:
        return True
    else:
        return False


def three_of_kind(hand):
    all_face = [h[0] for h in hand]
    combination = [f for f in all_face if all_face.count(f) == 3 or all_face.count(f) == 2]
    if len(combination) == 3:
        return True, hand, combination
    else:
        return False


def straight(hand):
    face_for_straight = [h[0] for h in hand]
    change_face = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                   '9': 9, '1': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for i in range(5):
        if face_for_straight[i] in change_face.keys():
            face_for_straight[i] = change_face[face_for_straight[i]]
    combination = sorted(face_for_straight)
    if max(combination) - min(combination) == 4 or combination == [2, 3, 4, 5, 14]:
        return True
    else:
        return False


def flush(hand):
    all_suit = [h[-1] for h in hand]
    combination = [f for f in all_suit if all_suit.count(f) == 5]
    if len(combination) == 5:
        return True
    else:
        return False


def full_house(hand):
    all_face = [h[0] for h in hand]
    combination = [f for f in all_face if all_face.count(f) == 2 or all_face.count(f) == 3]
    if len(combination) == 5:
        return True
    else:
        return False


def four_of_kind(hand):
    all_face = [h[0] for h in hand]
    combination = [f for f in all_face if all_face.count(f) == 4]
    if len(combination) == 4:
        return True
    else:
        return False


def straight_flush(hand):
    if straight(hand) and flush(hand):
        return True
    else:
        return False


def royal_flush(hand):
    print(hand)
    

if __name__ == '__main__':
    # print(deck)
    
    print(royal_flush(('3♥', '4♥', '5♥', '3♥', 'A♥')))
    
    # print()
    #
    # count_one_pair = 0
    # count_two_pairs = 0
    # count_three_of_kind = 0
    # count_full_house = 0
    # count_four_of_kind = 0
    #
    # number_of_hands = 1000
    #
    # for n in range(number_of_hands):
    #     random.shuffle(deck)
    #     handy = [deck[i] for i in range(5)]
    #     comb = ''
    #     if one_pair(handy):
    #         count_one_pair += 1
    #         comb = 'ONE PAIR'
    #     elif two_pairs(handy):
    #         count_two_pairs += 1
    #         comb = 'TWO PAIRS'
    #     elif three_of_kind(handy):
    #         count_three_of_kind += 1
    #         comb = 'THREE OF KIND'
    #     elif full_house(handy):
    #         count_full_house += 1
    #         comb = 'FULL HOUSE'
    #     elif four_of_kind(handy):
    #         count_four_of_kind += 1
    #         comb = 'FOUR OF KIND'
    #
    #     # print(n + 1, *handy, comb)
    #
    # print()
    # print('ONE PAIR:', count_one_pair / number_of_hands * 100)
    # print('TWO PAIRS:', count_two_pairs / number_of_hands * 100)
    # print('THREE OF KIND:', count_three_of_kind / number_of_hands * 100)
    # print('FULL HOUSE:', count_full_house / number_of_hands * 100)
    # print('FOUR OF KIND:', count_four_of_kind / number_of_hands * 100)
    # print('NOTHING:', (number_of_hands - count_one_pair - count_two_pairs - count_three_of_kind -
    #                    count_full_house - count_four_of_kind) / number_of_hands * 100)
