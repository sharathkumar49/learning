"""
1117. Building H2O

There are two kinds of threads: oxygen and hydrogen. You must ensure that every two hydrogen threads and one oxygen thread can form water (H2O). Implement the methods hydrogen() and oxygen() to output "H" and "O" respectively.

Constraints:
- There will be exactly 2 * n hydrogen threads and n oxygen threads.
- 1 <= n <= 100

Example:
Input: "HOH"
Output: "HHO"
"""
import threading

class H2O:
    def __init__(self):
        self.hydrogen_sem = threading.Semaphore(2)
        self.oxygen_sem = threading.Semaphore(1)
        self.barrier = threading.Barrier(3)

    def hydrogen(self, releaseHydrogen):
        self.hydrogen_sem.acquire()
        self.barrier.wait()
        releaseHydrogen()
        self.hydrogen_sem.release()

    def oxygen(self, releaseOxygen):
        self.oxygen_sem.acquire()
        self.barrier.wait()
        releaseOxygen()
        self.oxygen_sem.release()

# Example usage:
# h2o = H2O()
# from threading import Thread
# Thread(target=h2o.hydrogen, args=(lambda: print("H", end=''),)).start()
# Thread(target=h2o.hydrogen, args=(lambda: print("H", end=''),)).start()
# Thread(target=h2o.oxygen, args=(lambda: print("O", end=''),)).start()
