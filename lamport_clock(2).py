class LamportClock:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1

    def send_event(self):
        self.tick()
        return self.time

    def receive_event(self, sender_time):
        self.time = max(self.time, sender_time) + 1

p1 = LamportClock()
p2 = LamportClock()

print("P1 sends message")
t1 = p1.send_event()
print("P2 receives message")
p2.receive_event(t1)

print(f"Final P1: {p1.time}, P2: {p2.time}")
