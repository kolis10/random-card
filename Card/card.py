import random

symbols = ['\u2660','\u2663','\u2665','\u2666']
numbers = ['A',2,3,4,5,6,7,8,9,'J','Q','K']

random_symbol = random.choice(symbols)
random_numbers = random.choice(numbers)
print(random_symbol, random_numbers)