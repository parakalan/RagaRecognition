from ann import PQModelANN
import os
import numpy as np


def load_surfaces():
    files = os.listdir("surfaces/")
    surfaces = {}
    for file in files:
        sf = np.load("surfaces/" + file)
        surfaces[file] = sf.ravel()
    return surfaces


surfaces = load_surfaces()

pq = PQModelANN(indexed_data=list(surfaces.keys()))
x = list(surfaces.values())
pq.fit(x)
pq.dump("")

