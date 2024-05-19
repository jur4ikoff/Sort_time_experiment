import os
import matplotlib.pyplot as plt


def create_liniar_graph(path_to_file, calculate_method):
    plt.figure(figsize=(20, 10))
    # os.path добавляет путь к месту, откуда запущена программа
    # files = [os.path.abspath(f"proceed_data/{file}") for file in files]
    files = os.listdir(path_to_file)
    # print(files)
    to_legend = []
    for basename in files:
        if not basename.startswith(calculate_method):
            continue
        file = os.path.abspath(f"proceed_data/{basename}")
        times, sizes = [], []
        to_legend.append(basename)

        with open(file, "r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip().split()
                sizes.append(int(line[0]))
                times.append(float(line[1]))

                # name = os.path.basename(file).split(".")[0]

            # Построение линейно-кусочного графика
            # plt.subplots()
            data = [sizes, times]
            plt.plot(sizes, times, marker="o", linewidth=1, markersize=4)
            plt.xticks(sizes[::2])
            plt.xlabel("Размер сортируемого массива")
            plt.ylabel("Время в наносекундах")
            plt.title(
                f"График зависимости размера от времени. Метод измерения: {calculate_method}"
            )
            plt.grid(True)
            plt.legend(to_legend)
    # plt.show()

    plt.savefig(f"./charts/liniar_{calculate_method}.svg", format="svg")


def create_liniar_graph_with_error(path_to_file):
    plt.figure(figsize=(20, 10))
    times, sizes, mins, maxs = [], [], [], []

    with open(path_to_file, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip().split()
            sizes.append(int(line[0]))
            times.append(float(line[1]))
            mins.append(float(line[3]))
            maxs.append(float(line[4]))

        # Построение линейно-кусочного графика
        # plt.subplots()
        name = os.path.basename(path_to_file).split(".")[0]
        plt.plot(sizes, times, marker="o", linewidth=1, markersize=4)
        plt.plot(sizes, mins, marker="o", linewidth=1, markersize=4)
        plt.plot(sizes, maxs, marker="o", linewidth=1, markersize=4)
        plt.xticks(sizes[::2])
        plt.xlabel("Размер сортируемого массива")
        plt.ylabel("Время в наносекундах")
        plt.title(f"График с ошибкой. Метод измерения: {name}")
        plt.grid(True)
        plt.legend(["time", "min", "max"])
        plt.savefig(f"./charts/line_error_{name}.svg", format="svg")


def create_moustache_graph(path_to_file):
    plt.figure(figsize=(20, 10))

    with open(path_to_file, "r") as file:
        sizes, times = [], []
        for line in file:
            values = [float(value) for value in line.strip().split()]
            size = values[0]
            time, median, min_value, max_value, q1, q3 = values[1:]

            sizes.append(size)
            times.append(time)

            plt.vlines(size, min_value, max_value, colors='blue', linewidth=1)
            # plt.scatter(size, time, marker='o', s=6)
            plt.li(size, max_value, color='blue', marker='*', s=2)
            plt.scatter(size, min_value, color='blue', marker='*', s=2)
            plt.scatter(size, q1, color='orange', marker='o', s=2)
            plt.scatter(size, median, color='orange', marker='o', s=2)
            plt.scatter(size, q3, color='orange', marker='o', s=2)

        plt.plot(sizes, times, label='avg_time', color='blue', linewidth=1, marker='o', markersize=1)

    plt.yticks(times)
    plt.xticks(sizes)
    plt.title(f"График с усами")
    plt.xlabel("Размер сортируемого массива")
    plt.ylabel("Время в наносекундах")
    plt.grid(True)
    plt.legend(['size', 'median', 'q1', 'q3', 'min', 'max'])
    plt.savefig(f"./charts/moustache_{os.path.basename(path_to_file)}.svg", format="svg")
