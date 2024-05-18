import os
import matplotlib.pyplot as plt
from make_liniar_graph import create_liniar_graph



def main():
    path_to_files = os.path.dirname(os.path.abspath(__file__))
    create_liniar_graph(f"{path_to_files}/proceed_data/external_sort_1.txt")
if __name__ == "__main__":
    main()
