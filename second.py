# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

def main():
    l = [x + 1 for x in range(101)]
    lst = l[::2] + l[::2] + l[::-3]
    no_duplicates = set(lst)
    print(f"Origianl list:\n{lst}\nNo duplicates list:\n{list(no_duplicates)}")
    return 0


if __name__ == "__main__":
    main()
