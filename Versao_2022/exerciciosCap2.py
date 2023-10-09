import numpy as np


if __name__ == "__main__":
    print("1. Dados os vetores u = (1, 2), v = (2, -1) e w = (3, 1)")
    vetor_u = np.array([1, 2])
    vetor_v = np.array([2, -1])
    vetor_w = np.array([3, 1])
    print("(a) u + v = {}".format(vetor_u + vetor_v))
    print("(b) u - v = {}".format(vetor_u - vetor_v))
    print("(c) u + v - w = {}".format(vetor_u + vetor_v - vetor_w))
    print("(d) 2 · u - 3 · v + w = {}".format((2 * vetor_v) - (3 * vetor_v) + vetor_w))
    print("(e) u · (v · w) = {}".format(vetor_u * np.dot(vetor_v, vetor_w)))
    print("(f) (u . v) . w = {}".format(np.dot(vetor_u, vetor_v) * vetor_w))

    print("2. Dados os vetores u = (1, 2, 3), v = (-1, 2, -1) e w = (2, -1, 0), calcule:")
    vetor_u = np.array([1, 2, 3])
    vetor_v = np.array([1, 2, -1])
    vetor_w = np.array([2, -1, 0])
    print("(a) u + v = {}".format(vetor_u + vetor_v))
    print("(b) u - v = {}".format(vetor_u - vetor_v))
    print("(c) -3 . u + 4 . v + w = {}".format((-3 * vetor_u) + (4 * vetor_v) + vetor_w))
    print("(d) 2 · u - 3 · v + w = {}".format((2 * vetor_v) - (3 * vetor_v) + vetor_w))
    print("(e) 2 . u · (v · w) = {}".format((2 * vetor_u) * np.dot(vetor_v, vetor_w)))
    print("(f) (u . v) . w = {}".format(np.dot(vetor_u, vetor_v) * vetor_w))


