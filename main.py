#!/usr/bin/env python3

import argparse
import re

import process_list
import fcfs
import rr
import sjf
import srtf


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("scheduler",
        default="all",
        choices=["fcfs","rr", "sjf", "srtf", "all"],
        help="Choose your process scheduler:\nall (Run all scheduler)\nfcfs (First-Come-First-Serve)\nrr (Round Robin)\nsjf (Shortest Job First)\nsrtf (Shortest Remaining Time First)")
    parser.add_argument("--quantum",
        type=int,
        default=4,
        help="Only applicable to Round Robin, will be ignored for other scheduler algorithms")
    parser.add_argument("--alpha",
        type=float,
        default=0.5,
        help="Only applicable to Shortest Job First, will be ignored for other scheduler algorithms")
    parser.add_argument("--initial_guess",
        type=int,
        default=5,
        help="Only applicable to Shortest Job First, will be ignored for other scheduler algorithms")
    args = parser.parse_args()
    custom_args(parser, args)

    raw_processes = input_parser("/dev/stdin")

    print("printing input ----")
    for p in raw_processes:
        print(process_list.Process(*p))


    if args.scheduler == "fcfs":
        print("simulating FCFS ----")
        output = fcfs.runner(raw_processes)
        writer(output, "FCFS.txt")
        print("FCFS: {}".format(output[-1]))
    elif args.scheduler == "rr":
        print("simulating RR ----")
        output = rr.runner(raw_processes, args.quantum)
        writer(output, "RR.txt")
        print("RR: {}".format(output[-1]))
    elif args.scheduler == "sjf":
        print("simulating SJF ----")
        output = sjf.runner(raw_processes, args.alpha, args.initial_guess)
        writer(output, "SJF.txt")
        print("SJF: {}".format(output[-1]))
    elif args.scheduler == "srtf":
        print("simulating SRTF ----")
        output = srtf.runner(raw_processes)
        writer(output, "SRTF.txt")
        print("SRTF: {}".format(output[-1]))
    elif args.scheduler == "all":
        print("simulating FCFS ----")
        output = fcfs.runner(raw_processes)
        writer(output, "FCFS.txt")
        print("FCFS: {}".format(output[-1]))
        print("simulating RR ----")
        output = rr.runner(raw_processes, args.quantum)
        writer(output, "RR.txt")
        print("RR: {}".format(output[-1]))
        print("simulating SJF ----")
        output = sjf.runner(raw_processes, args.alpha, args.initial_guess)
        writer(output, "SJF.txt")
        print("SJF: {}".format(output[-1]))
        print("simulating SRTF ----")
        output = srtf.runner(raw_processes)
        writer(output, "SRTF.txt")
        print("SRTF: {}".format(output[-1]))
    else:
        print("!! ERROR: code path should not go here")


def custom_args(parser, args):
    if args.scheduler == "rr" and not args.quantum:
        parser.error("Round-robin scheduler requires QUANTUM argument")
    if args.scheduler == "sjf":
        if not (args.alpha and args.initial_guess):
            parser.error("Shortest Job First requires ALPHA and INITIAL_GUESS arguments")
        elif not (args.alpha > 0 and args.alpha < 1):
            parser.error("ALPHA argument should be between 0 and 1")


def input_parser(f):
    ret = []
    parse_line = re.compile(r"^(\d+) +(\d+) +(\d+)$")

    with open(f) as fh:
        line = fh.readline().strip()
        
        parsed = parse_line.match(line)
        if parsed:
            ret.append([int(x) for x in parsed.groups()])

        line_count = 1
        while line:
            if line is None:
                continue
            line = fh.readline().strip()
            
            parsed = parse_line.match(line)
            if parsed:
                ret.append([int(x) for x in parsed.groups()])

            line_count += 1

    return ret

def writer(arr, f):
    with open(f, "w") as fh:
        for line in arr:
            fh.write("{}\n".format(line))


if __name__ == "__main__":
    main()