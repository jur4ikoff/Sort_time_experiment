import os
import matplotlib.pyplot as plt
from make_liniar_graph import create_liniar_graph

path_to_files = os.path.dirname(os.path.abspath(__file__))
if not (os.path.exists(f"{path_to_files}/charts/")):
    os.mkdir(f"{path_to_files}/charts/")

files = os.listdir(path_to_files + "/proceed_data/")

for file in files:
    # print(file)
    create_liniar_graph(f"{path_to_files}/proceed_data/{file}")