import asg4

def main():
    rr_test1()

def rr_test1():
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

    for line in asg4.rr(test_data3):
        print(line)

if __name__ == "__main__":
    main()