from math import floor
import numpy as np


def binning(x, eta):
    temp = ((eta * x / 1200.0) % eta)
    return floor(temp)


def generate_surface(normalized_pitch_profile, eta, tau):
    s = np.zeros((eta, eta))
    N = len(normalized_pitch_profile)
    c = normalized_pitch_profile

    for i in range(len(c)):
         c[i] = binning(c[i], eta)

    c_for_j = c[: N - tau]
    inter_matrix_c_for_j = np.reshape(np.repeat(c_for_j, eta), [N - tau, eta])
    inter_matrix_j = np.tile(range(eta), [N - tau, 1])

    c_for_i = c[tau:]
    inter_matrix_c_for_i = np.tile(c_for_i, [eta, 1])
    inter_matrix_i = np.reshape(np.repeat(range(eta), N - tau), [eta, N - tau])

    first = (inter_matrix_i == inter_matrix_c_for_i)
    second = (inter_matrix_j == inter_matrix_c_for_j)

    s = np.dot(first.astype(int), second.astype(int))
    """
    inter_matrix_j = np.reshape(np.repeat(range(eta), N - 1 - tau), [tau, N - 1 -tau])

    inter_matrix_i = np.tile(range(tau), [N - tau, 1])
    inter_matrix_c_for_i = np.tile(c, [1, tau])
    
    print('inter_matrix_j shape : ', inter_matrix_j.shape)
    print('inter_matrix_c_for_j shape : ', inter_matrix_c_for_j.shape)
    print('inter_matrix_i shape : ', inter_matrix_i.shape)
    print('inter_matrix_c_for_i shape : ', inter_matrix_c_for_i.shape)
    
    n = len(normalized_pitch_profile)
    for i in range(0, eta):
        for j in range(0, eta):
            for t in range(tau, n):
                first = (c[t] == i)
                second = (c[t - tau] == j)
                s[i][j] += int(first) * int(second)
    print(np.array_equal(s, s_sanity))
    """
    return s

if __name__ == '__main__':
    # Sanity check
    normalized = [1, 2, 3, 4, 5, 6, 7, 8, 333, 876]
    eta = 5
    tau = 2
    generate_surface(normalized,eta,tau)