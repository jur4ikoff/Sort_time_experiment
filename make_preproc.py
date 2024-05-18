import sys
import os
import statistics
import math

"""подготовка данных из набора, провести первичный анализ: посчитать среднее арифметическое, медианное,
найти максимум и минимум, вычислить нижний и верхний квартили, etc."""

path_to_files = os.path.dirname(os.path.abspath(__file__)) + "/data/"
files = os.listdir(path_to_files)

if not (os.path.exists(f"{path_to_files}/sort_data/")):
    os.mkdir(f"{path_to_files}/sort_data/")


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
    number = "".join(filter(str.isdigit, input_string))
    return int(number[:-1])


for file in files:
    if not file.endswith(".txt"):
        continue
    size = extract_file_size(file)
    experiment = strcspn(file, "_")
    stats_filename = file[:experiment] + "_" + \
        file[experiment + 2 + len(str(size)):]

    data = []
    count = 0
    with open(path_to_files + file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            count += 1
            data.append(float(line))

    # работа над файлом
    average = statistics.mean(data)
    median = statistics.median(data)
    max_value = max(data)
    min_value = min(data)
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    count = len(data)

    if count % 2 == 0:
        q1 = statistics.median(data[: (count // 2)])
        q3 = statistics.median(data[(count // 2):])
    else:
        q1 = statistics.median(data[: (count // 2)])
        q3 = statistics.median(data[(count // 2) + 1:])
    # q1 = statistics.median(data[: (count // 2)])
    # q3 = statistics.median(data[(count // 2):])

    # with open("path_to_files + "sort_data/" + stats_filename, "a") as f:
    #    pass
    # f.read(f"{size} {average} {median} {min_value} {max_value} {q1} {q3}")

    print(average, median, min_value, max_value, q1, q3)
    break
