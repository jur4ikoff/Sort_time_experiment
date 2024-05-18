import os
import matplotlib.pyplot as plt


def create_liniar_graph(path_to_file):
    print(path_to_file)
    times, sizes = [], []
    with open(path_to_file, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip().split()
            sizes.append(int(line[0]))
            times.append(float(line[1]))

    sizes.sort()
    times.sort()

    # Построение линейно-кусочного графика
    plt.plot(sizes, times, "o-")
    plt.xlabel("Размер")
    plt.ylabel("Время")
    plt.title("График зависимости размера от времени")
    plt.grid(True)
    plt.show()
