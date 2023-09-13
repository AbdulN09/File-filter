import tkinter
from tkinter import *
import os
import win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]


a=(os.walk("D:/"))
l=[]
for i in a:
    l.extend(i)

complete_list=[]
for i in l:
    if type(i)==str:
        complete_list.append(i)
    elif type(i)==list:
        complete_list.extend(i)


def search():
    search1 = entry.get()
    for item in complete_list:
        if item==search1:
            clear_text_field()
            return change_text_field(item)
    else:
        return change_text_field("sorry this file is not there ")


def pdf():
    new_pdf=""
    for item in complete_list:
        if ".pdf" in item:
            new_pdf += str(item) + "\n"
    change_text_field(new_pdf)

def pdf_clear():
    value = text_field.get(1.0, END)
    value = value.split("\n")
    for each in value[:]:
        if ".pdf" in each:
            value.remove(each)
    string = ""
    for each in value:
        string += each + "\n"
    clear_text_field()
    change_text_field(string)

def txt():
    new_txt=""
    for item in complete_list:
        if ".txt" in item:
            new_txt+=str(item)+"\n"
    change_text_field(new_txt)

def txt_clear():
    value = text_field.get(1.0, END)
    value = value.split("\n")
    for each in value[:]:
        if ".txt" in each:
            value.remove(each)
    string = ""
    for each in value:
        string += each + "\n"
    clear_text_field()
    change_text_field(string)


def py():
    new_py=""
    for item in complete_list:
        if ".py" in item:
            new_py+=str(item)+"\n"
    change_text_field(new_py)

def py_clear():
    value = text_field.get(1.0, END)
    value = value.split("\n")
    for each in value[:]:
        if ".py" in each:
            value.remove(each)
    string = ""
    for each in value:
        string += each + "\n"
    clear_text_field()
    change_text_field(string)

def html():
    new_html=""
    for item in complete_list:
        if ".html" in item:
            new_html += str(item) + "\n"
    change_text_field(new_html)

def html_clear():
    value = text_field.get(1.0, END)
    value = value.split("\n")
    for each in value[:]:
        if ".html" in each:
            value.remove(each)
    string = ""
    for each in value:
        string += each + "\n"
    clear_text_field()
    change_text_field(string)

def css():
    new_css=""
    for item in complete_list:
        if ".css" in item:
            new_css += str(item) + "\n"
    change_text_field(new_css)

def css_clear():
    value=text_field.get(1.0,END)
    print(value)
    value=value.split("\n")
    for each in value[:]:
        if ".css" in each:
            value.remove(each)
    string=""
    for each in value:
        string+=each+"\n"
    clear_text_field()
    change_text_field(string)

def images():
    new_images=""
    for item in complete_list:
        if ".png" in item or ".jpeg" in item:
            new_images += str(item) + "\n"
    change_text_field(new_images)

def images_clear():
    value = text_field.get(1.0, END)
    value = value.split("\n")
    for each in value[:]:
        if ".png" in each or ".jpeg" in each:
            value.remove(each)
    string = ""
    for each in value:
        string += each + "\n"
    clear_text_field()
    change_text_field(string)

def change_text_field(st):
    text_field.insert(1.0,st)


def clear_text_field2():
    text_field.delete(1.0, END)
    html_checkbox.deselect()
    css_checkbox.deselect()
    pdf_checkbox.deselect()
    txt_checkbox.deselect()
    images_checkbox.deselect()
    py_checkbox.deselect()
    entry.delete(0,100)

def clear_text_field():
    text_field.delete(1.0,END)

def open():
    file_name = entry.get()

    # Directory to search for file
    search_dir = "D:/"

    # Search for file in all subdirectories
    for dirpath, dirnames, filenames in os.walk(search_dir):
        for filename in filenames:
            # Check if file name and extension match
            if filename == file_name:
                # Construct absolute path using os module
                absolute_path = os.path.join(dirpath, filename)
                print("Absolute path:", absolute_path)

    os.startfile(absolute_path)

screen=Tk()
screen.geometry("600x600",)
screen.config(bg="#DEAEA5")

pdf_var=BooleanVar()
pdf_checkbox=Checkbutton(variable=pdf_var,command=lambda:pdf() if pdf_var.get() else pdf_clear(),bg="#DEAEA5")
pdf_checkbox.place(x="30",y="30")

pdf_label=Label(text="pdf",font=("Courier New",16,"bold"),bg="#DEAEA5")
pdf_label.place(x="80",y="30")

txt_var=BooleanVar()
txt_checkbox=Checkbutton(variable=txt_var,command=lambda:txt() if txt_var.get() else txt_clear(),bg="#DEAEA5")
txt_checkbox.place(x="30",y="100")

txt_label=Label(text="txt",font=("Courier New",16,"bold"),bg="#DEAEA5")
txt_label.place(x="80",y="100")

py_var=BooleanVar()
py_checkbox=Checkbutton(variable=py_var,command=lambda:py() if py_var.get() else py_clear(),bg="#DEAEA5")
py_checkbox.place(x="30",y="180")

py_label=Label(text="py",font=("Courier New",16,"bold"),bg="#DEAEA5")
py_label.place(x="80",y="180")

html_var=BooleanVar()
html_checkbox=Checkbutton(variable=html_var,command=lambda:html() if html_var.get() else html_clear(),bg="#DEAEA5")
html_checkbox.place(x="200",y="30")

html_label=Label(text="html",font=("Courier New",16,"bold"),bg="#DEAEA5")
html_label.place(x="250",y="30")

css_var=BooleanVar()
css_checkbox=Checkbutton(variable=css_var,command=lambda:css() if css_var.get() else css_clear(),bg="#DEAEA5")
css_checkbox.place(x="200",y="100")

css_label=Label(text="css",font=("Courier New",16,"bold"),bg="#DEAEA5")
css_label.place(x="250",y="100")

images_var=BooleanVar()
images_checkbox=Checkbutton(variable=images_var,command=lambda:images() if images_var.get() else images_clear(),bg="#DEAEA5")
images_checkbox.place(x="200",y="180")

images_label=Label(text="images",font=("Courier New",16,"bold"),bg="#DEAEA5")
images_label.place(x="250",y="180")


clear_button=Button(screen,text="Clear Text Field",width=19,height=2,command=clear_text_field2,font=("Courier New",10,"bold"))
clear_button.place(x="400",y="180")
#
label=Label(screen,text="🔎",bg="#DEAEA5",font=("Arial",16,"bold"))
label.place(x="360",y="30")

entry=Entry(screen,width=15,font=("Courier New",14,"bold"))
entry.place(x="400",y="30")
#
#
button=Button(screen,text="SEARCH",command=search,bg="black",height=2,width=7,fg="white")
button.place(x="400",y="100")


open_button=Button(screen,text="OPEN",command=open,bg="black",height=2,width=7,fg="white")
open_button.place(x="505",y="100")



text_field=Text(screen,width=72,height=21,font=("Courier New",10,"bold"))
text_field.config(bg="#cdf8c9")
text_field.place(x="10",y="250")


screen.mainloop()