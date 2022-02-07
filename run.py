# Triggering the entire project
import constants as const
import helpers as help


def run():
    # Creating new instance of the class Merge
    MERge = help.Merge()
    # Merging the intervals
    print(MERge.merge(const.INTERVALS))


# running the method run directly
if __name__ == '__main__':
    run()
