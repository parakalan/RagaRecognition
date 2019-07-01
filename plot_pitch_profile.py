from math import log
import matplotlib.pyplot as plt
import predict_swara_sthanam
from constants import swara_ratio
import load_normalize

from access_dataset import get_random_song, list_songs

def plot_pitch_profile(song, x):
    song.audio = song.audio[100:-100]
    plt.axhline(y=song.tonic_pitch, color='r', linestyle='-')
    len_by_x = int(len(song.audio) / x)

    l = []
    for i in range(x):
        audio = song.audio[i * len_by_x : (i + 1) * len_by_x]
        #pitch_profile = load_normalize.get_pitch_profile(audio)
        tonic_lead_artist = load_normalize.tonic_lead_artist(audio)
        l.append(tonic_lead_artist)
        """
        normalized_pitch_profile = load_normalize.normalize(pitch_profile, tonic_lead_artist)

        predicted_swaras = predict_swara_sthanam.predict_swaras(audio=audio, pitch_profile=pitch_profile, tonic_lead_artist=tonic_lead_artist, normalized_pitch_profile=normalized_pitch_profile)
        predicted_swaras = [1200 * log(swara_ratio[i],2) for i in predicted_swaras]
        #plt.plot(normalized_pitch_profile)
        xmax = len(normalized_pitch_profile) - 1000
        maximum_frequency_reached = max(normalized_pitch_profile)

        for i in swara_ratio:
            plt.hlines(y=1200 * log(swara_ratio[i],2), xmin=0, xmax=xmax, linestyle='--')
            plt.text(xmax, 1200 * log(swara_ratio[i],2),i)

        plt.title(song.ragam)
        plt.show()
        """
    plt.plot(l)
    plt.title(song.get_name())
    plt.savefig(song.get_name() + '.png')
    plt.close()


if __name__ == '__main__':
    songs = list_songs()

    for song in songs:
        plot_pitch_profile(song, 5)