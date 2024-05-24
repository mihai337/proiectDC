import threading
import time

class CPUThreadedRoots:

    def __init__(self, numbers , nThreads):
        self.numbers = numbers
        self.nThreads = nThreads
        self.results = []
        self.threads = []
        self.initialise()

    def Newton_Raphson(self, n):
        x = n
        while True:
            root = 0.5 * (x + n / x)
            if abs(root - x) < 0.0000001:
                break
            x = root
        return root
    
    def calculateInterval(self, start, end):
        for i in range(start, end):
            self.results.append(self.Newton_Raphson(self.numbers[i]))

    def start(self):
        for thread in self.threads:
            thread.start()

        for thread in self.threads:
            thread.join()

        return self.results
    
    def initialise(self):
        for i in range(self.nThreads):
            start = i * len(self.numbers) // self.nThreads
            end = (i + 1) * len(self.numbers) // self.nThreads
            thread = threading.Thread(target=self.calculateInterval, args=(start, end))
            self.threads.append(thread)