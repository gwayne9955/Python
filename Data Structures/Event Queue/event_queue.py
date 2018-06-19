#
# Garrett Wayne
#

from priority_queue import *
# An EventQueue is a class containing a PriorityQueue and time represented by an integer
class EventQueue:
    def __init__(self):
        self.pq = PriorityQueue(comes_before_priority)      # a PriorityQueue
        self.time = 0                                       # an int

    def __eq__(self, other):
        return (type(other) == EventQueue
                and self.pq == other.pq
                and self.time == other.time)

    def __repr__(self):
        return "EventQueue({!r}, {!r})".format(self.pq, self.time)

# An Event is a fuction to be executed at a specific time
class Event:
    def __init__(self, time, function):
        self.time = time                       # a PriorityQueue
        self.function = function               # an int

    def __eq__(self, other):
        return (type(other) == Event
                and self.time == other.time
                and self.function == other.function)

    def __repr__(self):
        return "EventQueue({!r}, {!r})".format(self.time, self.function)

# Event Event -> bool
# Returns true if event 1 should come before event 2, based on their times
def comes_before_priority(e_1, e_2):
    return e_1.time < e_2.time

# EventQueue Event int -> None
# Stores the event to be scheduled in the EventQueue
def add_event(eq, func, time_delay):
    event = Event(time_delay + eq.time, func)
    eq.pq = enqueue(eq.pq, event)


# EventQueue -> None
# This function will wait until the "next" event in the queue is ready to execute.
# The function will then execute all "ready" events and should continue until
# there are no events pending
def run_events(eq):
    while (is_empty(eq.pq) == False):
        event, pq = dequeue(eq.pq)
        if eq.time != event.time:
            eq.time = event.time
        event.function(eq)
