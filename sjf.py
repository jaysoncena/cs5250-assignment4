import process_list
# from test import test_data4

test_data4 = [
    process_list.Process(1, 0, 24),
    process_list.Process(2, 0, 3),
    process_list.Process(3, 0, 3)
]

class SJFProcess(process_list.Process):
    def __init__(self, process, initial_time):
        # super(SJFProcess, self).__init__(*args, **kwargs)

        if not isinstance(process, process_list.Process):
            raise ValueError("{} is not Process class".format(process))

        self.predicted_time = initial_time
        self.actual_time = -1
        
        self.convert_from_process(process)

    def convert_from_process(self, process):
        if not isinstance(process, process_list.Process):
            raise ValueError("{} is not Process class".format(process))

        self.id = process.id
        self.arrive_time = process.arrive_time
        self.burst_time = process.burst_time
        self.total_waiting_time = process.total_waiting_time
        self.last_preempt_time = process.last_preempt_time

    def _sort_by_sjf(self):
        pass


        

class SJFList(process_list.ProcessList):
    def __init__(self, alpha=0.5, initial_time=5, data=None):
        super(SJFList, self).__init__(data=data)

        self._list = [SJFProcess(x, initial_time) for x in self._list]

        # self._alpha = alpha
        # self._pid_last_time = dict([(k.id, initial_time) for k in self._list])
        # # self._sort_by_sjf()

    # def _sort_by_sjf(self):
    #     self._list = sorted(self._list, key=lambda k, t=self._pid_initial_time: t[k.id])


def main():
    sjf = SJFList(data=test_data4)
    for item in sjf._list:
        print(item)


if __name__ == "__main__":
    main()