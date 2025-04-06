import os
import sys
import tkinter as tk
from tkinter import Frame
import cv2
from tkinter import *
import argparse
import tkinter.filedialog
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename # Open dialog box
from PIL import Image
tk=Tk()
ap = argparse.ArgumentParser()
ap.add_argument("-m1", "--user1", required=True,
	help="path to trained model model")
ap.add_argument("-m2", "--user2", required=True,
	help="path to trained model model")
ap.add_argument("-m3", "--user3", required=True,
	help="path to trained model model")

args = vars(ap.parse_args())

root=tk
root.geometry('500x500')
root.title("DEPRESSION DETECTION USING MACHINE LEARNING")
root.configure(background="#AC3B61")

label_0 = Label(root, text="Depression Detection",fg="#FFFFFF",bg="#AC3B61", width=30,font=("Algerian", 20))
label_0.place(x=15,y=15)

label_1 = Label(root, text="Brouse Image to Predict depression",bg="#AC3B61",fg="#FFFFFF",width=30,font=("bold", 14))
label_1.place(x=100,y=50)

#create label
#Label(root, text="\ndefintion\n other", bg="white", fg="black", font="none 12 bold" ).grid(row=10, column=8, sticky=W)


def open_File():   

    filename = askopenfilename(filetypes=[("images","*.*")])
    img = cv2.imread(filename)
    print(filename,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #fname = filename.read()
    path, filename1 = os.path.split(filename)
    print(path,"0000000000000000000000000000000000000000000000")
    print(filename1,"-----------------------------------------------------")
    new='python prdict.py --model pokedex.model --labelbin lb.pickle --image examples/'+filename1+' --user1 '+args["user1"]+' --user2 '+args["user2"]+' --user3 '+args["user3"]
    print(new,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    #os.system(new)
    #print(fname)
    os.system(new)

    #cv2.imshow("Shapes", img) # I used cv2 to show image 
    #cv2.waitKey(0)
    #filename.close()


l1=Label(root, text="Select image to detect ",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 20))
l1.place(x=120,y=380)
btn1=Button(root,text="Browse image",bg="#AC3B61",fg="#FFFFFF", width =16,font=("bold", 16))
btn1.place(x=160,y=420)
btn1.config(command=open_File)

path = "d1.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img,bg="#AC3B61")
panel.config( width=500 )
panel.config( height=250 )
panel.config( anchor="center" )
panel.place(x=8,y=10)
#panel.place(x=150,y=160)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "left",anchor="center")#side = "up", fill = "both", expand = "yes")




root.mainloop()
# main...
#window=tk()
#window.title("Preventions to avoid Brain Cancer")

