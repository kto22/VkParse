from tkinter import PhotoImage, Label, Frame, Entry, Button, Tk
import os
import func

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def check_dir(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)


class App:

    def __init__(self, master):

        our_img = PhotoImage(file="kona2.gif")
        our_img = our_img.subsample(5, 5)
        our_label = Label(root)
        our_label.image = our_img
        our_label['image'] = our_label.image
        our_label.place(x=0, y=0)

        frame_top = Frame(root, bg='#000000', bd=5)
        lbl = Label(root, text="nya~ nipaaa~~ (づ｡◕‿‿◕｡)づ", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0)

        frame_top.place(relx=0, rely=0.71, relwidth=1, relheight=0.40)

        self.token = Entry(frame_top, bg='white', font=30)
        self.token.pack()

        self.You = Entry(frame_top, bg='white', font=30)
        self.You.pack()

        self.user_name = Entry(frame_top, bg='white', font=30)
        self.user_name.pack()

        self.user_id = Entry(frame_top, bg='white', font=30)
        self.user_id.pack()

        btn = Button(frame_top, text='Nipaaah~~~', command=self.main)
        btn.pack(padx=2, pady=12)

    def main(self) -> None:

        func.downloader(self.token.get(), int(self.user_id.get()))
        func.repeat_filt()
        func.csv_table_maker(self.You.get(), self.user_name.get())


root = Tk()

root['bg'] = '#fafafa'

root.title('VkParser!')

root.geometry('355x474')

root.resizable(width=False, height=False)

app = App(root)

root.mainloop()
