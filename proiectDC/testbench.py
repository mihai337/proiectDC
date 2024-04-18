from logging.ConsoleLogger import ConsoleLogger
from logging.FileLogger import FileLogger
from timing.ITimer import ITimer
from time import sleep

logger = ConsoleLogger()
timer = ITimer()
file_logger = FileLogger()


timer.start()
sleep(1)
timer.pause()
sleep(2)
timer.resume()
sleep(1)
timer.stop()

logger.write("Total time: ", timer.total_time)
file_logger.write("Total time: ", timer.total_time)
file_logger.close()

