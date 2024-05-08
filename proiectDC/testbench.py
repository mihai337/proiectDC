from log.ConsoleLogger import ConsoleLogger
from log.FileLogger import FileLogger
from timing.ITimer import ITimer
from time import sleep
from bench.cpu.CPUDigitsOfPI import CPUDigitsOfPI

logger = ConsoleLogger()
timer = ITimer()
file_logger = FileLogger("log.txt")


#cpu testing
cpu= CPUDigitsOfPI()
    
val=[50,100,500,1000,5000,10000,50000,100000]
result={}

for n in val:
    timer.start()
    cpu.start(cpu.monte_carlo, n)
    result[n]=timer.stop()

cpu.plot(result)
file_logger.write("Digits\tRuntime (seconds)")
for n, runtime in result.items():
    file_logger.write(f"{n}\t{runtime}")

file_logger.close()

