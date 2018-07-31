# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 19:02:20 2018

@author: ctneal21
"""

import flicklib
import requests
import signal
from os import system
import time
import curses
from curses import wrapper
#import time

@flicklib.move()
def move(x, y, z):
    global xyztxt
    xyztxt = '{:5.3f} {:5.3f} {:5.3f}'.format(x,y,z)


@flicklib.flick()
def flick(start, finish):
    global flicktxt
    global remote_cd
    flicktxt = start + '-' + finish
    try:
        direction = start + '-' + finish
        #print(direction)
        if direction == 'west-east':
            requests.get(host + '/next')
            remote_cd = 'Channel: Previous'
            #print(remote_cd)
            system("irsend SEND_ONCE TV KEY_CHANNELDOWN")
        elif direction == 'east-west':
            requests.get(host + '/prev')
            remote_cd = 'Channel: Next'
            #print(remote_cd)
            system("irsend SEND_ONCE Digibox KEY_CHANNELUP")
        elif direction == 'south-north':
            requests.get(host + '/toggleVis')
            remote_cd = 'Volume: Up'
            #print(remote_cd)
            system("irsend SEND_ONCE TV KEY_VOLUMEUP")
        elif direction == 'north-south':
            requests.get(host + '/changeVis')
            remote_cd = 'Volume: Down'
            #print(remote_cd)
            system("irsend SEND_ONCE TV KEY_VOLUMEDOWN")

    except:
        print("Error connecting to host")

@flicklib.double_tap()
def dt(position):
    global doubletaptxt
    doubletaptxt = position
    try:
        print('double-tap: ' + position)
        requests.get(host + '/toggle')
    except:
        print("Error connecting to host")

@flicklib.tap()
def tap(position):
    global taptxt
    taptxt = position

@flicklib.touch()
def touch(position):
    global touchtxt
    touchtxt = position

#import time
#import curses
#from curses import wrapper
def main(stdscr):
    global xyztxt
    global flicktxt
    global remote_cd
    global touchtxt
    global taptxt
    global doubletaptxt

    xyztxt = ''
    flicktxt = ''
    flickcount = 0
    touchtxt = ''
    touchcount = 0
    taptxt = ''
    tapcount = 0
    doubletaptxt = ''
    doubletapcount = 0

    # Clear screen and hide cursor
    stdscr.clear()
    curses.curs_set(0)

    # Add title and footer
    exittxt = 'Control-C to exit'
    title = '**** Flick Demo ****'
    stdscr.addstr( 0, (curses.COLS - len(title)) / 2, title)
    stdscr.addstr(22, (curses.COLS - len(exittxt)) / 2, exittxt)
    stdscr.refresh()

    fw_info = flicklib.getfwinfo()

    datawin = curses.newwin( 8, curses.COLS - 6,  2, 3)

    # Update data window continuously until Control-C
    while True:
        datawin.erase()
        datawin.border()
        datawin.addstr(1, 2, 'X Y Z     : ' + xyztxt)
        datawin.addstr(2, 2, 'TV        : ' + remote_cd)
        datawin.addstr(3, 2, 'Touch     : ' + touchtxt)
        datawin.addstr(4, 2, 'Tap       : ' + taptxt)
        datawin.addstr(5, 2, 'Doubletap : ' + doubletaptxt)
        datawin.refresh()

        xyztxt = ''

        if len(flicktxt) > 0 and flickcount < 5:
            flickcount += 1
          
        else:
            flicktxt = ''
            flickcount = 0

        if len(touchtxt) > 0 and touchcount < 5:
            touchcount += 1
        else:
            touchtxt = ''
            touchcount = 0

        if len(taptxt) > 0 and tapcount < 5:
            tapcount += 1
        else:
            taptxt = ''
            tapcount = 0

        if len(doubletaptxt) > 0 and doubletapcount < 5:
            doubletapcount += 1
        else:
            doubletaptxt = ''
            doubletapcount = 0

        time.sleep(0.1)

wrapper(main)
