import os
import matplotlib.pyplot as plt
from make_charts import (
    create_liniar_graph,
    create_liniar_graph_with_error,
    create_moustache_graph,
)


def main():
    path_to_files = os.path.dirname(os.path.abspath(__file__))
    if not (os.path.exists(f"{path_to_files}/charts/")):
        os.mkdir(f"{path_to_files}/charts/")

    files = os.listdir(path_to_files + "/proceed_data/")
    create_liniar_graph(f"{path_to_files}/proceed_data/", "internal")
    create_liniar_graph(f"{path_to_files}/proceed_data/", "external")

    for file in files:
        full_path = f"{path_to_files}/proceed_data/{file}"
        create_liniar_graph_with_error(full_path)

    for file in files:
        full_path = f"{path_to_files}/proceed_data/{file}"
        create_moustache_graph(full_path)


if __name__ == "__main__":
    main()
