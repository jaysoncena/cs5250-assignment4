import process_list
from test import test_data1, test_data2, test_data3, test_data4, test_data5, test_data6, test_data7

class SJFProcess(process_list.Process):
    def __init__(self, process, initial_time):
        # super(SJFProcess, self).__init__(*args, **kwargs)

        if not isinstance(process, process_list.Process):
            raise TypeError("{} is not Process class".format(process))

        self.initial_time = initial_time
        self.predicted_time = -1
        self.actual_time = 0
        
        self.convert_from_process(process)

    def convert_from_process(self, process):
        if not isinstance(process, process_list.Process):
            raise ValueError("{} is not Process class".format(process))

        self.id = process.id
        self.arrive_time = process.arrive_time
        self.burst_time = process.burst_time
        self.total_waiting_time = process.total_waiting_time
        self.last_preempt_time = process.last_preempt_time


class SJFList(process_list.ProcessList):
    def __init__(self, alpha=0.5, initial_guess=5, data=None):
        # assigns data to self._list
        super(SJFList, self).__init__(data=data)
        
        self._alpha = alpha
        self._list = [SJFProcess(x, initial_guess) for x in self._list]
        self._process_history = {}
        for proc in self._list:
            self._process_history[proc.id] = {"actual": -1, "predicted": initial_guess}

    def pop_earliest(self):
        """
            1. get the list
            2. sort by arrive_time
            3. get the earliest process
            4. get the arrive_time of the earliest process
            5. look for the same arrive_time and put to earliest_procs[]
            6. sort earliest_procs by burst_time
            7. get earliest_procs[0]
            8. delete earliest_procs[0] from self._list
            9. return earliest_procs[0]
        """
        process_list = self._list
        # 1. sort by arrive_time
        process_list = sorted(process_list, key=lambda p: p.arrive_time)

        # we don't have anything on process_list
        if len(process_list) < 1:
            return None

        # 2. get the earliest process
        earliest_procs = [process_list[0]]
        # del process_list[0]
        # 4. get the arrive_time of the earliest process
        # 5. look for the same arrive_time and put to earliest_procs[]
        earliest_procs += [x for x in process_list
            if x.arrive_time == earliest_procs[0].arrive_time
            and x.id != earliest_procs[0].id]

        if len(earliest_procs) < 1:
            # this looks like a dead code block to me
            return None
        elif len(earliest_procs) == 1:
            # if earliest_procs is just 1, there's no reason to sort this
            p = earliest_procs[0]
            p_index = self._list.index(p)
            self._list.index
            del self._list[p_index]
            return p
        # else

        # 6. sort earliest_procs by predicted time
        earliest_procs = sorted(earliest_procs, key=lambda p: self.proc_predict_next_time(p))
        # 7. get earliest_procs[0]
        p = earliest_procs[0]
        p_index = self._list.index(p)
        # 8. delete earliest_procs[0] from self._list
        del self._list[p_index]
        
        # 9. return earliest_procs[0]
        return p

    def proc_predict_next_time(self, proc):
        p = self._process_history[proc.id]
        if p["actual"] == -1:
            return p["predicted"]
        return (self._alpha * p["actual"]) + ((1 - self._alpha) * p["predicted"])

    def iter(self):
        current_time = 0
        while self._list:
            p = self.pop_earliest()

            if current_time < p.arrive_time:
                current_time = p.arrive_time

            p.update_waiting_time(current_time)

            yield (current_time, p.id, self.proc_predict_next_time(p), p)
            # update actual and predicted
            self._process_history[p.id]["predicted"] = self.proc_predict_next_time(p)
            self._process_history[p.id]["actual"] = p.burst_time

            current_time += p.burst_time

            self._total_waiting_time += p.total_waiting_time
            self._total_queued_process += 1
        

# this main() is for testing only
def main():
    # for i in range(1,100):
    #     alpha = i / float(100)
    #     sjf = SJFList(data=test_data7, alpha=alpha)
        
    #     total_waiting_time = 0
    #     schedule_count = 0
    #     for p in sjf.iter():
    #         print((p[0], p[1]))

    #         schedule_count += 1
    #         total_waiting_time += (p[0] - p[3].arrive_time)
    #         # print(p)
    #     print("Average waiting time for alpha={}: {}".format(alpha, total_waiting_time / schedule_count))

        # for i in range(1,100):
    alpha = 0.5
    sjf = SJFList(data=test_data7, alpha=alpha)
    
    total_waiting_time = 0
    schedule_count = 0
    for p in sjf.iter():
        print((p[0], p[1]))

        schedule_count += 1
        total_waiting_time += (p[0] - p[3].arrive_time)
        # print(p)
    print("Average waiting time for alpha={}: {}".format(alpha, total_waiting_time / schedule_count))
    print(sjf.waiting_time())


if __name__ == "__main__":
    main()