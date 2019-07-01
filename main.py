import matplotlib.pyplot as plt
import numpy as np
import load_normalize
import surface_generation
import scipy.ndimage as ndimage
from access_dataset import list_songs
from csong import CarnaticSong
from access_dataset import get_random_song


def majority_average(a, tolerance = 8):
	m = 0
	i = 0
	for x in a:
		if i == 0:
			m = x
			i = 1
		elif abs(m - x) < tolerance:
			i += 1
		else:
			i -= 1
	avg = 0
	cnt = 0
	for x in a:
		if abs(m - x) < tolerance:
			avg += x
			cnt += 1
	avg /= cnt
	return avg
#TODO: Find surfaces of all songs in dataset.
"""
Separate DATASET into TRAIN/TEST
Total : 
Average surfaces of all songs of same raga, store in json file (?).
Run program on new songs.
"""
def main(song, segments=3, tau = 1000):
	length_of_segment = int(len(song.audio) / segments)
	tonic_pitches = []
	for i in range(segments):
		audio_reduced = song.audio[i * length_of_segment:(i+1) * length_of_segment]
		pitch_profile = load_normalize.get_pitch_profile(audio_reduced)
		tonic_lead_artist = load_normalize.tonic_lead_artist(audio_reduced)
		tonic_pitches.append(tonic_lead_artist)
	tonic_lead_artist = majority_average(tonic_pitches)
	normalized_pitch_profile = load_normalize.normalize(pitch_profile, tonic_lead_artist)
	surface = surface_generation.generate_surface(normalized_pitch_profile, 120, 100)
	surface = surface / np.amax(surface)
	alpha = 0.75
	surface = np.power(surface, alpha)
	surface = ndimage.gaussian_filter(surface, sigma=2, order=0)
	norm = np.linalg.norm(surface)
	surface = surface / norm


if __name__ == '__main__':
	"""
	songs = list_songs()
	for song in songs:
		print(song, end='')
		main(song, segments=2)
	
	song = get_random_song()
	print(song)
	main(song, 5)
	"""
	audio = load_normalize.load('/Users/sudharsantirumalai/Downloads/Raga_Yaman.mp3')
	song = CarnaticSong('/Users/sudharsantirumalai/Downloads/Raga_Yaman', audio, 'Yaman')
	main(song)
