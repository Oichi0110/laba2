# Напишите функцию, которая будет принимать один аргумент. Если в
# функцию передаётся словарь, Найдите три ключа с самыми большими
# значениями в словаре
# Если список, найти количество четных чисел. Удалить все
# повторяющиеся элементы.
# Число – найти сумму цифр.
# Строка – убрать лишние символы. Вывести количество слов.
# Сделать проверку со всеми этими случаями. – 4 балла
def end():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣶⣄⠀⠀⠀⠀⠀⢀⠀⠀⣠⢞⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣏⠙⠲⣤⣴⡒⣿⠛⠻⣧⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⡴⢉⣿⠀⠀⣷⣄⡈⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠
⠀⠀⠉⠓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣼⢻⣧⡀⢹⣿⣿⡆⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠂⠁⠀
⠀⠀⠀⠀⠀⠀⠉⠓⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⣴⠛⠻⣿⣿⠿⣿⠀⠱⣤⣸⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠊⠀⠀⠀⠀⠀
⢦⡀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⢻⣦⣼⣈⣁⣀⣈⣻⡤⠿⣿⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⢠
⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⣿⣽⡛⠿⠷⡛⣁⣷⣼⡿⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁
⠀⠀⠈⠳⢤⣀⡀⠀⠀⣀⡼⠻⣄⠀⠀⠙⠲⣄⠀⠀⠀⠀⠀⣠⠿⡿⠿⠿⠿⠿⢷⠀⠸⠿⠛⠛⠛⠓⣲⠾⢧⠀⠀⠀⠀⠀⠀⢀⡴⠞⠁⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠹⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠑⢦⡀⢠⡞⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠺⠷⡄⠀⢀⡤⠞⠉⠀⠀⠀⠀⠉⠙⠷⢦⣤⣤⡤⠶⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢾⡀⠀⠀⠀⠀⠀⠀⠀⢀⡄⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⢀⣠⠴⠋⠀⠀⠙⠲⢤⣄⣀⠀⢀⡴⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣾⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⣀⣤⠤⢤⣄⣀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠦⣄⣻⠁⠀⣼⠀⠀⢈⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⢠⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⢸⣿⡧⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣦⡿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⣠⡶⠋⠉⠀⠉⠳⣄⡀⠀⠀⠀⠀⠀⠀⢀⣠⡾⡛⣿⡿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⠒⠒⢒⡶⠛⠀⠀⠀⠀⠀⠀⠚⢿⡶⠶⠶⠶⠒⠚⠉⠈⠙⣿⣽⣿⠿⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)


def isdict(test_dict):
    try:
        test_dict = dict(test_dict)
        if type(test_dict) == dict:
            return True
    except (TypeError, ValueError):
        return False
    else:
        return False


def islist(test_list):
    try:
        if type(test_list) == list:
            return True
    except (TypeError, ValueError):
        return False
    else:
        return False


def isint(s):
    try:
        s = int(s)
        if type(s) == int:
            return True
    except (ValueError, TypeError):
        return False
    else:
        return False


def isstr(s):
    try:
        s = str(s)
        if type(s) == str:
            return True
    except (TypeError, ValueError):
        return False
    else:
        return False


def Init_Dict():
    while(True):
        quantity_elements = input("Введите количество элементов словаря: ")
        if isint(quantity_elements):
            quantity_elements = int(quantity_elements)
            if quantity_elements > 3:
                test_dict = {}
                Keys = []
                i = 0
                while i < quantity_elements:
                    print("Введите {} ключ" .format(i))
                    key = input()
                    if key in Keys:
                        print("Такой ключ уже есть в словаре")
                        continue
                    print("Введите {} значение".format(i))
                    value = input()
                    if isint(value):
                        value = int(value)
                        Keys.append(key)
                        test_dict[key] = value
                    else:
                        continue
                    i = i + 1
                return test_dict
            else:
                print("Должно быть минимум 3 элемента")
        else:
            print("Введите целое число")


def Init_List():
    while (True):
        quantity_elements = input("Введите количество элементов списка: ")
        if isint(quantity_elements):
            quantity_elements = int(quantity_elements)
            if quantity_elements > 0:
                i = 0
                test_list = []
                while i < quantity_elements:
                    print("Введите {} элемент".format(i))
                    element = input()
                    if isint(element):
                        element = int(element)
                        test_list.append(element)
                    else:
                        print("Введите целый тип данных")
                        continue
                    i = i + 1
                return test_list
            else:
                print("Введите больше 0 элементов")
        else:
            print("Введите целый тип данных")


def InitInt():
    while(True):
        test_int = input("Введите число: ")
        if isint(test_int):
            test_int = int(test_int)
            if test_int >= 0:
                return test_int
            else:
                print("Отрицательное число")
        else:
            print("Введите целое число")


def function(argument):
    if isdict(argument):
        try:
            print("Исходный словарь: \033[32m{}\033[0m" .format(argument))
            Output = []
            value = sorted(argument.values())
            value = value[len(value) - 3: len(value)]
            for i in value:
                for k, v in argument.items():
                    if i == v:
                        Output.append(k)
                        del argument[k]
                        break
            print("Ключи с наибольшими значениями: \033[32m{}\033[0m" .format(Output))
            return Output
        except (ValueError, TypeError):
            return None
        finally:
            end()
    elif islist(argument):
        try:
            print("Исходный список: \033[32m{}\033[0m" .format(argument))
            count_chet = 0
            for i in argument:
                if i % 2 == 0 and i != 0:
                    count_chet += 1
            i = 0
            while i < len(argument):
                if argument[i] in argument[i + 1: len(argument)]:
                    del argument[i]
                i += 1
            print("Список без повторяющихся элементов: \033[32m{}\033[0m"  .format(argument),
                  "\nКоличество четных элементов из исходного списка: \033[32m{}\033[0m" .format(count_chet))
            count_chet = 0
            for i in argument:
                if i % 2 == 0 and i != 0:
                    count_chet += 1
            print("Количество четных элементов из списка после удаления: \033[32m{}\033[0m" .format(count_chet))
            return argument
        except (ValueError, TypeError):
            return None
        finally:
            end()
    elif isint(argument):
        try:
            print("Число: \033[32m{}\033[0m".format(argument))
            argument = str(argument)
            sum = 0
            for i in argument:
                sum += int(i)
            print("Сумма цифр числа: \033[32m{}\033[0m" .format(sum))
        except (ValueError, TypeError):
            return None
        finally:
            end()
    elif isstr(argument):
        try:
            print("Искомая строка: \033[32m{}\033[0m" .format(argument))
            i = 0
            while i < len(argument):
                if i == 0 and argument[i] == ' ':
                    argument = argument[1:]
                    continue
                if not argument[i].isalnum() or argument[i].isspace():
                    if argument[i] == " " and not argument[i + 1] == " ":
                        i = i + 1
                        continue
                    else:
                        argument = argument[: i] + argument[i + 1:]
                        continue
                i = i + 1
            quantity_word = len(argument.split())
            print("Строка после удаления лишних символов: \033[32m{}\033[0m" .format(argument),
                  "\nКоличество слов в строке: {}" .format(quantity_word))
        except (ValueError, TypeError, IndexError):
            return None
        finally:
            end()


def menu():
    print("\033[31mМеню\033[0m".center(45), "\n\033[31m1.\033[0m \033[33mСловарь\033[0m\n\033[31m2.\033[0m "
                                            "\033[33mСписок\033[0m\n\033[31m3.\033[0m \033[33mЧисло\033[0m\n"
                                            "\033[31m4.\033[0m \033[33mСтрока\033[0m\n\033[31m5. \033[0m"
                                            "\033[33mВыход\033[0m")
    choice = input("\033[31mВвод:\033[0m ")
    if isint(choice):
        choice = int(choice)
        if choice == 1:
            new_dict = Init_Dict()
            function(new_dict)
            menu()
        if choice == 2:
            new_list = Init_List()
            function(new_list)
            menu()
        if choice == 3:
            new_int = InitInt()
            function(new_int)
            menu()
        if choice == 4:
            new_str = input("Введите строку: ")
            function(new_str)
            menu()
        if choice == 5:
            exit()
    else:
        print("Введите целый тип данных")
        menu()


if __name__ == "__main__":
    menu()
