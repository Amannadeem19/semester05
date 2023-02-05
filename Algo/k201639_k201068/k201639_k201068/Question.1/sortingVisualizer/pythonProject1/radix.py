import time
from tkinter import *
from tkinter import ttk

numCount = 0
inCount = 0


def countingSort(data, exp1, drawdata, speed):
    global inCount, numCount
    disp = []
    disp1 = []
    n = len(data)

    output = [0] * (n)
    count = [0] * (10)

    strin = ""
    for i in count:
        strin += str(i);
        strin += " "
    disp.append(strin);

    for i in range(0, n):
        inCount += 1
        index = (data[i] / exp1)
        count[int(index % 10)] += 1

    strin = ""
    for i in count:
        strin += str(i);
        strin += " "
    disp.append(strin);

    for i in range(1, 10):
        inCount += 1
        count[i] += count[i - 1]
    strin = ""
    for i in count:
        strin += str(i);
        strin += " "
    disp.append(strin);
    # print(strin)

    i = n - 1
    newStrin = ""
    while i >= 0:
        inCount += 1
        index = (data[i] / exp1)
        output[count[int(index % 10)] - 1] = data[i]
        count[int(index % 10)] -= 1
        i -= 1

        disp1.append(count);
        ###############################################
        disp1.append(output);

    for i in range(0, len(data)):
        data[i] = output[i]

    drawdata(data, ['cyan' for x in range(len(data))])
    time.sleep(speed + 0.3)

    return disp, disp1


def radixSort(data, drawdata, speed):
    global numCount, inCount
    root1 = Tk()
    root1.wm_state('iconic')

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

    max1 = max(data)

    exp = 1
    numss = len(str(max(data)))

    r = 1
    while numss != 0:
        numCount += 1
        disp, disp1 = countingSort(data, exp, drawdata, speed)
        lb.insert('end', str(r) + "Iteration")
        r += 1
        k = 0
        for item in disp:
            if k == 0:
                lb.insert('end', "Count Array(Start)")
            elif k == 1:
                lb.insert('end', "Count Array(Count)")
            elif k == 2:
                lb.insert('end', "Count Array(Commulative Sum)")
            lb.insert('end', item)
            k += 1

        j = 0
        k = 0
        for item in disp1:
            if j % 2 == 0:
                lb.insert('end', "Move " + str(k + 1))
                k += 1
            lb.insert('end', item)
            j += 1

        exp *= 10
        numss -= 1
    lb.insert('end', item)
    lb.insert(END, "RADIX SORT COMPLETED")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "SPACE COMPLEXITY: ")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "FOR ALGORITHM: ")
    lb.insert(END, "n = len(data): ------> O(1)")
    lb.insert(END, " output = [0] * (n): ------> 0(1)")
    lb.insert(END, "count = [0] * (10): ------> O(1)")
    lb.insert(END, "strin = "": ------> O(1)")
    lb.insert(END, "for i in count: ------> O(1) for i")
    lb.insert(END, "index = (data[i] / exp1): ------> O(1)")
    lb.insert(END, "i = n - 1: ------> O(1)")
    lb.insert(END, "for j in output: ------> O(1) for j")
    lb.insert(END, "\n")
    lb.insert(END, "FOR DRY RUN: ")
    lb.insert(END, "disp = []: ------> O(n)")
    lb.insert(END, "disp1 = []: ------> O(n)")
    lb.insert(END,
              "def radixSort(data, drawdata, speed): ------> (n) for data, (1) for speed")
    lb.insert(END,
              "def countingSort(data, exp1, drawdata, speed): ------> (n) for data, (1) for speed, O(1) for exp1")
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
    lb.insert(END, "ALGORITHM'S SPACE COMPLEXITY(After Each Call on No. of Units 'd') -----> O(n*2d)")
    lb.insert(END,
              "FINAL SPACE COMPLEXITY(Including Array Size Passed/Iterative Containers) -----> O(1) + O(n*2d) = O(n*2d)")
    lb.insert(END, "\n")
    lb.insert(END, "TIME COMPLEXITY")
    lb.insert(END, "\n")
    lb.insert(END, "\n")
    lb.insert(END, "All Cases: O(d(n+k))------>" + str(numCount * (len(data) + (int(max(data)) - int(min(data))))))
    lb.insert(END, "Iterations -----> " + str(inCount * numCount))
    inCount = 0
    numCount = 0
    return data
