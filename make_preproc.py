import os
import statistics

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


def calc_rse(time_array, count):
    t_avg = sum(time_array) / count
    dispersion = 0
    for i in range(count):
        dispersion += (time_array[i] - t_avg) ** 2

    dispersion /= count - 1
    standard_deviation = dispersion**0.5
    std_error = standard_deviation / count**0.5
    rse = std_error * 100 / t_avg
    return rse


def check_is_data_unique(f, data: str):
    while True:
        line = f.readline()
        if not line:
            break
        if line == data:
            return False
    return True


def collect_data(file):
    count = 0
    data = []
    if not (os.path.exists(f"{path_to_files}/{file}")):
        return None, None
    with open(file, mode="r") as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            count += 1
            data.append(float(line))

    return data, count


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

    output_file = path_to_files + "sort_data/" + stats_filename
    cur_data, count = collect_data(output_file)
    string_to_output = f"{size} {average} {median} {min_value} {max_value} {q1} {q3}"
    if cur_data and string_to_output not in cur_data:
        with open(output_file, "a") as f:
            f.read(string_to_output)

    # Для таблицы
    # rse = calc_rse(data, count)
    # print(average, median, min_value, max_value, q1, q3, rse)
    break
