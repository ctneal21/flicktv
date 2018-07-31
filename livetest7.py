# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:20:02 2018

@author: ctneal21
"""

import flicklib
import tkinter as tk
from PIL import ImageGrab
#from tkinter import *
import requests
import signal
from os import system
import time
import threading
import turtle

@flicklib.double_tap()
def doubletap(position):
    global doubletaptxt
    doubletaptxt = position
 
@flicklib.move()
def move(x, y, z):
    global xpos
    global ypos
    global zpos
    xpos = x
    ypos = y
    zpos = z

  
global doubletaptxt    
global touchtxt
global xpos
global ypos

doubletaptxt = ''
doubletapcount = 0

root = tk.Tk()
canvas = tk.Canvas(master = root, width = 250, height = 250)
canvas.pack(side="top", fill="both", expand=True)
canvas.config(scrollregion=(0,0,250,250))
canvas.pack()
t = turtle.RawTurtle(canvas,visible=False)
t.speed('fastest')

while True:
    
    #plt.close
    if len(doubletaptxt) > 0: #and doubletapcount < 5:

        while zpos < .4:
            if doubletapcount == 0:
                t.penup()
                t.goto(canvas.canvas(xpos*250),canvas.canvas(ypos*250))
            t.pendown()
            print(xpos)
            print(ypos)
            t.goto(xpos*250,ypos*250)
            doubletapcount += 1
            t.penup()
        if doubletapcount > 0:
            time.sleep(2)
            box = (canvas.winfo_rootx(),canvas.winfo_rooty(),canvas.winfo_rootx()+canvas.winfo_width(),canvas.winfo_rooty() + canvas.winfo_height())
            scsh = ImageGrab.grab(bbox = box)
            scsh.save('num.jpg')
            canvas.delete("all")
            doubletapcount = 0
            doubletaptxt = ''

    else:
        doubletaptxt = ''
        doubletapcount = 0
        canvas.delete("all")
        
