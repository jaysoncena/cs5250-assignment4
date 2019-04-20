import asg4

test_data1 = [
    asg4.Process(0, 0, 9),
    asg4.Process(1, 1, 2),
    asg4.Process(2, 2, 1)
]

test_data2 = [
    asg4.Process(0, 0, 7),
    asg4.Process(1, 1, 6),
    asg4.Process(2, 2, 9),
    asg4.Process(3, 3, 10)
]

test_data3 = [
    asg4.Process(0, 0, 9),
    asg4.Process(1, 5, 2),
    asg4.Process(2, 6, 1)
]

test_data4 = [
    asg4.Process(0, 0, 1)
]

# testing wait time
test_data3 = [
    asg4.Process(0, 0, 1),
    asg4.Process(1, 5, 3),
    asg4.Process(2, 6, 2)
]

# from lecture
test_data4 = [
    asg4.Process(1, 0, 24),
    asg4.Process(2, 0, 3),
    asg4.Process(3, 0, 3)
]

# simulate out-of-order burst_time
test_data5 = [
    # t, p, b
    asg4.Process(0, 0, 9),
    asg4.Process(1, 1, 2),
    asg4.Process(2, 2, 1),
    asg4.Process(3, 3, 12),
]


def srtf_test():
    previous_pid = -1

    for line in asg4.srtf(test_data5):
        # if previous_pid != line[1].id:
            print(line)
            # previous_pid = line[1].id
    # asg4.srtf(test_data5)
    # for line in

def rr_test():
    for line in asg4.rr(test_data4, quantum=4):
        print(line)

if __name__ == "__main__":
    srtf_test()