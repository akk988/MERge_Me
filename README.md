# Coding_Challenge_Private
Coding Task 2. Deadline 14.02.2022

# MERGE
This merge function were implemmented as a solution to Coding Task 2

# Program Discription
Python was chosen as the programming language to implement the MERGE function because it offers many libraries for data processing.
The program implements a merge function that takes a list of intervals and returns a list of merged intervals as a result, where all overlapping intervals should be merged and all non-overlapping intervals are unaffected.
The merging of the intervals is based on a sorting algorithm, which is the basic building block of the program. To implement an efficient merging algorithm, an efficient sorting algorithm should be chosen.
The **Quicksort** algorithm was chosen for use because it has linear complexity. This algorithm applies the divide-and-conquer principle to split the input array into two lists (partitioning), and then sorts both lists recursively until the resulting list is fully sorted.
A method has been prepared for partitioning the list, which takes an array, a start value and an end value and returns the pivot indext value. Then the list is partitioned around the selected pivot index using the quicksort method.
A method called merge has been prepared to merge the specified intervals after sorting them using the quicksort method.
To measure the runtime, a default timer was started before running the program and stopped after merfing.
os and psutil Python libraries were used to calculate RAM usage. Information about running processes can be retrieved with psutil. 

# Project Structure
The project structure contains three python files: 
- helper.py 
- constants.py 
- run.py

The helper contains the methods, e.g. for sorting, merging. In the constants.py there is the array Intervals which should be merged. And the run.py is for running the program. 

# Docker

A Dockerfile were prepared for the project. When Docker is installed on the machine, the following command can build the Docker Image
```
docker build -t merge .
```
To run a Docker Container from the Docker Image, the following command can be used:

```
docker run merge 
```

# Testing the program
In the project the following Input were given:

INTERVALS = [[1, 2], [1, 7], [8, 11], [11, 14], [8, 10], [32, 36], [33, 35], [105, 108]]

The resulted merged Output was:   [[1, 7], [8, 14], [32, 36], [105, 108]]

# Run Time

The absolute runtime on a VM, Ubuntu x86_64 GNU/Linux, is: **0.0008698925375938416 seconds**
The absolute runtime on a PC, MS Windows 10 LTSC x64 with 2.6 GHz CPU and 16GB RAM is: **0.0002486000012140721 seconds**

The robustness can be ensured with a time-efficient sorting algorithm that has a linear complexity, such as the merge sort or quick sort with O(n log(n)). In addition, the computing power of the computer / server plays an important role.
Mergesort and Quicksort are very efficient sorting algorithms. They are based on the divide and conquer approach.


# RAM Usage

The measured value of memory consumption of the sorting and merging process was **12.12890625 MiB**

# Sources

- https://docs.python.org/

- https://realpython.com

- https://openbook.rheinwerk-verlag.de/python/

- https://andreaheilrath.github.io

- https://www.geeksforgeeks.org/quick-sort/

- https://stackoverflow.com
