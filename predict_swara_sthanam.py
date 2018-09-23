from constants import swara_ratio
from math import log
import load_normalize
import sys

def predict_swaras(filename=None, audio=None, pitch_profile=None, tonic_lead_artist=None, normalized_pitch_profile=None):
    if audio is None:
        audio = load_normalize.load(filename=filename)
    if pitch_profile is None:
        pitch_profile = load_normalize.get_pitch_profile(audio)
    if tonic_lead_artist is None:
        tonic_lead_artist = load_normalize.tonic_lead_artist(audio)
    if normalized_pitch_profile is None:
        normalized_pitch_profile = load_normalize.normalize(pitch_profile, tonic_lead_artist)
    swaras = []
    for i in normalized_pitch_profile:
        mini = 10**7
        swara = ""
        for j in swara_ratio:
            diff = abs(1200 * log(swara_ratio[j] ,2) - i)
            if diff < mini:
                swara = j
                mini = diff
        swaras.append(swara)
    return swaras



if __name__ == '__main__':
    filename = sys.argv[1]
    swaras = predict_swaras(filename)
    print(swaras)