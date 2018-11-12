import matplotlib.pyplot as plt
import numpy as np
import sys
import load_normalize
import surface_generation
import scipy.ndimage as ndimage

def main(filename):
    audio = load_normalize.load(filename=filename)
    pitch_profile = load_normalize.get_pitch_profile(audio)
    tonic_lead_artist = load_normalize.tonic_lead_artist(audio)
    normalized_pitch_profile = load_normalize.normalize(pitch_profile, tonic_lead_artist)
    surface = surface_generation.generate_surface(normalized_pitch_profile, 120, 100)
    surface = surface / np.amax(surface)
    surface = np.power(surface, 3)
    surface = ndimage.gaussian_filter(surface, sigma=(20), order=0)
    norm = np.linalg.norm(surface)
    surface = surface / norm
    plt.imshow(surface, vmin=surface.min(), vmax=surface.max(), origin='lower',
           extent=[0, 120, 120, 0])
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename=filename)