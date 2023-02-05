from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from quick import win
from radix import radixSort
from count import count_sort
from merge import winn
from bucket import win4
from heap import heapsort
from book1 import winwo
from book2 import winwo2
from insertion import winwo3
from bubble import winwo4

root = Tk()
root.title("Sorting Visualizer")
root.config(bg="purple2")

select_alg = StringVar()
output = []

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))


def generate():
    global output
    file = fd.askopenfile(parent=root, mode='r', title='Choose a file')
    output = []
    if file:
        data = file.read()

        appender = ''
        # s=len(data);
        # for i in range(10):

        # thread=Thread(target=threaded_func,args=(,))
        for letter in data:

            if letter != ' ' and letter != ',':
                appender += letter
            if letter == ' ' or letter == ',':
                output.append(float(appender));
                appender = "";

        output.append(float(appender));
    # inital look of the bars color is pulm
    drawData(output, ['Plum' for x in range(len(output))])


def drawData(data, colorlist):
    canvas.delete("all")
    can_height = 450
    can_width = 1250
    x_width = can_width / (len(data) + 1)
    offset = 30
    spacing = 8
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = can_height - height * 400

        # bottom right
        x1 = ((i + 1) * x_width) + offset
        y1 = can_height

        canvas.create_rectangle(x0, y0, x1, y1,
                                fill=colorlist[i])
        if len(normalized_data) <= 250:
            canvas.create_text(x0 + 2, y0, anchor=SE,
                               text=str(data[i]))
    root.update_idletasks()


def start_algorithm():
    global output

    if not output:
        return


    if (algmenu.get() == 'Insertion Sort'):
        elems = Canvas(root, width=1000, height=40, bg="Grey")
        elems.grid(row=2, column=0, padx=10, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)
        Label(elems, text="Starting Element To Be Compared",
              fg='yellow', bg='grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=0,
                                                                                 padx=20, pady=5)
        Label(elems, text="Key Element",
              fg='blue', bg='grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=1,
                                                                               padx=20, pady=5)
        Label(elems, text="Element Swapped Rightwards",
              fg='pink', bg='grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=2,
                                                                               padx=20, pady=5)
        Label(elems, text="Remaining Elements",
              fg='black', bg='grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=3,
                                                                                padx=20, pady=5)
        Label(elems, text="Sorting Completed",
              fg='green', bg='grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=4,
                                                                                padx=20, pady=5)

        # output is the files data
        winwo3(output, drawData, speedbar.get())
        drawData(output, ['Green' for x in range(len(output))])

    elif (algmenu.get() == 'Quick Sort'):

        elems = Canvas(root, width=1200, height=43, bg="Grey")
        elems.grid(row=2, column=0, padx=7, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)

        Label(elems, text="Pivot(Partioned Element)",
              fg='Red', bg='Grey', font=("Times", 10, "italic", "bold")).grid(row=0, column=0,
                                                                              padx=7, pady=5)

        Label(elems, text="Elements < pivot (Before Swapping)",
              fg='Pink', bg='Grey', font=("Times", 10, "italic", "bold")).grid(row=0, column=1,
                                                                               padx=7, pady=5)
        Label(elems, text="Elements < pivot (After Swapping)",
              fg='coral', bg='Grey', font=("Times", 10, "italic", "bold")).grid(row=0, column=2,
                                                                                padx=7, pady=5)
        Label(elems, text="Before pivot and greatest swapping", fg='linen', bg='Grey',
              font=("Times", 10, "italic", "bold")).grid(row=0, column=3, padx=7, pady=5)
        Label(elems, text="After pivot and greatest swapping", fg='thistle', bg='Grey',
              font=("Times", 10, "italic", "bold")).grid(row=0, column=4, padx=7, pady=5)
        Label(elems, text="Left Call",
              fg='cyan', bg='Grey', font=("Times", 10, "italic", "bold")).grid(row=0, column=5,
                                                                               padx=7, pady=5)
        Label(elems, text="Right Call",
              fg='Yellow', bg='Grey', font=("Times", 10, "italic", "bold")).grid(row=0, column=6,
                                                                                 padx=7, pady=5)
        Label(elems, text="Sorted Array",
              fg='Green', bg='Grey', font=("Times", 10, "italic", "bold")).grid(row=0, column=7,
                                                                                padx=7, pady=5)
        Label(elems, text="Remaining Elements",
              fg='Black', bg='Grey', font=("Times", 10, "italic", "bold")).grid(row=0, column=8,
                                                                                padx=7, pady=5)
        win(output, drawData, speedbar.get())

    elif (algmenu.get() == 'Merge Sort'):
        elems = Canvas(root, width=1000, height=40, bg="Grey")
        elems.grid(row=2, column=0, padx=10, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)
        Label(elems, text="Intermediate Sorted Result",
              fg='white', bg='grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=0,
                                                                                padx=20, pady=5)

        Label(elems, text="Left Recursive",
              fg='cyan', bg='grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=2,
                                                                               padx=20, pady=5)
        Label(elems, text="Right Recursive",
              fg='yellow', bg='grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=3,
                                                                                 padx=20, pady=5)
        Label(elems, text="Merge",
              fg='purple', bg='grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=4,
                                                                                 padx=20, pady=5)
        Label(elems, text="Sorting Completed",
              fg='green', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=5,
                                                                                padx=20, pady=5)

        winn(output, 0, len(output) - 1, drawData, speedbar.get())
        drawData(output, ['Green' for x in range(len(output))])

    elif (algmenu.get() == 'Bubble Sort'):
        elems = Canvas(root, width=1000, height=40, bg="Grey")
        elems.grid(row=2, column=0, padx=10, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)

        Label(elems, text="Sorting Completed",
              fg='green', bg='Grey', font=("Times", 12, "italic", "bold")).grid(row=0, column=0,
                                                                                padx=15, pady=5)
        Label(elems, text="Intermediate Sorted Element",
              fg='blue', bg='Grey', font=("Times", 12, "italic", "bold")).grid(row=0, column=1,
                                                                               padx=15, pady=5)
        Label(elems, text="Remaining Elements",
              fg='black', bg='Grey', font=("Times", 12, "italic", "bold")).grid(row=0, column=2,
                                                                                padx=15, pady=5)
        Label(elems, text="Elements Before Swapping",
              fg='red', bg='Grey', font=("Times", 12, "italic", "bold")).grid(row=0, column=3,
                                                                              padx=15, pady=5)
        Label(elems, text="One Iteration Completed",
              fg='white', bg='Grey', font=("Times", 12, "italic", "bold")).grid(row=0, column=4,
                                                                                padx=15, pady=5)
        Label(elems, text="Elements After Swapping",
              fg='purple', bg='Grey', font=("Times", 12, "italic", "bold")).grid(row=0, column=5,
                                                                                 padx=15, pady=5)
        winwo4(output, drawData, speedbar.get())
        drawData(output, ['Green' for x in range(len(output))])

    elif (algmenu.get() == 'Radix Sort'):
        elems = Canvas(root, width=1000, height=40, bg="Grey")
        elems.grid(row=2, column=0, padx=10, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)

        Label(elems, text="Units Sorting",
              fg='cyan', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=0,
                                                                               padx=20, pady=5)
        Label(elems, text="Sorting Completed",
              fg='green', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=1,
                                                                                padx=20, pady=5)

        radixSort(output, drawData, speedbar.get())
        drawData(output, ['Green' for x in range(len(output))])

    elif (algmenu.get() == 'Bucket Sort'):
        elems = Canvas(root, width=1000, height=40, bg="Grey")
        elems.grid(row=2, column=0, padx=8, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)

        Label(elems, text="Element In Bucket",
              fg='cyan', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=0,
                                                                               padx=20, pady=5)
        Label(elems, text="Bucket Placement Completed",
              fg='white', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=1,
                                                                                padx=20, pady=5)
        Label(elems, text="Insertion Sort Completed",
              fg='orange', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=2,
                                                                                 padx=20, pady=5)
        Label(elems, text="Sorting Completed",
              fg='green', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=3,
                                                                                padx=20, pady=5)
        Label(elems, text="Concatenated Elements",
              fg='purple', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=4,
                                                                                 padx=20, pady=5)
        Label(elems, text="Other Elements",
              fg='red', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=5,
                                                                              padx=20, pady=5)
        win4(output, drawData, speedbar.get())
        drawData(output, ['Green' for x in range(len(output))])

    elif (algmenu.get() == 'Counting Sort'):
        elems = Canvas(root, width=1000, height=40, bg="Grey")
        elems.grid(row=2, column=0, padx=10, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)

        Label(elems, text="Intermediate Results",
              fg='cyan', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=0,
                                                                               padx=20, pady=5)
        Label(elems, text="Sorting Completed",
              fg='green', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=1,
                                                                                padx=20, pady=5)
        count_sort(output, drawData, speedbar.get())
        drawData(output, ['Green' for x in range(len(output))])
    elif (algmenu.get() == '7.4.5 (BOOK)'):
        enteries = []

        def book11():
            a = enteries[0].get()
            b = enteries[1].get()
            elems = Canvas(root, width=1000, height=40, bg="Grey")
            elems.grid(row=2, column=0, padx=10, pady=5)
            elems.place(relx=.5, rely=.36, anchor=CENTER)
            Label(elems, text="Elements In Range",
                  fg='Purple', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=0,
                                                                                     padx=20, pady=5)
            Label(elems, text="Maximum Element",
                  fg='orange', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=1,
                                                                                     padx=20, pady=5)
            Label(elems, text="Minimum Element",
                  fg='blue', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=2,
                                                                                   padx=20, pady=5)
            Label(elems, text="Remaining Elements",
                  fg='black', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=3,
                                                                                    padx=20, pady=5)
            winwo(output, drawData, speedbar.get(), a, b)

        elems = Canvas(root, width=1000, height=40, bg="Grey")
        elems.grid(row=2, column=0, padx=10, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)
        Label(elems, text="Enter A and B?", fg="yellow", bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=5)
        for x in range(2):
            myentry = Entry(elems)
            Label(myentry.grid(row=0, column=x + 1, pady=10, padx=5))
            enteries.append(myentry)
        mybutton = Button(elems, text="CHECK", command=book11, bg="yellow")
        mybutton.grid(row=0, column=3, padx=10, pady=5)

    elif (algmenu.get() == '8.2.4 (BOOK)'):
        enteries = 0

        def book12():
            K = enteries.get()
            k = int(K)
            elems = Canvas(root, width=1000, height=40, bg="Grey")
            elems.grid(row=2, column=0, padx=8, pady=5)
            elems.place(relx=.5, rely=.36, anchor=CENTER)
            Label(elems, text="Left Partition Calls",
                  fg='Cyan', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=0,
                                                                                   padx=5, pady=1)
            Label(elems, text="Right Partition Calls",
                  fg='yellow', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=1,
                                                                                     padx=5, pady=1)
            Label(elems, text="PartitionE(QS) and KeyE(IS)",
                  fg='blue', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=2,
                                                                                   padx=5, pady=1)
            Label(elems, text="Remaining Elements",
                  fg='black', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=3,
                                                                                    padx=5, pady=1)
            Label(elems, text="QS Completed",
                  fg='white', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=4,
                                                                                    padx=5, pady=1)
            Label(elems, text="Start Comparing (IS)",
                  fg='yellow', bg='grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=5,
                                                                                     padx=20, pady=1)
            Label(elems, text="Swap Right (IS)",
                  fg='pink', bg='grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=6,
                                                                                   padx=20, pady=1)
            Label(elems, text="IS Completed",
                  fg='plum', bg='Grey', font=("Times", 13, "italic", "bold")).grid(row=0, column=7,
                                                                                   padx=5, pady=1)
            winwo2(output, drawData, speedbar.get(), k)
            drawData(output, ['Green' for x in range(len(output))])

        elems = Canvas(root, width=1000, height=40, bg="Grey")
        elems.grid(row=2, column=0, padx=10, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)
        Label(elems, text="Enter K", fg="yellow", bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=0,
                                                                                                        padx=10, pady=5)
        myentry = Entry(elems)
        Label(myentry.grid(row=0, column=1, pady=10, padx=5))
        enteries = myentry
        mybutton = Button(elems, text="APPLY QS", command=book12, bg="yellow")
        mybutton.grid(row=0, column=2, padx=10, pady=5)

    elif (algmenu.get() == 'Heap Sort'):
        elems = Canvas(root, width=1000, height=40, bg="Grey")
        elems.grid(row=2, column=0, padx=10, pady=5)
        elems.place(relx=.5, rely=.36, anchor=CENTER)

        Label(elems, text="Parent Node",
              fg='yellow', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=0,
                                                                                 padx=5, pady=5)
        Label(elems, text="Child Node",
              fg='red', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=1,
                                                                              padx=5, pady=5)
        Label(elems, text="New Larger",
              fg='cyan', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=2,
                                                                               padx=5, pady=5)
        Label(elems, text="Max Heap Built",
              fg='white', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=3,
                                                                                padx=5, pady=5)
        Label(elems, text="After Swapping",
              fg='purple', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=4,
                                                                                 padx=5, pady=5)
        Label(elems, text="Before Swapping",
              fg='orange', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=5,
                                                                                 padx=5, pady=5)
        Label(elems, text="Sorted Element",
              fg='blue', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=6,
                                                                               padx=5, pady=5)
        Label(elems, text="Heap Sort Done",
              fg='plum', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=7,
                                                                               padx=5, pady=5)
        Label(elems, text="Sorting Completed",
              fg='green', bg='Grey', font=("Times", 15, "italic", "bold")).grid(row=0, column=8,
                                                                                padx=5, pady=5)

        heapsort(output, drawData, speedbar.get())
        drawData(output, ['Green' for x in range(len(output))])


root.state('zoomed')
Mainframe = Frame(root, width=600, height=200, bg="lightblue")
Mainframe.grid(row=1, column=0, padx=10, pady=5, sticky="")
Mainframe.place(relx=.5, rely=.25, anchor=CENTER)

canvas = Canvas(root, width=1300, height=450, bg="Grey")
canvas.grid(row=3, column=0, padx=5, pady=5)
canvas.place(relx=.5, rely=.66, anchor=CENTER)

project = Frame(root, width=600, height=200, bg="lightblue")
project.grid(row=0, column=0, padx=10, pady=5)
project.place(relx=.5, rely=.08, anchor=CENTER)

Label(project, text="DESIGN AND ANALYSIS OF ALGORITHMS",
      bg='lightblue', font=("Times", 25, "bold")).grid(row=0, column=0,
                                                  padx=5, pady=5, columnspan=5)
Label(project, text="CS-2009",
      bg='lightblue').grid(row=1, column=0,
                      padx=5, pady=5, columnspan=5)
Label(project, text="Muhammad Aman",
      bg='lightblue', font=("Times", 14, "italic")).grid(row=2, column=0,
                                                    padx=5, pady=5)
Label(project, text="Syed AbuBakr",
      bg='lightblue', font=("Times", 14, "italic")).grid(row=2, column=4,
                                                    padx=5, pady=5,
                                                    sticky=E)
Label(Mainframe, text="CHOOSE A SORTING ALGORITHM",
      bg='lightblue', font=("Times", 11, "bold")).grid(row=0, column=0,
                                                  padx=5, pady=5,
                                                  sticky=W, columnspan=4)
algmenu = ttk.Combobox(Mainframe,
                       textvariable=select_alg,
                       values=["Insertion Sort", "Bubble Sort", "Merge Sort", "Heap Sort", "Quick Sort", "Radix Sort",
                               "Bucket Sort", "Counting Sort", "7.4.5 (BOOK)", "8.2.4 (BOOK)"])
algmenu.grid(row=0, column=5, padx=5, pady=5)
algmenu.current(0)

Button(Mainframe, text="START",
       bg="yellow",
       command=start_algorithm).grid(row=1,
                                     column=3,
                                     padx=5,
                                     pady=5)

speedbar = Scale(Mainframe, from_=0,
                 to=2, length=100, digits=2,
                 resolution=0.2, orient=HORIZONTAL,
                 label="Playback Speed")
speedbar.grid(row=1, column=0,
              padx=5, pady=5)

Button(Mainframe, text="Open A File",
       bg="green",
       command=generate).grid(row=1,
                              column=2,
                              padx=5,
                              pady=5)

root.mainloop()
