class FileLogger:
    def __init__(self): #constructor, pentru necunoscatori
        self.file = open('log.txt', 'w')

    def write(self, *args):
        for x in args:
            print(x, end=' ', file=self.file)
        print("\n", file=self.file)

    def close(self):
        self.file.close()