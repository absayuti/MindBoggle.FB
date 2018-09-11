#!/usr/bin/python
"""
  MindBoggle	 	
		A Mastermind game
		Based on a C64 program "Mind Boggle" from Gazette Disk May 1984
				
  0.21	27 Sep 2015
  0.20	20 Feb 2015
		Rewriting using Tkinter
  0.10	18 May 2014
		Converting from FreeBASIC to Python
-------------------------------------------------------------------------------
"""
from __future__ import print_function  # for compatibility

version='0.21'

#-------------------------------------------------------------------------------

import sys, os, datetime
import random
from tkinter import *


#-------------------------------------------------------------------------------

class MainWindow(object):

	def __init__( self, master ):

		master.title('Mind Boggle')
		frame = Frame( master )
		frame.pack()

		self.topLabel = Label( frame, text='Chose four colours and click the OK button', fg='blue' )
		self.topLabel.grid( row=0, column=0, columnspan=5 )

		# User tries / selections
		#self.selection1 = Label( frame, width=10, text='           ', bg='black' )
		#self.selection1.grid( row=1, column=0 )

		self.textbox = Text( frame, font=('Consolas',16), width=36, height=10, bg='lightgrey' )
		self.textbox.grid( row=1, column=0, columnspan=5 )
		for n in range(1,11):
			self.textbox.insert(END, str(n)+'\n')

		# The choices
		self.colourLabel1 = Label( frame, width=10, text='          ', bg=colour[userchoice[0]] )
		self.colourLabel1.grid( row=2, column=0 )
		self.colourLabel2 = Label( frame, width=10, text='          ', bg=colour[userchoice[1]] )
		self.colourLabel2.grid( row=2, column=1 )
		self.colourLabel3 = Label( frame, width=10, text='          ', bg=colour[userchoice[2]] )
		self.colourLabel3.grid( row=2, column=2 )
		self.colourLabel4 = Label( frame, width=10, text='          ', bg=colour[userchoice[3]] )
		self.colourLabel4.grid( row=2, column=3 )

		self.okbutton = Button( frame, text='OK', width=10, command=self.find_matches )
		self.okbutton.grid( row=2, column=4 )

		self.listbox1 = Listbox( frame, width=10, height=6, selectmode=SINGLE )
		self.listbox1.grid( row=3, column=0)
		for i in range(len(colour)):
			self.listbox1.insert( i, colour[i] )
			self.listbox1.itemconfigure( i, fg=colour[i])
		self.listbox1.bind('<<ListboxSelect>>', self.change_colour1 )

		self.listbox2 = Listbox( frame, width=10, height=6, selectmode=SINGLE )
		self.listbox2.grid( row=3, column=1)
		for i in range(len(colour)):
			self.listbox2.insert( i, colour[i] )
			self.listbox2.itemconfigure( i, fg=colour[i])
		self.listbox2.bind('<<ListboxSelect>>', self.change_colour2 )

		self.listbox3 = Listbox( frame, width=10, height=6, selectmode=SINGLE )
		self.listbox3.grid( row=3, column=2)
		for i in range(len(colour)):
			self.listbox3.insert( i, colour[i] )
			self.listbox3.itemconfigure( i, fg=colour[i])
		self.listbox3.bind('<<ListboxSelect>>', self.change_colour3 )

		self.listbox4 = Listbox( frame, width=10, height=6, selectmode=SINGLE )
		self.listbox4.grid( row=3, column=3)
		for i in range(len(colour)):
			self.listbox4.insert( i, colour[i] )
			self.listbox4.itemconfigure( i, fg=colour[i])
		self.listbox4.bind('<<ListboxSelect>>', self.change_colour4 )

		#self.quitButton = Button( frame, text='Close', width=10, command=frame.quit )
		#self.quitButton.grid( row=2, column=5 )

		# Perform initial setup
		self.generate_answer()
		for n in range(1,10):
			self.textbox.insert(END,' '+str(n)+'\n')
		self.textbox.insert(END,'10')
		global tries
		tries = 0

	def generate_answer( self ):
		random.seed()
		self.textbox.insert( END, " I AM CHOOSING 4 COLORS NOW")
		answer[0] = random.randint( 0,6 )
		answer[1] = random.randint( 0,6 )
		while answer[1]==answer[0]:
			answer[1] = random.randint( 0,6 )
		answer[2] = random.randint( 0,6 )
		while answer[2]==answer[0] or answer[2]==answer[1]:
			answer[2] = random.randint( 0,6 )
		answer[3] = random.randint( 0,6 )
		while answer[3]==answer[0] or answer[3]==answer[1] or answer[3]==answer[2]:
			answer[3] = random.randint( 0,6 )
		self.textbox.delete('1.0', END)

	def find_matches( self ):
		global tries
		tries = tries+1
		for i in range(4):
			yx = str(tries)+'.'+str(i*20+5)
			self.textbox.insert(yx,' '+colour[userchoice[i]])
		
	def change_colour1( self, ch ):
		global userchoice
		userchoice[0] = self.listbox1.curselection()[0]
		uc = self.listbox1.get( ANCHOR )
		self.colourLabel1.configure( bg=uc )

	def change_colour2( self, ch ):
		global userchoice
		userchoice[1] = self.listbox2.curselection()[0]
		uc = self.listbox2.get( ANCHOR )
		self.colourLabel2.configure( bg=uc )

	def change_colour3( self, ch ):
		global userchoice
		userchoice[2] = self.listbox3.curselection()[0]
		uc = self.listbox3.get( ANCHOR )
		self.colourLabel3.configure( bg=uc )

	def change_colour4( self, ch ):
		global userchoice
		userchoice[3] = self.listbox4.curselection()[0]
		uc = self.listbox4.get( ANCHOR )
		self.colourLabel4.configure( bg=uc )


#-------------------------------------------------------------------------------
# Global variables
colour      = ["BLUE", "GREEN", "YELLOW", "ORANGE", "RED", "PURPLE"]
answer      = [0,0,0,0]
userchoice  = [0,1,2,3]

# ----------------------------------------------------------------------------
# Main program

# setup gui
root = Tk()
mainwin = MainWindow( root )

root.mainloop()


"""

#-------------------------------------------------------------------------------

def print_colored( row, col, s ):

	#orgcol = color()
	for n in range(1, 200):
		locate row, col
		for i in range( s.length() ):
			#c = 32 + (n+i) mod 22
			#color c
			#print mid(s,i,1);
			time.sleep(300)
	#color loword(orgcol), hiword(orgcol)


'-------------------------------------------------------------------------------

def introduction():

	#'screen SCRMODE
	#'color FRCOLOR, BGCOLOR
	#'cls
	#'locate 22, 18
	print("ABSayuti HMSaman April 2014")
	#'locate 23, 10
	print("Loosely based on a C64 program 'Mind Boggle'")
	#'locate 24, 10
	print("   from COMPUTE!s Gazette Disk May 1984")
	#'print_colored( 12, 20, " M I N D  B O G G L E ")


'-------------------------------------------------------------------------------

def generate_answer( ans ):

##    'cls
##    'print_colored( 12, 17, " I AM CHOOSING 4 COLORS NOW")
##
##    'ans(1) = int(rnd(1)*6)+1
##    'do
##    '        ans(2) = int(rnd(1)*6)+1
##    'loop while ans(2) = ans(1)
##    'do 
##    '        ans(3) = int(rnd(1)*6)+1
##    'loop while ans(1)=ans(3) or ans(2)=ans(3)
##    'do
##    '        ans(4) = int(rnd(1)*6)+1
##    'loop while ans(1)=ans(4) or ans(2)=ans(4) or ans(3)=ans(4)
##    'sleep 500
##    'cls


#-------------------------------------------------------------------------------

def disp_options():

##    dim as integer c   ', orgcol
##    'orgcol = color()
##    locate 23,5
##    print "                                 "
##    for c=1 to 6
##            locate 23, 40+c*3
##            color 0, bckcol(c) 								
##            print c;" "
##    next c
##    color FRCOLOR, BGCOLOR
##    beep


'-------------------------------------------------------------------------------

def get_selection( selection ):

##	dim as integer i, v, n
##	dim as string  s
##
##	do
##		beep
##		disp_options()
##		locate 23,5
##		input "SELECT COLORS"; s
##		n = 0	
##		if len(s)=4 then
##			for i=1 to 4
##				v = val(mid(s,i,1))		
##				if v<1 or v>6 then
##					beep
##					locate 23,5
##					print "ILLEGAL INPUT                    "
##					sleep 2000
##					continue do
##				else
##					selection(i) = v
##					n = n+1					' count correct entries
##				end if
##			next i
##		else
##			beep
##			locate 23,5
##			print "ILLEGAL INPUT                    "
##			sleep 2000
##		end if			
##	loop until n = 4 
##end sub


# -------------------------------------------------------------------------------

def print_selection( s, selection ):

##	dim as integer i, x ', orgcol
##	'orgcol = color()
##	for i=1 to 4 
##		x = selection(i)	
##		locate s*2, 10+i*6
##		color 0, bckcol(x)
##		print " ";x;"  "
##		beep
##		sleep 50
##	next
##	color FRCOLOR, BGCOLOR
##	
##end sub


#-------------------------------------------------------------------------------

def find_matches( ans, sel, black, white ): # black, white by ref

##	dim as integer x(1 to 4), a(1 to 4), j, k, match
##	
##	black = 0
##	white = 0
##	for j=1 to 4					
##		x(j) = sel(j)		
##		a(j) = ans(j) 	
##		if x(j) = a(j) then			
##			black = black+1
##			x(j) = 0
##			a(j) = 0
##		end if
##	next j						
##	for j=1 to 4
##		if a(j)<>0 then
##			match = 0
##			for k = 1 to 4
##				if a(j) = x(k) then 
##					match = 1 
##					x(k) = 0
##					a(j) = 0
##				end if
##			next k
##			white = white + match
##		end if
##	next j
##	'print "black", black, "white", white	
##end sub
##
##
##'-------------------------------------------------------------------------------

def print_matches( st, b, w ):  # return integer
##
##	dim as integer i
##
##	locate st*2, 42
##	for i=1 to b
##		color 15, 0			' white over black
##		print " B ";
##		beep
##		sleep 50
##	next
##	for i=1 to w
##		color 0, 15			' black over white
##		print " W ";
##		beep
##		sleep 50
##	next
##	color FRCOLOR, BGCOLOR
##	return 0
##	
##end function
##
##
##'-------------------------------------------------------------------------------

def game_over( win, st ): # return integer
##
##	dim as integer i ', orgcol
##	dim as ubyte    k
##
##	'orgcol = color()
##	locate 22,5
##	if win = 1 then
##		select case st
##			case 1
##					print "LUCKY GUESS!"
##			case 1, 2
##					print "EXPERT!!!"
##			case 3, 4, 5, 6
##					print "PRETTY GOOD!"
##			case 7, 8
##					print "SO SO!"
##			case else
##					print "YOU BARELY GOT IT!"
##		end select
##		locate 23,5
##		print "PRESS [ENTER]                    "
##		k = getkey
##	else
##		locate 22,5
##		print "CORRECT COLORS: ";
##		locate 23,5
##		print "                                           PRESS [ENTER]"
##		locate 23,16
##		for i=1 to 4
##			color 0, bckcol(i)
##			print " ";i;"  ";
##			color FRCOLOR, BGCOLOR
##			print " ";
##			beep
##		next
##		k = getkey
##		locate 22,5
##		print "TOO BAD YOU MISSED! 10 TRIES IS ENOUGH."
##	end if
##
##	locate 23,5
##	print "WANT TO PLAY AGAIN?  Y OR N?                            ";
##	k = getkey
##	if k = asc("n") then
##		print "TOO BAD..."
##		return 0
##	else
##		return 1
##	end if
##	
##end function
##
##
##'===============================================================================

answer = []
selection = []
playagain = 1

introduction()
##randomize 
##
while playagain==1:
	generate_answer( answer )
	## disp_options()
	step = 1
	gameover = 0
	win = 0

	while gameover==0:
	get_selection( selection )
	print_selection( step, selection )
	find_matches( answer, selection, black, white )
	'print "black", black, "white", white
	print_matches( step, black, white )
	if black = 4:
			win = 1
			gameover = 1
		else:
			step = step + 1
			if step > 10:
				gameover==1

	playagain = game_over( win, st )
"""
