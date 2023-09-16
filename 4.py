# 4. Напишите программу, демонстрирующую работу try\except\finally– 2
# балла
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def try_except_finally(num, driver):
    try:
        num = num / driver
        return num
    except ZeroDivisionError:
        num = None
        return None
    finally:
        print("\nnum = {}" .format(num))


def main():
    num = input("num = ")
    if isint(num):
        divider = input("divider: ")
        if isint(divider):
            num = int(num)
            divider = int(divider)
            try_except_finally(num, divider)
        else:
            print("Введите целое число\n")
            main()
    else:
        print("Введите целое число\n")
        main()


if __name__ == "__main__":
    main()