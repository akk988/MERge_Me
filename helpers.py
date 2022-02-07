#import input_output as ip

# Create class called Merge inheriting from  the upper level class Object
class Merge(object):

    # define the init method, for instantiating the object when it's created
    def __init__(self):
        pass

    # define method called merge with two or more intervals as arguement and returns merged intervals as a stack
    def merge(self, intervals):

        # return an empty array if no intervals where entered
        if len(intervals) == 0:
            return []

        # sorting the intervals using quicksort method
        self.quicksort(intervals, 0, len(intervals)-1)

        # printing out the sorted intervals
        # for i in intervals:
        #    print(i[0], i[1])

        # defining an array called stack to store the merged intervals
        stack = []

        return stack

    # define a method which takes an array and a range (e.g. from 0 to 5) and return a pivot-index to be used in the quicksort method
    def partition(self, array, start, end):
        # initializing pivot's index equal to the start of the range (e. g. 0)
        pivot_index = start

        return pivot_index

    # define a method which partitions the given array around a picked pivot (partition_index).
    def quicksort(self, array, start, end):

        # Creating new instance of the class
        #mer = Merge()
        #intervalls = input()
        #print('Input, ' + intervalls)
        # Calling merge method of class Merge and passing in the intervals
        #print('Output, ' + mer.merge([intervalls]))
        #print(mer.merge([[1, 3], [1, 5], [3, 7], [11, 14], [8, 10], [15, 18]]))
