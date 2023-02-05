import time
from tkinter import *
from tkinter import ttk

bubble=[]
bubblesub=[]
iteration=0
countswaps=0
countcomp=0
countiter=0
total=0

def time_complexity(n):
    global iteration
    iteration=(n*n)

def bubble_sort(data, drawdata, speed):
    global countswaps, countcomp, countiter, total
    n = len(data)
    k=n-1
    for i in range(n):
        strin1 = ""
        countiter+=1
        for j in range(0, n - i - 1):
            countiter += 1
            countcomp += 1
            if data[j] > data[j + 1]:
                countswaps += 1
                drawdata(data, ['red' if x == j +
                                         1 or x == j else 'black' for x in range(len(data))])
                time.sleep(speed)
                data[j], data[j + 1] = data[j + 1], data[j]
                drawdata(data, ['purple' if x == j +
                                         1 or x == j else 'black' for x in range(len(data))])
                time.sleep(speed)
            strin1 += str(data)
            strin1 += " --> "
        drawdata(data, ['blue' if x == k else 'black' for x in range(len(data))])
        time.sleep(speed)
        drawdata(data, ['white' for x in range(len(data))])
        time.sleep(speed)
        k=k-1
        bubblesub.append(strin1)
        bubble.append(str(data))
    total=countswaps+countiter+countcomp
    # sorted elements generated with Green color
    drawdata(data, ['Green' for x in range(len(data))])


def winwo4(array, drawdata, speed):
    bubble_sort(array, drawdata, speed)
    global countswaps, countcomp, countiter, total
    root1 = Tk()
    root1.wm_state('iconic')
    root1.title("Iterations")
    root1.config(bg="white")
    root1.geometry()

    time_complexity(len(array))
    scroll_bar = Scrollbar(root1)
    scroll_h = Scrollbar(root1, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")
    scroll_bar.pack(side=RIGHT,
                    fill=Y)
    mylist1 = Listbox(root1, yscrollcommand=scroll_bar.set, xscrollcommand=scroll_h.set, width=1000)
    j = 0
    for i in bubblesub:
        mylist1.insert(END, "ITERATION " + str(j + 1) + ": ")
        mylist1.insert(END, "Sub Iterations: ")
        mylist1.insert(END, i)
        mylist1.insert(END, "Resulting Array: ")
        mylist1.insert(END, bubble[j])
        mylist1.insert(END, "\n")
        j += 1
    mylist1.insert(END, "BUBBLE SORT COMPLETED")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "SPACE COMPLEXITY: ")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR ALGORITHM: ")
    mylist1.insert(END, "n = len(data) ------> O(1) for n")
    mylist1.insert(END, "k=n-1 ------> O(1) for k")
    mylist1.insert(END, "for i in range(n): ------> O(1) for i")
    mylist1.insert(END, "strin1 = "" ------> O(1) for strin1")
    mylist1.insert(END, "for j in range(0, n - i - 1): ------> O(1) for j")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "FOR DRY RUN: ")
    mylist1.insert(END, "bubble = []: ------> O(n)")
    mylist1.insert(END, "bubblesub = []: ------> O(n)")
    mylist1.insert(END, "iteration = 0: ------> O(1)")
    mylist1.insert(END, "countswaps = 0 ------> O(1)")
    mylist1.insert(END, "countcomp = 0: ------> O(1)")
    mylist1.insert(END, "countiter=0: ------> O(1)")
    mylist1.insert(END, "total=0: ------> O(1)")
    mylist1.insert(END, "def bubble_sort(array, drawdata, speed): ------> O(n) for array, O(1) for speed")
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
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "All Cases: O(n^2) ----> " + str(iteration))
    mylist1.insert(END, "Iterations ----> " + str(countiter))
    mylist1.insert(END, "Swappings ----> " + str(countswaps))
    mylist1.insert(END, "Comparisions ----> " + str(countcomp))
    mylist1.insert(END, "Total ----> " + str(total))
    mylist1.insert(END, "\n")
    total=0
    countiter=0
    countswaps=0
    countcomp=0
    mylist1.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=mylist1.yview)
    scroll_h.config(command=mylist1.xview)