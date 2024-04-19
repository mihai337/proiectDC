class ConsoleLogger:

    def write(self, *args):
        for x in args:
            print(x,end=' ')
        print("\n")