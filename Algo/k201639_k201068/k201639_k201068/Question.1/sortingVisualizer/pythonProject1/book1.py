import time
from tkinter import *
from tkinter import ttk

maxelem = 0
minelem = 0
countarr = ""
countarrit = []
countarrcum = []
result = 0
n = 0


def book(arr, drawdata, speed, a, b):
    global maxelem, minelem, result, countarr, n
    max_element = int(max(arr))
    maxelem = max_element
    drawdata(arr, ["orange" if arr[x] == maxelem else "black" for x in range(len(arr))]);
    time.sleep(speed);
    min_element = int(min(arr))
    minelem = min_element
    drawdata(arr, ["blue" if arr[x] == minelem else "black" for x in range(len(arr))]);
    time.sleep(speed);
    range_of_elements = max_element - min_element + 2
    count_arr = [0 for _ in range(int(range_of_elements))]
    output_arr = [0 for _ in range(len(arr))]
    count_arr[0] = 0
    countarr = str(count_arr)
    for i in range(0, len(arr)):
        count_arr[int(arr[i] - min_element + 1)] += 1
        countarrit.append(str(count_arr))
        n += 1
    for i in range(2, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
        countarrcum.append(str(count_arr))
        n += 1
    res = count_arr[(int(b) - int(min_element)) + 1] - count_arr[int(a) - int(min_element)]
    result = res
    drawdata(arr, ["purple" if arr[x] >= int(a) and arr[x] <= int(b) else "black" for x in range(len(arr))]);


    time.sleep(speed);


def winwo(output, drawdata, speed, a, b):
    book(output, drawdata, speed, a, b)
    global maxelem, minelem, result, countarr, n
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
    j = 0;
    mylist1.insert(END, "MAXIMUM ELEMENT OF ARRAY: ")
    mylist1.insert(END, maxelem)
    mylist1.insert(END, "\n")
    mylist1.insert(END, "MINIMUM ELEMENT OF ARRAY: ")
    mylist1.insert(END, minelem)
    mylist1.insert(END, "\n")
    mylist1.insert(END, "COUNT ARRAY AT START: ")
    mylist1.insert(END, countarr)
    mylist1.insert(END, "\n")
    mylist1.insert(END, "ITERATIONS OF COUNT ARRAY: ")
    for i in countarrit:
        mylist1.insert(END, i)
    mylist1.insert(END, "\n")
    mylist1.insert(END, "ITERATIONS OF COUNT CUMMULATIVE ARRAY: ")
    for i in countarrcum:
        mylist1.insert(END, i)
    mylist1.insert(END, "\n")
    mylist1.insert(END, "RESULT: ")
    mylist1.insert(END, result)
    mylist1.insert(END, "BOOK1 ALGORITHM COMPLETED")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "SPACE COMPLEXITY: ")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR ALGORITHM: ")
    mylist1.insert(END, "maxelem = max_element: ------> O(1)")
    mylist1.insert(END, "min_element = int(min(arr)): ------> 0(1)")
    mylist1.insert(END, "minelem = min_element: ------> O(1)")
    mylist1.insert(END, "range_of_elements = max_element - min_element + 2: ------> O(1)")
    mylist1.insert(END, "count_arr = [0 for _ in range(int(range_of_elements))]: ------> O(k)")
    mylist1.insert(END, "output_arr = [0 for _ in range(len(arr))]: ------> O(n)")
    mylist1.insert(END, "countarr = str(count_arr): ------> O(1)")
    mylist1.insert(END, "for i in range(0, len(arr)): ------> O(1) for i")
    mylist1.insert(END,
                   "res = count_arr[(int(b) - int(min_element)) + 1] - count_arr[int(a) - int(min_element)]: ------> O(1)")
    mylist1.insert(END, "result = res: ------> O(1)")
    mylist1.insert(END, "FOR DRY RUN: ")
    mylist1.insert(END, "maxelem = 0: ------> O(1)")
    mylist1.insert(END, "minelem = 0: ------> 0(1)")
    mylist1.insert(END, "countarr = "": ------> O(1)")
    mylist1.insert(END, "countarrit = []: ------> O(k)")
    mylist1.insert(END, "countarrcum = []: ------> O(k)")
    mylist1.insert(END,
                   "def book(output, drawdata, speed, a, b): ------> O(n) for output, 0(1) for speed, 0(1) for a, 0(1) for b")
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
    mylist1.insert(END, "def drawData(data, colorlist): ------> O(n) for data, colorlist")
    mylist1.insert(END, "\n")
    mylist1.insert(END,
                   "ALGORITHM'S SPACE COMPLEXITY(where k is the largest number in the provided sample) -----> O(n+k)")
    mylist1.insert(END,
                   "FINAL SPACE COMPLEXITY(Including Array Size Passed/Iterative Containers) -----> O(1) + O(n+k) = O(n+k)")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "TIME COMPLEXITY: ")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "All Cases: O(n+k)------>" + str(len(output) + (maxelem - minelem)))
    mylist1.insert(END, "Iterations -----> " + str(n))
    n = 0
    mylist1.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=mylist1.yview)
    scroll_h.config(command=mylist1.xview)
