import random

Words = ['Life', 'Rain', 'Earth', 'Land', 'Fire']

while True:
    Random = random.randint(0, len(Words) - 1)
    Random2 = random.randint(0, len(Words) - 1)
    SumOfThings = input(f"{Words[Random]} + {Words[Random2]} = ? ")
    Words.append(SumOfThings)
    continue
