# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

def main():
    l = [x for x in range(101)]
    l += l[::-1]
    print(l)
    return 0


if __name__ == "__main__":
    main()