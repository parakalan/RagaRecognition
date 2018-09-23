from math import floor

def binning(x, eta):
    temp = ((eta * x / 1200.0) % eta)
    return floor(temp)

def indicator(x, y):
    if x==y:
        return 1
    return 0

def generate_surface(normalized_pitch_profile, eta, tau):
    s = [[0 for x in range(eta)] for y in range(eta)]
    N = len(normalized_pitch_profile)
    for i in range(0, eta):
        for j in range(0, eta):
            for t in range(tau, N):
                first  = indicator(binning(normalized_pitch_profile[t], eta), i)
                second = indicator(binning(normalized_pitch_profile[t - tau], eta), j)
                s[i][j] += first*second

    return s