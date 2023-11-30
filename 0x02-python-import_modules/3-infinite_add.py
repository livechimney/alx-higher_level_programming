#!/usr/bin/python3
import sys, math

if __name__ == "__main__":
    result = 0
    for i in sys.argv[1:]:
        result += int(i)
        print("{}".format(result))
