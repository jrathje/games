#-------------------------------------------------------------------------------
# Name:        Tkinter_test.py
# Purpose:      testing tkinter
#
# Author:      Jim Rathje
#
# Created:     20/03/2015
# Copyright:   (c) mlc 2015

#-------------------------------------------------------------------------------
##from Tkinter import *
import Tkinter as tk
def main():
    pass

#if __name__ == '__main__':
    #main()


counter = 0
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()

    #To initialize Tkinter, we have to create a Tk root widget, which is a
    #window with a title bar and other decoration provided by the window manager.
    # The root widget has to be created before any other widgets and there can
    # only be one root widget.

root = tk.Tk()
root.title("Counting Seconds")

    #The next line of code contains the Label widget. The first parameter of
    #the Label call is the name of the parent window, in our case "root".
    #So our Label widget is a child of the root widget.
label = tk.Label(root, fg="red")
    #The pack method tells Tk to fit the size of the window to the given text.
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)


button.pack()

#The window won't appear until we enter the Tkinter event loop:
root.mainloop()