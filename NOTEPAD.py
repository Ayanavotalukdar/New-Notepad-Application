from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import colorchooser
import tkinter.messagebox as tmsg

# A basic testing function...

def func():
    print("This Menu is working Properly..")

# Help Function 

def helps():
    tmsg.showinfo("Help","This is a text editing Application\nused for any kind of editing.\nChoose correct options from the upward menubar\nto perform any action")

# Undo Function 

def undos():
    pass

# Quit Function 

def quitn():
    ask=tmsg.askquestion("Close App","If you are not save this File\nyour all progress will refreshed\nwill you close it without saving?")
    if(ask=="yes"):
        savefunc()
    else:
        quit()     

# Save Function

def savefunc():
    filesave=filedialog.asksaveasfile(defaultextension=".txt")
    filetext=str(textarea.get(1.0,END))
    filesave.write(filetext)
    filesave.close()
    tmsg.showinfo("save","File Saved Successfully")
    
# Open Function 

def openfunc():
    file=filedialog.askopenfilename()
    fo=open(file,'r')
    read=fo.read()
    textarea.insert(END,read)
    fo.close()

# Editing-cut

def cut():
    selected=textarea.selection_get()
    textarea.delete("sel.first","sel.last")

# Editing-copy

def copy():
    global selected
    selected=textarea.selection_get()

# Editing-paste

def paste():
    
    position = textarea.index(INSERT)
    textarea.insert(position,selected)

# Zoom++ Function 

def zoomout():
    font1[1]=font1[1]+2
    textarea.config(font=font1)

# Zoom-- Function

def zoomin():
    font1[1]=font1[1]-2
    textarea.config(font=font1)

# Change Background Color

def background():
        cd=colorchooser.askcolor()
        textarea.configure(background=cd[1])

# Change Fg Color
    
def foreground():
    color=colorchooser.askcolor()
    textarea.configure(foreground=color[1])


# openwindow function

def openwindow():
    root=Tk()
    root.geometry("800x500")
    root.title("Untitled")

    # Default Font Size

    global font1
    font1=["Times",16,"normal"]
    
    # Font Size Changing

    label1=Label(text='''Font Size:''',font="cathlic 10 bold").pack(side=LEFT,anchor="ne")
    size=IntVar
    font_size=ttk.Combobox(root,textvariable=size,width=2)
    font_size['values']=[8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60]
    font_size.current(8)
    font_size.pack(side=LEFT,anchor="ne")

    # Font Style Changing

    label2=Label(text="Font Style:",font="cathlic 10 bold").pack(side=LEFT,anchor="nw")
    style=StringVar()
    font_style=ttk.Combobox(root,textvariable=style,width=5)
    font_style['values']=["bold","italic","underline","overstrike","normal"]
    font_style.current(1)
    font_style.pack(side=LEFT,anchor="nw")

    # Font Family Changinmg

    label3=Label(text="Font:",font="cathlic 10 bold").pack(side=LEFT,anchor="ne")
    type=StringVar()
    font_type=ttk.Combobox(root,textvariable=type,width=6)
    font_type['values']=["Helvetica","Times","Algerian","Wide Latin","Viner Hand Itc","Tempus Sans Itc","Vladimir Script","Agency FB"]
    font_type.current(2)
    font_type.pack(side=LEFT,anchor="ne")
    
    # Change Font Button

    def fontsize():
        font1[1]=font_size.get()
        font1[2]=font_style.get()
        font1[0]=font_type.get()
        textarea.config(font=font1)

    # Status Bar

    def status():
        statusvar=StringVar()
        status=Label(root,textvariable=statusvar,bd=1,relief=SUNKEN)
        status.pack(side=BOTTOM,fill=X)
        status.configure(bg="blue",fg="white")
        def motion(event):
            x,y=event.x,event.y
            statusvar.set(f"Line:{y},Column:{x}")
        textarea.bind("<Motion>",motion)

    # Change Font Button Making

    button=Button(root,text="Change Font",command=fontsize).pack(side=LEFT,anchor="ne")

    # Main Menubar

    Mymenu=Menu(root)

    # File Menu Main Window

    StudentMenu=Menu(Mymenu,tearoff=0)
    StudentMenu.add_command(label="New Window",command=openwindow)
    StudentMenu.add_separator()
    StudentMenu.add_command(label="Open File",command=openfunc)
    StudentMenu.add_command(label="Open Folder",command=func)
    StudentMenu.add_separator()
    StudentMenu.add_command(label="Save",command=savefunc)
    StudentMenu.add_command(label="Save As",command=savefunc)
    StudentMenu.add_separator()
    StudentMenu.add_command(label="Close Window",command=quitn)
    StudentMenu.add_command(label="Print",command=func)
    Mymenu.add_cascade(label="File",menu=StudentMenu)

    # Edit Menu Main Window

    edit=Menu(Mymenu,tearoff=0)
    edit.add_command(label="Cut                  ctrl+x",command=cut)
    edit.add_command(label="Copy               ctrl+c",command=copy)
    edit.add_command(label="Paste               ctrl+v",command=paste)
    edit.add_separator()
    edit.add_command(label="Font Color",command=foreground)
    edit.add_command(label="Background Color",command=background)
    edit.add_separator()
    edit.add_command(label="Zoom++            ctrl+z",command=zoomout)
    edit.add_command(label="Zoom--            ctrl+z",command=zoomin)
    Mymenu.add_cascade(label="Edit",menu=edit)

    # Find Menu Main Window

    find=Menu(Mymenu,tearoff=0)
    find.add_command(label="Find",command=func)
    find.add_command(label="Status Bar",command=status)
    Mymenu.add_cascade(label="Find",menu=find)

    # Exit Menu Main Window

    TeacherMenu=Menu(Mymenu,tearoff=0)
    TeacherMenu.add_command(label="Undo",command=undos)
    TeacherMenu.add_command(label="Quit Notepad",command=quitn)
    Mymenu.add_cascade(label="Exit",menu=TeacherMenu)

    # Help Menu Main Window

    help=Menu(Mymenu,tearoff=0)
    help.add_command(label="Help",command=helps)
    Mymenu.add_cascade(label="Help",menu=help)

    # Packing the menubar

    root.config(menu=Mymenu)

    # Entry Field Main Window

    yscrollbar=Scrollbar(root)
    yscrollbar.pack(side=RIGHT,fill=Y)
    global textarea
    textarea=Text(root,yscrollcommand=yscrollbar.set,font=font1)
    yscrollbar.config(command=textarea.yview)
    textarea.pack(expand=1,fill=BOTH)
    
    # closing window

    root.mainloop()

# main function

d=openwindow()