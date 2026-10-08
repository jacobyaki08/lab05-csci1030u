# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    # TODO: add an optional flag -i / --ignore-case  (use action="store_true")
    parser.add_argument("-i", "--ignore-case", action="store_true", help="ignore case distinctions")
    args = parser.parse_args()

    # TODO: open args.filename and read its lines. For each line, numbered starting
    #   at 1, print "<number>: <line>" when the line contains args.pattern.
    #   If the --ignore-case flag was given, match without caring about upper/lower
    #   case (hint: compare the lowercased versions of both).

    with open(args.filename, "r") as f:
        for number, line in enumerate(f, start=1):
          line_to_check = line.lower() if args.ignore_case else line
          pattern_to_check = args.pattern.lower() if args.ignore_case else args.pattern
          
          if pattern_to_check in line_to_check:
                         print(f"{number}: {line.rstrip('\n')}")
        


if __name__ == "__main__":
    main()
