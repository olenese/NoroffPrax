from tkinter import *
from tkinter import messagebox

sup_files = [".txt", ".docx"]



def open_file():
    file_path = my_ent_box.get()
    if file_path[-4:] ==".txt":

        with open(file_path, "r") as f:
            my_txt_box.insert(END, open(file_path, "r").read())
            f.close()
        with open("log.txt", "w") as r:
            r.write(file_path)
            r.close()

    else:
         messagebox.showerror("Error", f"That is not a valid filetype! Supported file types: {*sup_files,}")

def save_file():
    file_content = my_txt_box.get("1.0", "end-1c")
    file_path = my_ent_box.get()
    if file_path[-4:] == ".txt":

        with open(file_path, "w") as f:
            f.write(file_content)
            f.close()
    
    else:
        messagebox.showerror("Error", f"That is not a valid filetype! Supported file types: {*sup_files,}")

def create_file():
    new_file = my_ent_box.get()
    if new_file[-4:] == ".txt":
        f = open(new_file, "w")
        messagebox.showinfo("New file created", f"New file Created: {new_file}")
        f.close
    else: 
        messagebox.showerror("Error", f"That is not a valid filetype! Supported file types: {*sup_files,}")





window = Tk()
window.title("GUIApp")
window.geometry("900x500")

my_lbl_1 = Label(window, text="File Editor", font=("Arial", 25))
my_lbl_1.place(x=280, y=10)

my_lbl_2 = Label(window)

my_txt_box = Text(window)
my_txt_box.place(x=280, y=55)

my_ent_box = Entry(window)
my_ent_box.place(x=50, y=60)
my_ent_box.insert(0, "File Path")

my_btn_1 = Button(window, text="Open File", command=open_file)
my_btn_1.place(x=50, y=80)

my_btn_2 = Button(window, text="Save File", command=save_file)
my_btn_2.place(x=50, y=110)

my_btn_3 = Button(window, text="Create File", command=create_file)
my_btn_3.place(x=50, y=150)

lb_box = Listbox(window, width=20, height=5)

with open("log.txt", "r") as l:
    for x in l.readlines():
        lb_box.insert(END, x)

log_lbl = Label(window, text="Recently used files: ")
log_lbl.place(x=50, y=180)

lb_box.place(x=50, y=200)


window.mainloop()

