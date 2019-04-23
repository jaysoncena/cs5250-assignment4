#!/usr/bin/env python3

import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scheduler",
        choices=["rr", "sjf", "srtf"],
        help="Choose your process scheduler: rr (Round Robin), sjf (Shortest Job First) or srtf (Shortest Remaining Time First)")
    parser.add_argument("--quantum",
        type=int,
        help="Only applicable to Round Robin, will be ignored for other scheduler algorithms")
    parser.add_argument("--alpha",
        type=float,
        help="Only applicable to Shortest Job First, will be ignored for other scheduler algorithms")
    parser.add_argument("--initial_guess",
        type=int,
        help="Only applicable to Shortest Job First, will be ignored for other scheduler algorithms")
    args = parser.parse_args()
    custom_args(parser, args)

    lines = input_parser("/dev/stdin")
    print(lines)


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


if __name__ == "__main__":
    main()