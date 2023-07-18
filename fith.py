# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.
import itertools


# Backpack can have up to 25 kg of items in it.
_backpack = 25
# Items that friends can take.
_things = {"canteen": 0.6, "fire starter": 0.3, "MRE": 8, "Sleeping-bag": 3, "water bottles": 4, "sweets": 3,
           "water-purifier tablet": 0.5, "tent": 12, "map": 0.1, "compass": 0.4, "satellite phone": 1.5, "pot": 5}

count = 0

for i in range(12):
    for j in itertools.permutations(_things.values(), i):
        for k in j:
            count += k
        if 20 <= count <= 25:
            print(f"{j} : {count} kg")
            count = 0
        else:
            count = 0
