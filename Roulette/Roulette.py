import random


class RouletteNumber:
    def __init__(self, name, low_bet, high_bet, even, odd, red, black,
                 first_dozen, second_dozen, third_dozen,
                 first_column, second_column, third_column,
                 tier):
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
        self.tier = tier
        # self.voisin
        # self.orphelin
        # self.zerospiel


numbers = (
    RouletteNumber(0, False, False, False, False, False, False, False, False, False, False, False, False, False),  # 0
    RouletteNumber(1, True, False, False, True, True, False, True, False, False, True, False, False, False),  # 1
    RouletteNumber(2, True, False, True, False, False, True, True, False, False, False, True, False, False),  # 2
    RouletteNumber(3, True, False, False, True, True, False, True, False, False, False, False, True, False),  # 3
    RouletteNumber(4, True, False, True, False, False, True, True, False, False, True, False, False, False),  # 4
    RouletteNumber(5, True, False, False, True, True, False, True, False, False, False, True, False, True),  # 5
    RouletteNumber(6, True, False, True, False, False, True, True, False, False, False, False, True, False),  # 6
    RouletteNumber(7, True, False, False, True, True, False, True, False, False, True, False, False, False),  # 7
    RouletteNumber(8, True, False, True, False, False, True, True, False, False, False, True, False, True),  # 8
    RouletteNumber(9, True, False, False, True, True, False, True, False, False, False, False, True, False),  # 9
    RouletteNumber(10, True, False, True, False, False, True, True, False, False, True, False, False, True),  # 10
    RouletteNumber(11, True, False, False, True, False, True, True, False, False, False, True, False, True),  # 11
    RouletteNumber(12, True, False, True, False, True, False, True, False, False, False, False, True, False),  # 12
    RouletteNumber(13, True, False, False, True, False, True, False, True, False, True, False, False, True),  # 13
    RouletteNumber(14, True, False, True, False, True, False, False, True, False, False, True, False, False),  # 14
    RouletteNumber(15, True, False, False, True, False, True, False, True, False, False, False, True, False),  # 15
    RouletteNumber(16, True, False, True, False, True, False, False, True, False, True, False, False, True),  # 16
    RouletteNumber(17, True, False, False, True, False, True, False, True, False, False, True, False, False),  # 17
    RouletteNumber(18, True, False, True, False, True, False, False, True, False, False, False, True, False),  # 18
    RouletteNumber(19, False, True, False, True, True, False, False, True, False, True, False, False, False),  # 19
    RouletteNumber(20, False, True, True, False, False, True, False, True, False, False, True, False, False),  # 20
    RouletteNumber(21, False, True, False, True, True, False, False, True, False, False, False, True, False),  # 21
    RouletteNumber(22, False, True, True, False, False, True, False, True, False, True, False, False, False),  # 22
    RouletteNumber(23, False, True, False, True, True, False, False, True, False, False, True, False, True),  # 23
    RouletteNumber(24, False, True, True, False, False, True, False, True, False, False, False, True, True),  # 24
    RouletteNumber(25, False, True, False, True, True, False, False, False, True, True, False, False, False),  # 25
    RouletteNumber(26, False, True, True, False, False, True, False, False, True, False, True, False, False),  # 26
    RouletteNumber(27, False, True, False, True, True, False, False, False, True, False, False, True, True),  # 27
    RouletteNumber(28, False, True, True, False, False, True, False, False, True, True, False, False, False),  # 28
    RouletteNumber(29, False, True, False, True, False, True, False, False, True, False, True, False, False),  # 29
    RouletteNumber(30, False, True, True, False, True, False, False, False, True, False, False, True, True),  # 30
    RouletteNumber(31, False, True, False, True, False, True, False, False, True, True, False, False, False),  # 31
    RouletteNumber(32, False, True, True, False, True, False, False, False, True, False, True, False, False),  # 32
    RouletteNumber(33, False, True, False, True, False, True, False, False, True, False, False, True, True),  # 33
    RouletteNumber(34, False, True, True, False, True, False, False, False, True, True, False, False, False),  # 34
    RouletteNumber(35, False, True, False, True, False, True, False, False, True, False, True, False, False),  # 35
    RouletteNumber(36, False, True, True, False, True, False, False, False, True, False, False, True, True))  # 36

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


number_list = [random.choice(numbers) for _ in range(1000000)]
result = 0
count = 0
flag = False
count_flag = 0

# for num in number_list:
#     count += 1
#
#     if num.tier is True:
#         if count_flag == 1:
#             result += 12
#         elif count_flag == 2:
#             result += 30
#         elif count_flag == 3:
#             result += 56
#         elif count_flag == 4:
#             result += 96
#
#         result += 24
#
#         count_flag = 0
#     else:
#         if count_flag == 1:
#             result -= 6
#         elif count_flag == 2:
#             result -= 15
#         elif count_flag == 3:
#             result -= 28
#         elif count_flag == 4:
#             result -= 48
#             count_flag = -1
#
#         result -= 12
#
#         count_flag += 1
#
#     # print(str(count) + ':', num.name, result)

for num in number_list:
    count += 1

    if num.name in [1]:
        result += 35
    else:
        result -= 1

    # print(str(count) + ':', num.name, result)

# for num in number_list:
#     count += 1
#     if flag is True:
#         flag = False
#         if (num.first_dozen or num.second_dozen) is True:
#             result += 75
#         else:
#             result -= 150
#     else:
#         if (num.first_dozen or num.second_dozen) is True:
#             result += 25
#         else:
#             flag = True
#             result -= 50
#
#     print(str(count) + ': ' + str(num.name) + '\t' + str(result))

# for i in range(len(number_list)):
#     if (number_list[i].first_dozen or number_list[i].second_dozen) is True:
#         result += 25
#     else:
#         result -= 50
#
#     print(str(i + 1) + ':', str(number_list[i].name)+'\t',count)


print('\nResult:', result)
