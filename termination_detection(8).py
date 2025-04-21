class Node:
    def __init__(self, pid):
        self.pid = pid
        self.children = []
        self.ack_received = 0

    def send_work(self):
        print(f"Node {self.pid} sending work to children")
        for child in self.children:
            child.send_work()
        self.receive_ack()

    def receive_ack(self):
        self.ack_received += 1
        print(f"Node {self.pid} received ACK")
        if self.pid == 0 and self.ack_received == len(self.children):
            print("Termination Detected at root")

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.children = [child1, child2]
root.send_work()
