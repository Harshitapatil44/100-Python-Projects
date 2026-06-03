import sched
import time

# Initialize the scheduler
s = sched.scheduler(time.time, time.sleep)

def print_time(a='default'):
    print("From print_time", time.time(), a)

def schedule_tasks():
    print("Start time:", time.time())
    
    # arguments: (delay_in_seconds, priority, function, argument_tuple)
    s.enter(5, 1, print_time, argument=('first job',))
    s.enter(10, 1, print_time, argument=('second job',))

    # Run the scheduled events
    s.run()

schedule_tasks()
