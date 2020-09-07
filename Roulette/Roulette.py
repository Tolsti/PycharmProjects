import random


class RouletteNumber:
    def __init__(self, name, low_bet, high_bet, even, odd, red, black,
                 first_dozen, second_dozen, third_dozen,
                 first_column, second_column, third_column):
        self.name = name
        self.low_bet = low_bet
        self.high_bet = high_bet
        self.even = even
        self.odd = odd
        self.red = red
        self.black = black
        self.first_dozen = first_dozen
        self.second_dozen = second_dozen
        self.third_dozen = third_dozen
        self.first_column = first_column
        self.second_column = second_column
        self.third_column = third_column


numbers = (
    RouletteNumber(0, False, False, False, False, False, False, False, False, False, False, False, False),  # 0
    RouletteNumber(1, True, False, False, True, True, False, True, False, False, True, False, False),  # 1
    RouletteNumber(2, True, False, True, False, False, True, True, False, False, False, True, False),  # 2
    RouletteNumber(3, True, False, False, True, True, False, True, False, False, False, False, True),  # 3
    RouletteNumber(4, True, False, True, False, False, True, True, False, False, True, False, False),  # 4
    RouletteNumber(5, True, False, False, True, True, False, True, False, False, False, True, False),  # 5
    RouletteNumber(6, True, False, True, False, False, True, True, False, False, False, False, True),  # 6
    RouletteNumber(7, True, False, False, True, True, False, True, False, False, True, False, False),  # 7
    RouletteNumber(8, True, False, True, False, False, True, True, False, False, False, True, False),  # 8
    RouletteNumber(9, True, False, False, True, True, False, True, False, False, False, False, True),  # 9
    RouletteNumber(10, True, False, True, False, False, True, True, False, False, True, False, False),  # 10
    RouletteNumber(11, True, False, False, True, False, True, True, False, False, False, True, False),  # 11
    RouletteNumber(12, True, False, True, False, True, False, True, False, False, False, False, True),  # 12
    RouletteNumber(13, True, False, False, True, False, True, False, True, False, True, False, False),  # 13
    RouletteNumber(14, True, False, True, False, True, False, False, True, False, False, True, False),  # 14
    RouletteNumber(15, True, False, False, True, False, True, False, True, False, False, False, True),  # 15
    RouletteNumber(16, True, False, True, False, True, False, False, True, False, True, False, False),  # 16
    RouletteNumber(17, True, False, False, True, False, True, False, True, False, False, True, False),  # 17
    RouletteNumber(18, True, False, True, False, True, False, False, True, False, False, False, True),  # 18
    RouletteNumber(19, False, True, False, True, True, False, False, True, False, True, False, False),  # 19
    RouletteNumber(20, False, True, True, False, False, True, False, True, False, False, True, False),  # 20
    RouletteNumber(21, False, True, False, True, True, False, False, True, False, False, False, True),  # 21
    RouletteNumber(22, False, True, True, False, False, True, False, True, False, True, False, False),  # 22
    RouletteNumber(23, False, True, False, True, True, False, False, True, False, False, True, False),  # 23
    RouletteNumber(24, False, True, True, False, False, True, False, True, False, False, False, True),  # 24
    RouletteNumber(25, False, True, False, True, True, False, False, False, True, True, False, False),  # 25
    RouletteNumber(26, False, True, True, False, False, True, False, False, True, False, True, False),  # 26
    RouletteNumber(27, False, True, False, True, True, False, False, False, True, False, False, True),  # 27
    RouletteNumber(28, False, True, True, False, False, True, False, False, True, True, False, False),  # 28
    RouletteNumber(29, False, True, False, True, False, True, False, False, True, False, True, False),  # 29
    RouletteNumber(30, False, True, True, False, True, False, False, False, True, False, False, True),  # 30
    RouletteNumber(31, False, True, False, True, False, True, False, False, True, True, False, False),  # 31
    RouletteNumber(32, False, True, True, False, True, False, False, False, True, False, True, False),  # 32
    RouletteNumber(33, False, True, False, True, False, True, False, False, True, False, False, True),  # 33
    RouletteNumber(34, False, True, True, False, True, False, False, False, True, True, False, False),  # 34
    RouletteNumber(35, False, True, False, True, False, True, False, False, True, False, True, False),  # 35
    RouletteNumber(36, False, True, True, False, True, False, False, False, True, False, False, True))  # 36

# count_true = 0
# count_false = 0
# for num in numbers:
#     num_temp = num.second_column
#     if num_temp is True:
#         count_true += 1
#     if num_temp is False:
#         count_false += 1
#
# print(count_true, count_false)


# def first_second_dozen(number):
#     if (number.first_dozen or number.second_dozen) is True:
#         return 25
#     else:
#         return -50
#
#
# count = 0
#
# for _ in range(100):
#     random_number = random.choice(numbers)
#     count += first_second_dozen(random_number)
#
#     print(str(_ + 1) + ':', str(random_number.name) + '\t', count)
#
# print('\nResult:', count)


number_list = [random.choice(numbers) for _ in range(100)]
count = 0

for i in range(len(number_list)):
    if (number_list[i].first_dozen or number_list[i].second_dozen) is True:
        count += 25
    else:
        count -= 50

    print(str(i + 1) + ':', str(number_list[i].name)+'\t',count)

print('\nResult:', count)
