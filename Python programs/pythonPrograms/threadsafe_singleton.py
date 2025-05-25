# Thread-safe singleton in Python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == "__main__":
    def create_singleton():
        s = Singleton()
        print(id(s))
    threads = [threading.Thread(target=create_singleton) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
