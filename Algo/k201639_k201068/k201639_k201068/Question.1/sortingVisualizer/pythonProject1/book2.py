import time
from tkinter import *
from tkinter import ttk
import math

leftpart = []
rightpart = []
partitions = []
inser = []
insersub = []
call = 0
partitions1 = 0
comp = 0
swap = 0
swap1 = 0
comp1 = 0
iter1 = 0


def modi_quick(arr, p, r, k, drawdata, speed):
    quicksort(arr, p, r, k, drawdata, speed)
    insertion_sort(arr, p, r, drawdata, speed)


def quicksort(arr, p, r, k, drawdata, speed):
    global partitions1, call
    if r - p > k:
        strin = ""
        partitions1 += 1
        q = partition(arr, p, r, drawdata, speed)
        for i in range(len(arr)):
            if (i >= p and i <= q):
                strin += str(arr[i])
                strin += " "
        leftpart.append(strin)
        strin1 = ""
        for i in range(len(arr)):
            if (i >= q + 1 and i <= r):
                strin1 += str(arr[i])
                strin1 += " "
        rightpart.append(strin1)
        drawdata(arr, ["cyan" if x >= p and x <= q else "black" for x in range(len(arr))]);
        time.sleep(speed);
        call += 1
        quicksort(arr, p, q, k, drawdata, speed)
        drawdata(arr, ["yellow" if x >= q + 1 and x <= r else "black" for x in range(len(arr))]);
        time.sleep(speed);
        call += 1
        quicksort(arr, q + 1, r, k, drawdata, speed)


def partition(arr, p, r, drawdata, speed):
    global swap, comp
    x = arr[r - 1]
    i = p
    j = p

    while j < r - 1:
        # iter+=1
        comp += 1
        if arr[j] <= x:
            swap += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i + 1
        j = j + 1

    comp += 1
    swap += 1
    temp = arr[i]
    arr[i] = arr[r - 1]
    arr[r - 1] = temp
    partitions.append(str(arr[i]))
    drawdata(arr, ["blue" if x == i else "black" for x in range(len(arr))]);
    time.sleep(speed);
    return i


def insertion_sort(arr, p, r, drawdata, speed):
    drawdata(arr, ["white" for x in range(len(arr))]);
    time.sleep(speed);
    global iter1, comp1, swap1
    j = p + 1
    while j < r:
        iter1 += 1
        # comp1+=1
        key = arr[j]
        i = j - 1
        strin1 = ""
        drawdata(arr, ["yellow" if x == i else "green" if x < j else "blue" if x == j else "black" for x in
                       range(len(arr))]);
        time.sleep(speed);
        while i >= p and arr[i] > key:
            iter1 += 1
            swap1 += 1
            comp1 += 1
            arr[i + 1] = arr[i]
            drawdata(arr, ["pink" if x == i else "green" if x <= j else "black" for x in range(len(arr))]);
            time.sleep(speed);
            i = i - 1
            strin1 += str(arr)
            strin1 += " --> "

        comp1 += 1
        arr[i + 1] = key
        j = j + 1
        strin1 += str(arr)
        strin1 += " --> "
        insersub.append(strin1)
        inser.append(str(arr))
    drawdata(arr, ["plum" for x in range(len(arr))]);
    time.sleep(speed);


def winwo2(output, drawdata, speed, k):
    global partitions1, call, swap, comp, iter1, swap1, comp1
    n = len(output)
    modi_quick(output, 0, n, k, drawdata, speed)
    global maxelem, minelem, result, countarr
    root1 = Tk()
    root1.title("Iterations")
    root1.config(bg="white")
    root1.geometry()

    scroll_bar = Scrollbar(root1)
    scroll_h = Scrollbar(root1, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")
    scroll_bar.pack(side=RIGHT,
                    fill=Y)
    mylist1 = Listbox(root1, yscrollcommand=scroll_bar.set, xscrollcommand=scroll_h.set, width=1000)
    j = 0
    for i in leftpart:
        mylist1.insert(END, "RECORD " + str(j + 1) + ": ")
        mylist1.insert(END, "Partition Element: ")
        mylist1.insert(END, partitions[j])
        mylist1.insert(END, "Left Partition Call: ")
        mylist1.insert(END, i)
        mylist1.insert(END, "Right Partition Call: ")
        mylist1.insert(END, rightpart[j])
        mylist1.insert(END, "\n")
        j += 1
    mylist1.insert(END, "QUICK SORT COMPLETED")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    j = 0
    for i in insersub:
        mylist1.insert(END, "ITERATION " + str(j + 1) + ": ")
        mylist1.insert(END, "Sub Iterations: ")
        mylist1.insert(END, i)
        mylist1.insert(END, "Resulting Array: ")
        mylist1.insert(END, inser[j])
        mylist1.insert(END, "\n")
        j += 1
    mylist1.insert(END, "INSERTION SORT COMPLETED")
    mylist1.insert(END, "BOOK2 SORTING COMPLETED")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "SPACE COMPLEXITY: ")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR ALGORITHM: ")
    mylist1.insert(END, "strin="" ------> O(1)")
    mylist1.insert(END, "q = partition(arr, p, r, drawdata, speed): ------> 0(1) for q")
    mylist1.insert(END, "for i in range(len(arr)): ------> O(1) for i")
    mylist1.insert(END, "x = arr[r - 1] ------> O(1) for x")
    mylist1.insert(END, "i = p ------> O(1) for i")
    mylist1.insert(END, "j = p ------> O(1) for j")
    mylist1.insert(END, "temp = arr[i] ------> O(1) for temp")
    mylist1.insert(END, "call = 0 ------> O(1)")
    mylist1.insert(END, "partitions1 = 0 ------> O(1)")
    mylist1.insert(END, "comp = 0 ------> O(1)")
    mylist1.insert(END, "swap = 0 ------> O(1)")
    mylist1.insert(END, "swap1 = 0 ------> O(1)")
    mylist1.insert(END, "comp1 = 0 ------> O(1)")
    mylist1.insert(END, "iter1 = 0 ------> O(1)")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR DRY RUN: ")
    mylist1.insert(END, "leftpart = []: ------> O(n)")
    mylist1.insert(END, "rightpart = []: ------> O(n)")
    mylist1.insert(END, "partitions = []: ------> O(n)")
    mylist1.insert(END, "inser = []: ------> O(n)")
    mylist1.insert(END, "insersub = []: ------> O(n)")
    mylist1.insert(END,
                   "def modi_quick(output, 0, n, k, drawdata, speed): ------> (n) for output, (1) for n, 0(1) for k, 0(1) for speed")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR VISUALIZATION: ")
    mylist1.insert(END, "can_height = 380: ------> O(1) for can_height")
    mylist1.insert(END, "can_width = 1000: ------> O(1) for can_width")
    mylist1.insert(END, "x_width = can_width/(len(data) + 1): ------> O(1) for x_width")
    mylist1.insert(END, "offset = 30: ------> O(1)")
    mylist1.insert(END, "spacing = 8: ------> O(1)")
    mylist1.insert(END, "normalized_data = [i / max(data) for i in data]: ------> O(1) for normalized_data")
    mylist1.insert(END, "for i, height in enumerate(normalized_data): ------> O(1) for i, height")
    mylist1.insert(END, "x0 = i*x_width + offset + spacing: ------> O(1) for x0")
    mylist1.insert(END, "y0 = can_height - height*340: ------> O(1) for y0")
    mylist1.insert(END, "x1 = ((i+1)*x_width) + offset: ------> O(1) for x1")
    mylist1.insert(END, "y1 = can_height: ------> O(1) for y1")
    mylist1.insert(END, "def drawData(data, colorlist):: ------> O(n) for data, colorlist")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "ALGORITHM'S SPACE COMPLEXITY -----> O(1)")
    mylist1.insert(END,
                   "FINAL SPACE COMPLEXITY(Including Array Size Passed/Iterative Containers) -----> O(1) + O(n) = O(n)")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "TIME COMPLEXITY: ")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "All Cases: O(nlogn)------>" + str(len(output) * math.log(len(output))))
    mylist1.insert(END, "Partitions -----> " + str(partitions1))
    mylist1.insert(END, "Calls -----> " + str(call))
    mylist1.insert(END, "Swappings (quick) -----> " + str(swap))
    mylist1.insert(END, "Comparisions (quick) -----> " + str(comp))
    mylist1.insert(END, "Iterations -----> " + str(iter1))
    mylist1.insert(END, "Swappings (insertion) -----> " + str(swap1))
    mylist1.insert(END, "Comparisions (insertion) -----> " + str(comp1))
    mylist1.insert(END, "Total(insertion+quick)-----> " + str(partitions1 + call + swap + comp + comp1 + swap1 + iter1))
    mylist1.insert(END, "\n")
    partitions1 = 0
    call = 0
    swap = 0
    comp = 0
    iter1 = 0
    swap1 = 0
    comp1 = 0
    mylist1.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=mylist1.yview)
    scroll_h.config(command=mylist1.xview)
