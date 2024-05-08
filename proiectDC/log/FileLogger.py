class FileLogger:
    def __init__(self,file_name : str): #constructor, pentru necunoscatori
        self.file = open(file_name, 'w')

    def write(self, *args):
        for x in args:
            print(x, end=' ', file=self.file)
        print(" ", file=self.file)   #\n

    def close(self):
        self.file.close()