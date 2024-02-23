import tkinter
from tkinter import*
from  tkinter import ttk
from tkinter import messagebox
from cbookmethods import view,add,update,remove,search
import csv
#to add the values
def insert():
    name=nametext.get()
    gender=gendertext.get()
    telephone=phonetext.get()
    email=emailtext.get()
    print(name)
    data=[name,gender,telephone,email]

    if name==''or gender==''or telephone==' 'or email==" ":
       tkinter.messagebox.showwarning(title="Error",message="Please fill all fields")
    else:
        add(data)
        tkinter.messagebox.showwarning(title="success",message="Data added successfully ")
        nametext.delete(0,'end')
        gendertext.delete(0,'end')
        phonetext.delete(0,'end')
        emailtext.delete(0,'end')
        show()


def to_update():
    try:
        tree_data=tree.focus()# get data user selects
        tree_dictionary=tree.item(tree_data)
        tree_list=tree_dictionary['values']

        name=str(tree_list[0])
        gender=str(tree_list[1])
        telephone=str(tree_list[2])
        email=str(tree_list[3])

        nametext.insert(0,name)
        gendertext.insert(0,gender)
        phonetext.insert(0,telephone)
        emailtext.insert(0, email)

        def confirm():
            new_name=nametext.get()
            new_gender=gendertext.get()
            new_telephone=phonetext.get()
            new_email=emailtext.get()

            data=[new_telephone,new_name, new_gender,new_telephone,new_email]

            update(data)

            messagebox.showinfo("success","data updated successfully ")

            nametext.delete(0, 'end')
            gendertext.delete(0, 'end')
            phonetext.delete(0, 'end')
            emailtext.delete(0, 'end')

            for widget in frametable.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()

        b_confirm = tkinter.Button(frame2, text="confirm", command=confirm)
        b_confirm.grid(row=4, column=3, sticky="news", padx=10, pady=10)
    except IndexError:
        messagebox.showerror('Error','select one of  them table ')

def to_remove():
    try:
        tree_data=tree.focus()# get data user selects
        tree_dictionary=tree.item(tree_data)
        tree_list=tree_dictionary['values']
        tree_telephone=str(tree_list[2])

        remove(tree_telephone)

        messagebox.showinfo('success',"Data has deleted successfully ")

        for widget in frametable.winfo_children():
            widget.destroy()

        show()

    except IndexError:
        messagebox.showerror('Error','select one of  them table ')

def to_search():
    name=searchtext.get()

    data =search(name)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('','end',values=item)



window=tkinter.Tk()
window.title("")
window.resizable(width=False,height=False)
window.configure(background="#ffffff")
frame=tkinter.Frame(window)
frame.pack()


frame1=tkinter.LabelFrame(frame,text="",bg="#4456F0")
frame1.grid(row=0,column=0,padx=10,pady=10)
frame1namelabel=tkinter.Label(frame1,text="Contact Book",font=('verdana 30 bold'))
frame1namelabel.grid(row=0,column=0)

frame2=tkinter.LabelFrame(frame,width=1000,height=150)
frame2.grid(row=1,column=0,padx=10,pady=10)
#
namelabel=tkinter.Label(frame2,text="Name",)
namelabel.grid(row=0,column=0,sticky="news",padx=10,pady=10)
nametext=tkinter.Entry(frame2)
nametext.grid(row=0,column=1,padx=10,pady=10)
#
genderlabel=tkinter.Label(frame2,text="Gender")
genderlabel.grid(row=1,column=0,sticky="news",padx=10,pady=10)
gendertext=ttk.Combobox(frame2,values=["M","F"])
gendertext.grid(row=1,column=1,padx=10,pady=10)
#
phonelabel=tkinter.Label(frame2,text="ContactNumber")
phonelabel.grid(row=2,column=0,sticky="news",padx=10,pady=10)
phonetext=tkinter.Entry(frame2)
phonetext.grid(row=2,column=1,padx=10,pady=10)
#
emaillabel=tkinter.Label(frame2,text="E-Mail")
emaillabel.grid(row=3,column=0,sticky="news",padx=10,pady=10)
emailtext=tkinter.Entry(frame2)
emailtext.grid(row=3,column=1,padx=10,pady=10)
#
searchbtn=tkinter.Button(frame2,text="Search",command=to_search)
searchbtn.grid(row=1,column=2,sticky="news",padx=10,pady=10)
searchtext=tkinter.Entry(frame2)
searchtext.grid(row=1,column=3,padx=10,pady=10)
#
#viewbtn=tkinter.Button(frame2,text="View",command=show)
#viewbtn.grid(row=2,column=3,sticky="news",padx=10,pady=10)

addbtn=tkinter.Button(frame2,text="Add",command=insert)
addbtn.grid(row=3,column=3,sticky="news",padx=10,pady=10)

updatebtn=tkinter.Button(frame2,text="Update",command=to_update)
updatebtn.grid(row=2,column=4,sticky="news",padx=10,pady=10)

deletebtn=tkinter.Button(frame2,text="Delete",command=to_remove)
deletebtn.grid(row=3,column=4,sticky="news",padx=10,pady=10)
#
frametable=tkinter.LabelFrame(frame,width=100,height=10,bg="#000000",relief=FLAT)
frametable.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

#to show the values in the table
def show():
    global tree

    listheader=['Name','Gender','Telephone','Email']
    sample_list=view()

    tree=ttk.Treeview(frametable,selectmode="extended",columns=listheader,show='headings')
    vsb = ttk.Scrollbar(frametable, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frametable, orient='horizontal', command=tree.xview)
    tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
    tree.grid(row=0,column=0,sticky="news")
    vsb.grid(row=1,column=1,sticky="ns")
    hsb.grid(row=2,column=1,sticky="ew")

    tree.heading(0, text="Name",anchor=NW)
    tree.heading(1, text="Gender",anchor=NW)
    tree.heading(2, text="Telephone",anchor=NW)
    tree.heading(3, text="Email",anchor=NW)

    tree.column(0,width=120,anchor="nw")
    tree.column(1, width=150, anchor="nw")
    tree.column(2, width=200, anchor="nw")
    tree.column(3, width=280, anchor="nw")


    for item in sample_list:
        tree.insert('','end',values=item)

show()
viewbtn=tkinter.Button(frame2,text="View",command=show)
viewbtn.grid(row=2,column=3,sticky="news",padx=10,pady=10)


window.mainloop()
