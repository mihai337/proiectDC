from logging.ConsoleLogger import ConsoleLogger
from logging.FileLogger import FileLogger
from timing.ITimer import ITimer
import time

logger = ConsoleLogger()
timer = ITimer()
file_logger = FileLogger("log.txt")


timer.start()
time.sleep(1)
timer.pause()
time.sleep(1)
timer.resume()
time.sleep(1)
elapsed_time_sec = timer.stop()
print("Elapsed time (seconds):", elapsed_time_sec)
print("Elapsed time (milliseconds):", timer.convert_time_unit('millisec'))


