from constants import *
from load_normalize import load
from csong import CarnaticSong
import random
import json


def get_random_song():
	with open(BASE_PATH + REDUCED) as f:
		song_dict = json.load(f)

	with open(BASE_PATH + RAGAID_RAGANAME_JSON_PATH) as f:
		ragams = json.load(f)

	key = random.choice(list(song_dict.keys()))
	random_piece = song_dict[key]
	audio = load(BASE_PATH + random_piece['path'] + '.mp3')
	song = CarnaticSong(path=random_piece['path'], audio=audio, ragam=ragams[random_piece['ragaid']], mbid=key)
	return song


def list_songs(batch_no):
	songs = []
	keys = list(mbid_to_ragaid.keys())
	for key in keys[10 * batch_no : 10 * (batch_no + 1)]:
		audio = load(BASE_PATH + mbid_to_ragaid[key]['path'] + '.mp3')
		song = CarnaticSong(path=mbid_to_ragaid[key]['path'], audio=audio, ragam=ragaid_to_raganame[mbid_to_ragaid[key]['ragaid']], mbid=key)
		songs.append(song)

	return songs


if __name__ == '__main__':
	print(get_random_song())

