import multiprocessing
import time

class CPUMultiPcRoots:

    def __init__(self, numbers , nThreads):
        self.numbers = numbers
        self.nThreads = nThreads
        self.results = []
        self.threads = []

    def Newton_Raphson(self, n):
        x = n
        while True:
            root = 0.5 * (x + n / x)
            if abs(root - x) < 0.0000001:
                break
            x = root
        return root

    def start(self):
        with multiprocessing.Pool(self.nThreads) as p:
            self.results = p.map(self.Newton_Raphson, self.numbers)

        return self.results
    