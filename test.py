from process_list import Process
from asg4 import rr, srtf

test_data1 = [
    Process(0, 0, 9),
    Process(1, 1, 2),
    Process(2, 2, 1)
]

test_data2 = [
    Process(0, 0, 7),
    Process(1, 1, 6),
    Process(2, 2, 9),
    Process(3, 3, 10)
]

test_data3 = [
    Process(0, 0, 9),
    Process(1, 5, 2),
    Process(2, 6, 1)
]

test_data4 = [
    Process(0, 0, 1)
]

# testing wait time
test_data3 = [
    Process(0, 0, 1),
    Process(1, 5, 3),
    Process(2, 6, 2)
]

# from lecture
test_data4 = [
    Process(1, 0, 24),
    Process(2, 0, 3),
    Process(3, 0, 3)
]

# simulate out-of-order burst_time
test_data5 = [
    # t, p, b
    Process(0, 0, 9),
    Process(1, 1, 2),
    Process(2, 2, 1),
    Process(3, 3, 12),
]

test_data6 = [
    # id, t, b
    Process(1, 0, 9),
    Process(2, 0, 2),
    Process(3, 2, 1),
    Process(4, 2, 4),
    Process(5, 3, 2)
]


def srtf_test():
    previous_pid = -1

    for line in srtf(test_data5):
        # if previous_pid != line[1].id:
            print(line)
            # previous_pid = line[1].id
    # asg4.srtf(test_data5)
    # for line in

def rr_test():
    for line in rr(test_data4, quantum=4):
        print(line)

if __name__ == "__main__":
    srtf_test()