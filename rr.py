import process_list
from test import test_data1, test_data2, test_data3, test_data4
from test import test_data5, test_data6, test_data7, test_data8

class RRProcess(process_list.Process):
    def __init__(self, process):
        # super(SJFProcess, self).__init__(*args, **kwargs)

        if not isinstance(process, process_list.Process):
            raise TypeError("{} is not Process class".format(process))
        
        self.convert_from_process(process)

    def convert_from_process(self, process):
        if not isinstance(process, process_list.Process):
            raise ValueError("{} is not Process class".format(process))

        self.id = process.id
        self.arrive_time = process.arrive_time
        self.burst_time = process.burst_time
        self.total_waiting_time = process.total_waiting_time
        self.last_preempt_time = process.last_preempt_time

    # def update_waiting_time(self, current_time):
    #     self.total_waiting_time += current_time - self.last_process_time()

class RRList(process_list.ProcessList):
    def __init__(self, quantum=4, data=None):
        # assigns data to self._list
        super(RRList, self).__init__(data=data)
        
        self._quantum = quantum
        self._list = [RRProcess(x) for x in self._list]

    def pop_earliest(self):
        if len(self._list) < 0:
            return None
        return self._list[0]
       

    def iter(self):
        """
            1. get the index 0
            2. delete from self._list
            3. if arrive_time > 0, then add back to list
        """
        current_time = 0
        last_process = None

        while self._list:
            p = self._list[0]
            del self._list[0]

            if current_time < p.arrive_time:
                current_time = p.arrive_time

            p.update_waiting_time(current_time)

            yield (current_time, p.id, p)

            # we have over-deducted (less than 0) so we need to fix this
            # e.g. before burst=1 and quantum=2
            current_time += self._quantum
            p.burst_time -= self._quantum

            # after all logics are finished, we set the last current_time
            # the process was run
            if p.burst_time < 0:
                current_time += p.burst_time
                p.burst_time = 0

            # after all logics are finished, we set the last current_time
            # the process was run
            p.last_preempt_time = current_time

            if p.burst_time > 0:
                self._list.append(p)
                last_process = p
            else:
                self._total_waiting_time += p.total_waiting_time
                self._total_queued_process += 1


# this main() is for testing only
def main():
    rr = RRList(data=test_data7, quantum=4)

    for item in rr.iter():
        print(item)

    print(rr.waiting_time())

def runner(raw_processes, quantum):
    processes = []
    for p in raw_processes:
        processes.append(process_list.Process(*p))

    lines = []
    rr = RRList(data=processes)
    last_p_id = None
    for p in rr.iter():
        if last_p_id == p[2].address():
            continue
        lines.append("({}, {})".format(p[0], p[1]))
        last_p_id = p[2].address()
    
    lines.append(rr.waiting_time())

    return lines

    


if __name__ == "__main__":
    main()