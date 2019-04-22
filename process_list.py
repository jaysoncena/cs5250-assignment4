import sys

from collections import deque, MutableSequence

class Process:
    def __init__(self, id, arrive_time, burst_time, last_preempt_time=0):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time
        self.last_preempt_time = last_preempt_time
        self.total_waiting_time = 0
    #for printing purpose
    def __str__(self):
        # return ('[id %d : arrive_time %d,  burst_time %d]'%(self.id, self.arrive_time, self.burst_time))
        return ("<{}: id={}, arrive_time={}, burst_time={}, last_preempt_time={}>".format(
            self.__class__.__name__,
            self.id,
            self.arrive_time,
            self.burst_time,
            self.last_preempt_time))

    def __repr__(self):
        return ("<{} at {}: id={}, arrive_time={}, burst_time={}, last_preempt_time={}>".format(
            self.__class__.__name__,
            hex(id(self)),
            self.id,
            self.arrive_time,
            self.burst_time,
            self.last_preempt_time))

    def last_process_time(self):
        return max([self.arrive_time, self.last_preempt_time])

    def update_waiting_time(self, current_time):
        self.total_waiting_time += current_time - self.last_process_time()

class ProcessList(MutableSequence):
    def __init__(self, data=None):
        super(ProcessList, self).__init__()
        if data is None:
            self._list = list()
        else:
            self._list = list(data)

        self._total_waiting_time = 0
        self._total_queued_process = 0
        
    def __repr__(self):
        ret = ["<{2}> {0} {1}".format(type(x), x, self.__class__.__name__) for x in self._list]
        return "\n".join(ret)
    def __len__(self):
        return len(self._list)
    def __getitem__(self, ii):
        return self._list[ii]
    def __delitem__(self, ii):
        del self._list[ii]
    def __setitem__(self, ii, val):
        self._list[ii] = val
    def __str__(self):
        return self.__repr__()
    def insert(self, val):
        self.append(val)
    def append(self, val):
        self._list.append(val)
    def waiting_time(self):
        return "Avg waiting time: {}\nTotal waiting time: {}\nQueued Process: {}".format(
            self._total_waiting_time / self._total_queued_process,
            self._total_waiting_time,
            self._total_queued_process
        )