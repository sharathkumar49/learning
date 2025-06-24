"""
1226. The Dining Philosophers

Implement the Dining Philosophers problem using threads and locks. Each philosopher can only pick up one fork at a time and must pick up both forks to eat.

Constraints:
- 1 <= n <= 5

Example:
Input: calls = ["wantsToEat","wantsToEat","wantsToEat","wantsToEat","wantsToEat"],
       arguments = [[0],[1],[2],[3],[4]]
Output: [[1,2,0,4,3],[1,2,0,4,3],[1,2,0,4,3],[1,2,0,4,3],[1,2,0,4,3]]

"""
import threading
class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]
    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left = philosopher
        right = (philosopher + 1) % 5
        first, second = (left, right) if left < right else (right, left)
        with self.forks[first]:
            with self.forks[second]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()

# Example usage (single-threaded simulation):
if __name__ == "__main__":
    dp = DiningPhilosophers()
    def pickLeftFork(): print("Pick left", end=' ')
    def pickRightFork(): print("Pick right", end=' ')
    def eat(): print("Eat", end=' ')
    def putLeftFork(): print("Put left", end=' ')
    def putRightFork(): print("Put right", end=' ')
    dp.wantsToEat(0, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)
    print()
