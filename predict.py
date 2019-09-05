import sys
import pickle
import numpy as np
from ann import PQModelANN
from load_normalize import *
from surface_generation import generate_surface, postprocess

p = PQModelANN()


def predict(path):
    audio = load(path)
    pitch_profile = get_pitch_profile(audio)
    tonic = tonic_lead_artist(audio)
    normalized_p = normalize(pitch_profile, tonic)
    surface = generate_surface(normalized_p, 120, 100)
    surface = postprocess(surface)
    surface = surface.ravel()
    p.load("")
    index_dump = pickle.load(open("index_dump.pickle", "rb"))
    nearest = [index_dump[i].ragam for i in p.predict(np.float32(surface), top_n=3)]
    print(nearest)


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        print(predict(path))
    except IndexError:
        exit()

