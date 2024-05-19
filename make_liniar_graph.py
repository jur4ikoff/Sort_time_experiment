import os
import matplotlib.pyplot as plt

def create_liniar_graph(path_to_file, calculate_method):
    plt.figure()
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

            plt.plot(sizes, times, marker="o", linewidth=1, markersize=4)
            plt.xticks(sizes[::2])
            plt.xlabel("Размер сортируемого массива")
            plt.ylabel("Время в наносекундах")
            plt.title(f"График зависимости размера от времени. Метод измерения: {calculate_method}")
            plt.grid(True)
            plt.legend(to_legend)
    # plt.show()

    plt.savefig(f"./charts/liniar_{calculate_method}.svg", format="svg")
    plt.plot()
