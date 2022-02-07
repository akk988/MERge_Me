# Triggering the entire project
import constants as const
import helpers as help
import timeit


def run():
    # Creating new instance of the class Merge
    MERge = help.Merge()
    # Merging the intervals
    print(MERge.merge(const.INTERVALS))


# running the method run directly
if __name__ == '__main__':
    # calculates the run time of the program
    start = timeit.default_timer()
    # runs the program to merge intervals
    run()
    stop = timeit.default_timer()
    print('Laufzeit: ', stop - start)
