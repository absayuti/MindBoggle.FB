'
'	Originally a C64 program "Mind Boggle" from Gazette Disk May 1984
'
'   V 0.21
'-------------------------------------------------------------------------------

dim shared as string*6 colour(1 to 6) => {"BLUE", "GREEN", "YELLOW", "ORANGE", "RED", "PINK"}
dim shared as integer bckcol(1 to 6) = { 9, 10, 14, 12, 4, 13 }
const SCRMODE = 16
const SCRWID  = 64
const SCRHGT  = 24
const FRCOLOR = 15
const BGCOLOR = 8


'-------------------------------------------------------------------------------

sub print_colored( row as integer, col as integer, s as string )

	dim as integer orgcol, i, n, c

	orgcol = color()
	for n = 1 to 200
		locate row, col
		for i=1 to len(s)
			c = 32 + (n+i) mod 22 
			color c
			print mid(s,i,1);
		next i
		sleep 30
	next n
	color loword(orgcol), hiword(orgcol)

end sub


'-------------------------------------------------------------------------------

sub introduction()

	Dim k As integer
	screen SCRMODE
	color FRCOLOR, BGCOLOR
	cls
	locate 22, 18
	print "ABSayuti HMSaman April 2014"
	locate 23, 10
	print "Loosely based on a C64 program 'Mind Boggle'"
	locate 24, 10
	print "   from COMPUTE!s Gazette Disk May 1984"
	print_colored( 12, 20, " M I N D  B O G G L E ")
    sleep 500
    
end sub


'-------------------------------------------------------------------------------

sub generate_answer( ans() as integer )

	cls
	print_colored( 12, 17, " I AM CHOOSING 4 COLORS NOW")

	ans(1) = int(rnd(1)*6)+1
	do
		ans(2) = int(rnd(1)*6)+1
	loop while ans(2) = ans(1)
	do 
		ans(3) = int(rnd(1)*6)+1
	loop while ans(1)=ans(3) or ans(2)=ans(3)
	do
		ans(4) = int(rnd(1)*6)+1
	loop while ans(1)=ans(4) or ans(2)=ans(4) or ans(3)=ans(4)
	sleep 500
	cls

end sub


'-------------------------------------------------------------------------------

sub disp_options()

	dim as integer c   ', orgcol
	'orgcol = color()
	locate 23,5
	print "                                 "
	for c=1 to 6
		locate 23, 40+c*3
		color 0, bckcol(c) 								
		print c;" "
	next c
	color FRCOLOR, BGCOLOR
	beep
	
end sub


'-------------------------------------------------------------------------------

sub get_selection( selection() as integer )

	dim as integer i, v, n
	dim as string  s

	do
		beep
		disp_options()
		locate 23,5
		input "SELECT COLORS"; s
		n = 0	
		if len(s)=4 then
			for i=1 to 4
				v = val(mid(s,i,1))		
				if v<1 or v>6 then
					beep
					locate 23,5
					print "ILLEGAL INPUT                    "
					sleep 2000
					continue do
				else
					selection(i) = v
					n = n+1					' count correct entries
				end if
			next i
		else
			beep
			locate 23,5
			print "ILLEGAL INPUT                    "
			sleep 2000
		end if			
	loop until n = 4 
end sub


'-------------------------------------------------------------------------------

sub print_selection( s as integer, selection() as integer  )

	dim as integer i, x ', orgcol
	'orgcol = color()
	for i=1 to 4 
		x = selection(i)	
		locate s*2, 10+i*6
		color 0, bckcol(x)
		print " ";x;"  "
		beep
		sleep 50
	next
	color FRCOLOR, BGCOLOR
	
end sub


'-------------------------------------------------------------------------------

sub find_matches( ans() as integer, sel() as integer, byref black as integer, byref white as integer )

	dim as integer x(1 to 4), a(1 to 4), j, k, match
	
	black = 0
	white = 0
	for j=1 to 4					
		x(j) = sel(j)		
		a(j) = ans(j) 	
		if x(j) = a(j) then			
			black = black+1
			x(j) = 0
			a(j) = 0
		end if
	next j						
	for j=1 to 4
		if a(j)<>0 then
			match = 0
			for k = 1 to 4
				if a(j) = x(k) then 
					match = 1 
					x(k) = 0
					a(j) = 0
				end if
			next k
			white = white + match
		end if
	next j
	'print "black", black, "white", white	
end sub


'-------------------------------------------------------------------------------

function print_matches( st as integer, b as integer, w as integer) as integer

	dim as integer i

	locate st*2, 42
	for i=1 to b
		color 15, 0			' white over black
		print " B ";
		beep
		sleep 50
	next
	for i=1 to w
		color 0, 15			' black over white
		print " W ";
		beep
		sleep 50
	next
	color FRCOLOR, BGCOLOR
	return 0
	
end function


'-------------------------------------------------------------------------------

function game_over( win as integer, st as integer ) as integer

	dim as integer i ', orgcol
	dim as ubyte    k

	'orgcol = color()
	locate 22,5
	if win = 1 then
		select case st
			case 1
					print "LUCKY GUESS!"
			case 1, 2
					print "EXPERT!!!"
			case 3, 4, 5, 6
					print "PRETTY GOOD!"
			case 7, 8
					print "SO SO!"
			case else
					print "YOU BARELY GOT IT!"
		end select
		locate 23,5
		print "PRESS [ENTER]                    "
		k = getkey
	else
		locate 22,5
		print "CORRECT COLORS: ";
		locate 23,5
		print "                                           PRESS [ENTER]"
		locate 23,16
		for i=1 to 4
			color 0, bckcol(i)
			print " ";i;"  ";
			color FRCOLOR, BGCOLOR
			print " ";
			beep
		next
		k = getkey
		locate 22,5
		print "TOO BAD YOU MISSED! 10 TRIES IS ENOUGH."
	end if

	locate 23,5
	print "WANT TO PLAY AGAIN?  Y OR N?                            ";
	k = getkey
	if k = asc("n") then
		print "TOO BAD..."
		return 0
	else
		return 1
	end if
	
end function


'===============================================================================

dim as integer answer(1 to 4), selection(1 to 4)
dim as integer gameover, win, playagain, st, black, white

introduction()
randomize 

do
	generate_answer( answer() )
	'disp_options()
	st = 1
	gameover = 0
	win = 0
	do until gameover = 1 
		get_selection( selection() )
		print_selection( st, selection() )
		find_matches( answer(), selection(), black, white )
		'print "black", black, "white", white
		print_matches( st, black, white )
		if black = 4 then
			win = 1
			gameover = 1
		end if
		st = st+1
		if st > 10 then
			gameover = 1
		end if
	loop

	playagain = game_over( win, st )
	
loop while playagain = 1


