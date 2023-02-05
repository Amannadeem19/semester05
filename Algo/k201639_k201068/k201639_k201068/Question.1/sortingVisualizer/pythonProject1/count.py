# Python program for counting sort
# which takes negative numbers as well
from tkinter import *
from tkinter import ttk
import time

disp = []
disp1 = []
subcount = []
sc = 0
subcountcum = []
scc = 0
n = 0


# The function that sorts the given arr[]
def count_sort(arr, drawdata, speed):
    global n
    root1 = Tk()
    root1.wm_state('iconic')
    root1.title("Iterations")
    root1.config(bg="white")

    # width = root1.winfo_screenwidth()
    # height = root1.winfo_screenheight()
    root1.geometry()
    # root1.geometry("%dx%d" % (width, height))
    scroll_bar = Scrollbar(root1)
    scroll_h = Scrollbar(root1, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")
    scroll_bar.pack(side=RIGHT,
                    fill=Y)

    lb = Listbox(root1, yscrollcommand=scroll_bar.set, width=1000)
    lb.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=lb.yview)
    scroll_h.config(command=lb.xview)

    global disp, disp1

    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    # Store count of each character
    strin = ""
    for i in count_arr:
        strin += str(i);
        strin += " "
    disp.append(strin);
    # print(strin)
    #######################################
    for i in range(0, len(arr)):
        subcount.append(str(count_arr))
        count_arr[int(arr[i]) - min_element] += 1
        n += 1
    subcount.append(str(count_arr))
    sc = str(subcount)
    ###############################################3
    strin = ""
    for i in count_arr:
        strin += str(i);
        strin += " "
    disp.append(strin);
    # print(strin)
    #####################################################3
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        subcountcum.append(str(count_arr))
        count_arr[i] += count_arr[i - 1]
        n += 1
    subcountcum.append(str(count_arr))
    scc = str(subcountcum)
    ##########################################################3
    strin = ""
    for i in count_arr:
        strin += str(i);
        strin += " "
    disp.append(strin);
    # print(strin)
    k = 0
    for item in disp:
        if k == 0:
            lb.insert('end', "Count Array(Start)")
        elif k == 1:
            lb.insert('end', "Count Array(Count)")
            lb.insert('end', sc)
        elif k == 2:
            lb.insert('end', "Count Array(Commulative Sum)")
            lb.insert('end', scc)
        lb.insert('end', item)
        lb.insert('end', "\n")
        k += 1

    newStrin = ""
    ##################################################3
    # Build the output character array
    for i in range(len(arr) - 1, -1, -1):
        n += 1
        output_arr[count_arr[int(arr[i]) - min_element] - 1] = arr[i]
        drawdata(output_arr, ['cyan' for x in range(len(output_arr))])
        time.sleep(speed)
        count_arr[int(arr[i]) - min_element] -= 1
        #########################################3
        newStrin = ""
        for i in count_arr:
            newStrin += str(i);
            newStrin += " "
        disp1.append(newStrin);
        ###############################################
        newStrin = ""
        for i in output_arr:
            newStrin += str(i);
            newStrin += " "
        disp1.append(newStrin);

    j = 0
    k = 0
    for item in disp1:
        if j % 2 == 0:
            lb.insert('end', "Move " + str(k + 1))
            k += 1
        lb.insert('end', item)
        j += 1

    lb.insert(END, "COUNT SORT COMPLETED")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "SPACE COMPLEXITY: ")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "FOR ALGORITHM: ")
    lb.insert(END, "max_element = int(max(arr)): ------> O(1)")
    lb.insert(END, "min_element = int(min(arr)): ------> O(1)")
    lb.insert(END, "range_of_elements = max_element - min_element + 1: ------> O(1)")
    lb.insert(END, "count_arr = [0 for _ in range(range_of_elements)]: ------> O(k)")
    lb.insert(END, "output_arr = [0 for _ in range(len(arr))]: ------> 0(n)")
    lb.insert(END, "for i in range(len(data)): ------> O(1) for i")
    lb.insert(END, "strin = "": ------> O(1) for strin")
    lb.insert(END, "for i in count_arr: ------> O(1) for i")
    lb.insert(END, "newstrin=" ": ------> O(1)")
    lb.insert(END, "j = 0: ------> O(1)")
    lb.insert(END, "k = 0: ------> O(1) ")
    lb.insert(END, "\n")
    lb.insert(END, "FOR DRY RUN: ")
    lb.insert(END, "disp = []: ------> O(n)")
    lb.insert(END, "disp1 = []: ------> O(n)")
    lb.insert(END, "subcount = []: ------> O(k)")
    lb.insert(END, "sc = 0: ------> O(n)")
    lb.insert(END, "subcountcum = []: ------> O(k)")
    lb.insert(END, "scc = 0: ------> O(1)")
    lb.insert(END, "n = 0: ------> O(1)")
    lb.insert(END,
              "def count_sort(arr,drawdata,speed): ------> (n) for arr, 0(1) for speed")
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
    lb.insert(END,
              "FINAL SPACE COMPLEXITY(where k is the largest number in the provided sample) -----> O(1) + O(n+k) = O(n+k)")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "TIME COMPLEXITY: ")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "All Cases: O(n+k)------>" + str(len(arr) + (int(max(arr)) - int(min(arr)))))
    lb.insert(END, "Iterations -----> " + str(n))
    n = 0
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

# return arr

# drawdata(data, ['cyan' for x in range(len(data))])

# Driver program to test above function
# arr = [-5, -10, 0, -3, 8, 5, -1, 10]
# count_sort(arr)
# print("Sorted character array is " + str(ans))
