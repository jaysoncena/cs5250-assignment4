import process_list

def FCFS_scheduling(process_list):
    #store the (switching time, proccess_id) pair
    schedule = []
    current_time = 0
    waiting_time = 0
    for process in process_list:
        if(current_time < process.arrive_time):
            current_time = process.arrive_time
        schedule.append((current_time,process.id))
        waiting_time = waiting_time + (current_time - process.arrive_time)
        current_time = current_time + process.burst_time
    average_waiting_time = waiting_time/float(len(process_list))
    return schedule + ["Average waiting time {:.2f}".format(average_waiting_time)]


def runner(raw_processes):
    # processes = []
    # for p in raw_processes:
    #     processes.append(process_list.Process(*p))

    # lines = []
    # srtf = SRTFList(data=processes)
    # last_p_id = None
    # for p in srtf.iter():
    #     if last_p_id == p[2].address():
    #         continue
    #     lines.append("({}, {})".format(p[0], p[1]))
    #     last_p_id = p[2].address()
    
    # lines.append(srtf.waiting_time())

    # return lines
    processes = []
    for p in raw_processes:
        processes.append(process_list.Process(*p))

    return FCFS_scheduling(processes)
        

if __name__ == "__main__":
    main()