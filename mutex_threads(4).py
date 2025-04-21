import threading
import time

lock = threading.Lock()

def critical_section(pid):
    with lock:
        print(f"Process {pid} entering critical section")
        time.sleep(1)
        print(f"Process {pid} exiting critical section")

threads = [threading.Thread(target=critical_section, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
