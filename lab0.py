# Rebecca Lin
# 3/6/17

file = input("Which file do you want encrypted? ")
f = open(file, 'r')

decrypt = open("decrypt.txt", 'r+') 

contents = f.read() # Makes the file into a str

shift = 1 
count = 1 # This is just to keep track of the shift
while shift < 95: # The shift is between 32 and 126 (ordinal numbers of printable characters)
	decrypt.write("Shift {}: ".format(count)) 
	
	# Each character in the string is tested in this for loop
	for char in contents: 
		char = ord(char)
		# Get the ordinal number without the shift
		woShift = char - shift 
		
		# At some point, the woShift will become a number that doesn't correspond to a printable character (a number below 32)
		# In other words, if after being shifted, the ordinal number is greater than 126,
		# the numbers succeeding 126 wrap around to 32 
		if woShift >= 32:
			orig = chr(woShift)
		else:
			# There is a constant difference of 95 between woShift and the actual original ordinal number
			# ex. if shift is 3 and the char is 33, woShift will be 30. 
			# 	  30 is 2 from 32 (first printable character), so it is wrapped around to the end of the printable characters (126) and counted backwards
			#	  The original ordinal number would be 125
			#	  To go from 30 to 125, you add 95  <-- this is the same for other scenarios
			wrap = woShift + 95	
			orig = chr(wrap)
		
		# This writes each original character one after another
		decrypt.write(orig)
		
	# Since decrypt.write() doesn't automatically add a new line, to make it look better,
	# there will be two new lines after each time the whole text in the file is read and translated
	decrypt.write("\n\n")
	
	shift += 1 # The count of the shift will concatenate as each string is tested
	count += 1

f.close()
decrypt.close()

