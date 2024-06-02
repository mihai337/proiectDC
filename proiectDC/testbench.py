from log.ConsoleLogger import ConsoleLogger
from log.FileLogger import FileLogger
from timing.ITimer import ITimer
from time import sleep
from bench.cpu.CPUDigitsOfPI import CPUDigitsOfPI
from bench.cpu.CPUThreadedRoots import CPUThreadedRoots
from bench.cpu.CPUMultiPcRoots import CPUMultiPcRoots
import matplotlib.pyplot as plt

logger = ConsoleLogger()
timer = ITimer()
file_logger = FileLogger("log.txt")


def plot(result):
    plt.plot(result.keys(), result.values(), marker='o')
    plt.xlabel('Number of Threads')
    plt.ylabel('Runtime (seconds)')
    plt.title('Newton Raphson Calculation Runtime')
    plt.grid(True)
    plt.show()

#cpu testing digits of pi
def test_pi():
    val=[50,100,500,1000,5000,10000,50000,100000]
    cpu= CPUDigitsOfPI(val)
        
    result={}

    for n in val:
        timer.start()
        cpu.start()
        result[n]=timer.stop()

    cpu.plot(result)
    file_logger.write("Digits\tRuntime (seconds)")
    for n, runtime in result.items():
        file_logger.write(f"{n}\t{runtime}")


#cpu testing newton raphson
def test_newton_raphson():
    if __name__ == '__main__':
        no_threads = [1,2,4,8,16]
        results = {}
        for n in no_threads:
            # cpu = CPUThreadedRoots([i for i in range(1,1000000)], n)  this is with threads, but doesn't work as expected because of the GIL
            cpu = CPUMultiPcRoots([i for i in range(1,1000000)], n)
            timer.start()
            cpu.start()
            result=timer.stop()
            results[n] = result

        for n, runtime in results.items():
            file_logger.write(f"{n}\t{runtime}")
            
        plot(results)


if __name__ == '__main__':
    print("Testbench your:\n\t 1. CPU\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Choose your test:\n\t 1. Digits of PI\n\t 2. Newton Raphson\n")
        choice = input("Enter your choice:")
        match choice:
            case "1":
                test_pi()
            case "2":
                test_newton_raphson()
            case _:
                logger.write("Invalid choice")
    else:
        logger.write("Invalid choice")
    file_logger.close()

