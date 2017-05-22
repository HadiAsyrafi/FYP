try:
    import Tkinter as tk     ## Python 2.x
except ImportError:
    import tkinter as tk     ## Python 3.x

from functools import partial

class OpenToplevels():
    """ open and close additional Toplevels with a button
    """
    def __init__(self):
        self.root = tk.Tk()
        #self.button_ctr=0
        but=tk.Button(self.root, text="Open a Toplevel",
                      command=self.open_another)
        but.grid(row=0, column=0)
        tk.Button(self.root, text="Exit Tkinter", bg="red",
                  command=self.root.quit).grid(row=1, column=0, sticky="we")
        self.root.mainloop()

    def close_it(self):
        self.top.destroy()

    def open_another(self):
        #self.button_ctr += 1
        self.top = tk.Toplevel(self.root)
        self.top.title("Toplevel")
        tk.Button(self.top, text="Close Toplevel",
                  command=self.close_it,
                  bg="orange", width=20).grid(row=1, column=0)

Ot=OpenToplevels()
