from itertools import permutations


def search_wow(set_word):
    set_word.lower()
    all_combinations = list()
    found_words = list()
    count = len(set_word)
    while count >= 3:
        for i in permutations(set_word, count):
            all_combinations.append(''.join(i))
        count -= 1
    file = open('TMP.txt').read().splitlines()
    for i in file:
        if i in all_combinations:
            found_words.append(i)
    return found_words


print(search_wow('облоко'))
