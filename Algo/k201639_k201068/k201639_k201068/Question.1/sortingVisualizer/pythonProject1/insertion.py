import time
from tkinter import *
from tkinter import ttk

inser=[]
insersub=[]
keys=[]
comp=0
swaps=0
iter=0

def insertion_sort(array, drawdata, speed):
    global swaps, comp, iter
    for j in range(1, len(array)):
        iter += 1
        strin1 = ""
        key = array[j]
        keys.append(key)
        i = j - 1
        drawdata(array, ["yellow" if x == i else "green" if x < j else "blue" if x==j else "black" for x in range(len(array))]);
        time.sleep(speed);
        comp += 1
        while i >= 0 and array[i] > key:
            comp += 1
            swaps += 1
            iter += 1
            array[i + 1] = array[i]
            drawdata(array, ["pink" if x == i else "green" if x <= j else "black" for x in range(len(array))]);
            time.sleep(speed);
            i -= 1
            strin1 += str(array)
            strin1 += " --> "
        array[i + 1] = key
        strin1 += str(array)
        strin1 += " --> "
        insersub.append(strin1)
        inser.append(str(array))

def winwo3(array, drawdata, speed):
    insertion_sort(array, drawdata, speed)
    global iter, swaps, comp
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
    for i in insersub:
        mylist1.insert(END, "ITERATION " + str(j+1) + ": ")
        mylist1.insert(END, "Key Element: ")
        mylist1.insert(END, keys[j])
        mylist1.insert(END, "Sub Iterations: ")
        mylist1.insert(END, i)
        mylist1.insert(END, "Resulting Array: ")
        mylist1.insert(END, inser[j])
        mylist1.insert(END, "\n")
        j += 1
    mylist1.insert(END, "INSERTION SORT COMPLETED")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "SPACE COMPLEXITY: ")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR ALGORITHM: ")
    mylist1.insert(END, "for j in range(1, len(array)): ------> O(1) for j")
    mylist1.insert(END, "key = array[j] ------> O(1) for key")
    mylist1.insert(END, "i = j - 1 ------> O(1) for i")
    mylist1.insert(END, "i = j - 1 ------> O(1) for i")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR DRY RUN: ")
    mylist1.insert(END, "inser=[]: ------> O(n)")
    mylist1.insert(END, "insersub=[] ------> O(n)")
    mylist1.insert(END, "keys=[] ------> O(n)")
    mylist1.insert(END, "strin1 = "": ------> O(1)")
    mylist1.insert(END, "comp = 0: ------> O(1)")
    mylist1.insert(END, "swaps = 0: ------> O(1)")
    mylist1.insert(END, "inter = 0: ------> O(1)")
    mylist1.insert(END, "def insertion_sort(array, drawdata, speed): ------> O(n) for array, O(1) for speed")
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
    mylist1.insert(END, "FINAL SPACE COMPLEXITY(Including Array Size Passed/Iterative Containers) -----> O(1) + O(n) = O(n)")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "TIME COMPLEXITY: ")
    global swaps, comp, iter
    length = len(array)
    mylist1.insert(END, "WORST: O(n^2)---------> " + str(length * length))
    mylist1.insert(END, "BEST: O(n)---------> " + str(length))
    mylist1.insert(END, "ITERATIONS---------> " + str(iter))
    mylist1.insert(END, "NO OF SWAPS---------> " + str(swaps))
    mylist1.insert(END, "NO OF COMPARISIONS---------> " + str(comp))
    mylist1.insert(END, "TOTAL---------> " + str(swaps + comp + iter))
    iter=0
    swaps=0
    comp=0
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")

    mylist1.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=mylist1.yview)
    scroll_h.config(command=mylist1.xview)