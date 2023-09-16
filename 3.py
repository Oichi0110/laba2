# Дана целочисленная прямоугольная матрица. Определить количество
# столбцов, не содержащих ни одного нулевого элемента. – 2 балла
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def matrix_0_element(massive, row, col):
    try:
        count = 0
        for j in range(0, col):
            for i in range(0, row):
                if massive[i][j] == 0:
                    count += 1
                    break
        count = col - count
    except ValueError:
        return None
    else:
        print("Столбцов без нулей: {}\n" .format(count))


def two_d_matrix(row, col):
    Output = []
    for i in range(row):
        row = []
        j = 0
        while j < col:
            num = input(f"Enter the matrix [{i}][{j}]: ")
            if isint(num):
                num = int(num)
                row.append(num)
                j += 1
            else:
                print("Введите целочисленный тип данных")
        Output.append(row)
    print("\n")
    for i in Output:
        for j in i:
            print(j, end=" ")
        print()
    return Output


def main():
    try:
        rows = input("\nСтроки = ")
        if isint(rows):
            columns = input("Столбцы = ")
            if isint(columns):
                rows = int(rows)
                columns = int(columns)
                if rows == columns:
                    print("Матрица должна быть прямоугольной")
                    main()
                arr = two_d_matrix(rows, columns)
                matrix_0_element(arr, rows, columns)
                exit()
            else:
                print("Введите целочисленный тип данных")
                main()
        else:
            print("Введите целочисленный тип данных")
            main()
    finally:
        print("Выход из программы")


if __name__ == "__main__":
    main()
