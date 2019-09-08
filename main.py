import os
import pickle
import load_normalize
import surface_generation
from constants import *
from access_dataset import list_songs


def main(song):
	if os.path.exists("surfaces/" + song.mbid):
		return
	pitch_profile = load_normalize.get_pitch_profile(song.audio)
	tonic_lead_artist = song.tonic_pitch
	normalized_pitch_profile = load_normalize.normalize(pitch_profile, tonic_lead_artist)
	surface = surface_generation.generate_surface(normalized_pitch_profile, 120, 100)
	surface = surface_generation.postprocess(surface)
	surface.dump("surfaces/" + song.mbid)


if __name__ == '__main__':
	test_set = dict()
	index_dump = dict()
	errors = []
	total_no_songs = len(mbid_to_ragaid.keys())
	for batch in range(total_no_songs // 10):
		songs = list_songs(batch)
		for song in songs:
			if song.ragam not in test_set:
				test_set[song.ragam] = song.get_csong()
				print(f"TEST SET: {song}")
				continue
			try:
				main(song)
				index_dump[song.mbid] = song.get_csong()
			except:
				print(f"ERROR: {song}")
				errors.append(song.path)
				continue
			print(f"PROCESSED {song}")
		del songs
	pickle.dump(index_dump, open("index_dump.pickle", "wb"))
	pickle.dump(test_set, open(BASE_PATH + TESTING_FILE_PATH, "wb"))
	pickle.dump(errors, open("errors", "wb"))

