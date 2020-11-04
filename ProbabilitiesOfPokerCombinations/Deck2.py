import random


# Suits (in playing cards) – Масти (игральные).
# Deck – колода
# Suit – масть
# Hearts – червы
# Diamonds – бубны
# Clubs – трефы
# Spades – пики
# Jack – валет
# Queen – дама
# King – король
# Ace – туз
# Joker – джокер

class Card:
    def __init__(self, dignity, suit):
        self.dignity = dignity
        self.suit = suit
    
    def __str__(self):
        count = len(str(self.dignity) + str(self.suit))
        if count <= 12:
            count = 12 - count
        else:
            count = 1
        card = '|{} {}{}|'.format(self.dignity, count * ' ', self.suit)
        return card


class Deck:
    def __init__(self):
        a, j, q, k = 'Ace', 'Jack', 'Queen', 'King'
        h, c, d, s = 'Heart', 'Club', 'Diamond', 'Spade'
        self._deck = [Card(a, h), Card('2', h), Card('3', h), Card('4', h), Card('5', h), Card('6', h),
                      Card('7', h), Card('8', h), Card('9', h), Card('10', h), Card(j, h), Card(q, h), Card(k, h),
                      Card(a, c), Card('2', c), Card('3', c), Card('4', c), Card('5', c), Card('6', c),
                      Card('7', c), Card('8', c), Card('9', c), Card('10', c), Card(j, c), Card(q, c), Card(k, c),
                      Card(a, d), Card('2', d), Card('3', d), Card('4', d), Card('5', d), Card('6', d),
                      Card('7', d), Card('8', d), Card('9', d), Card('10', d), Card(j, d), Card(q, d), Card(k, d),
                      Card(a, s), Card('2', s), Card('3', s), Card('4', s), Card('5', s), Card('6', s),
                      Card('7', s), Card('8', s), Card('9', s), Card('10', s), Card(j, s), Card(q, s), Card(k, s)]
        self._deck = [Card(a, h),
                      Card('2', h),
                      Card('2', s),
                      Card('4', h),
                      Card(j, h)]
        self._dumped_cards = []
    
    def add_card(self):
        if len(self._dumped_cards) > 0:
            count_card = random.randint(0, len(self._dumped_cards) - 1)
            tmp_card = self._dumped_cards[count_card]
            self._deck.append(self._dumped_cards[count_card])
            self._dumped_cards.pop(count_card)
            return tmp_card
        else:
            print('Колода полная')
    
    def remove_card(self):
        if len(self._deck) > 0:
            self._dumped_cards.append(self._deck[0])
            tmp_card = self._dumped_cards[len(self._dumped_cards) - 1]
            self._deck.pop(0)
            return tmp_card
        else:
            print('Нет больше карт')
    
    def shuffle(self):
        random.shuffle(self._deck)
    
    def show_deck(self):
        count = 0
        for card in self._deck:
            if count >= 5:
                count = 1
                print()
            else:
                count += 1
            print(card, end = ' ')
        print()


if __name__ == '__main__':
    deck = Deck()
    
    while True:
        print('1 - добавить карту, '
              '2 - убрать карту, '
              '3 - сделать шафл, '
              '0 - выход')
        flag = input('Введите действие: ')
        if flag == '0':
            break
        elif flag == '1':
            tmp = deck.add_card()
            print(tmp)
        elif flag == '2':
            tmp = deck.remove_card()
            print(tmp)
        elif flag == '3':
            deck.shuffle()
        
        deck.show_deck()
