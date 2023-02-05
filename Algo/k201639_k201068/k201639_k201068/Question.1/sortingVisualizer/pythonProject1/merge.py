import time
from tkinter import *
import math
from tkinter import ttk

LRec = []
RRec = []
MRec = []
out = []
# mer - for calculating merging cost
mer = 0
# call - for calculating total calls
call = 0


def merge_sort2(data, left, right, drawdata, speed):
    global call, mer
    if left < right:
        strin = ""

        middle = (left + right) // 2;
        #######################
        for i in range(len(data)):
            if (i >= left and i <= middle):
                strin += str(data[i])
                strin += " "
        LRec.append(strin)
        #####################
        strin1 = ""
        for i in range(len(data)):
            if (i >= left and i <= right):
                strin1 += str(data[i])
                strin1 += " "

        MRec.append(strin1)
        ####################
        strin2 = ""
        for i in range(len(data)):
            if (i >= middle + 1 and i <= right):
                strin2 += str(data[i])
                strin2 += " "
        RRec.append(strin2)
        ####################
        # if data is on left recursive side cyan else black
        drawdata(data, ["cyan" if x >= left and x <= middle else "black" for x in range(len(data))]);
        call += 1
        time.sleep(speed);
        # recursive call
        merge_sort2(data, left, middle, drawdata, speed);
        # for right recursive side yellow color
        drawdata(data, ["yellow" if x >= middle + 1 and x <= right else "black" for x in range(len(data))]);
        time.sleep(speed);
        ###############################################################

        merge_sort2(data, middle + 1, right, drawdata, speed);
        #############################################################
        # merging all the data
        drawdata(data, ["purple" if x >= left and x <= right else "black" for x in range(len(data))]);
        time.sleep(speed);
        mer += 1

        # merge call

        merge(data, left, middle, right, drawdata, speed);


def merge(data, left, middle, right, drawdata, speed):
    # drawdata(data, color(len(data), left, middle, right));
    # time.sleep(speed);
    # print(left)
    # print(middle)
    # print(right)
    left_side = data[left:middle + 1];
    # print(data[left:middle+1])
    # print("left side")
    # print(left_side)
    right_side = data[middle + 1:right + 1];
    # print("right side")
    # print(right_side)
    i, j = 0, 0;

    for k in range(left, right + 1):
        if i < len(left_side) and j < len(right_side):
            if left_side[i] <= right_side[j]:
                data[k] = left_side[i];
                i += 1;
            else:
                data[k] = right_side[j];
                j += 1;

        elif i < len(left_side):
            data[k] = left_side[i];
            i += 1;
        else:
            data[k] = right_side[j];
            j += 1;
    r = 0
    strin3 = ""
    # out is used for showing the each merging data
    while r < len(data):
        strin3 += str(data[r])
        strin3 += " "
        r += 1
    out.append(strin3);

    # apparently sorted elements

    drawdata(data, ["white" if x >= left and x <= right else "black" for x in range(len(data))]);
    time.sleep(speed);


def winn(data, left, right, drawdata, speed):
    global mer, call
    merge_sort2(data, left, right, drawdata, speed);
    root1 = Tk()
    root1.title("Iterations")
    root1.config(bg="white")

    # width = root1.winfo_screenwidth()
    # height = root1.winfo_screenheight()

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

    # lb.insert('end',"Left Recursive Calls:")
    # for item in LRec:
    #     lb.insert('end', item)
    #
    # lb.insert('end', "Merge Recursive Calls:")
    # for item in MRec:
    #     lb.insert('end', item)
    #
    # lb.insert('end', "Right Recursive Calls:")
    # for item in RRec:
    #     lb.insert('end', item)

    # for i in range(len(LRec)):
    i = 0;
    while i < len(LRec):
        lb.insert('end', str(i + 1) + " Record:")
        # lb.insert('end', LRec[i])

        lb.insert('end', "Left Recursive Calls:")
        lb.insert('end', LRec[i])

        lb.insert('end', "Merge Recursive Calls:")
        lb.insert('end', MRec[i])

        lb.insert('end', "Right Recursive Calls:")
        lb.insert('end', RRec[i])

        lb.insert('end', "------------------------")
        i += 1

    i = 0
    while i < len(out):
        lb.insert('end', "After " + str(i + 1) + " merge implemented, Output Array:")
        lb.insert('end', out[i])
        i += 1

    lb.insert(END, "MERGE SORT COMPLETED")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "SPACE COMPLEXITY: ")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "FOR ALGORITHM: ")
    lb.insert(END, "strin = "": ------> O(1)")
    lb.insert(END, "middle = (left + right) // 2: ------> 0(1)")
    lb.insert(END, "for i in range(len(data)): ------> O(1) for i")
    lb.insert(END, "left_side = data[left:middle + 1]: ------> O(n) for left_side")
    lb.insert(END, "right_side = data[middle + 1:right + 1]: ------> O(n) for right_side")
    lb.insert(END, "i, j = 0, 0: ------> O(1) for i,j")
    lb.insert(END, "for k in range(left, right + 1): ------> O(1) for k")
    lb.insert(END, "strin3 = "": ------> O(1) for strin3")
    lb.insert(END, "\n")
    lb.insert(END, "FOR DRY RUN: ")
    lb.insert(END, "LRec = []: ------> O(n)")
    lb.insert(END, "RRec = []: ------> O(n)")
    lb.insert(END, "MRec = []: ------> O(n)")
    lb.insert(END, "out = []: ------> O(n)")
    lb.insert(END, "mer = 0: ------> O(1)")
    lb.insert(END, "call = 0: ------> O(1)")
    lb.insert(END,
              "def merge_sort2(data, left, right, drawdata, speed): ------> (n) for data, (1) for left, 0(1) for right, 0(1) for speed")
    lb.insert(END,
              "def merge(data, left, middle, right, drawdata, speed): ------> (n) for data, (1) for left, 0(1) for right, 0(1) for speed, 0(1) for middle")
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
    lb.insert(END, "\nALGORITHM'S SPACE COMPLEXITY -----> O(n)")
    lb.insert(END, "FINAL SPACE COMPLEXITY(Including Array Size Passed/Iterative Containers) -----> O(1) + O(n) = O(n)")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "TIME COMPLEXITY: ")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "All Cases: O(nlogn)------>" + str(len(data) * math.log(len(data))))
    lb.insert(END, "Mergings -----> " + str(mer))
    lb.insert(END, "Calls -----> " + str(call))
    lb.insert(END, "Total -----> " + str(call + mer))
    mer = 0
    call = 0
    # if j % 2 == 0:
    #     lb.insert('end', "Move " + str(k + 1))
    # k += 1
    #
    #     # j += 1
    # scroll_bar1 = Scrollbar(root1)
    #
    # scroll_bar1.pack(side=RIGHT,
    #                 fill=Y)
    #
    # lb1 = Listbox(root1, yscrollcommand=scroll_bar1.set, width=333)
    # lb1.pack(side=CENTER, fill=BOTH)
    # scroll_bar1.config(command=lb1.yview)
    # for item in MRec:
    #     lb1.insert('end', item)
    #
    # scroll_bar2 = Scrollbar(root1)
    #
    # scroll_bar2.pack(side=RIGHT,
    #                  fill=Y)
    #
    # lb2 = Listbox(root1, yscrollcommand=scroll_bar2.set, width=333)
    # lb2.pack(side=RIGHT, fill=BOTH)
    # scroll_bar2.config(command=lb2.yview)
    # for item in RRec:
    #     lb2.insert('end', item)
# def color(lenn, left, middle, right):
#     color_list = [];
#
#     for i in range(lenn):
#         if i >= left and i <= right:
#             color_list.append('red');
#             if i <= left and i >= middle:
#                 color_list.append('red');
#             else:
#                 color_list.append('red');
#         else:
#             color_list.append('black');
#
#     return color_list
