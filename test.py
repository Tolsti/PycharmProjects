import re

arr = '//облоко'

if '//' in re.findall('\S\S', arr):
    print(re.findall(r'\w+',arr))
else:
    print(False)

print("Test")

# print(re.search('//',arr))
# print(re.search('\S\S', arr))
