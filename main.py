import sys
import

from collections import deque

class Process:
    last_scheduled_time = 0
    def __init__(self, id, arrive_time, burst_time):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time
    #for printing purpose
    def __repr__(self):
        return ('[id %d : arrival_time %d,  burst_time %d]'%(self.id, self.arrive_time, self.burst_time))

def rr(process_list, quantum):
    current_time = 0
    queue = deque(process_list)

    while queue:
        item = queue.popleft()

        if current_time < item[0]:
            current_time = item[0]

        # for every processing of item, it
        # deducts quantum from burst time
        item[2] -= quantum

        # we have over-deducted so we need to fix it back
        # e.g. burst=1 and quantum=2
        if item[0] < 0:
            current_time += item[2]
            item[2] = 0

        yield [current_time, item[1], item[2]]
        current_time += quantum

        if item[2] > 0:
            queue.append(item)

if __name__ == "__main__":
    main()