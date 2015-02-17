import sys

#PRE-CONDITION: Must order the pitch-set before inputting as string
#Prints all possible orderings of the notes + how much they span to determine normal order
def print_orderings(pitch_set):
	for i in range(0, len(pitch_set)):
		x = i
		current = ""
		for a in range(x, len(pitch_set)):
			#sys.stdout.write(pitch_set[a])
			current += pitch_set[a]
		for a in range(0, x):
			#sys.stdout.write(pitch_set[a])
			current += pitch_set[a]
		print current
		distance(current,0,-1)
		#remove the pound in fromt of the line below should you encounter a tie
		#distance(current,0,-2) 

#For normal form calculations: Calculate distance between last and first
def distance(pitch_set, left, right):
	first = pitch_set[left]
	last = pitch_set[right]
	if first == 't':
		first = 10
	elif first == 'e':
		first = 11
	else:
		first = int(first)
	if last == 't':
		last = 10
	elif last == 'e':
		last = 11
	else:
		last = int(last)
	result = last - first;
	if result < 0:
		result += 12
	print pitch_set, "spans", result, "semitones"

#Calculates Tn(pitch_set)
def transpose(pitch_set, n):
	current = ''
	for i in pitch_set:
		if i == 't':
			i = 10
		elif i == 'e':
			i = 11
		else:
			i = int(i)
		result = (i + n) % 12
		current += str(result)
	print pitch_set, "transposed by", n, "is", current

def invert(pitch_set):
	current = ''
	for i in pitch_set:
		if i == 't':
			i = 10
		elif i == 'e':
			i = 11
		else:
			i = int(i)
		inverted = 12 - i
		current += str(inverted)
	print pitch_set, "inverted is", current


def index_sum(pitch_set_1, pitch_set_2):
	first = pitch_set_1[0]
	last = pitch_set_2[-1]
	if first == 't':
		first = 10
	elif first == 'e':
		first = 11
	else:
		first = int(first)
	if last == 't':
		last = 10
	elif last == 'e':
		last = 11
	else:
		last = int(last)
	sum = (first + last) % 12
	print "Index sum of", pitch_set_1, "and", pitch_set_2, "is", sum

#If I need to...turn this into invert(), then just transpose(invert(),n)
def transpose_and_invert(pitch_set, n):
	current = ''
	for i in pitch_set:
		if i == 't':
			i = 10
		elif i == 'e':
			i = 11
		else:
			i = int(i)
		inverted = 12 - i
		result = (inverted + n) % 12
		current += str(result)
	print pitch_set, "inverted and then transposed by", n, "is", current