import process_list
from test import test_data1, test_data2, test_data3, test_data4, test_data5, test_data6

class SJFProcess(process_list.Process):
    def __init__(self, process, initial_time):
        # super(SJFProcess, self).__init__(*args, **kwargs)

        if not isinstance(process, process_list.Process):
            raise TypeError("{} is not Process class".format(process))

        self.predicted_time = initial_time
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

    def predict_next_burst(self, alpha):
        predicted_time = (alpha * self.actual_time) + ((1 - alpha) * self.predicted_time)
        # print("{}: next={}".format(self.id, next_predicted_time))
        return predicted_time


        

class SJFList(process_list.ProcessList):
    def __init__(self, alpha=0.5, initial_guess=5, data=None):
        super(SJFList, self).__init__(data=data)
        
        self._alpha = alpha
        self._list = [SJFProcess(x, initial_guess) for x in self._list]
        self._process_performance = {}
        for proc in self._list:
            self._process_performance[proc.id] = {"actual": 0, "predicted": initial_guess}
    def _sorted_by_next_predicted_time(self):
        self._list = sorted(self._list, key=lambda k, alpha=self._alpha: k.predict_next_burst(alpha))

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
        earliest_procs += [x for x in process_list
            if x.arrive_time == earliest_procs[0].arrive_time
            and x.id != earliest_procs[0].id]

        return earliest_procs
        
        



def main():
    sjf = SJFList(data=test_data6)
    print(sjf)
    
    x = sjf.pop_earliest()
    print(x[0])



if __name__ == "__main__":
    main()