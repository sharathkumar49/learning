"""
LeetCode 2694. Event Emitter

Implement an event emitter class.

Constraints:
- 1 <= calls.length <= 10^5
"""
class EventEmitter:
    def __init__(self):
        self.events = {}
    def subscribe(self, event, fn):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(fn)
        return lambda: self.events[event].remove(fn)
    def emit(self, event, *args):
        return [fn(*args) for fn in self.events.get(event, [])]
# Example usage:
# emitter = EventEmitter()
# unsub = emitter.subscribe('event', lambda x: x+1)
# print(emitter.emit('event', 1))  # Output: [2]
# unsub()
# print(emitter.emit('event', 1))  # Output: []
