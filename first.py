# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

def main():
    t = (1, 2.0, True, "Something", [1, 2, 3], (1, 2, 3), {1: 2})

    d = {type(x): x for x in t}
    for i, j in d.items():
        print(f"{i}: {j}")

    h = (1, 2, 3, 2.0, 3.0, True, "Something", "Nothing", False)

    set_of_types = (type(x) for x in h)

    d_2 = {x: [] for x in set_of_types}

    temp = []

    for x in h:
        temp = d_2.get(type(x))
        temp.append(x)

    for i, j in d_2.items():
        print(f"{i}: {j}")

    return 0


if __name__ == "__main__":
    main()
