import essentia.standard
from math import log

def load(filename, sampleRate=44100):
    loader = essentia.standard.MonoLoader(filename=filename, sampleRate=sampleRate)
    audio = loader()
    return audio

def get_pitch_profile(audio):
    equal_loudness = essentia.standard.EqualLoudness()
    audio = equal_loudness(audio)
    predominant_melody = essentia.standard.PredominantPitchMelodia(hopSize=196, frameSize=2028)
    pitch_profile_data = predominant_melody(audio)
    pitch_profile = pitch_profile_data[0]
    return pitch_profile

def tonic_lead_artist(audio, print_val = False):
    T = essentia.standard.TonicIndianArtMusic()
    tonic_lead_artist = T(audio)
    if print_val:
        print("Tonic_lead_artist:", tonic_lead_artist)
    return tonic_lead_artist

def normalize(pitch_profile, tonic_lead_artist, zeroval = -200):
    normalized_pitch_profile = []
    for i in range(0, len(pitch_profile)):
        try:
            normalized_pitch_profile.append(1200 * (log(pitch_profile[i],2) - log(tonic_lead_artist, 2)))
        except ValueError:
            pass
    return normalized_pitch_profile