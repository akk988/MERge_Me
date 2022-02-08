# Triggering the entire project

import constants as const
import helpers as help
import timeit
import psutil


def run():
    # Creating new instance of the class Merge
    MERge = help.Merge()
    # Merging the intervals
    print('Zusammengeführte Intervalle: ', MERge.merge(const.INTERVALS))


# running the method "run" directly, calculating run time and memory consumption
if __name__ == '__main__':

    # calculates the run time of the program
    start = timeit.default_timer()

    # runs the program to merge intervals and calculate RAM usage
    process = psutil.Process(run())
    print('RAM usage:                   ',
          process.memory_info()[0] / float(2 ** 20), ' MiB')

    stop = timeit.default_timer()
    print('Laufzeit:                    ', stop - start)
