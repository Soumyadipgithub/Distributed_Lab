import threading
import time
import random

class Process(threading.Thread):
    def __init__(self, pid, processes):
        super().__init__()
        self.pid = pid
        self.clock = 0
        self.queue = []
        self.processes = processes
        self.replies = 0
        self.event = threading.Event()

    def request_cs(self):
        self.clock += 1
        print(f"Process {self.pid} requesting CS at time {self.clock}")
        self.queue.append((self.clock, self.pid))
        for p in self.processes:
            if p.pid != self.pid:
                p.receive_request(self.pid, self.clock)
        self.event.wait()
        while self.queue[0][1] != self.pid:
            time.sleep(0.1)

    def receive_request(self, pid, timestamp):
        self.clock = max(self.clock, timestamp) + 1
        print(f"Process {self.pid} received request from {pid} at time {timestamp}")
        self.queue.append((timestamp, pid))
        self.queue.sort()
        for p in self.processes:
            if p.pid == pid:
                p.receive_reply()

    def receive_reply(self):
        self.replies += 1
        if self.replies == len(self.processes) - 1:
            self.event.set()

    def run(self):
        time.sleep(random.uniform(1, 2))
        self.request_cs()
        print(f"Process {self.pid} entered CS")
        time.sleep(1)
        print(f"Process {self.pid} exiting CS")
        self.queue = [x for x in self.queue if x[1] != self.pid]

processes = [Process(i, []) for i in range(3)]
for p in processes:
    p.processes = processes
for p in processes:
    p.start()
for p in processes:
    p.join()
