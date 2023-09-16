# 1. Написать функцию для определения количества гласных и согласных
# в строке. – 2 балла
def vowels_and_consonants(s):
    try:
        vowels = "AEIOUYАУОЫЭЯЮЁИЕ"
        count_vowels = 0
        consonants = "BCDFGHJKlMNPQRSTVWXYZБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
        count_consonants = 0
        s = s.upper()
        for i in range(0, len(s)):
            if s[i] in vowels:
                count_vowels += 1
            elif s[i] in consonants:
                count_consonants += 1
    except ValueError:
        return False
    else:
        print("Гласные = {}" .format(count_vowels))
        print("Соласные = {}".format(count_consonants))
    finally:
        print("\nВыход из программы")


def main():
    s1 = input("Введите строку: ")
    vowels_and_consonants(s1)


if __name__ == "__main__":
    main()
