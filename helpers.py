#import input_output as ip

# Create class called Merge inheriting from  the upper level class Object
class Merge(object):

    # define the init method, for instantiating the object when it's created
    def __init__(self):
        pass

    # define method called merge with two or more intervals as arguement and returns merged intervals as a stack
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
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
        # Adding the first (smallest) interval to the stack
        stack.append(intervals[0])
        # Comparing the end of the interval appended to the stack (called "last_element") to the end of the next intervalls in a for loop
        for i in range(1, len(intervals)):
            last_element = stack[len(stack)-1]
            # comparing the end (e.g. 3) of the first interval (e.g. [1, 3]) with the start (e.g. 1) of the second/next range (e.g. [1, 5])
            # In case there is an overlaping, then a merge will be operated
            if last_element[1] >= intervals[i][0]:
                # set the end of the last_element to be equal to the larger number between the two ends of the compared intervalls (e.g. 5 > 3 --> end of last-element = 5)
                last_element[1] = max(intervals[i][1], last_element[1])
                # deleting the first interval ( [1, 3]) from the stack and adding the extended last_element
                stack.pop(len(stack)-1)
                stack.append(last_element)
            # In case there is no overlaping, the interval will be added to the stack as it is.
            else:
                stack.append(intervals[i])
        return stack

    # define a method which takes an array and a range (e.g. from 0 to 5) and return a pivot-index to be used in the quicksort method
    def partition(self, array, start, end):
        # initializing pivot's index equal to the start of the range (e. g. 0)
        pivot_index = start
        for i in range(start, end):
            # place all elements smaller than the pivot to the left of the pivot
            if array[i][0] <= array[end][0]:
                array[i], array[pivot_index] = array[pivot_index], array[i]
                pivot_index += 1
        array[end], array[pivot_index] = array[pivot_index], array[end]
        return pivot_index

    # define a method which partitions the given array around a picked pivot (partition_index).
    def quicksort(self, array, start, end):
        if start < end:
            partition_index = self.partition(array, start, end)
            self.quicksort(array, start, partition_index-1)
            self.quicksort(array, partition_index + 1, end)


# Creating new instance of the class
#mer = Merge()
#intervalls = input()
#print('Input, ' + intervalls)
# Calling merge method of class Merge and passing in the intervals
#print('Output, ' + mer.merge([intervalls]))
#print(mer.merge([[1, 3], [1, 5], [3, 7], [11, 14], [8, 10], [15, 18]]))
