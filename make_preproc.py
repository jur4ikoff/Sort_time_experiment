import os
import statistics

"""подготовка данных из набора, провести первичный анализ: посчитать среднее арифметическое, медианное,
найти максимум и минимум, вычислить нижний и верхний квартили, etc."""


def strcspn(string, characters):
    """
    Возвращает длину начального сегмента строки string,
    который не содержит ни одного символа из строки characters.
    """
    count = 0
    for char in string:
        if char in characters:
            return count
        count += 1
    return count


def extract_file_size(input_string):
    # Получение длины массива из названия файла
    number = "".join(filter(str.isdigit, input_string))
    return int(number[:-1])


def calc_rse(time_array, count):
    # Подсчет RSE
    t_avg = sum(time_array) / count
    dispersion = 0
    for i in range(count):
        dispersion += (time_array[i] - t_avg) ** 2

    dispersion /= count - 1
    standard_deviation = dispersion**0.5
    std_error = standard_deviation / count**0.5
    rse = std_error * 100 / t_avg
    return rse


def collect_data(file):
    """Функция для сбора данных из файла"""
    count = 0
    data = []
    if not (os.path.exists(file)):
        return data, count
    with open(file, mode="r") as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            count += 1
            data.append(float(line))

    return data, count


def make_file_unique(filename):
    # Удаление дубликатов из файла
    with open(filename, "r") as file:
        lines = file.readlines()

    unique_lines = set(lines)

    with open(filename, "w") as file:
        for line in unique_lines:
            file.write(line)


# Получение путя к файлам и названий файлов
path_to_files = os.path.dirname(os.path.abspath(__file__)) + "/data/"
files = os.listdir(path_to_files)

if not (os.path.exists(f"{path_to_files}/sort_data/")):
    os.mkdir(f"{path_to_files}/sort_data/")

# Перебираем все файлы в папке data
for file in files:
    if not file.endswith(".txt"):
        continue

    size = extract_file_size(file)
    experiment = strcspn(file, "_")
    stats_filename = file[:experiment] + "_" + file[experiment + 2 + len(str(size)) :]

    # Получение массива времени
    data, count = collect_data(path_to_files + file)

    # Сбор статистики
    average = statistics.mean(data)
    median = statistics.median(data)
    max_value = max(data)
    min_value = min(data)
    data.sort()
    if count % 2 == 0:
        q1 = statistics.median(data[: (count // 2)])
        q3 = statistics.median(data[(count // 2) :])
    else:
        q1 = statistics.median(data[: (count // 2)])
        q3 = statistics.median(data[(count // 2) + 1 :])

    # Запись статистики в файл
    output_file = path_to_files + "sort_data/" + stats_filename
    string_to_output = f"{size} {average} {median} {min_value} {max_value} {q1} {q3}\n"

    with open(output_file, "a+") as f:
        f.write(string_to_output)  # Добавляем статистику в конец файла

    make_file_unique(output_file)
