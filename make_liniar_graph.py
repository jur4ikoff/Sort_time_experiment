import os
import matplotlib.pyplot as plt


def create_liniar_graph(path_to_file):
    times, sizes = [], []
    with open(path_to_file, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip().split()
            sizes.append(int(line[0]))
            times.append(float(line[1]))

    name = os.path.basename(path_to_file).split(".")[0]

    # Построение линейно-кусочного графика
    plt.subplots()
    plt.plot(sizes, times, "o-")
    plt.xticks(sizes[::2] + [sizes[-1]])
    plt.xlabel("Размер")
    plt.ylabel("Время")
    plt.title(f"График зависимости размера от времени сортировки {name}")
    plt.grid(True)
    # plt.show()

    plt.savefig(f"./charts/liniar_{name}.svg", format="svg")


# plt.savefig(f'linear_{s}.svg', format='svg')
