import os
import shutil
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")


# Функция создает линейные графики
def create_liniar_graph(path_to_file, calculate_method):
    plt.figure(figsize=(20, 10))

    files = os.listdir(path_to_file)
    to_legend = []
    for basename in files:
        if not basename.startswith(calculate_method):
            continue
        file = os.path.abspath(f"proceed_data/{basename}")
        times, sizes = [], []
        if "sort_1" in basename:
            to_legend.append("Сортировка с индексами")
        elif "sort_2" in basename:
            to_legend.append("Сортировка с формальной заменой")
        elif "sort_3" in basename:
            to_legend.append("Сортировка с указателями")

        with open(file, "r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip().split()
                sizes.append(int(line[0]))
                times.append(float(line[1]))

            # Построение линейно-кусочного графика
            # plt.subplots()
            data = [sizes, times]
            plt.plot(sizes, times, marker="o", linewidth=1, markersize=4)
            plt.xticks(sizes)
            plt.xlabel("Размер сортируемого массива")
            plt.ylabel("Время в наносекундах")
            plt.title(
                f"График зависимости размера от времени. Метод измерения: {calculate_method}"
            )
            plt.grid(True)
            plt.legend(to_legend)

    plt.savefig(f"./charts/liniar_{calculate_method}.svg", format="svg")


# Построение графика с ошибкой
def create_liniar_graph_with_error(path_to_file):
    plt.figure(figsize=(20, 10))
    times, sizes, mins, maxs = [], [], [], []
    with open(path_to_file, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip().split()
            # Заглушка, чтобы график получился "ровным"
            sizes.append(int(line[0]))
            times.append(float(line[1]))
            mins.append(float(line[3]))
            maxs.append(float(line[4]))

        # Построение линейно-кусочного графика
        name = os.path.basename(path_to_file).split(".")[0]
        plt.plot(sizes, times, marker="o", linewidth=1, markersize=3)

        plt.vlines(sizes, mins, maxs, colors="orange", linewidth=2)
        plt.scatter(sizes, maxs, color="red", marker="*", s=5)
        plt.scatter(sizes, mins, color="green", marker="*", s=5)

        calculate_method = name[:8]
        if "sort_1" in name:
            sort_method = "индексация"
        elif "sort_2" in name:
            sort_method = "Формальная замена"
        elif "sort_3" in name:
            sort_method = "Указатели"

        plt.title(
            f"График с ошибкой. Метод измерения: {calculate_method} {sort_method}"
        )
        plt.xticks(sizes)
        plt.xlabel("Размер сортируемого массива")
        plt.ylabel("Время в наносекундах")
        plt.grid(True)
        plt.legend(["time", "max", "min"])

        plt.savefig(f"./charts/line_error_{name}.svg", format="svg")


def create_moustache_graph(path_to_file):
    plt.figure(figsize=(14, 20))
    df = []
    sizes = []
    means = []
    with open(path_to_file, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.strip().split()
            size = int(line[0])

            mean, median, min_value, max_value, q1, q3 = (
                float(line[1]),
                float(line[2]),
                float(line[3]),
                float(line[4]),
                float(line[5]),
                float(line[6]),
            )
            if size > 10000:
                break
            sizes.append(size)
            means.append(mean)
            df.append([min_value, q1, median, q3, max_value])

        plt.boxplot(
            df,
            positions=sizes,
            widths=300,
            whis=10**6,
            manage_ticks=False,
        )

        name = os.path.basename(path_to_file).split(".")[0]
        calculate_method = name[:8]
        if "sort_1" in name:
            sort_method = "индексация"
        elif "sort_2" in name:
            sort_method = "Формальная замена"
        elif "sort_3" in name:
            sort_method = "Указатели"

        plt.plot(sizes, means, color="blue")
        plt.xticks(sizes)
        plt.yticks(means)
        plt.xlabel("Размер сортируемого массива")
        plt.ylabel("Время в наносекундах")
        plt.grid(True)
        plt.title(
            f"График с усами. Метод измерения {calculate_method}, сортировка {sort_method}"
        )
        plt.savefig(
            f"./charts/moustache_{os.path.basename(path_to_file)}.svg", format="svg"
        )


def main(path_to_files):
    if not (os.path.exists(f"{path_to_files}/charts/")):
        os.mkdir(f"{path_to_files}/charts/")
    else:
        shutil.rmtree(f"{path_to_files}/charts/")
        os.mkdir(f"{path_to_files}/charts/")

    files = os.listdir(path_to_files + "/proceed_data/")
    create_liniar_graph(f"{path_to_files}/proceed_data/", "internal")
    create_liniar_graph(f"{path_to_files}/proceed_data/", "external")
    create_liniar_graph(f"{path_to_files}/proceed_data/", "ticks")

    for file in files:
        if "ticks" in file:
            continue
        full_path = f"{path_to_files}/proceed_data/{file}"
        create_liniar_graph_with_error(full_path)

    for file in files:
        if "ticks" in file:
            continue
        full_path = f"{path_to_files}/proceed_data/{file}"
        create_moustache_graph(full_path)


if __name__ == "__main__":
    path_to_files = os.path.dirname(os.path.abspath(__file__))
    main(path_to_files)
