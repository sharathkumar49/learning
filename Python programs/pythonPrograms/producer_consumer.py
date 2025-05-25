# Producer-consumer problem (threading)
import threading
import queue
import time

def producer(q):
    for i in range(5):
        print(f"Produced {i}")
        q.put(i)
        time.sleep(1)

def consumer(q):
    for _ in range(5):
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()

if __name__ == "__main__":
    q = queue.Queue()
    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start(); t2.start()
    t1.join(); t2.join()
