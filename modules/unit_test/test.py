import sys
from collections import Counter, defaultdict, OrderedDict
import datetime
import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(3, 'abcd')

print(datetime.date.today())

li = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7]
sentence = 'elif seven asdfg kjakana'
print(Counter(li)),
print(Counter(sentence))

# dictionary = {'a':1, 'b':2}
# print(dictionary['c'])

dictionary = defaultdict(lambda: 'does not exist!', {'a': 1, 'b': 2})
print(dictionary['c'])

# print(sys)

# print(dir(sys))

try:
    with open('./test.txt', mode='r') as my_file:
        print(my_file.read())
except:
    print('check your file path')
