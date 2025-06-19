from tkinter import *
root = Tk()
root.geometry("500x300")
def getvals():
    print(" your registration has been Accepted ")
Label(root, text="Free Fire Diamond Topup ", font="ar 15 bold").grid(row=0, column=3)
player = Label(root, text="Player UID")
password =  Label(root, text="Password")
email = Label(root,text="Email Address")
diamond = Label(root, text="Diamond")
phoneno = Label(root, text="Phone No")
player.grid(row=1, column=2)
password.grid(row=2, column=2)
email.grid(row=3, column=2)
diamond.grid(row=4, column=2)
phoneno.grid(row=5, column=2)
playervalue = StringVar
Passwordvalue = StringVar
Emailvalue = StringVar
Diamondvalue = StringVar
Phonenovalue = StringVar
Checkvalue = IntVar
playerentry = Entry(root, textvariable =playervalue)
passwordentry = Entry(root, textvariable =Passwordvalue)
emailentry = Entry(root, textvariable =Emailvalue)
diamondentry = Entry(root, textvariable =Diamondvalue)
phonenoentry = Entry(root, textvariable =Phonenovalue)
playerentry.grid(row=1, column=3)
passwordentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)
diamondentry.grid(row=4, column=3)
phonenoentry.grid(row=5, column=3)
Button(text="Submit", command=getvals).grid(row=7, column=3)
root.mainloop()