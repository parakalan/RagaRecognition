from ann import PQModelANN
from csong import CarnaticSong
from
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

pq = PQModelANN(indexed_data=surfaces.keys())
pq.fit(surfaces.values())
pq.dump()
pq.predict()

