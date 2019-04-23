from asg4 import rr, srtf, Process
from process_list import Process

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

# from the assignment
test_data7 = [
    # id, t, b
    Process(0, 0, 9),
    Process(1, 1, 8),
    Process(2, 2, 2),
    Process(3, 5, 2),
    Process(3, 30, 5),
    Process(4, 30, 2),#
    Process(5, 30, 3),#
    Process(1, 31, 2),
    Process(2, 32, 6),
    Process(0, 38, 8),
    Process(2, 60, 7),
    Process(0, 62, 2),
    Process(1, 65, 3),
    Process(3, 66, 8),
    Process(4, 66, 2),#
    Process(5, 66, 3),#
    Process(1, 90, 10),
    Process(0, 95, 10),
    Process(2, 98, 9),
    Process(3, 99, 8),
]

# process arrive_time with huge gap
test_data8 = [
    # id, t, b
    Process(1, 0, 2),
    Process(2, 0, 3),
    Process(3, 0, 3),
    Process(4, 20, 5),
    Process(5, 21, 3)
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