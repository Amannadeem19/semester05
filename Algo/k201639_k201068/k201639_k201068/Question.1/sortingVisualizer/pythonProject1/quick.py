# Python3 implementation of QuickSort
import time
from tkinter import *
from tkinter import ttk
import math

LRec = []
RRec = []
MRec = []
ins = []
out = []
out1 = []
swap = 0
comp = 0
partition1 = 0
call = 0


# Function to find the partition position
def partition(array, low, high, drawdata, speed):
    global ins, out, out1, swap, comp
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    temp = ""
    for j in range(low, high):
        comp += 1
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            swap += 1
            i = i + 1

            # element before swapping

            drawdata(array, ["pink" if x == i or x == j else "black" for x in range(len(array))]);
            time.sleep(speed);
            st = "Element("
            st += str(array[i])
            st += ") "
            st += "smaller than or equal to pivot( "
            st += str(array[j])
            st += ") found, Swapping both"

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            # element after swapping
            drawdata(array,
                     ["coral" if x == i or x == j else "black" for x in range(len(array))]);
            time.sleep(speed);
            temp += st
            temp += "-->"
    swap += 1
    comp += 1
    ins.append(temp)
    st1 = "Swapping the pivot("
    st1 += str(array[high])
    st1 += ") "
    st1 += "with the greater element("
    st1 += str(array[high])
    st1 += ") "
    out.append(st1)

    st3 = "Now all elements to the left of Partioned Element( "
    st3 += str(array[high])
    st3 += " are smaller and higher elements present at it's right"
    out1.append(st3)

    # Swap the pivot element with
    # e greater element specified by i
    drawdata(array, ["linen" if x == i + 1 or x == high else "black" for x in range(len(array))]);
    time.sleep(speed);
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    drawdata(array,
             ["thistle" if x == i + 1 or x == high else "black" for x in range(len(array))]);
    time.sleep(speed);
    # drawdata(array, ["Red" if x==i+1 else "black" for x in range(len(array))]);
    # time.sleep(speed);
    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort


def quick_sort(array, low, high, drawdata, speed):
    if low < high:
        global partition1, call
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        partition1 += 1
        pi = partition(array, low, high, drawdata, speed)
        global LRec, RRec, MRec
        strin = ""
        for i in range(len(array)):
            if (i >= low and i <= high):
                strin += str(array[i])
                strin += " "
        MRec.append(strin)

        strin1 = ""
        for i in range(len(array)):
            if (i >= low and i <= pi - 1):
                strin1 += str(array[i])
                strin1 += " "
        LRec.append(strin1)

        strin2 = ""
        for i in range(len(array)):
            if (i >= pi + 1 and i <= high):
                strin2 += str(array[i])
                strin2 += " "
        RRec.append(strin2)
        # Recursive call on the left of pivot

        drawdata(array, ["cyan" if x >= low and x <= pi - 1 else "black" for x in range(len(array))]);
        time.sleep(speed);
        call += 1
        quick_sort(array, low, pi - 1, drawdata, speed)

        drawdata(array, ["yellow" if x >= pi + 1 and x <= high else "black" for x in range(len(array))]);
        time.sleep(speed);
        # Recursive call on the right of pivot
        call += 1
        quick_sort(array, pi + 1, high, drawdata, speed)


def win(array, drawdata, speed):
    # Driver code
    # array = [10, 7, 8, 9, 1, 5]
    #     quick_sort(array, 0, len(array) - 1)
    # drawData(array, ['Green' for x in range(len(array))])
    global ins, out, out1, LRec, MRec, RRec, partition1, call, swap, comp
    quick_sort(array, 0, len(array) - 1, drawdata, speed)
    drawdata(array, ['Green' for x in range(len(array))])
    root1 = Tk()
    root1.title("Iterations")
    root1.config(bg="white")

    root1.geometry()

    scroll_bar = Scrollbar(root1)
    scroll_h = Scrollbar(root1, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")
    scroll_bar.pack(side=RIGHT,
                    fill=Y)

    lb = Listbox(root1, yscrollcommand=scroll_bar.set, width=1000)
    lb.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=lb.yview)
    scroll_h.config(command=lb.xview)

    i = 0
    while i < len(MRec):
        lb.insert('end', str(i + 1) + " Record:")
        lb.insert('end', "Finding Partioning Index on:")
        lb.insert('end', MRec[i])

        lb.insert('end', "Partioning Swappings:")
        # lb.insert('end', "Finding Partioning Index on:")
        lb.insert('end', ins[i])
        lb.insert('end', out[i])
        lb.insert('end', out1[i])

        lb.insert('end', "Elements to the left of partition are:")
        # lb.insert('end', "Finding Partioning Index on:")
        lb.insert('end', LRec[i])

        lb.insert('end', "Elements to the right of partition are:")
        # lb.insert('end', "Finding Partioning Index on:")
        lb.insert('end', RRec[i])

        lb.insert('end', "----------------------------------------------")
        lb.insert('end', "")

        i += 1

    lb.insert('end', "Final Array:")
    # lb.insert('end', "Finding Partioning Index on:")

    lb.insert('end', ' '.join(map(str, array)))
    lb.insert(END, "QUICK SORT COMPLETED")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "SPACE COMPLEXITY: ")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "FOR ALGORITHM: ")
    lb.insert(END, "pi = partition(array, low, high,drawdata, speed): ------> O(1)")
    lb.insert(END, "strin = "": ------> 0(1)")
    lb.insert(END, "for i in range(len(array)): ------> O(1) for i")
    lb.insert(END, "strin1 = "": ------> O(1)")
    lb.insert(END, "strin2 = "": ------> O(1)")
    lb.insert(END, "pivot = array[high]: ------> O(1)")
    lb.insert(END, "i = low - 1: ------> O(1)")
    lb.insert(END, "temp = "": ------> O(1)")
    lb.insert(END, "for j in range(low, high):: ------> O(1) for j")
    lb.insert(END, "st = Element(: ------> O(1)")
    lb.insert(END, "st1 = Swapping the pivot(: ------> O(1)")
    lb.insert(END, "st3 = Now all elements to the left of Partioned Element(: ------> O(1)")
    lb.insert(END, "FOR DRY RUN: ")
    lb.insert(END, "LRec=[]: ------> O(1)")
    lb.insert(END, "RRec=[]: ------> 0(1)")
    lb.insert(END, "MRec=[]: ------> O(1)")
    lb.insert(END, "ins= []: ------> O(n)")
    lb.insert(END, "out= []: ------> O(n)")
    lb.insert(END, "out1= []: ------> O(n)")
    lb.insert(END, "call = 0 ------> O(1)")
    lb.insert(END, "partitions1 = 0 ------> O(1)")
    lb.insert(END, "comp = 0 ------> O(1)")
    lb.insert(END, "swap = 0 ------> O(1)")
    lb.insert(END,
              "def quick_sort(array, 0, len(array) - 1,drawdata, speed) ------> O(n) for array, 0(1) for speed")
    lb.insert(END,
              "def partition(array, low, high,drawdata, speed): ------> O(n) for array, 0(1) for speed, O(1) for low, O(high) for high")
    lb.insert(END, "\n")
    lb.insert(END, "FOR VISUALIZATION: ")
    lb.insert(END, "can_height = 380: ------> O(1) for can_height")
    lb.insert(END, "can_width = 1000: ------> O(1) for can_width")
    lb.insert(END, "x_width = can_width/(len(data) + 1): ------> O(1) for x_width")
    lb.insert(END, "offset = 30: ------> O(1)")
    lb.insert(END, "spacing = 8: ------> O(1)")
    lb.insert(END, "normalized_data = [i / max(data) for i in data]: ------> O(1) for normalized_data")
    lb.insert(END, "for i, height in enumerate(normalized_data): ------> O(1) for i, height")
    lb.insert(END, "x0 = i*x_width + offset + spacing: ------> O(1) for x0")
    lb.insert(END, "y0 = can_height - height*340: ------> O(1) for y0")
    lb.insert(END, "x1 = ((i+1)*x_width) + offset: ------> O(1) for x1")
    lb.insert(END, "y1 = can_height: ------> O(1) for y1")
    lb.insert(END, "def drawData(data, colorlist): ------> O(n) for data, colorlist")
    lb.insert(END, "\n")
    lb.insert(END, "ALGORITHM'S SPACE COMPLEXITY -----> O(1)")
    lb.insert(END, "FINAL SPACE COMPLEXITY (Including Array Size Passed/Iterative Containers)-----> O(1) + O(n) = O(n)")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "TIME COMPLEXITY: ")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "BEST: O(nlogn)------>" + str(len(array) * math.log(len(array))))
    lb.insert(END, "WORST: O(n^2)------>" + str(len(array) * len(array)))
    lb.insert(END, "Partitions -----> " + str(partition1))
    lb.insert(END, "Calls -----> " + str(call))
    lb.insert(END, "Swappings -----> " + str(swap))
    lb.insert(END, "Comparisions -----> " + str(comp))
    lb.insert(END, "Total -----> " + str(comp + swap + call + partition1))
    partition1 = 0
    call = 0
    swap = 0
    comp = 0
# partition1
# print(f'Sorted array: {array}')
