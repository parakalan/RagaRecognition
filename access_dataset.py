from constants import *
from load_normalize import load
from csong import CarnaticSong
import random
import json

def get_random_song():
	song_dict = {}
	ragams = {}

	with open(BASE_PATH + REDUCED) as f:
		song_dict = json.load(f)

	with open(BASE_PATH + RAGAID_RAGANAME_JSON_PATH) as f:
		ragams = json.load(f)

	key = random.choice(list(song_dict.keys()))
	random_piece = song_dict[key]
	audio = load(BASE_PATH + random_piece['path'] + '.mp3')
	song = CarnaticSong(path=random_piece['path'], audio=audio, ragam=ragams[random_piece['ragaid']], mbid=key)
	return song

def list_songs():
	songs = []
	song_dict = {}
	ragams = {}

	with open(BASE_PATH + REDUCED) as f:
		song_dict = json.load(f)

	with open(BASE_PATH + RAGAID_RAGANAME_JSON_PATH) as f:
		ragams = json.load(f)

	for key in song_dict.keys():
		audio = load(BASE_PATH + song_dict[key]['path'] + '.mp3')
		song = CarnaticSong(path=song_dict[key]['path'], audio=audio, ragam=ragams[song_dict[key]['ragaid']], mbid=key)
		songs.append(song)

	return songs


if __name__ == '__main__':
	print(get_random_song())

