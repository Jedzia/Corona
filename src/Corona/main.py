import argparse
import os
import sys
from time import sleep

from Corona.Virus import Virus


# print("Hello from the Repository Tool")


def main(args):
    """Main entry point for external applications
    Args:
        args ([str]): command line arguments
    """
    # see https://github.com/pyscaffold/pyscaffold/blob/master/src/pyscaffold/cli.py
    print("Your personal devastation calculator is starting up. Please wait...")
    sleep(2)
    print()
    cwd = os.getcwd()
    # print("os.getcwd(): \t\t\t\t\t\t" + cwd)

    own_path = os.path.dirname(os.path.realpath(__file__))
    # print("os.path.dirname(os.path.realpath(__file__)): \t\t" + own_path)
    # print("dirname(abspath(file)): \t\t\t\t" + dirname(abspath(own_path)))
    # print("dirname(dirname(abspath(file))): \t\t\t" + dirname(dirname(abspath(own_path))))

    # file = os.path.dirname(os.path.realpath(__file__))

    # Program arguments
    ap = argparse.ArgumentParser()
    # Add the arguments to the parser
    # ap.add_argument('integers', metavar='N', type=int, nargs='+',
    #                    help='an integer for the accumulator')
    ap.add_argument('days', metavar='N', type=int,
                    help='Days to do the morbid business')
    # ap.add_argument("-d", "--days", required=False,
    #                help="Days to do the morbid business")
    ap.add_argument("-s", "--spreadrate", required=False,
                    help="Virus Spread Rate")
    # args = vars(ap.parse_args())
    args = ap.parse_args()
    days = 10
    #    if args[0]:
    #        days = args[0]
    days = args.days
    print("Range of days to calculate: ", days)
    virus = Virus(own_path, "COVID-19")
    virus.statistics(days)


if __name__ == '__main__':
    main(sys.argv[1:])
