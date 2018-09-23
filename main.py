import matplotlib.pyplot as plt
import sys
import load_normalize
import surface_generation

def main(filename):
    audio = load_normalize.load(filename=filename)
    pitch_profile = load_normalize.get_pitch_profile(audio)
    tonic_lead_artist = load_normalize.tonic_lead_artist(audio)
    normalized_pitch_profile = load_normalize.normalize(pitch_profile, tonic_lead_artist)
    surface = surface_generation.generate_surface(normalized_pitch_profile, 120, 50)
    print(surface)


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename=filename)