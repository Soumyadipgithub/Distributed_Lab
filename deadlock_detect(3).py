wait_for = {
    0: 1,
    1: 2,
    2: 0
}

def detect_deadlock(initiator):
    visited = set()

    def forward(pid):
        if pid in visited: return
        visited.add(pid)
        nxt = wait_for.get(pid)
        if nxt is None: return
        if nxt == initiator:
            print("Deadlock detected!")
        else:
            forward(nxt)

    forward(initiator)

detect_deadlock(0)
