import random

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
d = random.randint(1, 10)
e = random.randint(1, 10)
print('a:{}, b:{}, c:{}, d:{}, e:{}'.format(a, b, c, d, e))
if any(i for i in [a, b] if i in [1, 2, 3]):
    # for i in (i for i in [a, b] if i in [1, 2, 3]):
    print(True)

# print('a: {}\n'
#       'b: {}\n'
#       'c: {}\n'
#       'd: {}\n'
#       'e: {}\n'.format(a, b, c, d, e))
