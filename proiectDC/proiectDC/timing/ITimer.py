import time

class ITimer:
    total_time = 0
    start_time = 0
    end_time = 0
    paused = False

    def start(self):
        self.total_time = 0
        self.start_time = time.time()
        self.paused = False
        return self.start_time

    def pause(self):
        if not self.paused:
            self.end_time = time.time()
            self.total_time += self.end_time - self.start_time
            self.paused = True
        return self.total_time

    def resume(self):
        if self.paused:
            self.start_time = time.time()
            self.paused = False
        return self.start_time

    def stop(self):
        if not self.paused:
            self.end_time = time.time()
            self.total_time += self.end_time - self.start_time
        return self.total_time

    def convert_time_unit(self, unit='sec'):
        if unit == 'sec':
            return self.total_time
        elif unit == 'millisec':
            return self.total_time * 1000
        elif unit == 'microsec':
            return self.total_time * 1000000
        else:
            raise ValueError("Invalid time unit specified. Please choose 'sec', 'millisec', or 'microsec'.")
