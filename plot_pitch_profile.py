from math import log
import matplotlib.pyplot as plt
import sys
import predict_swara_sthanam
from constants import swara_ratio, RAGAMS_PATH
import load_normalize

def plot_pitch_profile(filename):
    audio = load_normalize.load(filename=filename)
    print("Length of audio : ", len(audio))
    pitch_profile = load_normalize.get_pitch_profile(audio)
    print("Length of pitch_profile : ", len(pitch_profile))
    tonic_lead_artist = load_normalize.tonic_lead_artist(audio)
    normalized_pitch_profile = load_normalize.normalize(pitch_profile, tonic_lead_artist)

    predicted_swaras = predict_swara_sthanam.predict_swaras(audio=audio, pitch_profile=pitch_profile, tonic_lead_artist=tonic_lead_artist, normalized_pitch_profile=normalized_pitch_profile)
    predicted_swaras = [1200 * log(swara_ratio[i],2) for i in predicted_swaras]
    plt.plot(normalized_pitch_profile)

    xmax = len(normalized_pitch_profile) - 1000

    maximum_frequency_reached = max(normalized_pitch_profile)
    print("Tonic Lead Artist : ", tonic_lead_artist)
    print("Maximum Frequency Reached : ", maximum_frequency_reached)

    for i in swara_ratio:
        plt.hlines(y=1200 * log(swara_ratio[i],2), xmin=0, xmax=xmax, linestyle='--')
        plt.text(xmax, 1200 * log(swara_ratio[i],2),i)

    plt.title(filename.split('/')[-1])
    plt.show()


if __name__ == '__main__':
    filename = sys.argv[1]
    plot_pitch_profile(filename)
