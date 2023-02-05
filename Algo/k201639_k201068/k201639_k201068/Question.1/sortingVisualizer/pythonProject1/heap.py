import time
from tkinter import *
from tkinter import ttk
###############################
import math

##############################
heapifyy = []
subheapify = []
sorted = []
sortedheapify = []
sortedsubheapify = []
strin = ""
strin1 = ""
flag = 0

###############
call = 0
comp = 0
swap = 0
iter = 0


################

def heapify(a, size, i, drawdata, speed):
    global strin, strin1, flag
    ######################################
    global iter, comp, swap
    ###################################
    top = a[i]
    larger = 0
    drawdata(a, ["yellow" if x == larger else "black" for x in range(len(a))]);
    time.sleep(speed);
    while i < size // 2:
        ########################
        iter += 1
        ###################
        if flag == 0:
            strin += str(a)
            strin += " --> "
        if flag == 1:
            strin1 += str(a)
            strin1 += " --> "
        left = 2 * i + 1
        right = 2 * i + 2
        drawdata(a,
                 ["red" if x == left or x == right else "yellow" if x == larger else "black" for x in range(len(a))]);
        time.sleep(speed);
        ################################
        comp += 1
        #################################
        if right < size and a[right] > a[left]:
            drawdata(a, ["cyan" if x == larger or x == right else "black" for x in range(len(a))]);
            time.sleep(speed);
            larger = right
        else:
            drawdata(a, ["cyan" if x == larger or x == left else "black" for x in range(len(a))]);
            time.sleep(speed);
            larger = left
        ####################
        comp += 1
        ####################
        if top >= a[larger]:
            break;
        ########################################
        swap += 1
        #########################################
        a[i], a[larger] = a[larger], a[i]
        drawdata(a, ["purple" if x == larger or x == i else "black" for x in range(len(a))]);
        time.sleep(speed);
        i = larger

    ##########################
    iter += 1
    ##########################
    if flag == 0:
        strin += str(a)
        strin += " --> "
    if flag == 1:
        strin1 += str(a)
        strin1 += " --> "
    if flag == 0:
        subheapify.append(strin)
    if flag == 1:
        sortedsubheapify.append(strin1)
    return a


# The main function to sort an array of given size

def heapSort(arr, N, drawdata, speed):
    global strin, strin1, flag
    ########################change
    global call, swap
    #####################
    # Build a maxheap.
    for i in range(N // 2 - 1, -1, -1):
        flag = 0
        strin = ""
        ###############change
        call += 1
        ################
        heapifyy.append(str((heapify(arr, N, i, drawdata, speed))))
    drawdata(arr, ["white" for x in range(len(arr))]);
    time.sleep(speed);
    # One by one extract elements
    for i in range(N - 1, 0, -1):
        drawdata(arr, ["orange" if x == i or x == 0 else "black" for x in range(len(arr))]);
        time.sleep(speed);
        ##################################
        swap += 1
        ###################################
        arr[i], arr[0] = arr[0], arr[i]  # swap
        sorted.append(str(arr[i]))
        drawdata(arr, ["purple" if x == i or x == 0 else "black" for x in range(len(arr))]);
        time.sleep(speed);
        drawdata(arr, ["blue" if x == i else "black" for x in range(len(arr))])
        time.sleep(speed);
        strin1 = ""
        flag = 1
        #########################################
        call += 1
        #########################################
        sortedheapify.append(str(heapify(arr, i, 0, drawdata, speed)))
        drawdata(arr, ["plum" for x in range(len(arr))]);
        time.sleep(speed);


def heapsort(arr, drawdata, speed):
    n = len(arr)
    heapSort(arr, n, drawdata, speed)
    global comp, call, swap, iter
    root1 = Tk()
    root1.title("Iterations")
    root1.config(bg="white")
    root1.geometry()

    scroll_bar = Scrollbar(root1)
    scroll_h = Scrollbar(root1, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")
    scroll_bar.pack(side=RIGHT, fill=Y)
    mylist1 = Listbox(root1, yscrollcommand=scroll_bar.set, xscrollcommand=scroll_h.set, width=1000)
    j = 0
    mylist1.insert(END, "Building Max Heap")
    for i in heapifyy:
        mylist1.insert(END, "Sub Iterations")
        mylist1.insert(END, subheapify[j])
        mylist1.insert(END, "Resulting Array")
        mylist1.insert(END, i)
        mylist1.insert(END, "\n")
        j += 1

    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    j = 0
    mylist1.insert(END, "Applying heap Sort")
    for i in sortedheapify:
        mylist1.insert(END, "Sorted Element")
        mylist1.insert(END, sorted[j])
        mylist1.insert(END, "Sub Iterations")
        mylist1.insert(END, sortedsubheapify[j])
        mylist1.insert(END, "Resulting Array")
        mylist1.insert(END, i)
        mylist1.insert(END, "\n")
        j += 1
    mylist1.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=mylist1.yview)
    scroll_h.config(command=mylist1.xview)
    #########################################################
    mylist1.insert(END, "SPACE COMPLEXITY: ")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR ALGORITHM: ")
    mylist1.insert(END, "for i in range(N//2 - 1, -1, -1): ------> O(1) for i")
    mylist1.insert(END, "k=n-1 ------> O(1) for k")
    mylist1.insert(END, "for i in range(n): ------> O(1) for i")
    mylist1.insert(END, "top = a[i] ------> O(1)")
    mylist1.insert(END, "larger = 0 ------> O(1)")
    mylist1.insert(END, "while i < size // 2: ------> O(1) for i")
    mylist1.insert(END, "left = 2 * i + 1 ------> O(1)")
    mylist1.insert(END, "right = 2 * i + 2: ------> O(1)")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR DRY RUN: ")
    mylist1.insert(END, "heapifyy = []: ------> O(n)")
    mylist1.insert(END, "subheapify = []: ------> O(n)")
    mylist1.insert(END, "sorted = []: ------> O(n)")
    mylist1.insert(END, "sortedheapify = []: ------> O(n)")
    mylist1.insert(END, "sortedsubheapify = []: ------> O(n)")
    mylist1.insert(END, "strin = "": ------> O(1)")
    mylist1.insert(END, "strin1 = "": ------> O(1)")
    mylist1.insert(END, "flag = 0: ------> O(1)")
    mylist1.insert(END, "heapSort(arr, n,drawdata,speed): ------> O(n) for arr, O(1) for speed")
    mylist1.insert(END,
                   "def heapify(a, size, i, drawdata, speed): ------> O(n) for a, O(1) for speed, O(1) for size, O(1) for i")
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
                   "FINAL SPACE COMPLEXITY(Including Array Size Passed/Iterative Containers)-----> O(1) + O(n) = O(n)")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "TIME COMPLEXITY ------>O(nlogn) " + str(math.log(len(arr)) * len(arr)))

    mylist1.insert(END, "Comparaisions ------->" + str(comp))
    mylist1.insert(END, "Heapify Calls -------->" + str(call))
    mylist1.insert(END, "Swaps----------->" + str(swap))
    mylist1.insert(END, "Iterations--------->" + str(iter))
    mylist1.insert(END, "Total--------->" + str(iter + swap + call + comp))
    comp = call = swap = iter = 0
######################################################################
