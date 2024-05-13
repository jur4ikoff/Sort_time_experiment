"""Файл с полезными функциями"""


def get_steps(end=10000, step=500):
    """Функция для получения шагов разбиения в удобном формате"""
    for i in range(step, end + 1, step):
        print(i, end=' ')


def main():
    get_steps(int(input("Введите размер массива: ")),
              int(input("Введите шаг разбиения массива: ")))


main()
