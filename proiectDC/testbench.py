from logging.ConsoleLogger import ConsoleLogger
from logging.FileLogger import FileLogger
from timing.ITimer import ITimer
from time import sleep

logger = ConsoleLogger()
timer = ITimer()
file_logger = FileLogger("log.txt")


timer.start()
sleep(1)
timer.pause()
sleep(1)
timer.resume()
sleep(1)
t = timer.pause()
sleep(2)
timer.stop()

logger.write("Total time: ", timer.total_time)
logger.write("Time: ", t)
file_logger.write("Total time: ", timer.total_time)
file_logger.close()

