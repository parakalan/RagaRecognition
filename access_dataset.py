from constants import *
from load_normalize import load
from csong import CarnaticSong
import random
import json

def get_random_song():
	"""
	Returns a random music piece from the dataset.
	:return: A CarnaticSong object with attribute of the selected random piece.
	"""

	dict = {}
	ragams = {}

	with open(BASE_PATH + REDUCED) as f:
		dict = json.load(f)

	with open(BASE_PATH + RAGAID_RAGANAME_JSON_PATH) as f:
		ragams = json.load(f)

	random_piece = dict[random.choice(list(dict.keys()))]

	audio = load(BASE_PATH + random_piece['path'] + '.mp3')

	song = CarnaticSong(path=random_piece['path'], audio=audio, ragam=ragams[random_piece['ragaid']])

	return song

def list_songs():
	"""
	Returns all songs in the list.
	:return: A list of CarnaticSong objects.
	"""
	songs = []
	dict = {}
	ragams = {}

	with open(BASE_PATH + REDUCED) as f:
		dict = json.load(f)

	with open(BASE_PATH + RAGAID_RAGANAME_JSON_PATH) as f:
		ragams = json.load(f)

	for key in dict.keys():
		audio = load(BASE_PATH + dict[key]['path'] + '.mp3')
		song = CarnaticSong(path=dict[key]['path'], audio=audio, ragam=ragams[dict[key]['ragaid']])
		songs.append(song)

	return songs
if __name__ == '__main__':
	print(get_random_song())

