from constants import *

class CarnaticSong:

	#features_ext = ['.flatSegNyas', '.pitch', '.pitchSilIntrpPP', '.taniSegKNN', '.tonic', '.tonicFine']
	def __init__(self, path, audio, ragam):
		self.path = path
		self.audio = audio
		self.ragam = ragam
		self.tonic_pitch = None



		#features_path = self._get_features_path()

		#with open(BASE_PATH + features_path + '.tonic') as f:
		#	self.tonic_pitch = float(f.read())





	def get_name(self):
		return self.path.split('/')[-1]

	def _get_features_path(self):
		return self.path.replace('audio', 'features')

	def __repr__(self):
		return "Song:"+self.get_name()+"----Ragam:"+self.ragam+"----TonicPitch:"+str(self.tonic_pitch)
