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
        if type(test_dict) == dict:
            return True
    except (TypeError, ValueError):
        return False
    else:
        return False


def islist(test_list):
    try:
        list(test_list)
        if type(test_list) == list:
            return True
    except (TypeError, ValueError):
        return False
    else:
        return False


def isint(s):
    try:
        int(s)
        if type(s) == int:
            return True
    except (ValueError, TypeError):
        return False
    else:
        return False


def isstr(s):
    try:
        str(s)
        if type(s) == str:
            return True
    except (TypeError, ValueError):
        return False
    else:
        return False


def function(argument):
    if isdict(argument):
        try:
            print("Исходный словарь: {}" .format(argument))
            Output = []
            value = sorted(argument.values())
            value = value[len(value) - 3: len(value)]
            for i in value:
                for k, v in argument.items():
                    if i == v:
                        Output.append(k)
                        del argument[k]
                        break
            print("Ключи с наибольшими значениями: ", Output)
            return Output
        except ValueError:
            return None
        finally:
            end()
    elif islist(argument):
        try:
            print("Исходный список: {}" .format(argument))
            count_chet = 0
            for i in argument:
                if i % 2 == 0 and i != 0:
                    count_chet += 1
            i = 0
            while i < len(argument):
                if argument[i] in argument[i + 1: len(argument)]:
                    del argument[i]
                i += 1
            print("Список без повторяющихся элементов: {}"  .format(argument),
                  "\nКоличество четных элементов из исходного списка: {}" .format(count_chet))
            count_chet = 0
            for i in argument:
                if i % 2 == 0 and i != 0:
                    count_chet += 1
            print("Количество четных элементов из списка после удаления: ", count_chet)
            return argument
        except ValueError:
            return None
        finally:
            end()
    elif isint(argument):
        try:
            print("Число: {}".format(argument))
            argument = str(argument)
            sum = 0
            for i in argument:
                sum += int(i)
            print("Сумма цифр числа: {}" .format(sum))
        except TypeError:
            return None
        finally:
            end()
    elif isstr(argument):
        try:
            print("Искомая строка: {}" .format(argument))
            i = 0
            while i < len(argument):
                if i == 0 and argument[i] == ' ':
                    argument = argument[1:]
                    continue
                break
            argument = argument.replace("  ", " ")
            argument = argument.replace(",,", ",")
            argument = argument.replace("!!", "!")
            argument = argument.replace("@@", "@")
            argument = argument.replace("##", "#")
            argument = argument.replace("$$", "$")
            argument = argument.replace("^^", "^")
            argument = argument.replace("--", "-")
            argument = argument.replace("..", ".")
            argument = argument.replace(";;", ";")
            print("Строка после удаления лишних символов: ", argument)
        except ValueError:
            return None
        finally:
            end()


if __name__ == "__main__":
    function("safkamfklaf,, asfkaf.. asfjsalfk, aofk!! wqplfqfq fqf,,,,,,,,,weqwe")
