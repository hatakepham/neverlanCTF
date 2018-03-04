f = open("temp_sum.txt","r")

sum = 0

for l in f:
	if not l.strip():
		continue
	
	sum += int(l.strip())

print sum
