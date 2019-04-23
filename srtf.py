import process_list
from test import test_data1, test_data2, test_data3, test_data4
from test import test_data5, test_data6, test_data7, test_data8


class SRTFProcess(process_list.Process):
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

class SRTFList(process_list.ProcessList):
    def __init__(self, data=None):
        super(SRTFList, self).__init__(data=data)
        
        self._list = [SRTFProcess(x) for x in self._list]
        self._force_next_p = None

    def add(self, val):
        if not isinstance(val, process_list.Process):
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


    def iter(self):
        current_time = 0
        waiting_time = 0

        while self._list:
            """
                1. sort by arrive_time
                2. pop [0]
                3. get [0].arrive_time and filter self._list
                4. if result is 1 or more, combine [0] and result
                5. from the combined result, get [0] and return the remaining to _list
                6. get next_p
            """
            p1 = self.next_p(current_time, pop=True)
            p2 = self.next_p(current_time, pop=False)

            if current_time < p1.arrive_time:
                current_time = p1.arrive_time

            p1.update_waiting_time(current_time)

            yield (current_time, p1.id, p1)
            if p2 is None:
                self._total_waiting_time += p1.total_waiting_time
                self._total_queued_process += 1
                continue

            step = self.minimum_progress(p1, p2)

            current_time += step
            p1.burst_time -= step

            p1.last_preempt_time = current_time

            if p1.burst_time > 0:
                self._list.append(p1)
            else:
                self._total_waiting_time += p1.total_waiting_time
                self._total_queued_process += 1


    def next_p(self, current_time, pop=False):
        """
            1. get the minimum arrive_time
            2. check for the same arrive_time
            3. for all p that has the same arrive_time, get the minimum burst_time
        """
        if len(self._list) < 1:
            return None
        
        min_time = min([p.arrive_time for p in self._list])
        if min_time > current_time:
            current_time = min_time
        
        filter_by_arrive_time = [p for p in self._list if p.arrive_time <= current_time]
        smallest_burst_time = sorted(filter_by_arrive_time, key=lambda p: p.burst_time)[0]

        if pop:
            del self._list[self._list.index(smallest_burst_time)]

        return smallest_burst_time

    def minimum_progress(self, p1, p2):
        # gets the minimum time the current process can be scheduled
        # until we pre-empt the current one and process the next one
        by_arrive_time = max([p2.arrive_time, p1.arrive_time]) - min([p2.arrive_time, p1.arrive_time])
        by_burst_time = max([p2.burst_time, p1.burst_time]) - min([p2.burst_time, p1.burst_time])

        return max([min([by_arrive_time, by_burst_time]), 1])


# this main() is for testing only
def main():
    srtf = SRTFList(data=test_data8)
    # add filter on next
    last_p_id = None
    for p in srtf.iter():
        if last_p_id == p[2].address():
            continue
        print(p)
        last_p_id = p[2].address()

    print(srtf.waiting_time())



if __name__ == "__main__":
    main()