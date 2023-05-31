from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "apartemen.jpeg"))
hunians.append(Rumah("Sekar MK", 5, 2, "rumah.jpg"))
hunians.append(Indekos("Bp. Romi", "Cahya", "kost.jpg"))
hunians.append(Rumah("Satria", 1, 4, "rumahjuga.jpg"))

root = Tk()
root.title("Praktikum DPBO Python")

foto_hunian = []


def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(
    ) + hunians[index].get_detail(), anchor="w").grid(row=0, column=0, sticky="w")

    img = Image.open("assets/" + hunians[index].get_foto())
    img = img.resize((180, 180))
    photo_img = ImageTk.PhotoImage(img)
    foto_hunian.append(photo_img)
    img_label = Label(d_frame, image=photo_img)
    img_label.grid(row=1, column=0)


def main_page():
    label.destroy()
    frameland.destroy()
    img_label.destroy()
    button.destroy()

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5,
                    borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15,
                     borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos":
            name = Label(frame, text=" " + h.get_nama_pemilik(),
                         width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(),
                         width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ",
                          command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)


label = Label(root, text="Landing Page")
label.pack()

img = Image.open("assets/home.jpg")
img = img.resize((240, 240))
photo_img = ImageTk.PhotoImage(img)
foto_hunian.append(photo_img)
frameland = Frame(root, padx=10, pady=10)
frameland.pack(padx=10, pady=10)
img_label = Label(frameland, image=photo_img)
img_label.pack()

button = Button(root, text="Home", command=main_page)
button.pack(side=BOTTOM)

root.mainloop()
