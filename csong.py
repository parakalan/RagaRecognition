from constants import *
from collections  import namedtuple

CSong = namedtuple(
	'CSong', (
		'path',
		'ragam',
		'artist',
		'tonic_pitch',
		'mbid'
	)
)


class CarnaticSong:

	def __init__(self, path, audio, ragam, mbid):
		self.path = path
		self.audio = audio
		self.ragam = ragam
		self.artist = path.split('/')[4]
		self.tonic_pitch = None
		self.mbid = mbid
		features_path = self._get_features_path()

		with open(BASE_PATH + features_path + '.tonic') as f:
			self.tonic_pitch = float(f.read())

	def get_name(self):
		return self.path.split('/')[-1]

	def _get_features_path(self):
		return self.path.replace('audio', 'features')

	def get_csong(self):
		return CSong(path=self.path, ragam=self.ragam, artist=self.artist, tonic_pitch=self.tonic_pitch, mbid=self.mbid)

	def __repr__(self):
		return f"Song: {self.get_name()}  Ragam: {self.ragam}  Artist: {self.artist}  TonicPitch: {str(self.tonic_pitch)}"
