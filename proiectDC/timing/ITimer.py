import time

class ITimer:
    total_time = 0
    start_time = 0
    end_time = 0

    def start(self):
        self.total_time = 0
        self.start_time = time.time()
        return self.start_time
    
    def pause(self):
        self.end_time = time.time()
        self.total_time += self.end_time - self.start_time
        return self.total_time
    
    def resume(self):
        self.start_time = time.time()
        return self.start_time
    
    def stop(self):
        self.end_time = time.time()
        self.total_time += self.end_time - self.start_time
        return self.total_time