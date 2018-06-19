from event_queue import *
import sys

def print_each_second(equeue):
    print('\ttime {}: every one'.format(equeue.time))
    add_event(equeue, print_each_second, 1)


def stop(equeue):
    print('\ttime {}: stopping'.format(equeue.time))
    sys.exit(0)

def print_a_word(equeue):
    print('\ttime {}: Forestry'.format(equeue.time))
    add_event(equeue, print_a_word, 15)


def say_hi(equeue):
    print('\ttime {}: Hello'.format(equeue.time))
    add_event(equeue, say_hi, 5)

if __name__ == '__main__':
    equeue = EventQueue()

    add_event(equeue, stop, 20)
    add_event(equeue, print_each_second, 1)
    add_event(equeue, say_hi, 5)
    add_event(equeue, print_a_word, 15)

    run_events(equeue)
