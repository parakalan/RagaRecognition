import sys
import pickle
import operator
import numpy as np
from ann import PQModelANN
from load_normalize import *
from surface_generation import generate_surface, postprocess

p = PQModelANN()

TEN_MINUTES = 620 * 44100


def predict(path, top_n):
    audio = load(path)
    if len(audio) > TEN_MINUTES:
        mid = len(audio) // 2
        audio = audio[mid - TEN_MINUTES//2: mid + TEN_MINUTES//2]
    pitch_profile = get_pitch_profile(audio)
    tonic = tonic_lead_artist(audio)
    normalized_p = normalize(pitch_profile, tonic)
    surface = generate_surface(normalized_p, 120, 100)
    surface = postprocess(surface)
    surface = surface.ravel()
    p.load("")
    index_dump = pickle.load(open("index_dump.pickle", "rb"))
    nearest = [index_dump[i].ragam for i in p.predict(np.float32(surface), top_n=top_n)]
    unique = set(nearest)
    d = dict()
    for u in unique:
        d[u] = 100*(nearest.count(u) / top_n)
    result = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    return result


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        top_n = 3
        if len(sys.argv) > 2:
            top_n = int(sys.argv[2])
        print(predict(path, top_n=top_n))
    except IndexError:
        exit()

