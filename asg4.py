import sys

from collections import deque

class Process:
    last_scheduled_time = 0
    def __init__(self, id, arrive_time, burst_time):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time
    #for printing purpose
    def __repr__(self):
        # return ('[id %d : arrival_time %d,  burst_time %d]'%(self.id, self.arrive_time, self.burst_time))
        return ("id={}, arrival_time={}, burst_time={}".format(self.id, self.arrive_time, self.burst_time))


def rr(process_list, quantum=2):
    current_time = 0
    queue = deque(process_list)

    while queue:
        p = queue.popleft()

        if current_time < p.arrive_time:
            current_time = p.arrive_time

        yield [current_time, p]

        current_time += quantum
        p.burst_time -= quantum

        # we have over-deducted (less than 0) so we need to fix this
        # e.g. before burst=1 and quantum=2
        if p.burst_time < 0:
            current_time += p.burst_time
            p.burst_time = 0

        if p.burst_time > 0:
            queue.append(p)


if __name__ == "__main__":
    main()