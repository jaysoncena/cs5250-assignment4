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
    def __repr__(self):
        # return ('[id %d : arrive_time %d,  burst_time %d]'%(self.id, self.arrive_time, self.burst_time))
        return ("id={}, arrive_time={}, burst_time={}, last_preempt_time={}".format(
            self.id,
            self.arrive_time,
            self.burst_time,
            self.last_preempt_time))
    def last_process_time(self):
        return max([self.arrive_time, self.last_preempt_time])

class SRTFList(MutableSequence):
    def __init__(self, alpha, initial_guess, data=None):
        super(SRTFList, self).__init__()

        self._pid_previous_actual = {}
        self._initial_guess = initial_guess
        self._alpha = float(alpha)

        if data is None:
            self._list = list()
        else:
            self._list = list(data)

        
        self._sorted_by_arrive_time()
    def __repr__(self):
        ret = ["{0} {1}".format(type(x), x) for x in self._list]
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

    def add(self, val):
        if not isinstance(val, Process):
            raise ValueError("<{0} {1}> is not an instance of {2}".format(val.__class__.__name__, val, Process.__class__.__name__))

        self._list.insert(len(self._list), val)
        self._sorted_by_arrive_time()

    def _sorted_by_arrive_time(self):
        self._list = sorted(self._list, key=lambda x: x.arrive_time)

    def _previous_actual_time(self, pid):


    # TODO
    def set_forceast_burst_time(self, pid, value=None):
        if pid in 

    def get_by_srtf(self, current_time, pop=False):
        if len(self._list) < 1:
            return None
        elif len(self._list)  == 1:
            # pop
            p = self._list[0]
            if pop:
                del self._list[0]
            return p
        # else
        filtered_list = [x for x in self._list if x.last_process_time() <= current_time]
        if not filtered_list:
            self._sorted_by_process_time()
            # pop
            p = self._list[0]
            if pop:
                del self._list[0]
            return p

        # least burst_time
        filtered_list = sorted(filtered_list, key=lambda x: x.burst_time)
        # pop
        p_num = self._list.index(filtered_list[0])
        p = self._list[p_num]
        if pop:
            del self._list[p_num]
        return p

    def pop_by_srtf(self, current_time):
        if len(self._list) < 1:
            return None
        elif len(self._list)  == 1:
            # pop
            p = self._list[0]
            del self._list[0]
            return p
        # else
        filtered_list = [x for x in self._list if x.last_process_time() <= current_time]
        if not filtered_list:
            self._sorted_by_process_time()
            # pop
            p = self._list[0]
            del self._list[0]
            return p

        # least burst_time
        filtered_list = sorted(filtered_list, key=lambda x: x.burst_time)
        # pop
        p_num = self._list.index(filtered_list[0])
        p = self._list[p_num]
        del self._list[p_num]
        return p

class SJFList(MutableSequence):
    def __init__(self, data=None):
        super(SJFList, self).__init__()
        if data is None:
            self._list = list()
        else:
            self._list = list(data)
        
        self._sorted()
    def __repr__(self):
        ret = ["{0} {1}".format(type(x), x) for x in self._list]
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

    def add(self, val):
        if not isinstance(val, Process):
            raise ValueError("<{0} {1}> is not an instance of {2}".format(val.__class__.__name__, val, Process.__class__.__name__))

        self._list.insert(len(self._list), val)
        self._sorted()

    def _sorted(self):
        self._list = sorted(self._list, key=lambda x: x.burst_time)

    def _sorted_by_process_time(self):
        self._list = sorted(self._list, key=lambda x: x.last_process_time())

    def get_next_arrive_time(self):
        """
            return the closest `arrive_time` from
            the given `current_time` argument
        """
        if len(self._list) > 0:
            self._sorted_by_process_time()
            return self._list[0].last_process_time()
        # else
        return -1

    def get(self):
        """ gets the process with SRTF """
        pass

    def get_by_srtf(self, current_time, pop=False):
        if len(self._list) < 1:
            return None
        elif len(self._list)  == 1:
            # pop
            p = self._list[0]
            if pop:
                del self._list[0]
            return p
        # else
        filtered_list = [x for x in self._list if x.last_process_time() <= current_time]
        if not filtered_list:
            self._sorted_by_process_time()
            # pop
            p = self._list[0]
            if pop:
                del self._list[0]
            return p

        # least burst_time
        filtered_list = sorted(filtered_list, key=lambda x: x.burst_time)
        # pop
        p_num = self._list.index(filtered_list[0])
        p = self._list[p_num]
        if pop:
            del self._list[p_num]
        return p

    def pop_by_srtf(self, current_time):
        if len(self._list) < 1:
            return None
        elif len(self._list)  == 1:
            # pop
            p = self._list[0]
            del self._list[0]
            return p
        # else
        filtered_list = [x for x in self._list if x.last_process_time() <= current_time]
        if not filtered_list:
            self._sorted_by_process_time()
            # pop
            p = self._list[0]
            del self._list[0]
            return p

        # least burst_time
        filtered_list = sorted(filtered_list, key=lambda x: x.burst_time)
        # pop
        p_num = self._list.index(filtered_list[0])
        p = self._list[p_num]
        del self._list[p_num]
        return p
    

def rr(process_list, quantum=2):
    current_time = 0
    waiting_time = 0
    queue = deque(process_list)

    while queue:
        p = queue.popleft()

        if current_time < p.arrive_time:
            current_time = p.arrive_time

        waiting_time += current_time - p.last_process_time()

        yield [current_time, p]

        current_time += quantum
        p.burst_time -= quantum

        # we have over-deducted (less than 0) so we need to fix this
        # e.g. before burst=1 and quantum=2
        if p.burst_time < 0:
            current_time += p.burst_time
            p.burst_time = 0

        # after all logics are finished, we set the last current_time
        # the process was run
        p.last_preempt_time = current_time

        if p.burst_time > 0:
            queue.append(p)

def srtf(process_list):
    # processes_srtf = SRTFList()
    # for p in process_list:
    #     processes_srtf.add(p)
    #     print("## add: {}".format(p))
    #     print("## entries\n{}".format(processes_srtf))
    # # for item in process_list:
    # #     processes.add(item)
    # #     print("## add: {}".format(item))
    # #     print("## entry\n{}".format(processes))

    # print(processes_srtf.get_next_arrive_time(0))
    # print("## entries\n{}".format(processes_srtf))
    proc_srtf = SRTFList(process_list)
    current_time = 0
    waiting_time = 0
    force_next_p = None

    while proc_srtf:
        # workaround to bypass srtf selection
        # and continue on the current process
        # this will only be triggered when
        # current p and next_p has the same burst_time
        p = None
        if force_next_p:
            p = force_next_p
            force_next_p = None
        else:
            p = proc_srtf.get_by_srtf(current_time, pop=True)

        if current_time < p.arrive_time:
            current_time = p.arrive_time

        yield [current_time, p]

        waiting_time += current_time - p.last_process_time()
        next_arrive_time = proc_srtf.get_next_arrive_time()
        # gets the next process without removing from list
        next_p = proc_srtf.get_by_srtf(current_time, pop=False)
        if next_p is not None and p.burst_time == next_p.burst_time:
            force_next_p = p
        

        if next_arrive_time < 0:
            continue # should quit the loop since this means no more items in list

        p.burst_time -= next_arrive_time
        current_time += next_arrive_time

        if p.burst_time < 0:
            diff = abs(p.burst_time)
            p.burst_time = 0
            current_time -= diff

        p.last_preempt_time = current_time
        if p.burst_time > 0:
            proc_srtf.add(p)




if __name__ == "__main__":
    main()