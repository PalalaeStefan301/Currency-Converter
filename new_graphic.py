import tkinter as tk
from tkinter import *
from crawl import *

class GUI():
    def _init_(self,root):
        self.root = root
        self.entry = tk.Entry(root)
        self.canvas = tk.Canvas(root,width=400,height=400,background='blue')
        self.canvas.grid(row=0,column=1)
        
        frame = Frame(self.root)
        frame.grid(row=0,column=0,sticky="n")

        