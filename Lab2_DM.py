from tkinter import *
import networkx as nx
import pylab as plt
import os

G = 14
N = 29
print("Моя група: ІО -", G)
print("Мій номер у групі:", N)
print("Мій варіант:", (N + G % 60) % 30 + 1)
women = ["Марія", "Оксана", "Дарина", "Марта", "Олександра", "Мирослава", "Катерина"]
men = ["Іван", "Дмитро", "Роман", "Євгеній", "Святослав", "Марк", "Єгор"]

root = Tk()
root.title("Вікно №1")
root.geometry("500x500")
menubar = Menu(root)
f = Frame(root, bd=10, bg="white", relief=GROOVE)
l1 = Label(f, text="Черноіваненко Вікторія Андріївна", bg="white",
           fg="blue", relief=SUNKEN, font="Times 14")
l2 = Label(f, text="Моя група: ІО - " + str(G), bg="white",
           fg="blue", relief=SUNKEN, font="Times 14")
l3 = Label(f, text="Мій номер у групі: " + str(N), bg="white",
           fg="blue", relief=SUNKEN, font="Times 14")
l4 = Label(f, text="Мій варіант: " + str((N + G % 60) % 30 + 1),
           bg="white", fg="blue", relief=SUNKEN, font="Times 14")
f.grid(row=0, column=0)
l1.grid(row=0, column=0, sticky="ew")
l2.grid(row=1, column=0, sticky="ew")
l3.grid(row=2, column=0, sticky="ew")
l4.grid(row=3, column=0, sticky="ew")


def win2():
    def insert_w():
        if var.get() == "A":
            listA.insert(END, listw.get(ACTIVE))
        elif var.get() == "B":
            listB.insert(END, listw.get(ACTIVE))

    def insert_m():
        if var.get() == "A":
            listA.insert(END, listm.get(ACTIVE))
        elif var.get() == "B":
            listB.insert(END, listm.get(ACTIVE))

    def del_A():
        listA.delete(ACTIVE)

    def del_B():
        listB.delete(ACTIVE)

    def save_A():
        global a
        s = open(r"fileA.txt", "w")
        a = {i for i in listA.get(0, END)}
        s.write(str(a))
        s.close()

    def save_B():
        global b
        s = open(r"fileB.txt", "w")
        b = {i for i in listB.get(0, END)}
        s.write(str(b))
        s.close()

    def read_A():
        with open(r"fileA.txt", "r") as r:
            text.delete(1.0, END)
            text.insert(INSERT, r.read())

    def read_B():
        with open(r"fileB.txt", "r") as r:
            text.delete(1.0, END)
            text.insert(INSERT, r.read())

    def clear_A():
        s = open(r"fileA.txt", "w")
        s.write(str({}))
        s.close()

    def clear_B():
        s = open(r"fileB.txt", "w")
        s.write(str({}))
        s.close()

    top = Toplevel(root)
    top.title("Вікно №2")
    listw = Listbox(top, font=("Comic", 14))
    for i in women:
        listw.insert(END, i)
    listm = Listbox(top, font=("Comic", 14))
    for i in men:
        listm.insert(END, i)
    labelw = Label(top, text="Жінки", font=("Times", 16))
    labelm = Label(top, text="Чоловіки", font=("Times", 16))
    listA = Listbox(top, font=("Comic", 14))
    listB = Listbox(top, font=("Comic", 14))
    labelA = Label(top, text="Множина А", font=("Times", 16))
    labelB = Label(top, text="Множина В", font=("Times", 16))
    var = StringVar()
    rbutA = Radiobutton(top, text="A", variable=var, value="A")
    rbutB = Radiobutton(top, text="B", variable=var, value="B")
    butw = Button(top, text="Додати", command=insert_w)
    butm = Button(top, text="Додати", command=insert_m)
    wscrollbar = Scrollbar(top, orient='vertical', command=listw.yview)
    listw.config(yscrollcommand=wscrollbar.set)
    mscrollbar = Scrollbar(top, orient='vertical', command=listm.yview)
    listm.config(yscrollcommand=mscrollbar.set)
    Ascrollbar = Scrollbar(top, orient='vertical', command=listA.yview)
    listA.config(yscrollcommand=Ascrollbar.set)
    Bscrollbar = Scrollbar(top, orient='vertical', command=listB.yview)
    listB.config(yscrollcommand=Bscrollbar.set)
    butdelA = Button(top, text="Видалити", command=del_A)
    butdelB = Button(top, text="Видалити", command=del_B)
    butsaveA = Button(top, text="Зберегти у файл", command=save_A)
    butsaveB = Button(top, text="Зберегти у файл", command=save_B)
    butreadA = Button(top, text="Зчитати з файлу", command=read_A)
    butreadB = Button(top, text="Зчитати з файлу", command=read_B)
    butclearA = Button(top, text="Очистити А", command=clear_A)
    butclearB = Button(top, text="Очистити B", command=clear_B)
    text = Text(top, height=15, font=("Verdana", 12))
    labelw.grid(row=0, column=0, columnspan=2, sticky="ew")
    labelm.grid(row=0, column=2, columnspan=2, sticky="ew")
    listw.grid(row=1, column=0, sticky="ew")
    listm.grid(row=1, column=2, sticky="ew")
    wscrollbar.grid(row=1, column=1, sticky="nsew")
    mscrollbar.grid(row=1, column=3, sticky="nsew")
    butw.grid(row=2, column=0, columnspan=2, sticky="ew")
    butm.grid(row=2, column=2, columnspan=2, sticky="ew")
    rbutA.grid(row=3, column=0, columnspan=2, sticky="ew")
    rbutB.grid(row=3, column=2, columnspan=2, sticky="ew")
    labelA.grid(row=4, column=0, columnspan=2, sticky="ew")
    labelB.grid(row=4, column=2, columnspan=2, sticky="ew")
    Ascrollbar.grid(row=5, column=1, sticky="nsew")
    Bscrollbar.grid(row=5, column=3, sticky="nsew")
    listA.grid(row=5, column=0, sticky="ew")
    listB.grid(row=5, column=2, sticky="ew")
    butdelA.grid(row=6, column=0, columnspan=2, sticky="ew")
    butdelB.grid(row=6, column=2, columnspan=2, sticky="ew")
    butsaveA.grid(row=7, column=0, columnspan=2, sticky="ew")
    butsaveB.grid(row=7, column=2, columnspan=2, sticky="ew")
    butreadA.grid(row=8, column=0, columnspan=2, sticky="ew")
    butreadB.grid(row=8, column=2, columnspan=2, sticky="ew")
    butclearA.grid(row=9, column=0, columnspan=2, sticky="ew")
    butclearB.grid(row=9, column=2, columnspan=2, sticky="ew")
    top.columnconfigure(1, weight=1)
    text.grid(row=10, column=0, columnspan=4, sticky="ew")


def win3():
    top = Toplevel(root)
    top.geometry("600x800")
    top.title("Вікно №3")
    labelA = Label(top, text="Множина А", font=("Times", 16))
    labelB = Label(top, text="Множина В", font=("Times", 16))
    listA = Listbox(top, font=("Arial", 14))
    for i in a:
        listA.insert(END, i)
    listB = Listbox(top, font=("Arial", 14))
    for i in b:
        listB.insert(END, i)
    Ascrollbar = Scrollbar(top, orient='vertical', command=listA.yview)
    listA.config(yscrollcommand=Ascrollbar.set)
    Bscrollbar = Scrollbar(top, orient='vertical', command=listB.yview)
    listB.config(yscrollcommand=Bscrollbar.set)
    labelS = Label(top, text="Відношення S", font=("Times", 16))
    labelR = Label(top, text="Відношення R", font=("Times", 16))
    g = nx.DiGraph()
    g.add_nodes_from(a)
    g.add_nodes_from(b)
    al = list(a)
    bl = list(b)
    for i in range(0, len(al)):
        for j in range(0, len(bl)):
            if al[i] in women and bl[j] in men:
                for n1, n2 in g.edges():
                    if n1 != al[i] and n2 != bl[j]:
                        global v
                        v = True
                        continue
                    else:
                        v = False
                        break
                if not g.edges() or v:
                    g.add_edge(al[i], bl[j])

    nx.draw(g, pos=nx.drawing.bipartite_layout(g, bl, align="horizontal"), with_labels=True, arrows=True)
    os.remove('graph.png')
    plt.savefig('graph.png')
    p = PhotoImage(file='graph.png')
    iml = Label(top, image=p)
    labelA.place(relx=0.0, rely=0.0, anchor="nw", relwidth=0.5, relheight=0.05)
    labelB.place(relx=0.5, rely=0.0, anchor="nw", relwidth=0.5, relheight=0.05)
    listA.place(relx=0.0, rely=0.05, anchor="nw", relwidth=0.45, relheight=0.2)
    listB.place(relx=0.5, rely=0.05, anchor="nw", relwidth=0.45, relheight=0.2)
    Ascrollbar.place(relx=0.45, rely=0.05, anchor="nw", relwidth=0.05, relheight=0.2)
    Bscrollbar.place(relx=0.95, rely=0.05, anchor="nw", relwidth=0.05, relheight=0.2)
    labelR.place(relx=0.0, rely=0.25, anchor="nw", relwidth=1, relheight=0.05)
    iml.place(relx=0.0, rely=0.3, anchor="nw", relwidth=1)
    labelS.place(relx=0.0, rely=0.6, anchor="nw", relwidth=1, relheight=0.05)

menubar.add_command(label="Вікно №2", font="Times 12", command=win2)
menubar.add_command(label="Вікно №3", font="Times 12", command=win3)
# menubar.add_command(label="Вікно №4", font="Times 12",command=win4)

root.config(menu=menubar)
root.columnconfigure(1, weight=1)
root.mainloop()
