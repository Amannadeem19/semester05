# Python3 program to sort an array
# using bucket sort
import time
from tkinter import *
from tkinter import ttk

inser=[]
buckets=[]
concat=[]
iter=0
comparision=0
swap=0

def insertionSort(b):
    global iter, swap, comparision
    for i in range(1, len(b)):
        iter+=1
        up = b[i]
        j = i - 1
        comparision+=1
        while j >= 0 and b[j] > up:
            iter+=1
            swap+=1
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSort(x, drawData, timeTick):
    global iter
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # print(arr) // [[], [], [], [], [], [], [], [], [], []]

    # Put array elements in different buckets
    i=0
    for j in x:
        print(j)
        iter+=1
        index_b = int(slot_num * j)
        print(index_b)
        arr[index_b].append(j)
        strin1=""
        strin1 = strin1 + "Iteration " + str(i) + ": "
        i+=1
        strin1 += str(arr)
        strin1 += " --> "
        buckets.append(strin1)
        drawData(x, ['cyan' if x[y] == j else 'red' for y in range(len(x))])
        time.sleep(timeTick)
    drawData(x, ["white" for y in range(len(x))])
    time.sleep(timeTick)

    # Sort individual buckets
    for i in range(slot_num):
        iter+=1
        arr[i] = insertionSort(arr[i])
        inser.append(arr[i])
    drawData(x, ["orange" for y in range(len(x))])
    time.sleep(timeTick)

    # concatenate the result
    k = 0
    for i in range(slot_num):
        iter+=1
        strin1 = ""
        for j in range(len(arr[i])):
            iter+=1
            x[k] = arr[i][j]
            k += 1
            strin1+=str(x)
            strin1+=" --> "
            drawData(x, ['purple' if k == y else 'red' for y in range(len(x))])
            time.sleep(timeTick)
        concat.append(strin1)
    drawData(x, ['green' for y in range(len(x))])
    time.sleep(timeTick)
    return x

def win4(data, drawData, timeTick):
    global comparision, swap, iter

    x=bucketSort(data, drawData, timeTick)
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
    mylist1.insert('end',"PLACING ITEMS IN BUCKETS: ")
    for i in buckets:
        mylist1.insert('end', i)
        mylist1.insert('end', "\n")
    mylist1.insert('end', "\n")
    mylist1.insert('end', "AFTER APPLYING INSERTION SORT ON EACH BUCKET: ")
    for i in range(len(inser)):
        mylist1.insert('end', "Bucket " + str(i) + ": ")
        mylist1.insert('end', inser[i])
        mylist1.insert('end', "\n")
    mylist1.insert('end', "\n")
    mylist1.insert('end', "AFTER CONCATENATING THE RESULTS: ")
    for i in range(len(concat)):
        mylist1.insert('end', "Iteration " + str(i) + ": ")
        mylist1.insert('end', concat[i])
        mylist1.insert('end', "\n")
    mylist1.insert(END, "BUCKET SORT COMPLETED")
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
    mylist1.insert(END, "inser = []: ------> O(n)")
    mylist1.insert(END, "buckets = []: ------> O(n)")
    mylist1.insert(END, "concat = []: ------> O(n)")
    mylist1.insert(END, "iter=0: ------> O(1)")
    mylist1.insert(END, "swap=0: ------> O(1)")
    mylist1.insert(END, "comparision=0: ------> O(1)")
    mylist1.insert(END, "def insertionSort(b): ------> O(n) for b")
    mylist1.insert(END, "def bucketSort(x, drawData, timeTick): ------> O(n) for x")
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
    mylist1.insert(END, "ALGORITHM'S SPACE COMPLEXITY('10' is the Total Buckets Formed) -----> O(n*10)")
    mylist1.insert(END, "FINAL SPACE COMPLEXITY -----> O(1) + O(n) = O(n)")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "TIME COMPLEXITY: ")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "\n")
    mylist1.insert(END, "BEST: O(n+k)------>" + str(len(data) + (int(max(data)) - int(min(data)))))
    mylist1.insert(END, "WORST: O(n^2)------>" + str(len(data) * len(data)))
    mylist1.insert(END, "Iterations (insertion + bucket) -----> " + str(iter))
    mylist1.insert(END, "Swappings (insertion) -----> " + str(swap))
    mylist1.insert(END, "Comparisions (insertion) -----> " + str(comparision))
    mylist1.insert(END, "Total -----> " + str(comparision+swap+iter))
    mylist1.insert(END, "\n")
    iter=0
    swap=0
    comparision=0
    mylist1.pack(side=LEFT, fill=BOTH)
    scroll_bar.config(command=mylist1.yview)
    scroll_h.config(command=mylist1.xview)