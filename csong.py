from constants import *

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

	def __repr__(self):
		return f"Song: {self.get_name()} \n Ragam: {self.ragam} \n Artist: {self.artist} \n TonicPitch: {str(self.tonic_pitch)}"
